import constants
import os
import random

PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/words.txt").read().splitlines()
list = []
for i in range(constants.STARTING_WORDS):
    list.append(LIBRARY[random.randint(0, 10000)])
    #print(LIBRARY[random.randint(0, 10000)])
print(list)
