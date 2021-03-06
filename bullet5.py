import pygame
from pygame.sprite import Sprite

#class inherits from Sprite , which we import from the pygame .sprite module.
#When you use sprites, you can group related elements in your game and act on all the grouped elements at once.
class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        #bullet is actually just a rect
        #coordinates from top left corner
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midright

        # Store the bullet's position as a decimal value.
        self.x = 0
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet RIGHT the screen."""
        # Update the decimal position of the bullet.
        self.x += self.settings.bullet_speed
        # Update the rect position (flying bullet)
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)