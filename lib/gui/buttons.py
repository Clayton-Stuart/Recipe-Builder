import pygame
import os
pygame.display.init()
pygame.font.init()

textAlignLeft = 0
textAlignRight = 1
textAlignCenter = 2
textAlignBlock = 3

class button:
    def __init__(self, x, y, color, text_color, text, font, function):
        self.font = font
        self.color = color
        self.text_color = text_color
        self.function = function
        self.x = x
        self.y = y
        self.text = self.font.render(text, True, self.text_color)
        self.height = self.text.get_height() * 1.5
        self.width = self.text.get_width() * 1.2
        self.box = [self.x, self.y, self.width, self.height]
    def pygame_draw(self, screen):
        pygame.draw.rect(screen, self.color, self.box)
        screen.blit(self.text, (self.x + 5, self.y + 5))
    def getSize(self):
        return [self.width, self.height]
    def changeCoord(self, x, y):
        self.x = x
        self.y = y
        self.box = [self.x, self.y, self.width, self.height]


class delImgButton:
    def __init__(self, x, y, color, text_color, font, tag_num, function):
        self.font = font
        self.color = color
        self.text_color = text_color
        self.function = function
        self.x = x
        self.y = y
        self.text = self.font.render("X", True, self.text_color)
        self.height = self.text.get_height() * 1.5
        self.width = self.text.get_width() * 1.7
        self.box = [self.x, self.y, self.width, self.height]
        self.tag_num = tag_num

    def pygame_draw(self, screen):
        pygame.draw.rect(screen, self.color, self.box)
        screen.blit(self.text, (self.x + 5, self.y + 5))

    def getSize(self):
        return [self.width, self.height]
    
    def changeCoord(self, x, y):
        self.x = x
        self.y = y
        self.box = [self.x, self.y, self.width, self.height]
    
    def run(self):
        self.function(self.tag_num)


class dropDown:
    def __init__(self, color_active, color_inactive, color_hover, text_color, x, y, width, items, active, current, font):
        self.font = font
        self.color_active = color_active
        self.color_inactive = color_inactive
        self.color_hover = color_hover
        self.text_color = text_color
        self.height = self.font.render("W" * 17, True, self.text_color).get_height() * 1.5
        self.x = x
        self.y = y
        self.width = self.font.render("W" * width, True, self.text_color).get_width() * 1.2
        self.box_inactive = [self.x, self.y, self.width, self.height]
        self.active = active
        self.hover = False
        self.items = items
        if self.font.render(current, True, self.text_color).get_width() > self.width:
            while self.font.render(current, True, self.text_color).get_width() > self.width:
                current = current[:-1]
            self.current = current[:-4] + '...'
        else:
            self.current = current
        self.text = self.font.render(self.current, True, self.text_color)
        self.box_active = [self.x, self.y + self.height, self.width, self.height * (len(items))]

    def drawMenu(self, surface):
        if self.active:
            pygame.draw.rect(surface, self.color_active, self.box_inactive)
            text = self.font.render(self.current, True, self.text_color)
            surface.blit(text, (self.x + 5, self.y + 5))
            for i in range(len(self.items)):
                pygame.draw.rect(surface, self.color_active, [self.x, self.y + (i+1) * self.height, self.width, self.height])
                if self.font.render(self.items[i], True, self.text_color).get_width() > self.width:
                    while self.font.render(self.items[i], True, self.text_color).get_width() > self.width:
                        self.items[i] = self.items[i][:-1]
                    text = self.font.render(self.items[i][:-4] + '...', True, self.text_color)
                else: 
                    text = self.font.render(self.items[i], True, self.text_color)
                surface.blit(text, (self.x + 5, self.y + 2.5 + (i+1) * self.height))


        else:
            pygame.draw.rect(surface, self.color_active, self.box_inactive)
            text = self.font.render(self.current, True, self.text_color)
            surface.blit(text, (self.x + 5, self.y + 2.5))

def drawText(surface, text, color, rect, font, align=textAlignLeft, aa=False, bkg=None):
    lineSpacing = -2
    spaceWidth, fontHeight = font.size(" ")[0], font.size("Tg")[1]

    listOfWords = text.split(" ")
    if bkg:
        imageList = [font.render(word, 1, color, bkg) for word in listOfWords]
        for image in imageList: image.set_colorkey(bkg)
    else:
        imageList = [font.render(word, aa, color) for word in listOfWords]

    maxLen = rect[2]
    lineLenList = [0]
    lineList = [[]]
    for image in imageList:
        width = image.get_width()
        lineLen = lineLenList[-1] + len(lineList[-1]) * spaceWidth + width
        if len(lineList[-1]) == 0 or lineLen <= maxLen:
            lineLenList[-1] += width
            lineList[-1].append(image)
        else:
            lineLenList.append(width)
            lineList.append([image])

    lineBottom = rect[1]
    lastLine = 0
    for lineLen, lineImages in zip(lineLenList, lineList):
        lineLeft = rect[0]
        if align == textAlignRight:
            lineLeft += + rect[2] - lineLen - spaceWidth * (len(lineImages)-1)
        elif align == textAlignCenter:
            lineLeft += (rect[2] - lineLen - spaceWidth * (len(lineImages)-1)) // 2
        elif align == textAlignBlock and len(lineImages) > 1:
            spaceWidth = (rect[2] - lineLen) // (len(lineImages)-1)
        if lineBottom + fontHeight > rect[1] + rect[3]:
            break
        lastLine += 1
        for i, image in enumerate(lineImages):
            x, y = lineLeft + i*spaceWidth, lineBottom
            surface.blit(image, (round(x), y))
            lineLeft += image.get_width() 
        lineBottom += fontHeight + lineSpacing

    if lastLine < len(lineList):
        drawWords = sum([len(lineList[i]) for i in range(lastLine)])
        remainingText = ""
        for text in listOfWords[drawWords:]: remainingText += text + " "
        return remainingText
    return ""
        

def drawButtons(screen, buttons) -> None:
    for i in buttons:
        i.pygame_draw(screen)

def drawDropdowns(screen, dropdowns) -> None:
    for i in dropdowns:
        i.drawMenu(screen)