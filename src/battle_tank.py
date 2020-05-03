import sys
import pygame
from src.settings import Settings
from src.player import Player


class BattleTank:

    clock = pygame.time.Clock()

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.bg = pygame.image.load('../images/bg.png')
        pygame.display.set_caption("Battle Tank")
        self.player = Player(self)

    def run_game(self):
        while True:

            self.clock.tick(30)
            self._check_events()
            self.player.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.move_right()
                elif event.key == pygame.K_LEFT:
                    self.player.move_left()
                elif event.key == pygame.K_UP:
                    self.player.move_up()
                elif event.key == pygame.K_DOWN:
                    self.player.move_down()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT\
                        or event.key == pygame.K_LEFT\
                        or event.key == pygame.K_UP\
                        or event.key == pygame.K_DOWN:
                    self.player.stop()

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.player.draw()
        pygame.display.flip()


if __name__ == '__main__':
    bt = BattleTank()
    bt.run_game()
