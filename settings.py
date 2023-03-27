import pygame
from pygame.locals import *
pygame.init()
# Main settings
CAPTION = "GRZYYYBKI"
SCREEN_SIZE = (1280, 656)
FONT_SIZE = 60
FONT_COLOR = (255,255,255)
FONT = "Amatic-Bold.ttf"
# Menu
FONT_MENU = "Amatic-Bold.ttf"
FONT_MENU_SIZE = 80
SCORE_SIZE = 40

#
BACKGROUND = pygame.image.load('img/background.png')
PLAYER = pygame.image.load('img/basket.svg')
GOOD_MUSH = pygame.image.load('img/ok_mushroom.svg')
BAD_MUSH = pygame.image.load('img/bad_mushroom.png')
ICON = pygame.image.load('img/bad_mushroom.png')
HOW_TP = pygame.image.load('img/background.png')
print(type(BACKGROUND))


