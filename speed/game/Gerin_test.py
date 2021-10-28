import constants
import os
import random

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
#postition = Point(x, y)
#self.set_position(postiion)
print(x, y)
