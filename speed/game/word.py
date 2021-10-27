import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here
class Word(Actor):
    """The food class. It keeps track of everything that the food is doing. moves it when needed and when collected helps to grow the snakes tail."""


    def __init__(self):
        """invokes the superclass, calls reset() when it's needed in order to pull a new word
        points keep track of the total number of correct words typed"""
        
        super().__init__()#this makes sure that everything in the Act class is pulled over and is ready to be used.
        self._points = 0
        self.reset()
        pass


    def get_points(self):
        """This helps to call _points whenever it is needed without changing the origional"""

        return self._points

    def move_words(self, direction):
        """Get the (rendomized)direction that the words move"""# maybe
        
        pass

    def reset(self):
        """pulls new word and puts it in a random location and maybe sets it to start moving."""
        pass