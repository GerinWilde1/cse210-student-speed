import os
import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Word class here
class Word(Actor):
    """The Word class. It keeps track of everything that the Word is doing. moves it when needed and when collected helps to grow the scores."""
    

    def __init__(self):
        """invokes the superclass, calls reset() when it's needed in order to pull a new word
        points keep track of the total number of correct words typed
        
        Args:
            self (Actor): an instance of Actor.
        
        """
        
        super().__init__()#this makes sure that everything in the Act class is pulled over and is ready to be used.
        self._points = 0
        self.reset()
        PATH = os.path.dirname(os.path.abspath(__file__))
        constants.LIBRARY = open(PATH + "/words.txt").read().splitlines()
        self.flying_words = constants.LIBRARY
        self._list = []
        self._velocity = Point(0, -1)


    def get_points(self):
        """This helps to call _points whenever it is needed without changing the origional
        
        Args:
            self (Word): an instance of Word.
        
        """

        return self._points

    #def move_words(self, direction):
    def move_words(self):
        return self._velocity
               
        # x1 = self._position.get_x()
        # y1 = self._position.get_y()
        # x2 = self._velocity.get_x()
        # y2 = self._velocity.get_y()
        # x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1)
        # y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)
        # position = Point(x, y)
        # self._position = position

    def reset(self):
        """pulls new word and puts it in a random location and maybe sets it to start moving.
        
         Args:
            self (Word): an instance of Word.
                
        """
        list = []
        self.points = 1
        for i in range(constants.STARTING_WORDS):
            list.append(constants.LIBRARY[random.randint(0, 10000)])
        x = random.randint(2, constants.MAX_X)
        y = random.randint(2, constants.MAX_Y)
        position = Point(x, y)
        self.set_position(position)

        for i in list:
            i = self.set_position(position)
 