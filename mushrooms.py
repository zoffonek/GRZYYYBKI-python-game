import pygame
from pygame.math import Vector2
from settings import *
from functions import *


class Mushrooms():

    def __init__(self, game):
        self.game = game
        size = self.game.screen.get_size()

        self.img = GOOD_MUSH
        self.size_img = GOOD_MUSH.get_size()
        self.width = self.size_img[0]
        self.height = self.size_img[1]

        self.pos = random_pos(self.width,self.height)
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)


    def tick(self):

        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)

    def draw(self):

        self.game.screen.blit(self.img, self.pos)
