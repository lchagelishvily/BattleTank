import pygame
import random
from pygame.sprite import Sprite

from src.bullet import Bullet


class Enemy(Sprite):

    def __init__(self, bt_game):
        super().__init__()
        self.settings = bt_game.settings
        self.speed = bt_game.settings.enemy_speed
        self.animation_count = 0
        self.is_moving = True
        self.direction = 'D'
        self.screen = bt_game.screen
        self.screen_rect = bt_game.screen.get_rect()
        self.bullets = pygame.sprite.Group()
        self.change_direction_delay = bt_game.settings.enemy_change_direction_delay

        self.move_up_sprites = [pygame.image.load('../images/player/ut1.png'),
                                pygame.image.load('../images/player/ut2.png'),
                                pygame.image.load('../images/player/ut3.png'),
                                pygame.image.load('../images/player/ut4.png'),
                                pygame.image.load('../images/player/ut5.png'),
                                pygame.image.load('../images/player/ut6.png')]

        self.move_right_sprites = [pygame.image.load('../images/player/rt1.png'),
                                   pygame.image.load('../images/player/rt2.png'),
                                   pygame.image.load('../images/player/rt3.png'),
                                   pygame.image.load('../images/player/rt4.png'),
                                   pygame.image.load('../images/player/rt5.png'),
                                   pygame.image.load('../images/player/rt6.png')]

        self.move_left_sprites = [pygame.image.load('../images/player/lt1.png'),
                                  pygame.image.load('../images/player/lt2.png'),
                                  pygame.image.load('../images/player/lt3.png'),
                                  pygame.image.load('../images/player/lt4.png'),
                                  pygame.image.load('../images/player/lt5.png'),
                                  pygame.image.load('../images/player/lt6.png')]

        self.move_down_sprites = [pygame.image.load('../images/player/dt1.png'),
                                  pygame.image.load('../images/player/dt2.png'),
                                  pygame.image.load('../images/player/dt3.png'),
                                  pygame.image.load('../images/player/dt4.png'),
                                  pygame.image.load('../images/player/dt5.png'),
                                  pygame.image.load('../images/player/dt6.png')]

        self.image = self.move_down_sprites[0]
        self.rect = self.image.get_rect()
        self.rect.midtop = self.screen_rect.midtop

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
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _can_move(self):
        return self._is_in_screen()

    def update(self):
        if self.change_direction_delay == 0:
            self.direction = random.choice(['R', 'L', 'U', 'D'])
            self.change_direction_delay = self.settings.enemy_change_direction_delay
        else:
            self.change_direction_delay -= 1

        rect = self.rect.copy()
        if self.is_moving:
            if self.direction == 'R':
                self.image = self.move_right_sprites[self._get_animation_idx() // 5]
                self.rect.x += self.speed
            elif self.direction == 'L':
                self.image = self.move_left_sprites[self._get_animation_idx() // 5]
                self.rect.x -= self.speed
            elif self.direction == 'U':
                self.image = self.move_up_sprites[self._get_animation_idx() // 5]
                self.rect.y -= self.speed

            elif self.direction == 'D':
                self.image = self.move_down_sprites[self._get_animation_idx() // 5]
                self.rect.y += self.speed
        if not self._can_move():
            self.rect = rect

    def _is_in_screen(self):
        return self.screen_rect.contains(self.rect)

    def _get_animation_idx(self):
        self.animation_count += 1
        if self.animation_count >= 30:
            self.animation_count = 0
        return self.animation_count

    def draw(self):
        self.screen.blit(self.image, self.rect)

