import sys
import pygame
from src.settings import Settings
from src.player import Player
from src.enemy import Enemy


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
        self.bullets = pygame.sprite.Group()
        self.player = Player(self)
        enemy = Enemy(self)
        self.enemies = pygame.sprite.Group()
        self.enemies.add(enemy)
        self.all_tanks = pygame.sprite.Group()
        self.all_tanks.add(self.player)
        self.all_tanks.add(enemy)

    def run_game(self):
        while True:

            self.clock.tick(30)
            self._check_events()
            self.player.update(self)
            self.bullets.update()
            self.enemies.update(self)
            self._update_screen()

    def _check_events(self):
        key_event = pygame.event.poll()

        if key_event.type == pygame.QUIT:
            sys.exit()
        elif key_event.type == pygame.KEYDOWN:
            self._check_keydown_events(key_event)
        elif key_event.type == pygame.KEYUP:
            self._check_keyup_events(key_event)

    def _check_keydown_events(self, key_event):
        if key_event.key == pygame.K_ESCAPE:
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
            self.bullets.add(self.player.fire())

    def _check_keyup_events(self, key_event):
        if key_event.key == pygame.K_RIGHT \
                or key_event.key == pygame.K_LEFT \
                or key_event.key == pygame.K_UP \
                or key_event.key == pygame.K_DOWN:
            self.player.stop()

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.all_tanks.draw(self.screen)
        self.bullets.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    bt = BattleTank()
    bt.run_game()
