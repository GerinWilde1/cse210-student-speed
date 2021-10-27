import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here
class Word(Actor):
    """The food class. It keeps track of everything that the food is doing. moves it when needed and when collected helps to grow the snakes tail."""


    def __init__(self):
        pass


    def get_points(self):
        """This helps to call _points whenever it is needed without changing the origional"""

        return self._points

    def reset(self):
        """moves the food to a new random location then it's picked up."""
        pass