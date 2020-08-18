# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import math
import random
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

secret_number = 0
num_range = 100
guess_limit = 7


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, guess_limit
    secret_number = random.randrange(num_range)
    guess_limit = int(math.ceil(math.log(num_range + 1, 2)))

    print "New game. Range is [0," + str(num_range) + ")"
    print "Number of remaining guesses is", guess_limit
    print


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_range
    num_range = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global num_range
    num_range = 1000
    new_game()


def input_guess(guess):
    # main game logic goes here
    guess = int(guess)
    print "Guess was", guess

    global guess_limit
    guess_limit -= 1
    print "Number of remaining guesses is", guess_limit

    if guess == secret_number:
        print "Correct\n"
        new_game()
        return

    if guess_limit <= 0:
        print "You ran out of guesses.  The number was", secret_number
        print
        new_game()
        return

    if guess > secret_number:
        print "Lower\n"
    else:
        print "Higher\n"


# create frame
f = simplegui.create_frame("Guess the Number!", 150, 200)

# register event handlers for control elements and start frame
f.add_input("Your guess", input_guess, 100)
f.add_button("Range 100", range100, 100)
f.add_button("Range 1000", range1000, 100)

# call new_game
new_game()
f.start()

# always remember to check your completed program against the grading rubric
