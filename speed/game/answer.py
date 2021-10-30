from game import constants
from game.actor import Actor
from game.point import Point
class Answer(Actor):
    def __init__(self):
        super().__init__()
        # self._buffer = Actor()
        # self._buffer.set_text("-Buffer: ")
        # self._text = ("-Buffer: ")
        # self._buffer._position = Point(0,20)
        self._word = " "
        position = Point(1, constants.MAX_Y)
        self.set_position(position)
        self.set_text(f"Buffer: {self._word}")

    def update_text(self, letter):
        """Adds the given letter to the word and sets the buffer text with the word and letter.
        
        Args:
            self (set_text): An instance of word.
            letter (letter): An instance of letter
        """
        self._word += letter
        self.set_text(f"Buffer: {self._word}")


    def get_word(self):
        """ Gets the cuurent word 
        
        Args:
            self (Buffer): An instance of buffer"""
        
        return self._word

    def reset(self):
        """ Resets the buffer
        
        Args:
            self (Buffer): An instance of buffer"""
        
        self._word = ''
        return self._word


    # def update_text(self, text):
    #     if text != "*":
    #         self._text += text
    #         self._buffer.set_text = text
    #     else:
    #         self._text = "-Buffer: "
    #         self._buffer.set_text()
    # def get_buffer(self):
    #     return self._buffer

    