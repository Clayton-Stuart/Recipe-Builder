import pygame
import os

WHITE = (255, 255, 255)
INVERT_WHITE = (20, 20, 20)
BLACK = (0, 0, 0)
INVERT_BLACK = (255, 255, 255)
GREEN = (0, 255, 0)
INVERT_GREEN = (255, 0, 255)
RED = (255, 0, 0)
INVERT_RED = (0, 255, 255)
BLUE = (0, 0, 255)
INVERT_BLUE = (255, 255, 0)
GREY = (128, 128, 128)
INVERT_GREY = (127, 127, 127)
LIGHT_GREY = (192, 192, 192)
INVERT_LIGHT_GREY = (63, 63, 63)
DARK_GREY = (30, 30, 30)
INVERT_DARK_GREY = (225, 225, 225)
DROPDOWN_ACTIVE = (200, 200, 200)
INVERT_DROPDOWN_ACTIVE = (55, 55, 55)

BUTTON_HEIGHT_SCALE = 10 # 15
BUTTON_WIDTH_SCALE = 11 # 16
BUTTON_FONT_RATIO = 90 # 70
PARAGRAPH_FONT_RATIO = 80 # 70
LOADING_MAIN_FONT_RATIO = 15

DISPLAY_SCALE = 1
IMAGE_SCALE = 0.2
MONITOR_WIDTH = pygame.display.Info().current_w 
MONITOR_HEIGHT = pygame.display.Info().current_h

MAX_IMG_WIDTH = int(MONITOR_WIDTH * IMAGE_SCALE)
MAX_IMG_HEIGHT = int(MONITOR_HEIGHT * IMAGE_SCALE)

HOME_BUTTON_SIZE = 40

TEMP_DIR = os.path.join('.', 'tmp')

USE_FIREFOX = False

SCRAPER_ATTEMPT_THRESHOLD = 5
SUPPORTED_DOMAINS = ['allrecipes.com', 'cooking.nytimes.com', 'sallysbakingaddiction.com', 'forksoverknives.com', 'ww.com', 'weightwatchers.com']
# need to do food.com, food network, 