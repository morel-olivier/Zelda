import sys

import pygame

from level import Level
from settings import *
from event import *


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption("Zelda")
        self.font_title = pygame.font.SysFont("Arial", 56)
        self.font_text = pygame.font.SysFont("Arial", 24)
        self.clock = pygame.time.Clock()

        self.level = Level()

        # sound
        main_sound = pygame.mixer.Sound("../audio/main.ogg")
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)

    def reset(self):

        self.level = Level()

        # sound
        main_sound = pygame.mixer.Sound("../audio/main.ogg")
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
                if event.type == ON_DEATH:

                    # Death screen
                    self.screen.fill("#000000")
                    txtsurf = self. font_title.render(
                        "Game Over looser !", True, "#FFFFFF")
                    self.screen.blit(
                        txtsurf, ((self.screen.get_width() - txtsurf.get_width()) // 2,
                                  (self.screen.get_height() - txtsurf.get_height()) // 2))

                    txtsurf = self. font_text.render(
                        "Press key to restart", True, "#FFFFFF")
                    self.screen.blit(
                        txtsurf, ((self.screen.get_width() - txtsurf.get_width()) // 2,
                                  (self.screen.get_height() - txtsurf.get_height()) // 2 + 50))
                    pygame.display.update()

                    # Wait until the player press a key
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                pygame.time.delay(1000)
                                self.reset()
                                self.run()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
