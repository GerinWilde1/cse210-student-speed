import constants
import os
import random

PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/words.txt").read().splitlines()

for i in range(constants.STARTING_WORDS):
    print(LIBRARY[random.randint(0, 10000)])
