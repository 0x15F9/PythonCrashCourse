import pygame

class Settings():
    """Class definition for storing general game variables and functions"""
    def __init__(self):
        """Initialize the class"""
        self.screen_width   = 720
        self.screen_height  = 480
        self.caption        = "Sideway Shooter"
        self.bg_color       = (0, 4, 59)

        self.max_bullets = 3

    def screen_size(self):
        return (self.screen_width, self.screen_height)