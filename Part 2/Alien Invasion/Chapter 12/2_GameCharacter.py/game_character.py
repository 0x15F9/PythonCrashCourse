import sys, pygame

from settings import Settings
from character import Dook
import game_functions as gf

def run_game():
    pygame.init()
    gc_settings = Settings()

    screen = pygame.display.set_mode(gc_settings.screen_size())
    dook = Dook(screen)

    while True:
        gf.check_events()
        gf.update_screen(gc_settings, screen, dook)


run_game()