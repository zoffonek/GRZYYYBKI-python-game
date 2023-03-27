import pygame, random
from pygame.math import Vector2
from settings import *
from functions import *


class Bad_mushrooms():
    def __init__(self, game):
        self.game = game
        self.size_scr = self.game.screen.get_size()

        self.img = BAD_MUSH
        self.size_img = BAD_MUSH.get_size()
        self.width = self.size_img[0]
        self.height = self.size_img[1]

        self.pos = (random_width(self.width), -self.height)


        print("pos_bad")


        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], self.width-20, self.height-20)


    def tick(self):
        self.ver = random.randrange(-2, 0)
        self.pos -= Vector2(0,self.ver)
        if self.pos[1] > self.size_scr[1]:
            self.pos = (random_width(self.width), -self.height)
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], self.width-20, self.height-20)



    def draw(self):

        self.game.screen.blit(self.img, self.pos)

