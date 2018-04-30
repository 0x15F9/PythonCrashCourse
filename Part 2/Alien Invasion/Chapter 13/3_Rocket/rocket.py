import pygame

class Rocket():
    """Class definition for creating a Rocket"""
    def __init__(self, screen):
        self.screen         = screen

        self.image          = pygame.image.load('assets/rocket.bmp')
        self.rect           = self.image.get_rect()
        self.screen_rect    = self.screen.get_rect()
        self.dx             = 1
        
        self.moving_right   = False
        self.moving_left    = False
        self.moving_up      = False
        self.moving_down    = False

        self.rect.centerx   = float(self.screen_rect.centerx)
        self.rect.centery   = float(self.screen_rect.centery)


    def blitme(self):
        """Blit rocket on screen"""
        if self.moving_right:
            self.move('right')
        if self.moving_left:
            self.move('left')
        if self.moving_up:
            self.move('up')
        if self.moving_down:
            self.move('down')
        self.screen.blit(self.image, self.rect)

    def move(self, direction):
        if direction == "up" and self.rect.centery > 0:
            self.rect.centery -= self.dx
            self.moving_up = True
        if direction == "down" and self.rect.centery < self.screen_rect.bottom:
            self.rect.centery += self.dx
            self.moving_down = True
        if direction == "right" and self.rect.centerx < self.screen_rect.right:
            self.rect.centerx += self.dx
            self.moving_right = True
        if direction == "left" and self.rect.centerx > self.screen_rect.left:
            self.rect.centerx -= self.dx
            self.moving_left = True

    def stop_moving(self):
        self.moving_right   = False
        self.moving_left    = False
        self.moving_up      = False
        self.moving_down    = False