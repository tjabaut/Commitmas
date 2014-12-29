__author__ = 'tjabaut'

import random
from flask import Flask, render_template

## Add Flask
app = Flask(__name__)

@app.route('/')
def coinflip(name=None):
    outcome = random.randint(0, 1)
    if outcome == 0:
        #print "Heads"
        flip = "Heads"

    else:
        #print "Tails"
        flip = "Tails"

    #print flip
    #return flip
    return render_template('hello.html', name=flip)


if __name__ == '__main__':
    app.debug = True
    app.run()


## Function to perform the act of flipping a coin and displaying results
## in a traditional Heads, or Tails.


#result = coinflip()
#print result
#a = coinflip()
# print a

## Test Function Call
#a = coinflip()
#print a

# raw_input("How many flips would you like? ")