
import pygame
from src.bullet import Bullet
from src.tank import Tank


class Player(Tank):

    def __init__(self, bt_game):
        super().__init__(bt_game)
        self.speed = bt_game.settings.player_speed

        self.move_sprites = [pygame.image.load('../images/player/ut1.png').convert_alpha(),
                             pygame.image.load('../images/player/ut2.png').convert_alpha(),
                             pygame.image.load('../images/player/ut3.png').convert_alpha(),
                             pygame.image.load('../images/player/ut4.png').convert_alpha(),
                             pygame.image.load('../images/player/ut5.png').convert_alpha(),
                             pygame.image.load('../images/player/ut6.png').convert_alpha()]
        self.rect.midbottom = self.screen_rect.midbottom

    def update(self, bt_game):
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
        return pygame.sprite.spritecollideany(self, bt_game.enemies)
