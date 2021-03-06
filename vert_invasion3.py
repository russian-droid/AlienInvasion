""" 
12-6. Sideways Shooter: Write a game that places a ship on the left side of the
screen and allows the player to move the ship up and down. Make the ship fire
a bullet that travels right across the screen when the player presses the space-
bar. Make sure bullets are deleted once they disappear off the screen. 
"""



#The pygame module con­tains the functionality we need to make a game
import pygame
#we’ll use tools in the sys to exit the game when the player quits
import sys

from settings3 import Settings
from ship3 import Ship
from bullet3 import Bullet

class AlienInvasion:
    """ Overall class to manage assets and behavior """
    def __init__(self):
        """ Initialize the game, and create game resources """
        pygame.init()
        self.settings = Settings()
        
        #create a display window, on which we’ll draw all the game’s graphical ele­ments
        #We assign this dis­play window to the attribute self.screen , so it will be available in all methods in the class.
        #this object is called surface, it reps the entire game window
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 
        pygame.display.set_caption("UP down")

        #above we created a screen, now we can create an obj ship from imported class ship
        self.ship = Ship(self)

        #bullets
        self.bullets = pygame.sprite.Group()

        # Set the background color.
        self.bg_color = (230, 230, 230)
    
    def run_game(self):
        """ Start the main loop for the game """
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            #when the rect (bullet) leaves screen, it will be deleted
            if bullet.rect.left >= self.settings.screen_width:
            #or a static version
            #if bullet.rect.left >= 1200:
                self.bullets.remove(bullet)
        #print(len(self.bullets)) #just to check that bullets disappear

    def _check_events(self):
        """ Respond to keypresses and mouse events """
        #watch for keyboard and mouse events
        #function returns a list of events that have taken place since the last time this function was called
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #watching for keydown events
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        #if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            #self.ship.moving_right = True
        #elif event.key == pygame.K_LEFT:
            #self.ship.moving_left = True
        if event.key == pygame.K_UP:#####
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:#####
            self.ship.moving_down = True
        #exit on Q
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        #if event.key == pygame.K_RIGHT:
            #self.ship.moving_right = False
        #elif event.key == pygame.K_LEFT:
            #self.ship.moving_left = False
        if event.key == pygame.K_UP:#####
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:#####
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """ update images on the screen, and flip to the new screen """
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #make the most recently drawn screen visible
        pygame.display.flip()

#programm execution 
if __name__ == '__main__':
    #make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()