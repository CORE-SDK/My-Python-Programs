# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# initialize global variables used in your code

secret_number = 0
low = 0
high = 100
trial_count = 0

# helper function to start and restart the game
def new_game():
    # remove this when you add your code  
    global secret_number, trial_count
    secret_number = random.randrange(low, high)
    if high == 100:
        trial_count = 7
    elif high == 1000:
        trial_count = 10
    #print low, high, secret_number
    print "New game started"
    print "Range is set to", low, "-", high
    print "Number of tries remaining", trial_count, "\n"


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global low, high, trial_count
    # remove this when you add your code    
    high = 100
    trial_count = 7
    print "The range is changed to 100\n"
    #print low, high
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global low, high, trial_count
    # remove this when you add your code    
    high = 1000
    trial_count = 10
    print "The range is changed to 1000\n"
    #print low, high
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    # remove this when you add your code
    global trial_count
    guess = int(guess)
    trial_count = trial_count - 1
    if secret_number > guess:
        print "Your Guess is", guess
        if trial_count == 0:
            print "Wrong Guess"
            print "\nSorry, GAME OVER.\nI'm sure you can do it. Try Again!\n\n\n"
            new_game()
        else:
            print "Guess Higher!"
            print "Number of tries remaining", trial_count, "\n"
    elif secret_number < guess:
        print "Your Guess is", guess
        if trial_count == 0:
            print "Wrong Guess"
            print "\nSorry, GAME OVER.\nI'm sure you can do it. Try Again!\n\n\n"
            new_game()
        else:
            print "Guess Lower!"
            print "Number of tries remaining", trial_count, "\n"

    else:
        print "Your Guess is", guess
        print "Correct Guess!!!"
        print "Hooray!!!  You Win!!! PLAY AGAIN???\n\n\n"
        new_game()
        
# create frame

frame = simplegui.create_frame("GUESSING GAME", 400, 400)

# register event handlers for control elements

frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_button("New Game", new_game, 200)
frame.add_input("Enter your Guess", input_guess, 200)

# call new_game and start frame

new_game()
frame.start()

# always remember to check your completed program against the grading rubric
