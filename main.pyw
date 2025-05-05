#python imports
import os
import sys
import pygame
from tkinter import filedialog
import tkinter.messagebox as tkm
import keyboard
import shutil

# project imports
from lib.generating.create_file import *
import lib.gui.buttons as button
import lib.gui.tkparagraphinput as tkparagraphinput
import lib.gui.tknameinput as tknameinput
from lib.encoding.xmlReader import *
from lib.constants import *
from lib.generating.generating import *
from lib.fonts.font_init import *
import lib.encoding.image_encode as ie
from lib.encoding.open_save import *
from lib.gui.mainscreen import *
from lib.dynamic import *
from lib.gui.imagescreen import *
from lib.gui.loadingscreen import *

#scrapers
import lib.website_scrapers.allrecipes as allrecipes
import lib.website_scrapers.newyorktimes as newyorktimes
import lib.website_scrapers.sallysbakingaddiction as sallysbakingaddiction
import lib.website_scrapers.forksoverknives as forksoverknives
import lib.website_scrapers.weightwatchers as weightwatchers
from lib.website_scrapers.recipe_scraper_utilities import extract_domain



os.chdir(os.path.dirname(os.path.realpath(__file__)))
EXECUTABLE_PATH = sys.executable

if os.path.exists(TEMP_DIR):
    shutil.rmtree(TEMP_DIR)
    os.mkdir(TEMP_DIR)

else:
    os.mkdir(TEMP_DIR)

if os.name == "nt":
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)

pygame.display.init()
pygame.font.init()

dropdowns.append(button.dropDown(0, 0, 0, 0, 0, 0, 500, ['None', 'None'], False, "Steps" , pygame.font.SysFont("Times New Roman", 20)))

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size=(MONITOR_WIDTH * DISPLAY_SCALE, MONITOR_HEIGHT * DISPLAY_SCALE), flags=pygame.RESIZABLE)
pygame.display.set_caption("Recipe HTML Generator")

def scraper() -> None:
    global screen, name, ingredients_text, titles, steps, screen_width, screen_height, TimesNewRomanLoadingScreenMain, text_box_active
    ask = tkm.askyesnocancel("Proceeding will overwrite recipe", "Save Recipe?")
    if ask == True:
        saveRecipe()
    elif ask == False:
        pass
    else:
        return
    
    text_box_active = True
    tktitleinput.make_textbox(screen_width // 2, screen_height // 5, message="Enter Recipe URL")
    url = tktitleinput.value.strip()
    text_box_active = False
    url_extracted = extract_domain(url)

    if url_extracted.lower() not in SUPPORTED_DOMAINS:
        tkm.showerror("Invalid or unsupported URL", "Please enter a supported URL")
        return
    
    
    if url_extracted.lower() == "allrecipes.com":

        for i in range(SCRAPER_ATTEMPT_THRESHOLD):
            drawScraperLoadingScreen(screen, screen_width, screen_height, TimesNewRomanLoadingScreenMain, dark, i+1, SCRAPER_ATTEMPT_THRESHOLD)
            try:
                recipe = allrecipes.readURL(url, FireFox=USE_FIREFOX)
            except:
                continue
            else:
                name = recipe.name
                steps = recipe.steps
                titles = recipe.titles
                ingredients_text = ""
                for ingredient in recipe.ingredients:
                    ingredients_text += ingredient + "\n"
                break
        else:
            tkm.showerror("Error", "Could not scrape recipe")
            return
        
    elif url_extracted.lower() == "cooking.nytimes.com":
        for i in range(SCRAPER_ATTEMPT_THRESHOLD):
            drawScraperLoadingScreen(screen, screen_width, screen_height, TimesNewRomanLoadingScreenMain, dark, i+1, SCRAPER_ATTEMPT_THRESHOLD)
            try:
                recipe = newyorktimes.readURL(url, FireFox=USE_FIREFOX)
            except:
                continue
            else:
                name = recipe.name
                steps = recipe.steps
                titles = recipe.titles
                ingredients_text = recipe.ingredients
                break
        else:
            tkm.showerror("Error", "Could not scrape recipe")
            return
        
    elif url_extracted.lower() == "sallysbakingaddiction.com":
        for i in range(SCRAPER_ATTEMPT_THRESHOLD):
            drawScraperLoadingScreen(screen, screen_width, screen_height, TimesNewRomanLoadingScreenMain, dark, i+1, SCRAPER_ATTEMPT_THRESHOLD)
            try:
                recipe = sallysbakingaddiction.readURL(url, FireFox=USE_FIREFOX)
            except:
                continue
            else:
                name = recipe.name
                steps = recipe.steps
                titles = recipe.titles
                ingredients_text = ""
                for ingredient in recipe.ingredients:
                    ingredients_text += ingredient + "\n"
                break
        else:
            tkm.showerror("Error", "Could not scrape recipe")
            return
        
    elif url_extracted.lower() == 'forksoverknives.com':
        for i in range(SCRAPER_ATTEMPT_THRESHOLD):
            drawScraperLoadingScreen(screen, screen_width, screen_height, TimesNewRomanLoadingScreenMain, dark, i+1, SCRAPER_ATTEMPT_THRESHOLD)
            try:
                recipe = forksoverknives.readURL(url, FireFox=USE_FIREFOX)
            except:
                continue
            else:
                name = recipe.name
                steps = recipe.steps
                titles = recipe.titles
                ingredients_text = recipe.ingredients
                break
        else:
            tkm.showerror("Error", "Could not scrape recipe")
            return
        
    elif url_extracted.lower() == "ww.com" or url_extracted.lower() == "weightwatchers.com":
        for i in range(SCRAPER_ATTEMPT_THRESHOLD):
            drawScraperLoadingScreen(screen, screen_width, screen_height, TimesNewRomanLoadingScreenMain, dark, i+1, SCRAPER_ATTEMPT_THRESHOLD)
            try:
                recipe = weightwatchers.readURL(url, FireFox=USE_FIREFOX)
            except:
                continue
            else:
                name = recipe.name
                steps = recipe.steps
                titles = recipe.titles
                ingredients_text = ""
                for ingredient in recipe.ingredients:
                    ingredients_text += ingredient + "\n"
                break
        else:
            tkm.showerror("Error", "Could not scrape recipe")
            return

def writePersistent() -> None:
    global dark
    file = open(os.path.join(".", "lib", "persistent_vars.txt"), "w")
    file.write(str(dark) + "\n")
    file.close()

def darkLightMode() -> None:
    global dark
    if dark:
        dark = False
    else:
        dark = True
    writePersistent()

def mid_generate() -> None:
    generate(name, ingredients_text, titles, steps, images, css)

def mid_addStep() -> None:
    global clickedOnLoop, saved, steps, titles 
    saved, clickedOnLoop, steps, titles = addStep(saved, clickedOnLoop, steps, titles, screen_width, screen_height)
    # Saved = False is in addStep()

def mid_removeStep() -> None:
    global saved, clickedOnLoop, steps, titles, d0
    saved, clickedOnLoop, steps, titles = removeStep(saved, clickedOnLoop, steps, titles, d0)
    # Saved = False is in removeStep()

def mid_updateCache() -> None:
    global images, cached_images, screen, screen_width, screen_height, py_img_obj, TimesNewRomanButton, img_up_box
    cached_images, py_img_obj = ie.updateCache(images, cached_images)
    img_up_box = drawImageScreen(cached_images, images, py_img_obj, mid_updateCache, screen_width, screen_height, screen, TimesNewRomanButton, scroll_offset_img, imgTop, TimesNewRomanBigButton, mid_deleteImage, dark)

def mid_deleteImage(tag) -> None:
    global images, cached_images, py_img_obj, steps, saved
    images, cached_images, py_img_obj, steps = deleteImage(images, cached_images, py_img_obj, tag, steps)
    saved = False

def changeName() -> None:
    global name, saved, clickedOnLoop, text_box_active
    saved = False
    clickedOnLoop = True
    text_box_active = True
    tknameinput.make_textbox(screen_width // 3, screen_height // 3, default=name)
    name = tknameinput.value
    text_box_active = False

def editStepText() -> None:
    global saved, clickedOnLoop, text_box_active
    saved, clickedOnLoop = False, True
    try:
        titles.index(d0[1])
    except:
        tkm.Message(title="Error", message="Please select a step to edit")
    else:
        text_box_active = True
        tkparagraphinput.make_textbox(pygame.display.Info().current_w // 2, pygame.display.Info().current_h // 2, default=steps[titles.index(d0[1])])
        steps[titles.index(d0[1])] = tkparagraphinput.value
        text_box_active = False

def editIngredients() -> None:
    global saved, clickedOnLoop, ingredients_text, text_box_active
    saved = False
    clickedOnLoop = True
    text_box_active = True
    tkparagraphinput.make_textbox(pygame.display.Info().current_w // 2, pygame.display.Info().current_h // 2, default=ingredients_text)
    ingredients_text = tkparagraphinput.value
    text_box_active = False

def saveRecipe() -> None:
    global saved, save_path
    if save_path is None:
        saveAs()
    else:
        writeSaveFile(open(save_path, "wb"), name, ingredients_text, titles, steps, css, images)
    saved = True

def saveAs() -> None:
    global saved, save_path
    file = filedialog.asksaveasfile(mode='wb', title=name, defaultextension=(".rgfs"))
    if file is None: return
    writeSaveFile(file, name, ingredients_text, titles, steps, css, images)
    save_path, saved = file.name, True

def goToImages() -> None:
    global clickedOnLoop, page, scroll_offset_img
    clickedOnLoop = True
    page = "images"
    scroll_offset_img = 0

def imgTop() -> None:
    global scroll_offset_img
    scroll_offset_img = 0

def addImage():
    global saved, clickedOnLoop, images, cached_images, py_img_obj
    saved = False
    clickedOnLoop = True
    file = filedialog.askopenfile(mode='rb', title=name, filetypes=[("PNG", "*.png"), ("JPG", "*.jpg"), ("JPEG", "*.jpeg")])
    if file is None: return

    enc = ie.encode(file)

    keys = list(images.keys())
    if len(keys) == 0:
        images[0] = enc
    else:
        images[keys[-1] + 1] = enc

    cached_images, py_img_obj = ie.updateCache(images, cached_images)



def mid_openRecipe() -> None:
    global save_path, name, titles, steps, css, images, cached_images, ingredients_text, py_img_obj
    save_path, name, ingredients_text, titles, steps, css, images = openRecipe(save_path, name, ingredients_text, titles, steps, css, images)
    cached_images, py_img_obj = ie.reBuildCache(images)

keyboard.add_hotkey('ctrl+s', saveRecipe)
keyboard.add_hotkey('ctrl+shift+s', saveAs)

# Main Loop
while running:
    clickedOnLoop = False
    if saved:
        pygame.display.set_caption(name.strip().replace('\n', ' '))
    else:
        pygame.display.set_caption(name.strip().replace('\n', ' ') + " *")
    if name is None or name.strip() == "":
        name = "New Recipe"

    # Set screen dependent variables
    screen_width, screen_height = pygame.display.get_surface().get_size()
    TimesNewRomanButton = pygame.font.Font(os.path.join('lib', 'fonts', 'Times New Roman.ttf'), getFontSizeButton(screen_width, screen_height))
    TimesNewRomanParagraph = pygame.font.Font(os.path.join('lib', 'fonts', 'Times New Roman.ttf'), getFontSizeParagraph(screen_width, screen_height))
    TimesNewRomanBigButton = pygame.font.Font(os.path.join('lib', 'fonts', 'Times New Roman.ttf'), getFontSizeButton(screen_width, screen_height) * 2)
    TimesNewRomanLoadingScreenMain = pygame.font.Font(os.path.join('lib', 'fonts', 'Times New Roman.ttf'), getFontSizeLoadingScreenMain(screen_width, screen_height))

    # Event loop
    if not text_box_active:
        for event in pygame.event.get():
            # Make the program able to quit properly
            if event.type == pygame.QUIT:
                if not saved:
                    result = tkm.askyesnocancel("Quit", "Recipe is not saved. Would you like to save?")
                    if result:
                        saveRecipe()
                        if saved:
                            running = False
                        
                    elif result == False:
                        running = False
                else:
                    running = False


            if page == "home":
                if event.type == pygame.MOUSEBUTTONUP:
                    if not clickedOnLoop:
                    # Check for clicking buttons
                        for i in buttons:
                            if i.box[0] < event.pos[0] < i.box[0] + i.box[2] and i.box[1] < event.pos[1] < i.box[1] + i.box[3]:
                                i.function()

                        # Check for clicking dropdowns
                        for i in dropdowns:
                            if i.active:
                                if i.box_active[0] < event.pos[0] < i.box_active[0] + i.box_active[2] and i.box_active[1] < event.pos[1] < i.box_active[1] + i.box_active[3]:
                                    # find clicked box
                                    for j in range(len(i.items)):
                                        if i.x < event.pos[0] < i.x + i.width and i.y + i.height * (j+1) < event.pos[1] < i.y + i.height * (j+1) + i.height:
                                            i.current = i.items[j]
                                            i.active = False

                                else:
                                    i.active = False

                            else:
                                if i.box_inactive[0] < event.pos[0] < i.box_inactive[0] + i.box_inactive[2] and i.box_inactive[1] < event.pos[1] < i.box_inactive[1] + i.box_inactive[3]:
                                    i.active = True

            elif page == "images":
                if event.type == pygame.MOUSEBUTTONUP:
                    if not clickedOnLoop:
                        if 0 < event.pos[0] < HOME_BUTTON_SIZE and 0 < event.pos[1] < 0 + HOME_BUTTON_SIZE:
                            page = "home"
                            if deleted_image:
                                cached_images, py_img_obj = ie.reBuildCache(images)
                        if img_up_box[0] < event.pos[0] < img_up_box[0] + img_up_box[2] and img_up_box[1] < event.pos[1] < img_up_box[1] + img_up_box[3]:
                            imgTop()

                    for i in buttons:
                        if i.box[0] < event.pos[0] < i.box[0] + i.box[2] and i.box[1] < event.pos[1] < i.box[1] + i.box[3]:
                            i.run()
                            deleted_image = True

                if event.type == pygame.MOUSEWHEEL:
                    scroll_offset_img += event.y * 10
                    if scroll_offset_img > 0:
                        scroll_offset_img = 0
        
        # Empty the screen
        if not dark:
            screen.fill(WHITE)
        else:
            screen.fill(INVERT_WHITE)
        match page:
            case "home":
                d0 = [dropdowns[0].active, dropdowns[0].current]
                buttons, dropdowns, titles, d0 = drawMainScreen(screen, steps, TimesNewRomanParagraph, buttons, dropdowns, screen_width, screen_height, titles, d0, TimesNewRomanButton, mid_generate, mid_addStep, mid_removeStep, editStepText, editIngredients, changeName, addImage, saveAs, saveRecipe, mid_openRecipe, goToImages, dark, darkLightMode, scraper)
                d0 = [dropdowns[0].active, dropdowns[0].current]


            case "images":
                img_up_box, buttons = drawImageScreen(cached_images, images, py_img_obj, mid_updateCache, screen_width, screen_height, screen, TimesNewRomanButton, scroll_offset_img, imgTop, TimesNewRomanBigButton, mid_deleteImage, dark)
                

        pygame.display.flip()
        clock.tick(60)

if os.path.exists(TEMP_DIR):
    shutil.rmtree(TEMP_DIR)
