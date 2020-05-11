
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, owner):
        super().__init__()
        self.screen = owner.screen
        self.settings = owner.settings
        self.image = pygame.image.load('../images/bullet.png').convert_alpha()
        self.direction = owner.direction
        self.owner = owner
        self.screen_rect = owner.screen.get_rect()

        if self.direction == 'U':
            self.rect = self.image.get_rect()
            self.rect.midtop = owner.rect.midtop
        elif self.direction == 'D':
            self.image = pygame.transform.rotate(self.image, 180)
            self.rect = self.image.get_rect()
            self.rect.midbottom = owner.rect.midbottom
        elif self.direction == 'L':
            self.image = pygame.transform.rotate(self.image, 90)
            self.rect = self.image.get_rect()
            self.rect.midleft = owner.rect.midleft
        elif self.direction == 'R':
            self.image = pygame.transform.rotate(self.image, -90)
            self.rect = self.image.get_rect()
            self.rect.midright = owner.rect.midright
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def _is_in_screen(self):
        return self.screen_rect.contains(self.rect)

    def update(self):
        if self.direction == 'U':
            self.rect.y -= self.settings.bullet_speed
        elif self.direction == 'D':
            self.rect.y += self.settings.bullet_speed
        elif self.direction == 'L':
            self.rect.x -= self.settings.bullet_speed
        elif self.direction == 'R':
            self.rect.x += self.settings.bullet_speed

        if not self._is_in_screen():
            self.kill()