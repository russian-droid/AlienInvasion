'''
13-1. Stars: Find an image of a star. Make a grid of stars appear on the screen.
13-2. Better Stars: You can make a more realistic star pattern by introducing
randomness when you place each star. Recall that you can get a random num-
ber like this:
from random import randint
random_number = randint(-10, 10)
This code returns a random integer between −10 and 10. Using your code
in Exercise 13-1, adjust each star’s position by a random amount.
'''

#The pygame module con­tains the functionality we need to make a game
import pygame
#we’ll use tools in the sys to exit the game when the player quits
import sys

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from random import randint

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
        pygame.display.set_caption('Alien Invasion')

        #above we created a screen, now we can create an obj ship from imported class ship
        self.ship = Ship(self)

        #bullets
        self.bullets = pygame.sprite.Group()

        #aliens
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Set the background color.
        self.bg_color = (230, 230, 230)
    
    def _create_fleet(self):
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the first row of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        # Create an alien and place it in the row.
        alien = Alien(self)
        #create a random number
        random_number = randint(1, 4)
        alien_width, alien_height = alien.rect.size
        #use random number
        #alien.x = alien_width + 2 * alien_width * alien_number
        alien.x = alien_width + random_number * alien_width * alien_number
        alien.rect.x = alien.x
        #use random number
        #alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        alien.rect.y = alien.rect.height + random_number * alien.rect.height * row_number
        self.aliens.add(alien)

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
            if bullet.rect.bottom <= 0:
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
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        #exit on Q
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

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
        #make an alien
        self.aliens.draw(self.screen)

        #make the most recently drawn screen visible
        pygame.display.flip()

#programm execution 
if __name__ == '__main__':
    #make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()