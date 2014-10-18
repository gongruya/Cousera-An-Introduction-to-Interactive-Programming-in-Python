# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

maxnum = 100
secret_number = 0
remain = 0
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global remain
    remain = int(math.ceil(math.log(maxnum, 2)))
    secret_number = random.randrange(0, maxnum)
    print 'Starting a new game with the range [0, ' + str(maxnum) +').'
    print 'You have', remain, 'chances to guess.\n'
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global maxnum
    maxnum = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global maxnum
    maxnum = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    print 'Guess was', guess
    x = int(guess)
    new = False
    if x > secret_number:
        print 'Lower'
    elif x < secret_number:
        print 'Higher'
    else:
        print 'Correct\n'
        new = True

    global remain
    remain = remain - 1
    if not new:
        if remain > 1:
            print 'You have', remain, 'chances remain.\n'
        elif remain == 1:
            print 'You have', remain, 'chance remains.\n'
        else:
            print 'Game over, the secret number is', secret_number, '\n'
            new = True

    if new:
        new_game()
        
    
# create frame
f = simplegui.create_frame("Guess the number", 300, 300)

# register event handlers for control elements and start frame
f.add_button('New Game with Range 100', range100, 200)
f.add_button('New Game with Range 1000', range1000, 200)
f.add_button('New Game with Current Range', new_game, 200)
f.add_input("guess", input_guess, 100)

# call new_game 
f.start()
new_game()
# always remember to check your completed program against the grading rubric
