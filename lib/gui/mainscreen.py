import lib.gui.buttons as button
from lib.constants import *
from os import system, path
from lib.encoding.xmlReader import *
import lib.gui.tktitleinput as tktitleinput
import tkinter.messagebox as tkm


def drawMainScreen(screen: pygame.surface, steps: list, font_paragraph: pygame.font.Font, buttons: list, dropdowns: list, screen_width: int, screen_height: int, titles: list, d0: list, font_button: pygame.font.Font, mid_generate: callable, mid_addStep: callable, mid_removeStep: callable, editStepText: callable, editIngredients: callable, changeName: callable, addImage: callable, saveAs: callable, saveRecipe: callable, mid_openRecipe: callable, goToImages: callable, dark: bool, darkLight: callable, scraper: callable) -> tuple:
    del buttons[:]
    del dropdowns[:]
    
    # Make all the buttons
    if not dark:
        dropdowns.append(button.dropDown(color_active=DROPDOWN_ACTIVE, color_inactive=DARK_GREY, color_hover=LIGHT_GREY, text_color=BLACK, x=screen_width // 1.3, y=screen_height // 15, width=12, items=titles, active=d0[0], current=d0[1], font=font_button))
        buttons.append(button.button(x=screen_width // 2, y=screen_height // 1.2, color=LIGHT_GREY, text_color=DARK_GREY, text="Generate", font=font_button, function=mid_generate))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 15, color=LIGHT_GREY, text_color=BLACK, text="Add Step", font=font_button, function=mid_addStep))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 8, color=LIGHT_GREY, text_color=BLACK, text="Remove Step", font=font_button, function=mid_removeStep))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 5.4, color=LIGHT_GREY, text_color=BLACK, text="Edit Step Text", font=font_button, function=editStepText))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 4.1, color=LIGHT_GREY, text_color=BLACK, text="Edit Ingredients", font=font_button, function=editIngredients))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 3.3, color=LIGHT_GREY, text_color=BLACK, text="Change Recipe Name", font=font_button, function=changeName))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 2.3, color=LIGHT_GREY, text_color=BLACK, text="Add images to recipe", font=font_button, function=addImage))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 2.03, color=LIGHT_GREY, text_color=DARK_GREY, text="Save Recipe", font=font_button, function=lambda: saveRecipe()))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 1.825, color=LIGHT_GREY, text_color=DARK_GREY, text="Save As", font=font_button, function=lambda: saveAs()))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 1.66, color=LIGHT_GREY, text_color=DARK_GREY, text="Open Saved", font=font_button, function=mid_openRecipe))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 1.53, color=LIGHT_GREY, text_color=DARK_GREY, text="Open XML", font=font_button, function=openXML))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 1.33, color=LIGHT_GREY, text_color=DARK_GREY, text="Open Images Viewer", font=font_button, function=goToImages))
        buttons.append(button.button(x=0, y=0, color=LIGHT_GREY, text_color=BLACK, text="?  ", font=font_button, function=lambda: system(path.join('documentation', 'index.html'))))
        buttons.append(button.button(x=0, y=0, color=LIGHT_GREY, text_color=DARK_GREY, text="  ☾  ", font=font_button, function=darkLight))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 1.18, color=LIGHT_GREY, text_color=DARK_GREY, text="Import from Website", font=font_button, function=scraper))

    else:
        dropdowns.append(button.dropDown(color_active=INVERT_DROPDOWN_ACTIVE, color_inactive=INVERT_DARK_GREY, color_hover=INVERT_LIGHT_GREY, text_color=INVERT_BLACK, x=screen_width // 1.3, y=screen_height // 15, width=12, items=titles, active=d0[0], current=d0[1], font=font_button))
        buttons.append(button.button(x=screen_width // 2, y=screen_height // 1.2, color=INVERT_LIGHT_GREY, text_color=INVERT_DARK_GREY, text="Generate", font=font_button, function=mid_generate))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 15, color=INVERT_LIGHT_GREY, text_color=INVERT_BLACK, text="Add Step", font=font_button, function=mid_addStep))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 8, color=INVERT_LIGHT_GREY, text_color=INVERT_BLACK, text="Remove Step", font=font_button, function=mid_removeStep))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 5.4, color=INVERT_LIGHT_GREY, text_color=INVERT_BLACK, text="Edit Step Text", font=font_button, function=editStepText))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 4.1, color=INVERT_LIGHT_GREY, text_color=INVERT_BLACK, text="Edit Ingredients", font=font_button, function=editIngredients))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 3.3, color=INVERT_LIGHT_GREY, text_color=INVERT_BLACK, text="Change Recipe Name", font=font_button, function=changeName))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 2.3, color=INVERT_LIGHT_GREY, text_color=INVERT_BLACK, text="Add images to recipe", font=font_button, function=addImage))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 2.03, color=INVERT_LIGHT_GREY, text_color=INVERT_DARK_GREY, text="Save Recipe", font=font_button, function=lambda: saveRecipe()))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 1.825, color=INVERT_LIGHT_GREY, text_color=INVERT_DARK_GREY, text="Save As", font=font_button, function=lambda: saveAs()))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 1.66, color=INVERT_LIGHT_GREY, text_color=INVERT_DARK_GREY, text="Open Saved", font=font_button, function=mid_openRecipe))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 1.53, color=INVERT_LIGHT_GREY, text_color=INVERT_DARK_GREY, text="Open XML", font=font_button, function=openXML))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 1.33, color=INVERT_LIGHT_GREY, text_color=INVERT_DARK_GREY, text="Open Images Viewer", font=font_button, function=goToImages))
        buttons.append(button.button(x=0, y=0, color=INVERT_LIGHT_GREY, text_color=INVERT_BLACK, text="?  ", font=font_button, function=lambda: system(path.join('documentation', 'index.html'))))
        buttons.append(button.button(x=0, y=0, color=INVERT_LIGHT_GREY, text_color=INVERT_DARK_GREY, text="  ☼  ", font=font_button, function=darkLight))
        buttons.append(button.button(x=screen_width // 20, y=screen_height // 1.18, color=INVERT_LIGHT_GREY, text_color=INVERT_DARK_GREY, text="Import from Website", font=font_button, function=scraper))


    displayStepText(titles, d0, steps, screen, screen_width, screen_height, font_paragraph, dark)
    buttons[13].changeCoord(screen_width - buttons[13].getSize()[0], 0)
    button.drawButtons(screen, buttons)
    button.drawDropdowns(screen, dropdowns) 

    return buttons, dropdowns, titles, d0


def displayStepText(titles, d0, steps, screen, screen_width, screen_height, TimesNewRomanParagraph, dark) -> None:
    try:
        titles.index(d0[1])
    except:
        text = "Select or create a step"
        align = button.textAlignLeft
    else:
        text = steps[titles.index(d0[1])]
        align = button.textAlignBlock
    if not dark:
        button.drawText(screen, text, BLACK, (screen_width // 4, screen_height // 60, screen_width // 2.5, screen_height // 1.2), TimesNewRomanParagraph, align, True)
    else:
        button.drawText(screen, text, INVERT_BLACK, (screen_width // 4, screen_height // 60, screen_width // 2.5, screen_height // 1.2), TimesNewRomanParagraph, align, True)

def addStep(saved, clickedOnLoop, steps, titles, screen_width, screen_height) -> tuple:
    saved, clickedOnLoop = False, True
    tktitleinput.make_textbox(screen_width // 3, screen_height // 3)
    titles.append(tktitleinput.value)
    steps.append("")
    return saved, clickedOnLoop, steps, titles

def removeStep(saved, clickedOnLoop, steps, titles, d0) -> tuple:
    saved, clickedOnLoop = False, True
    try:
        titles.index(d0[1])
    except:
        tkm.Message(title="Error", message="Please select a step to remove")
    else:
        if tkm.askyesno(title="Remove Currently Selected Step", message="Are you sure you want to remove step " + d0[1]):
            del steps[titles.index(d0[1])]
            del titles[titles.index(d0[1])]

    return saved, clickedOnLoop, steps, titles
