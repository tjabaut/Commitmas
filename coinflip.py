__author__ = 'tjabaut'

import random
from flask import Flask, render_template

## Add Flask
app = Flask(__name__)

@app.route('/')
def coinflip(name=None):
#def coinflip():
    outcome = random.randint(0, 1)
    if outcome == 0:
        #print "Heads"
        #print "Background: Blue"
        #print "Image: /images/heads.jpg"
        ## Create a list to hold all items
        flip = ["Heads", "blue", "static/heads.png"]
        return render_template('index.html', name=flip)

    else:
        #print "Tails"
        #print "Background: Orange"
        #print "Image: /images/tails.jpg"
        ## Create a list to hold all items
        flip = ["Tails", "red", "static/tails.png"]
        return render_template('index.html', name=flip)

    #print flip
    #return flip
    #return render_template('index.html', name=flip)


if __name__ == '__main__':
    app.debug = True
    app.run()


## Function to perform the act of flipping a coin and displaying results
## in a traditional Heads, or Tails.


result = coinflip()
#print result

## Unpack the variables

# response = input("How many flips would you like? ")
# print response
#
# Tally = 1
# ## Loop
# for item in range(response):
#     a = coinflip()
#     print a
#     a.append(Tally)
#     print a
#     Tally = Tally + 1

# print a

## Test Function Call
#a = coinflip()
#print a



## Create an array to store the results

## Potentially run analytics on the results