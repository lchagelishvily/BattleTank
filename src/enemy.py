import pygame
import random
from src.tank import Tank

from src.bullet import Bullet


class Enemy(Tank):

    def __init__(self, bt_game):
        super().__init__(bt_game)
        self.settings = bt_game.settings
        self.speed = bt_game.settings.enemy_speed
        self.is_moving = True
        self.direction = 'D'
        self.bullets = pygame.sprite.Group()
        self.change_direction_delay = bt_game.settings.enemy_change_direction_delay

        self.move_sprites = [pygame.image.load('../images/player/ut1.png'),
                             pygame.image.load('../images/player/ut2.png'),
                             pygame.image.load('../images/player/ut3.png'),
                             pygame.image.load('../images/player/ut4.png'),
                             pygame.image.load('../images/player/ut5.png'),
                             pygame.image.load('../images/player/ut6.png')]

        self.rect.midtop = self.screen_rect.midtop

    def update(self, bt_game):
        if self.change_direction_delay == 0:
            self.direction = random.choice(['R', 'L', 'U', 'D'])
            self.change_direction_delay = self.settings.enemy_change_direction_delay
        else:
            self.change_direction_delay -= 1

        rect = self.rect.copy()
        if self.is_moving:
            if self.direction == 'R':
                self.image = self.move_sprites[self._get_animation_idx() // 5]
                self.image = pygame.transform.rotate(self.image, -90)
                self.rect.x += self.speed
            elif self.direction == 'L':
                self.image = self.move_sprites[self._get_animation_idx() // 5]
                self.image = pygame.transform.rotate(self.image, 90)
                self.rect.x -= self.speed
            elif self.direction == 'U':
                self.image = self.move_sprites[self._get_animation_idx() // 5]
                self.rect.y -= self.speed

            elif self.direction == 'D':
                self.image = self.move_sprites[self._get_animation_idx() // 5]
                self.image = pygame.transform.rotate(self.image, 180)
                self.rect.y += self.speed
        if not self._can_move(bt_game):
            self.rect = rect

    def _is_collided(self, bt_game):
        bt_game.all_tanks.remove(self)
        is_collided = pygame.sprite.spritecollideany(self, bt_game.all_tanks)
        bt_game.all_tanks.add(self)
        return is_collided

    def draw(self):
        self.screen.blit(self.image, self.rect)

