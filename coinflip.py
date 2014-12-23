__author__ = 'tjabaut'

import random

# Function to perform the act of flipping a coin and displaying results
# in a traditional Heads, or Tails.
def coinflip():
    outcome = random.randint(0, 1)
    if outcome == 0:
        print "Heads"
    else:
        print "Tails"

    return outcome


a = coinflip()
# print a