class Settings():
    """Class for storing GameCharacter settings"""
    def __init__(self):
        """Initialize Settings class"""
        self.caption = "Game Character"
        self.window_width = 640
        self.window_height = 480
        # self.bg_color = (18, 100, 186)
        self.bg_color = (255, 255, 255)
    def screen_size(self):
        return (self.window_width, self.window_height)