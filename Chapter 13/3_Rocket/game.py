import pygame

from settings import Settings
import game_functions as gf
from rocket import Rocket

def run_game():
    pygame.init()
    ro_settings = Settings()

    screen = pygame.display.set_mode(ro_settings.screen_size())
    pygame.display.set_caption(ro_settings.caption)

    ro_rocket = Rocket(screen)

    while True:
        gf.event_check(ro_rocket)
        gf.update_screen(ro_settings, screen, ro_rocket)

run_game()