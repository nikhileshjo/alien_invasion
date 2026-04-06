import sys
import pygame

def run_game():

    # initialize pygame
    pygame.init()

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)

    # start main loop
    while True:
        
        # watch keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        
        # redrawing with new color
        screen.fill(bg_color)
        
        # refresh screen with updates
        pygame.display.flip()

run_game()