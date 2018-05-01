import pygame

class Rocket():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image  = pygame.image.load('asset/rocket.bmp')
        self.rect   = self.image.get_rect()
        self.dx     = 0.5

        self.rect.left = 0 #self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        self.center = float(self.rect.centery)
        self.stop()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def stop(self):
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up:
            self.move('up')
        if self.moving_down:
            self.move('down')

    def move(self, direction):
        if direction == "up" and self.rect.top > 0:
            self.center -= self.dx
            self.moving_up = True
        elif direction == "down" and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.dx
            self.moving_down = True
        self.rect.centery = self.center