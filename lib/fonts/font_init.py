from lib.constants import *

def getFontSizeButton(width, height):
    if width > height:
        return width // BUTTON_FONT_RATIO
    else:
        return height // BUTTON_FONT_RATIO
    
def getFontSizeParagraph(width, height):
    if width > height:
        return width // PARAGRAPH_FONT_RATIO
    else:
        return height // PARAGRAPH_FONT_RATIO
    
def getFontSizeLoadingScreenMain(width, height):
    if width > height:
        return width // LOADING_MAIN_FONT_RATIO
    else:
        return height // LOADING_MAIN_FONT_RATIO