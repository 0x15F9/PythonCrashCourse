import pygame

class Dook():
    """Class for creating the character dook"""
    def __init__(self, screen):
        """initialize the character dook"""
        self.screen         = screen

        self.image          = pygame.image.load('character/idle.bmp')
        self.rect           = self.image.get_rect()
        self.screen_rect    = screen.get_rect()

        self.rect.centerx   = self.screen_rect.centerx
        self.rect.bottom    = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)