import constants
import os
import random
import sys
from asciimatics.event import KeyboardEvent

from game.constants import STARTING_WORDS

#from point import Point

PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/words.txt").read().splitlines()
list = []
for i in range(constants.STARTING_WORDS):
    list.append(LIBRARY[random.randint(0, 10000)])
    #print(LIBRARY[random.randint(0, 10000)])


print(list)


x = random.randint(2, constants.MAX_X)
y = random.randint(2, constants.MAX_Y)
postition = Point(x, y)
#self.set_position(postiion)
print(x, y)


def get_letter(self):
    """Gets the letter that was typed. If the enter key was pressed returns an asterisk.

    Args:
        self (InputService): An instance of InputService.

    Returns:
        string: The letter that was typed.
    """
    result = ""
    event = self._screen.get_key()
    if not event is None:
        if event == 27:
            sys.exit()
        elif event == 10:
            result = "*"
        elif event >= 97 and event <= 122: 
            result = chr(event)
    return result

for i in range(constants.STARTING_WORDS):
    word_list = [constants.LIBRARY]
    print(word_list)


