import sys, pygame
from pygame.sprite import Group
from star import Star
from random import randint
from time import sleep

def main():
    pygame.init()

    screen = pygame.display.set_mode((920, 640))
    pygame.display.set_caption("Stars")

    galaxy = Group()
    star = Star(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
        screen.fill((0, 20, 137))
        for star_x in range(star.per_row):
            for star_y in range(star.per_col):
                star = Star(screen)
                jut_x = star.width * star_x
                jut_y = star.width * star_y
                star.x = randint(jut_x - star.width, jut_x + star.width)
                star.y = randint(jut_y - star.height, jut_y + star.height)
                star.rect.x = star.x
                star.rect.y = star.y
                galaxy.add(star)
        for star in galaxy:
            star.blitme()
        galaxy.empty()
        pygame.display.flip()
        sleep(0.5)

main()