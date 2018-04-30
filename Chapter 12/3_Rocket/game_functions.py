import sys, pygame

def event_check(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rocket.move('right')
            elif event.key == pygame.K_LEFT:
                rocket.move('left')
            elif event.key == pygame.K_UP:
                rocket.move('up')
            elif event.key == pygame.K_DOWN:
                rocket.move('down')
        elif event.type == pygame.KEYUP:
            rocket.stop_moving()


def update_screen(settings, screen, rocket):
    screen.fill(settings.bg_color)
    rocket.blitme()
    pygame.display.flip()