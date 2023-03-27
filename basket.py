import pygame
from pygame.math import Vector2
from settings import *

class Basket(object):

    def __init__(self, game):
        self.game = game

        size_scr = self.game.screen.get_size()
        self.size_img = PLAYER.get_size()

        self.pos = Vector2(size_scr[0]/2,size_scr[1]/2) #pozycja
        self.vel = Vector2(0,0) #predkosc
        self.acc = Vector2(0,0) #przyspieszenie

        self.turn = pygame.transform.flip(PLAYER, True, False)
        self.direction = True

        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], self.size_img[0], self.size_img[0])


    def add_force(self, force):
        self.acc += force

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and self.pos[1] > 100:
            self.add_force(Vector2(0,-1))
        elif pressed[pygame.K_DOWN] and self.pos[1] < SCREEN_SIZE[1]-200:
            self.add_force(Vector2(0,1))
        elif pressed[pygame.K_LEFT] and self.pos[0] > 100:
            self.add_force(Vector2(-1,0))
            self.direction = False
        elif pressed[pygame.K_RIGHT] and self.pos[0] < SCREEN_SIZE[0]-220:
            self.add_force(Vector2(1,0))
            self.direction = True

        #Physics
        self.vel *= 0.9
        #self.vel -= Vector2(0,-0.5)  #falling

        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], self.size_img[0], self.size_img[0])
    def draw(self):

        if self.direction:
            self.game.screen.blit(PLAYER, (self.pos.x, self.pos.y))
        else:
            self.game.screen.blit(self.turn, (self.pos.x, self.pos.y))




