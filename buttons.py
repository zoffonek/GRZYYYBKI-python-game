import pygame
from settings import *

class Buttons():


    def __init__(self, pos_y, txt, line_2):

        # Font
        self.font = pygame.font.Font(FONT_MENU, FONT_MENU_SIZE)
        self.color_h = (0,0,0)
        self.color = (255,255,255)

        if line_2: self.pos_x = SCREEN_SIZE[0] // 2
        else: self.pos_x = SCREEN_SIZE[0] // 4

        self.pos_y = pos_y
        self.hitbox = pygame.Rect(self.pos_x, self.pos_y, 23 * len(txt), FONT_MENU_SIZE)

        # Rendering
        self.text = pygame.font.Font.render(self.font, txt, True, self.color)
        self.text_h = pygame.font.Font.render(self.font, txt, True, self.color_h)


    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True


    def draw(self, screen):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            screen.blit(self.text_h, (self.pos_x, self.pos_y))
        else:
            screen.blit(self.text, (self.pos_x, self.pos_y))


