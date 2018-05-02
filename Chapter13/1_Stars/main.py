import sys, pygame
from pygame.sprite import Group
from star import Star

def main():
    pygame.init()

    screen = pygame.display.set_mode((920, 640))
    pygame.display.set_caption("Stars")

    galaxy = Group()
    star = Star(screen)

    for star_x in range(star.per_row):
        for star_y in range(star.per_col):
            star = Star(screen)
            star.x = star.width * star_x
            star.y = star.width * star_y
            star.rect.x = star.x
            star.rect.y = star.y
            galaxy.add(star)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
        screen.fill((0, 20, 137))
        for star in galaxy:
            star.blitme()
        pygame.display.flip()

main()