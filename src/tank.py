
import pygame
from pygame.sprite import Sprite
from src.bullet import Bullet


class Tank(Sprite):

    def __init__(self, bt_game):
        super().__init__()
        self.settings = bt_game.settings
        self.speed = 0
        self.animation_count = 0
        self.is_moving = False
        self.direction = 'U'
        self.screen = bt_game.screen
        self.screen_rect = bt_game.screen.get_rect()

        self.move_sprites = [pygame.image.load('../images/player/ut1.png'),
                             pygame.image.load('../images/player/ut2.png'),
                             pygame.image.load('../images/player/ut3.png'),
                             pygame.image.load('../images/player/ut4.png'),
                             pygame.image.load('../images/player/ut5.png'),
                             pygame.image.load('../images/player/ut6.png')]

        self.image = self.move_sprites[0]
        self.rect = self.image.get_rect()

    def move_right(self):
        self.is_moving = True
        self.direction = 'R'

    def move_left(self):
        self.is_moving = True
        self.direction = 'L'

    def move_up(self):
        self.is_moving = True
        self.direction = 'U'

    def move_down(self):
        self.is_moving = True
        self.direction = 'D'

    def stop(self):
        self.is_moving = False

    def fire(self):
        return Bullet(self)

    def _can_move(self, bt_game):
        return self._is_in_screen() and not self._is_collided(bt_game)

    def update(self, bt_game):
        pass

    def _is_collided(self, bt_game):
        pass

    def _is_in_screen(self):
        return self.screen_rect.contains(self.rect)

    def _get_animation_idx(self):
        self.animation_count += 1
        if self.animation_count >= 30:
            self.animation_count = 0
        return self.animation_count

#    def draw(self):
#       self.screen.blit(self.image, self.rect)

