import sys
import pygame
from pygame import event
from src.settings import Settings
from src.player import Player


class BattleTank:

    clock = pygame.time.Clock()

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        self.bg = pygame.image.load('../images/bg.png').convert()
        pygame.display.set_caption("Battle Tank")
        self.player = Player(self)

    def run_game(self):
        while True:

            self.clock.tick(30)
            self._check_events()
            self.player.update()
            self.player.bullets.update()
            self._update_screen()

    def _check_events(self):
        for key_event in pygame.event.get():
            if key_event.type == pygame.QUIT:
                sys.exit()
            elif key_event.type == pygame.KEYDOWN:
                self._check_keydown_events(key_event)
            elif key_event.type == pygame.KEYUP:
                self._check_keyup_events(key_event)

    def _check_keydown_events(self, key_event):
        if key_event.key == pygame.K_q:
            sys.exit()
        elif key_event.key == pygame.K_RIGHT:
            self.player.move_right()
        elif key_event.key == pygame.K_LEFT:
            self.player.move_left()
        elif key_event.key == pygame.K_UP:
            self.player.move_up()
        elif key_event.key == pygame.K_DOWN:
            self.player.move_down()
        elif key_event.key == pygame.K_SPACE:
            self.player.fire()

    def _check_keyup_events(self, key_event):
        if key_event.key == pygame.K_RIGHT \
                or key_event.key == pygame.K_LEFT \
                or key_event.key == pygame.K_UP \
                or key_event.key == pygame.K_DOWN:
            self.player.stop()

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.player.draw()
        for bullet in self.player.bullets.sprites():
            bullet.draw()
        pygame.display.flip()

if __name__ == '__main__':
    bt = BattleTank()
    bt.run_game()
