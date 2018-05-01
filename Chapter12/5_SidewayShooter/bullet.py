import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen, ship):
        super().__init__()
        self.screen = screen

        self.width  = 5
        self.height = 2
        self.color = (255, 255, 255)
        self.speed_factor = 0.75

        self.rect   = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)