import pygame

class Ship:
    """ a class to manage the ship """

    def __init__(self, ai_game):
        """ initialize the ship and set its starting position """
        #assign the screen to an attribute of Ship , so we can access it easily in all the methods in this class
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image from a folder and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midleft = self.screen_rect.midleft
        #self.rect.midbottom = self.screen_rect.center
        """ 
        top, left, bottom, right
        topleft, bottomleft, topright, bottomright
        midtop, midleft, midbottom, midright
        center, centerx, centery
        size, width, height 
        """
        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Ship settings
        self.ship_speed = 1.5

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect
        #stop when reached the edge of the screen
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed 
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """ Draw the ship at this current location on screen """
        self.screen.blit(self.image, self.rect)
