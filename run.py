import pygame, sys, random
from pygame.math import Vector2
from settings import *
from buttons import Buttons
from bad_mushroom import Bad_mushrooms
from basket import Basket
from functions import *
from mushrooms import Mushrooms as MU

global event


class Menu(object):

    def __init__(self):
        # Config
        self.tps = 60
        clock = 0

        self.how_to_play = False

        # Initialization
        pygame.init()
        pygame.display.set_caption(CAPTION)
        pygame.display.set_icon(ICON)
        pygame.display.set_icon(BAD_MUSH)
        self.font = pygame.font.Font(FONT, FONT_SIZE)
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

        # Buttons
        self.play_button = Buttons(200, "PLAY", False)
        self.name_button = Buttons(200, "ENTER NAME", True)
        self.scores_button = Buttons(300, "SCORES", False)
        self.exit_button = Buttons(400, "EXIT", False)

        show_line = False
        self.user_name = "NEW_USER"

        # classes
        self.run = True

        while self.run:
            clock += pygame.time.Clock().tick(self.tps) / 1000

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.user_name = self.user_name[:-1]
                    elif event.key == pygame.K_RETURN or len(self.user_name) > 15:
                        print("add user.name")
                        self.run = False
                        Game(self.user_name)
                    else:
                        self.user_name += event.unicode

            self.screen.blit(BACKGROUND, (0, 0))
            if self.play_button.tick():
                self.run = False
                print("game start")
                Game(self.user_name)
            if clock > 0.7:
                if self.name_button.tick():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_presses = pygame.mouse.get_pressed()
                        if mouse_presses[0]:
                            show_line = True
                if self.scores_button.tick():
                    self.run = False
                    GameBoard(False, False)
                if self.exit_button.tick():
                    sys.exit(0)

            self.play_button.draw(self.screen)
            self.scores_button.draw(self.screen)
            self.exit_button.draw(self.screen)
            self.name_button.draw(self.screen)
            if show_line:
                self.input_box()
                self.screen.blit(self.name_enter, (x1, y1))

            pygame.display.flip()

    def input_box(self):
        global x1, y1
        x1 = self.name_button.pos_x
        y1 = self.name_button.pos_y + 100
        y2 = y1 + FONT_MENU_SIZE
        pygame.draw.line(self.screen, (255, 255, 255), (x1, y1), (x1, y2))

        b = pygame.font.Font(FONT_MENU, FONT_MENU_SIZE)
        self.name_enter = b.render(self.user_name, True, (255, 255, 255))


class Game(object):
    def __init__(self, user_n):

        run = True
        self.user = user_n
        # Config
        self.tps = 60
        clock = 0

        # Leadboard
        self.score = 0
        self.hp = 5
        self.name = ""

        # Initialization
        pygame.init()
        pygame.display.set_caption(CAPTION)
        pygame.display.set_icon(ICON)
        self.font = pygame.font.Font(FONT, FONT_SIZE)
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

        # Other classes

        self.basket = Basket(self)
        self.BMU = Bad_mushrooms(self)
        self.bad_mush_list = []
        self.mush_list = []

        c = 2
        while run:

            clock += pygame.time.Clock().tick(self.tps) / 1000

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        Menu()
            if self.hp <= 0:
                print("add user.name_game")
                run = False
                print("SCORE: ", self.score, self.user)
                GameBoard(self.score, self.user)

            # Ticking
            self.tick()

            if clock >= c:

                self.mush_list.append(MU(self))
                if clock >= 3:
                    self.bad_mush_list.append(self.BMU)
                clock = 0
                c = random.randint(1, 4)

            # self.menu = Menu()

            # Rendering
            self.draw()

            # Hitbox
            self.hitbox()

    def hitbox(self):
        for mush in self.mush_list:
            if self.basket.hitbox.colliderect(mush.hitbox):
                self.mush_list.remove(mush)
                self.score += 1

        for bmush in self.bad_mush_list:
            if self.basket.hitbox.colliderect(bmush.hitbox):
                self.bad_mush_list.remove(bmush)
                self.hp -= 1
                self.BMU.pos = (random_width(bmush.width), -bmush.height)
                self.BMU.hitbox = pygame.Rect(self.BMU.pos[0], self.BMU.pos[1], self.BMU.width - 20,
                                              self.BMU.height - 20)

        for bmush in self.bad_mush_list:
            for mush in self.mush_list:
                if mush.hitbox.colliderect(bmush.hitbox):
                    self.mush_list.remove(mush)

    def tick(self):
        self.basket.tick()
        for mush in self.mush_list:
            mush.tick()
        for bmush in self.bad_mush_list:
            bmush.tick()

    def draw(self):
        self.screen.blit(BACKGROUND, (0, 0))

        # leadboard
        txt_score = pygame.font.Font.render(self.font, f"SCORE: {self.score}", True, FONT_COLOR)
        txt_user = pygame.font.Font.render(self.font, f"{self.user}", True, FONT_COLOR)
        txt_hp = pygame.font.Font.render(self.font, f"HP: {self.hp}", True, FONT_COLOR)
        txt_hp_x = SCREEN_SIZE[0] - txt_hp.get_size()[0] - 10
        self.screen.blit(txt_score, (10, 5))
        self.screen.blit(txt_hp, (txt_hp_x, 5))
        self.screen.blit(txt_user, ((txt_hp_x - 10) // 2, 5))

        self.basket.draw()

        for mush in self.mush_list:
            mush.draw()
        for bmush in self.bad_mush_list:
            bmush.draw()

        pygame.display.flip()


def GameBoard(gb_score, gb_user_name):
    print("GameBoard")

    # Config
    tps = 60
    clock = 0

    # Initialization
    pygame.init()
    pygame.display.set_caption(CAPTION)
    pygame.display.set_icon(ICON)
    font = pygame.font.Font(FONT, FONT_SIZE)
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Buttons
    menu_button = Buttons(250, "MENU", False)
    exit_button = Buttons(350, "EXIT", False)

    l_score="_"

    if gb_score:
        print("new score")
        lb_add(gb_score, gb_user_name)
        bubble_sort_file()
        l_score=f"LAST SCORE: {gb_score}   {gb_user_name}"

    last_score= pygame.font.Font.render(font,l_score, True, FONT_COLOR)
    run = True
    # Loop
    while run:
        clock += pygame.time.Clock().tick(tps) / 1000

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                sys.exit(0)
            if clock > 1:
                if exit_button.tick():
                    sys.exit(0)
                if menu_button.tick():
                    run = False
                    Menu()

        list_scores = lb_read(5)



        top1 = pygame.font.Font.render(font, list_scores[0], True, FONT_COLOR)
        top2 = pygame.font.Font.render(font, list_scores[1], True, FONT_COLOR)
        top3 = pygame.font.Font.render(font, list_scores[2], True, FONT_COLOR)
        top4 = pygame.font.Font.render(font, list_scores[3], True, FONT_COLOR)
        top5 = pygame.font.Font.render(font, list_scores[4], True, FONT_COLOR)
        top_x = SCREEN_SIZE[0] // 2  # SCREEN_SIZE[0] - top5.get_size()[0] - 150

        top1_y = 150
        od = 80

        screen.blit(BACKGROUND, (0, 0))
        menu_button.draw(screen)
        exit_button.draw(screen)
        screen.blit(last_score, (100, top1_y))
        screen.blit(top1, (top_x, top1_y))
        screen.blit(top2, (top_x, top1_y + od))
        screen.blit(top3, (top_x, top1_y + 2 * od))
        screen.blit(top4, (top_x, top1_y + 3 * od))
        screen.blit(top5, (top_x, top1_y + 4 * od))
        pygame.display.flip()


if __name__ == "__main__":
    Menu()
