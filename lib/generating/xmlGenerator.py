import pygame
import os

pygame.display.init()

if os.name == "nt":
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)