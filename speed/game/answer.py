from game import constants
from game.actor import Actor
from game.point import Point
class Answer:
    def __init__(self):
        super().__init__()
        self._buffer = Actor()
        self._buffer.set_text("-Buffer: ")
        self._text = ("-Buffer: ")
        self._buffer._position = Point(0,20)

    def update_text(self, text):
        if text != "*":
            self._text += text
            self._buffer.set_text = text
        else:
            self._text = "-Buffer: "
            self._buffer.set_text()
    def get_buffer(self):
        return self._buffer

    