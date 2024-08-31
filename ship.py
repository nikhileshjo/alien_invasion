import pygame

class Ship():
    def __init__(self,screen,settings) -> None:
        #intialize the ship and set it's starting postion
        self.screen=screen
        self.settings=settings

        #load ship image and get it's rect
        self.image=pygame.image.load('images/ship.bmp')
        new_size = (self.settings.screen_width*0.05, self.settings.screen_height*0.1)
        self.image=pygame.transform.scale(self.image, new_size)
        self.rect = self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #start each ship at the bottom centre of the screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        #update the centerx value to be float for more precision
        self.center = float(self.rect.centerx)

        #movement flag
        self.moving_right=False
        self.moving_left=False

    def update(self):
        #Update the ship's position based on the movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center+=self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center-=self.settings.ship_speed_factor
        
        # Update rect object from self.center
        self.rect.centerx = self.center


    def blitme(self):
        #Draw the ship at its current location
        self.screen.blit(self.image, self.rect)

