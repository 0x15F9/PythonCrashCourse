import pygame
from random import randint as random
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height

        self.image = pygame.image.load('star.bmp')
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height


        self.per_row = int(self.screen_width / self.width)
        self.per_col = int(self.screen_height / self.height)

        # self.x = random(0, self.screen_width)
        # self.y = random(0, self.screen_height)
        # self.rect.x = self.x
        # self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


