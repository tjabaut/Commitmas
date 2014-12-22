__author__ = 'tjabaut'

import random


def coinflip():
    outcome = random.randint(0, 1)
    return outcome

# print coinflip

if coinflip() == 0:
    print "Heads"
else:
    print "Tails"
