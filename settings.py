from screeninfo import get_monitors

class Settings():
    #class to store settings
    def __init__(self) -> None:
        monitor = get_monitors()[0]
        self.width = monitor.width
        self.height = monitor.height
        self.screen_width = self.width
        self.screen_height = self.height
        self.bg_color = (15, 22, 66)
        #speed factor
        self.ship_speed_factor=self.screen_width*0.003