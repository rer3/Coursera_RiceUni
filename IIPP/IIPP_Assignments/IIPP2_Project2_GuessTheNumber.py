"""
Rice University / Coursera: Intro to Interactive Programming in Python (Part 1)
Week 2: Project 2
Guess The Number
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

##=================================================================

# All code was pasted from the original python file containing project code.

# This program opens a frame that launches the game "Guess the Number".
#
# Run this code to open the game interface. Click one of the two buttons 
# to guess a number between either 0-100 or 0-1000. A random number will be 
# chosen, and you will have 7 or 10 attempts to solve it. Each guess and 
# subsequent result will be printed to the console. When the game is over, 
# a new game will begin that uses the same range last specified by the 
# player.

# Import required modules
import simplegui
import math
import random

# Set initial number range 
num_range = 100

# Define helper function to start and restart the game
def new_game():
    """Compute a random number between 0 and 100/1000, compute and 
    print the number of guesses that the player has to start."""
    global secret_number
    secret_number = random.randrange(0, num_range)
    global guesses_left
    guesses_left = int(math.ceil(math.log(num_range, 10) * 3 + 1))
    print ""
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is", guesses_left

# Define event handlers for control panel
def range100():
    """Change number range to [0, 100) and start a new game"""
    global num_range
    num_range = 100
    new_game()

def range1000():
    """Change number range to [0, 1000) and start a new game"""
    global num_range
    num_range = 1000
    new_game()

def input_guess(guess):
    """Convert player guess to an integer, decrement guesses left,
    print player guess and guesses left, compute and print outcome,
    begin a new round or game based on results."""
    guess_number = int(guess)
    global guesses_left
    guesses_left -= 1
    print ""
    print "Guess was", guess_number
    print "Number of remaining guesses is", guesses_left
    if guesses_left > 0:
        if guess_number == secret_number:
            print "Correct!"
            new_game()
        elif guess_number > secret_number:
            print "Lower!"
        else:
            print "Higher!"
    else: 
        if guess_number == secret_number:
            print "Correct!"
            new_game()
        else:
            print "You ran out of guesses. The number was", secret_number
            new_game()

# Create a frame for the game
game_frame = simplegui.create_frame("Guess the number", 200, 200)

# Register event handlers for control elements and start frame
game_frame.add_button("Range is [0, 100)", range100, 200)
game_frame.add_button("Range is [0, 1000)", range1000, 200)
game_frame.add_input("Enter a guess", input_guess, 200)
game_frame.start()

# Call new_game to begin playing
new_game()

##=================================================================
##=================================================================