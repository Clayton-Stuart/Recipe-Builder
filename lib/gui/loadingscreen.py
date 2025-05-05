import pygame
from lib.constants import *

def drawScraperLoadingScreen(screen, screen_width, screen_height, font, dark, attempt, max) -> None:
    if not dark:
        screen.fill(WHITE)
        text = font.render("Loading...", True, BLACK)
        text2 = font.render("Attempt " + str(attempt) + " of " + str(max), True, BLACK)
    else:
        screen.fill(INVERT_WHITE)
        text = font.render("Loading...", True, INVERT_BLACK)
        text2 = font.render("Attempt " + str(attempt) + " of " + str(max), True, INVERT_BLACK)

    screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height()))
    screen.blit(text2, (screen_width // 2 - text2.get_width() // 2, screen_height // 2 - text2.get_height() // 2 + text.get_height() + 5))
    pygame.display.update()

