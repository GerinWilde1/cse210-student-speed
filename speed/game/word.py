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
        flying_words = constants.LIBRARY



    def get_points(self):
        """This helps to call _points whenever it is needed without changing the origional"""

        return self._points

    #def move_words(self, direction):
    def move_next(self):
               
        x1 = self._position.get_x()
        y1 = self._position.get_y()
        x2 = self._velocity.get_x()
        y2 = self._velocity.get_y()
        x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1)
        y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)
        position = Point(x, y)
        self._position = position

    def reset(self):
        """pulls new word and puts it in a random location and maybe sets it to start moving."""
        pass