import sys, pygame

def check_events():
    """Respond to in-game events like keypresses etc"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, screen, character):
    """Updates images on the screen and then flip"""
    screen.fill(settings.bg_color)
    character.blitme()
    pygame.display.flip()