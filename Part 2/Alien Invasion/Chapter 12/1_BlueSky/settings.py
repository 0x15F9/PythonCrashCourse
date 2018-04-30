class Settings():
    """A class to store all the settings for BlueSky"""
    def __init__(self):
        """Initialize BlueSky settings"""
        self.caption = "Blue Sky"
        self.window_width = 640
        self.window_height = 480
        self.bg_color = (18, 100, 186)
    def screen_size(self):
        return (self.window_width, self.window_height)