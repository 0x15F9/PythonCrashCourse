import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load('rain.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.dy = float(0)
        self.ddy = float(9.81)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.gravitatize()
        self.y += self.dy * 0.1
        self.rect.y = self.y

    def gravitatize(self):
        self.dy += self.ddy * 0.1