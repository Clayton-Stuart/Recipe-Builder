from lib.constants import *
import pygame
import lib.gui.buttons as button

def drawImageScreen(cached_images: dict, img_b64: dict, img_obj: dict, uc: callable, screen_width: int, screen_height: int, screen: pygame.surface, font: pygame.font.Font, sc_offset: int, up: callable, bigFont: pygame.font.Font, deleteImage: callable, dark) -> tuple:
    if len(cached_images.keys()) != len(img_b64.keys()):
        uc()
        return
    
    if not dark:
        pygame.draw.rect(screen, LIGHT_GREY, [0, 0, screen_width // HOME_BUTTON_SIZE, screen_width // HOME_BUTTON_SIZE])
        screen.blit(font.render("X", True, BLACK), (screen_width // HOME_BUTTON_SIZE // 4, screen_width // HOME_BUTTON_SIZE // 4))
    else:
        pygame.draw.rect(screen, INVERT_LIGHT_GREY, [0, 0, screen_width // HOME_BUTTON_SIZE, screen_width // HOME_BUTTON_SIZE])
        screen.blit(font.render("X", True, INVERT_BLACK), (screen_width // HOME_BUTTON_SIZE // 4, screen_width // HOME_BUTTON_SIZE // 4))

    
    buttons = []
    if sc_offset < 0-screen_height:
        if not dark:
            uButton = button.button(x=0, y=0, color=LIGHT_GREY, text_color=DARK_GREY, text="Top", font=bigFont, function=up)
        else:
            uButton = button.button(x=0, y=0, color=INVERT_LIGHT_GREY, text_color=INVERT_BLACK, text="Top", font=bigFont, function=up)
        size = uButton.getSize()
        uButton.changeCoord(screen_width - size[0], screen_height - size[1])
    else:
        uButton = None
    scroll_offset = sc_offset + screen_width // HOME_BUTTON_SIZE + 5
    padding_left = screen_width * 0.05
    padding_top = screen_height * 0.05
    if not dark:
        tag_buffer = font.render("I", True, BLACK).get_height()
    else:
        tag_buffer = font.render("I", True, INVERT_BLACK).get_height()
    screen_height -= padding_top
    screen_width -= padding_left    
    
    nextCoord = (padding_left, padding_top + scroll_offset)
    
    tallestInLine = 0
    

    for key in img_obj.keys():
        if not dark:
            tag = font.render("<" + str(key) + ">", True, BLACK)
            buttons.append(button.delImgButton(0, 0, LIGHT_GREY, DARK_GREY, font, str(key), deleteImage))
        else:
            tag = font.render("<" + str(key) + ">", True, INVERT_BLACK)
            buttons.append(button.delImgButton(0, 0, INVERT_LIGHT_GREY, INVERT_BLACK, font, str(key), deleteImage))

        if img_obj[key].get_height() > tallestInLine:
            tallestInLine = img_obj[key].get_height()

        totalWidth = tag.get_width() + buttons[-1].getSize()[0]
        split = ((img_obj[key].get_width() - totalWidth) // 2) + tag.get_width()
        tag_offset = (img_obj[key].get_width() - tag.get_width()) // 4
        button_offset = split + tag_offset

        screen.blit(img_obj[key], nextCoord)
        screen.blit(tag, (nextCoord[0] + tag_offset, nextCoord[1] + tag_buffer + img_obj[key].get_height()))
        buttons[-1].changeCoord(nextCoord[0] + button_offset, nextCoord[1] + tag_buffer + img_obj[key].get_height())
        buttons[-1].pygame_draw(screen)

        nextCoord = (nextCoord[0] + img_obj[key].get_width() + padding_left, nextCoord[1])
        if nextCoord[0] + img_obj[key].get_width() > screen_width:
            nextCoord = (padding_left, nextCoord[1] + tallestInLine + padding_top + tag_buffer)
            tallestInLine = 0

        if uButton is not None:
            uButton.pygame_draw(screen)


    if uButton is not None:
        return uButton.box, buttons
    else:
        return [0, 0, 0, 0], buttons


def deleteImage(images, cached_images, py_img_obj, tag, steps) -> tuple:
    del images[int(tag)]
    del cached_images[int(tag)]
    del py_img_obj[int(tag)]
    for i in range(len(steps)):
        if steps[i].count("<" + str(tag) + ">") > 0:
            steps[i] = steps[i].replace("<" + str(tag) + ">", "")
    return images, cached_images, py_img_obj, steps