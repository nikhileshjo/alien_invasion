import sys
import pygame
from settings import Settings

def run_game():

    # initialize pygame and settings
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # start main loop
    while True:
        
        # watch keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        
        # redrawing with new color
        screen.fill(ai_settings.bg_color)
        
        # refresh screen with updates
        pygame.display.flip()

run_game()