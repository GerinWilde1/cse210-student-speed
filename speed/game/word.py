import os
import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Word class here
class Word(Actor):
    """The Word class. It keeps track of everything that the Word is doing. moves it when needed and when collected helps to grow the scores."""
    

    def __init__(self):mhgcv
        """invokes the superclass, calls reset() when it's needed in order to pull a new word
        points keep track of the total number of correct words typed
        
        Args:
            self (Actor): an instance of Actor.
        
        """
        
        super().__init__()#this makes sure that everything in the Act class is pulled over and is ready to be used.
        # self._points = 0
        # self.reset()
        # PATH = os.path.dirname(os.path.abspath(__file__))
        # constants.LIBRARY = open(PATH + "/words.txt").read().splitlines()
        # self.flying_words = constants.LIBRARY
        # self._velocity = Point(random.randint(-1, 1), random.randint(-1, 1))
        # self._list = []
        self._words = []
        self._points = 0
        self._reset()


        

    
    def get_all(self):
        """Gets all the words from the list of words the player can try to type. 
        
        Args:
            self (words): instances of words
        returns:
            list of words to be typed
        """
        return self._words
        

    
    def move_words(self, word, x, y):
        
        direction = Point(x, y)
        word = self._words[word]
        
        word.set_velocity(direction)
        
        word.next_move()
        

    
    def word_check(self, word):
        '''Checks the users typed input with the word list. Gets 
        Args:
            self (words): an instance of Words.
            text (string) the words text.
        '''    
        
        for x in self._words:
            if x.get_text() == word:
                self._set_points(word)
                x.set_text(constants.LIBRARY[random.randint(0, len(constants.LIBRARY))])
                return self._points
        else:
            return 0


    def _add_word(self, text, position, velocity):
        """Adds a new word to the words list using the passed in text, position and velocity.
        
        Args:
            self (Words): an instance of words
            text (string) the words text.
            position (Point): The word's position.
            velocity (Point): The word's velocity.
        """
        word = Actor()
        word.set_text(text)
        word.set_position(position)
        word.set_velocity(velocity)
        self._words.append(word)
        

    
    def _reset(self):
        """Resets the word list by adding words from the library constant words.txt.
        
        Args:
            self (Words): an instance of Words.
        """

        
        for i in range(constants.STARTING_WORDS):
            x = random.randint(1, constants.MAX_X - 2)
            y = random.randint(1, constants.MAX_Y - 2)
            text = constants.LIBRARY[random.randint(0, len(constants.LIBRARY))]
            position = Point(x, y - i)
            velocity = Point(1, 0)

            self._add_word(text, position, velocity)

    
    def _set_points(self, word):
        """Sets _points equal to the length of word.
        Args:
            self (Words): an instance of Words.
            word (string): the word to check the length of.
        """
        self._points = len(word)

    # def get_points(self):
    #     """This helps to call _points whenever it is needed without changing the origional
        
    #     Args:
    #         self (Word): an instance of Word.
        
    #     """

    #     return self._points

    # #def move_words(self, direction):
    # def move_words(self):
    #     return self._velocity
               
    #     # x1 = self._position.get_x()
    #     # y1 = self._position.get_y()
    #     # x2 = self._velocity.get_x()
    #     # y2 = self._velocity.get_y()
    #     # x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1)
    #     # y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)
    #     # position = Point(x, y)
    #     # self._position = position

    # def reset(self):
    #     """pulls new word and puts it in a random location and maybe sets it to start moving.
        
    #      Args:
    #         self (Word): an instance of Word.
                
    #     """
        
    #     self.points = 1
    #     for i in range(constants.STARTING_WORDS):
    #         self._list.append(constants.LIBRARY[random.randint(0, 10000)])
    #     x = random.randint(2, constants.MAX_X)
    #     y = random.randint(2, constants.MAX_Y)
    #     position = Point(x, y)
    #     self.set_position(position)

    #     for i in self._list:
    #         i = self.set_position(position)
 