from game import constants
from game.point import Point

class Actor():
    '''A visible, moveable thing that participates in the game. 
    The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.
    Stereotype:
        
        Information Holder
    Attributes:
        _text (string): is the word that is representing the actor
        _position (Point): is the actors location 
        _velocity (Point): this is the actor speed and direction '''

    def __init__(self):
        ''' Class constructor.
        Args:
            self (Actor): an instance of Actor'''
        self._text = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_position(self):
        '''this gets the actor position 
        Args:
            self (Actor): an instance of Actor.
        Returns:
            Point: this is the actor position'''

        return self._position

    def get_text(self):
        '''this gets the word of the actor
        Args:
            self (Actor): an instance of Actor.
        Returns:
            string: this is the view of the actor '''

        return self._text

    def get_velocity(self):
        '''this gets the direction and speed of the actor
        Args:
            self (Actor): an instance of Actor.
        Returns:
            Point: the actors speed and direction.
            '''

        return self._velocity

    def next_move(self):
        '''this moves the actor to the next position as indicated by the velocity. 
        Args:
            self (Actor): an instance of Actor.
        '''

        x1 = self._position.get_x()
        y1 = self._position.get_y()
        x2 = self._velocity.get_x()
        y2 = self._velocity.get_y()
        x = 1 + (x1 + x2 - 1)
        y = 1 + (y1 + y2 - 1)
        position = Point(x,y)
        self._position = position

    def set_position(self, position):
        '''Updates the actors position to the given one.
        
        Args:
            self (Actor): an instance of Actor.
            position (Point): the given position.
        '''

        self._position = position

    def set_text(self, text):
        '''Updates actor text to given value

        Args:
            self (Actor): an instance of Actor.
            text (string): The given value.
        '''

        self._text = text

    def set_velocity(self, velocity):
        '''Update actor's velocity to the set given velocity. 
        
        Args:
            self (Actor): An instance of Actor.
            position (Point): The given set velocity.
        '''

        self._velocity = velocity 