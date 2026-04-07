import sys
import pygame

def check_events():
    # respond to keypresses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

def update_screen(ai_settings, screen, ship):
    # redrawing with new color
    screen.fill(ai_settings.bg_color)
    ship.blitme()        
        
    # refresh screen with updates
    pygame.display.flip()