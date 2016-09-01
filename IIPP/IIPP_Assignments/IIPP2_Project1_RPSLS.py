"""
Rice University / Coursera: Intro to Interactive Programming in Python (Part 1)
Week 1: Project 1
Rock, Paper, Scissors, Lizard, Spock (RPSLS)
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

##=================================================================

# All code was pasted from the original python file containing project code.

# This program simulates a round of the hand game RPSLS. The 5 hands
# that you may choose from are "rock", "paper", "scissors", "lizard",
# and "Spock". 
#
# CIRCLE OF LIFE:
# 0: Rock beats scissors and lizard
# 2: Paper beats rock and Spock
# 4: Scissors beats paper and lizard
# 3: Lizard beats paper and Spock
# 1: Spock beats rock and scissors
#
# To run this program, call the rpsls function with your choice as an
# argument in quotations as shown below:
#
# Example: rpsls("Spock")
#
# The program will automatically choose an opposing hand and print out
# the game's results based on your choice.


# Helper functions

def name_to_number(name):
    """ Returns a hand name as a number """
    if (name == "rock"):
        return 0
    elif (name == "Spock"):
        return 1
    elif (name == "paper"):
        return 2
    elif (name == "lizard"):
        return 3
    elif (name == "scissors"):
        return 4
    else:
        print "You've entered an invalid hand."

def number_to_name(number):
    """ Returns a hand number as a name """
    if (number == 0):
        return "rock"
    elif (number == 1):
        return "Spock"
    elif (number == 2):
        return "paper"
    elif (number == 3):
        return "lizard"
    elif (number == 4):
        return "scissors"
    else:
        print "You've entered an invalid hand."

# Main function

def rpsls(player_choice):
    """ Prints the player's choice, chooses a random opposing hand for the 
        computer, compares both hands, and prints the result
    """
    print
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)
    import random
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice
    result = (comp_number - player_number) % 5
    if (result == 0):
        print "Player and computer tie!"
    elif (result > 2): 
        print "Player wins!"
    else:
        print "Computer wins!"

########## TESTING GROUNDS ##########
# The code can be tested with the calls below:

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

##=================================================================

# Minified version

import random as r;t,x,m,y,w='rock Spock paper lizard scissors'.split(),' chooses %s\n','Computer','Player',' wins'
for p in t:b=r.randrange(5);print y+x%p+m+x%t[b]+[y+" and computer tie",y+w,m+w][(t.index(p)-b)%-5/2]+'!\n'

##=================================================================

# Improved version using dictionaries and classes.

import random

CHOICES = {
    0: "rock",
    1: "Spock",
    2: "paper",
    3: "lizard",
    4: "scissors"
}

class RPSLS(object):
    """Class to play RPSLS."""
    def __init__(self, choice):
        self.choice = choice
        self.num = CHOICES.keys()[CHOICES.values().index(self.choice)]
        print
        print "Player chooses", self.choice
        self.compute_outcome()
        
    def compute_outcome(self):
        """Compute outcome of round."""
        comp_choice_num = random.randrange(0,5)
        print "Computer chooses", CHOICES[comp_choice_num]
        result = (comp_choice_num - self.num) % 5
        msg = "Player and computer tie!" if result == 0 else "Player wins!" if result > 2 else "Computer wins!"
        print msg
        
RPSLS("rock")
RPSLS("Spock")
RPSLS("paper")
RPSLS("lizard")
RPSLS("scissors")

##=================================================================
##=================================================================