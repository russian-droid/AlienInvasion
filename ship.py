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
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        # Ship settings
        self.ship_speed = 1.5

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect
        #stop when reached the edge of the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """ Draw the ship at this current location on screen """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)