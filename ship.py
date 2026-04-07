import pygame

class Ship():

    def __init__(self, screen):
        # Initialize the ship and set it's starting point
        self.screen = screen

        # Load the ship image and get it's rectangle
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        # draw a ship at it's current location
        self.screen.blit(self.image, self.rect)