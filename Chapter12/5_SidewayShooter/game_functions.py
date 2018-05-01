import pygame, sys

from bullet import Bullet

def check_event(settings, screen, rocket, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_UP:
                rocket.move('up')
            elif event.key == pygame.K_DOWN:
                rocket.move('down')
            elif event.key == pygame.K_SPACE:
                if len(bullets) < settings.max_bullets:
                    new_bullet = Bullet(screen, rocket)
                    bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                rocket.stop()

def update(settings, screen, rocket, bullets):
    screen.fill(settings.bg_color)
    rocket.blitme()
    bullet_functions(bullets, rocket.screen_rect)
    rocket.update()
    pygame.display.flip()

def bullet_functions(bullets, screen_rect):
    for bullet in bullets.sprites():
        bullet.update()
        bullet.draw_bullet()
    for bullet in bullets.copy():
        if bullet.rect.left >= screen_rect.right:
            bullets.remove(bullet)

