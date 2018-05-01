import pygame

class Settings():
    def __init__(self):
        self.caption = "Rocket"
        self.screen_width = 720
        self.screen_height = 480
        self.bg_color = (0, 0, 59)

    def screen_size(self):
        return (self.screen_width, self.screen_height)