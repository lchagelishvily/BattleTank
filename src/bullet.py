
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, owner):
        super().__init__()
        self.screen = owner.screen
        self.settings = owner.settings
        self.color = self.settings.bulet_color
        self.direction = owner.direction
        self.owner = owner
        if self.direction == 'U':
            self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
            self.rect.midtop = owner.rect.midtop
        elif self.direction == 'D':
            self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
            self.rect.midbottom = owner.rect.midbottom
        elif self.direction == 'L':
            self.rect = pygame.Rect(0, 0, self.settings.bullet_height, self.settings.bullet_width)
            self.rect.midleft = owner.rect.midleft
        elif self.direction == 'R':
            self.rect = pygame.Rect(0, 0, self.settings.bullet_height, self.settings.bullet_width)
            self.rect.midright = owner.rect.midright
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        if self.direction == 'U':
            self.y -= self.settings.bullet_speed
        elif self.direction == 'D':
            self.y += self.settings.bullet_speed
        elif self.direction == 'L':
            self.x -= self.settings.bullet_speed
        elif self.direction == 'R':
            self.x += self.settings.bullet_speed

        self.rect.x = self.x
        self.rect.y = self.y

        if self.rect.top < 0\
                or self.rect.bottom > self.owner.screen_rect.bottom\
                or self.rect.left < 0\
                or self.rect.right > self.owner.screen_rect.right:
            self.owner.bullets.remove(self)


    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
