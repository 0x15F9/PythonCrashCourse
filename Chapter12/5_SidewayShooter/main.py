import pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf
from rocket import Rocket

def main():
    pygame.init()
    ss_settings     = Settings()
    screen          = pygame.display.set_mode(ss_settings.screen_size())
    ss_rocket       = Rocket(screen)
    bullets         = Group()
    pygame.display.set_caption(ss_settings.caption)

    while True:
        gf.check_event(ss_settings, screen, ss_rocket, bullets)
        gf.update(ss_settings, screen, ss_rocket, bullets)

main()

