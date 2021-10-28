import game.constants
from game.actor import Actor
from game.point import Point

class Answer:
    def __init__(self):
        super().__init__()
        self._actor = Actor()
        self._buffer.set_text("-Buffer: ")
        self._text = ("-Buffer: ")

    def update_text(self, text):
        if text != "*":
            self._text += text
            self.buffer.set_text
        else:
            pass