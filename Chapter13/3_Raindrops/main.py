import pygame, time
import sys
from pygame.sprite import Group

from rain import Raindrop

def create_raindrops(screen, raindrops):
    raindrop = Raindrop(screen)
    raindrop_width = raindrop.rect.width
    raindrop_height = raindrop.rect.height
    w = screen.get_rect()
    available_space_x = w.width - 2 * raindrop_width
    number_raindrop_x = int(available_space_x / (2 * raindrop_width))
    available_space_y = w.height - 2 * raindrop_height
    number_raindrop_y = int(available_space_y / (2 * raindrop_height))

    for rdx in range(number_raindrop_x):
        for rdy in range(number_raindrop_y):
            raindrop = Raindrop(screen)
            raindrop.x = raindrop_width + 2 * raindrop_width * rdx
            raindrop.rect.x = raindrop.x
            raindrop.y = raindrop_height + 2 * raindrop_height * rdy
            raindrop.rect.y = raindrop.y
            raindrops.add(raindrop)

def main():
    pygame.init()

    screen = pygame.display.set_mode((920, 480))
    pygame.display.set_caption("Raindrops")
    raindrops = Group()
    create_raindrops(screen, raindrops)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

        pygame.display.flip()
        screen.fill((176, 176, 176))
        for rd_raindrop in raindrops:
            rd_raindrop.blitme()
            rd_raindrop.update()
        time.sleep(0.01)

main()