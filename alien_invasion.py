#The pygame module con­tains the functionality we need to make a game
import pygame
#we’ll use tools in the sys to exit the game when the player quits
import sys

class AlienInvasion:
    """ Overall class to manage assets and behavior """
    def __init__(self):
        """ Initialize the game, and create game resources """
        pygame.init()

        #create a display window, on which we’ll draw all the game’s graphical ele­ments
        #We assign this dis­play window to the attribute self.screen , so it will be available in all methods in the class.
        self.screen = pygame.display.set_mode((1200,800)) #this object is called surface, it reps the entire game window
        pygame.display.set_caption('Alien Invasion')
    
    def run_game(self):
        """ Start the main loop for the game """
        while True:
            #watch for keyboard and mouse events
            #function returns a list of events that have taken place since the last time this function was called
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #make the most recently drawn screen visible
            pygame.display.flip()

#programm execution 
if __name__ == '__main__':
    #make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
