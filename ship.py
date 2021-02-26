import pygame

class Ship:
    """ a class to manage the ship """

    def __init__(self, ai_game):
        """ initialize the ship and set its starting position """
        #assign the screen to an attribute of Ship , so we can access it easily in all the methods in this class
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image from a folder and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ Draw the ship at this current location on screen """
        self.screen.blit(self.image, self.rect)
