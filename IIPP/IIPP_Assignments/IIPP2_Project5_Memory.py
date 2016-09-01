"""
Rice University / Coursera: Intro to Interactive Programming in Python (Part 2)
Week 1: Project 5
Memory
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# All import statements needed.

import random
import simplegui

# Below is the link to the description of this assignment.

COURSE = "https://class.coursera.org/interactivepython2-009/"
DESCRIPTION = COURSE + "human_grading/view/courses/975652/assessments/32/submissions"

#-----------------------------------------------------------------
## Provided template examples-memory_template. All code is commented
## out as to not interfere with my implementation.

# # helper function to initialize globals
# def new_game():
    # pass  

# # define event handlers
# def mouseclick(pos):
    # # add game state logic here
    # pass
                        
# # cards are logically 50x100 pixels in size    
# def draw(canvas):
    # pass

# # create frame and add a button and labels
# frame = simplegui.create_frame("Memory", 800, 100)
# frame.add_button("Reset", new_game)
# label = frame.add_label("Turns = 0")

# # register event handlers
# frame.set_mouseclick_handler(mouseclick)
# frame.set_draw_handler(draw)

# # get things rolling
# new_game()
# frame.start()

#-----------------------------------------------------------------
## Provided code for simple state (examples-memory_states). All code
## is commented out as not to interfere with my implementation.

# # define event handlers
# def new_game():
    # global state
    # state = 0
    
# def buttonclick():
    # global state
    # if state == 0:
        # state = 1
    # elif state == 1:
        # state = 2
    # else:
        # state = 1
                         
# def draw(canvas):
    # canvas.draw_text(str(state) + " card exposed", [30, 62], 24, "White")

# # create frame and add a button and labels
# frame = simplegui.create_frame("Memory states", 200, 100)
# frame.add_button("Restart", new_game, 200)
# frame.add_button("Simulate mouse click", buttonclick, 200)


# # register event handlers
# frame.set_draw_handler(draw)

# # get things rolling
# new_game()
# frame.start()

#-----------------------------------------------------------------
## First attempt at this code, commented out.

# WIDTH = 500
# HEIGHT = 600

# card1 = simplegui.load_image("https://dl.dropboxusercontent.com/s/i5s2ayqiz2d5vyh/card1.jpg?dl=0")
# card2 = simplegui.load_image("https://dl.dropboxusercontent.com/s/m1wkmp4jqjru4pv/card2.jpg?dl=0")
# card3 = simplegui.load_image("https://dl.dropboxusercontent.com/s/bz7poe1lc1k739o/card3.jpg?dl=0")
# card4 = simplegui.load_image("https://dl.dropboxusercontent.com/s/gxfprn8wfi1v2wh/card4.jpg?dl=0")
# card5 = simplegui.load_image("https://dl.dropboxusercontent.com/s/vjajofzzv566tus/card5.jpg?dl=0")
# card6 = simplegui.load_image("https://dl.dropboxusercontent.com/s/577rfznpjgxorey/card6.jpg?dl=0")
# card7 = simplegui.load_image("https://dl.dropboxusercontent.com/s/4fh8ucd4nepgf74/card7.jpg?dl=0")
# card8 = simplegui.load_image("https://dl.dropboxusercontent.com/s/0mr0ns4utla67li/card8.jpg?dl=0")
# cardblank = simplegui.load_image("https://dl.dropboxusercontent.com/s/w3e8z6ielsojk8r/cardblank.jpg?dl=0")
# img = [86,107]

# # Define helper function to initialize globals
# def new_game():
    # global deck, turns, count
    # cards = [card1, card2, card3, card4, card5, card6, card7, card8]
    # cards.extend(cards)
    # random.shuffle(cards)
    # pos = []
    # for i in range(4):
        # if i==0:
            # y = 6.58
        # elif i==1:
            # y = 2.59
        # elif i==2:
            # y = 1.62
        # else:
            # y = 1.177
        # for j in range(4):
            # if j == 0:
                # x = 6.2
            # elif j==1:
                # x = 2.59
            # elif j==2:
                # x = 1.62
            # else:
                # x = 1.18
            # pos.append([WIDTH/x,HEIGHT/y])
    # opened = [False for i in range(16)]
    # locked = [False for i in range(16)]
    # deck = [list(a) for a in zip(cards, pos, opened, locked)]
    # turns = 0
    # label.set_text("Turns: " + str(turns))
    # count = 0
    
# # Define event handlers
# def click(pos):
    # global count, opened, turns
    # if count == 0:
        # for card in deck:
            # if card[2] and not card[3]:
                # card[2] = False
        # opened = []
        # count += 1
    # if count <= 2:
        # for card in deck:
            # if all([card[1][0] - img[0]/2 <= pos[0] <= card[1][0] + img[0]/2,
                    # card[1][1] - img[1]/2 <= pos[1] <= card[1][1] + img[1]/2]):
                # if card[2] != True:
                    # card[2] = True
                    # opened.append(card[0])
                    # count += 1
    # if count == 3:
        # count = 0
        # turns += 1
        # label.set_text("Turns: " + str(turns))
        # if opened[0] == opened[1]:
            # for card in deck:
                # if card[2] and not card[3]:
                    # card[3] = True

# def draw(c):
    # up = []
    # for card in deck:
        # if card[2]:
            # up.append(card[0])
        # else:
            # up.append(cardblank)
    # c.draw_image(up[0], (img[0]/2, img[1]/2), (img[0], img[1]), (WIDTH/6.2, HEIGHT/6.58), (img[0], img[1]))
    # c.draw_image(up[1], (img[0]/2, img[1]/2), (img[0], img[1]), (WIDTH/2.59, HEIGHT/6.58), (img[0], img[1]))
    # c.draw_image(up[2], (img[0]/2, img[1]/2), (img[0], img[1]), (WIDTH/1.62, HEIGHT/6.58), (img[0], img[1]))
    # c.draw_image(up[3], (img[0]/2, img[1]/2), (img[0], img[1]), (WIDTH/1.18, HEIGHT/6.58), (img[0], img[1]))
    # c.draw_image(up[4], (img[0]/2, img[1]/2), (img[0], img[1]), (WIDTH/6.2, HEIGHT/2.59), (img[0], img[1]))
    # c.draw_image(up[5], (img[0]/2, img[1]/2), (img[0], img[1]), (WIDTH/2.59, HEIGHT/2.59), (img[0], img[1]))
    # c.draw_image(up[6], (img[0]/2, img[1]/2), (img[0], img[1]), (WIDTH/1.62, HEIGHT/2.59), (img[0], img[1]))
    # c.draw_image(up[7], (img[0]/2, img[1]/2), (img[0], img[1]), (WIDTH/1.18, HEIGHT/2.59), (img[0], img[1]))
    # c.draw_image(up[8], (img[0]/2, img[1]/2), (img[0], img[1]), (WIDTH/6.2, HEIGHT/1.62), (img[0], img[1]))
    # c.draw_image(up[9], (img[0]/2, img[1]/2), (img[0], img[1]), (WIDTH/2.59, HEIGHT/1.62), (img[0], img[1]))
    # c.draw_image(up[10], (img[0]/2, img[1]/2), (img[0], img[1]), (WIDTH/1.62, HEIGHT/1.62), (img[0], img[1]))
    # c.draw_image(up[11], (img[0]/2, img[1]/2), (img[0], img[1]), (WIDTH/1.18, HEIGHT/1.62), (img[0], img[1]))
    # c.draw_image(up[12], (img[0]/2, img[1]/2), (img[0], img[1]), (WIDTH/6.2, HEIGHT/1.177), (img[0], img[1]))
    # c.draw_image(up[13], (img[0]/2, img[1]/2), (img[0], img[1]), (WIDTH/2.59, HEIGHT/1.177), (img[0], img[1]))
    # c.draw_image(up[14], (img[0]/2, img[1]/2), (img[0], img[1]), (WIDTH/1.62, HEIGHT/1.177), (img[0], img[1]))
    # c.draw_image(up[15], (img[0]/2, img[1]/2), (img[0], img[1]), (WIDTH/1.18, HEIGHT/1.177), (img[0], img[1]))

# # Create frame, button, label
# frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
# frame.add_button("--- RESET ---", new_game)
# frame.add_label("")
# label = frame.add_label("Turns: 0")

# # Register event handlers
# frame.set_mouseclick_handler(click)
# frame.set_draw_handler(draw)

# # Begin a new game
# new_game()
# frame.start()

##=================================================================

DIRECTIONS = '''
Memory
----------
Memory is a card game in which the player deals out a set of cards face down. In
Memory, a turn (or a move) consists of the player flipping over two cards. If they
match, the player leaves them face up. If they don't match, the player flips the
cards back face down. The goal of Memory is to end up with all of the cards
flipped face up in the minimum number of turns. For this project, we will keep
our model for Memory fairly simple. A Memory deck consists of 8 pairs of matching cards.

Development Process
----------
We suggest you start from the programming template (provided here).
1.) Model the deck of cards used in Memory as a list consisting of 16 numbers with
    each numbers lying in the range [0,8) and appearing twice. We suggest that you
    create this list by concatenating two lists with range [0,8) together. 
2.) Write a draw handler that iterates through the Memory deck using a for loop
    and uses draw_text to draw the number associated with each card on the canvas.
    The result should be a horizontal sequence of evenly-spaced numbers drawn.
3.) Shuffle the deck using random.shuffle(). Remember to debug your canvas
    drawing code before shuffling to make debugging easier.
4.) Next, modify the draw handler to either draw a blank green rectangle or the
    card's value. To implement this behavior, we suggest that you create a second
    list called exposed. In the exposed list, the ith entry should be True if the ith 
    card is face up and its value is visible or False if the ith card is face down and
    its value is hidden. We suggest you initialize exposed to some known values
    while testing your drawing code with this modification.
5.) Now, add functionality to determine which card you have clicked on with your
    mouse. Add an event handler for mouse clicks that takes the pos of the mouse
    click and prints the index of the card that you have clicked on to the console.
    To make determining which card you have clicked on easy, we suggest sizing
    the canvas so that the sequence of cards entirely filled the canvas.
6.) Modify the event handler for mouse clicks to flip cards based on the location
    of the mouse click. If the player clicked on the ith card, you can change the
    value of exposed[i] from False to True. If the card is already exposed, you
    should ignore the mouseclick. At this point, the basic infrastructure is done.
7.) You now need to add game logic to the mouse click handler for selecting
    two cards and determining if they match. We suggest following the game
    logic in the example code (provided) from the Memory video. State 0 corresponds
    to the start of the game. In state 0, if you click on a card, that card is exposed,
    and you switch to state 1. State 1 corresponds to a single exposed unpaired
    card. In state 1, if you click on an unexposed card, that card is exposed and 
    you switch to state 2. State 2 corresponds to the end of a turn. Here, if you
    click on an unexposed card, that card is exposed and you switch to State 1.
8.) Note that in state 2, you also have to determine if the previous two cards
    are paired or unpaired. If they are unpaired, you have to flip them back over so
    that they are hidden before moving to state 1. We suggest that you use two
    global vars to store the index of each of the two cards that were clicked in
    the previous turn.
9.) Add a counter that keeps track of the number of turns and uses set_text to
    update this counter as a label in the control panel (Joe's record is 12 turns).
    This counter should be incremented after either the first or second card is 
    flipped during a turn.
10.) Finally, implement the new_game() function so that the Reset button
    reshuffles the cards, resets the turn counter, and restarts the game. All cards
    should start the game hidden.
11.) (Optional) You may replace the draw_text for each card by a draw_image
    that uses one of eight different images.
    
Once the run button is clicked in CodeSkulptor, the game should start. You should
not have to hit the Reset button to start. Once the game is over, you should hit
the Reset button to restart the game. While this project may seem daunting at
first glance, our full implementation took well under 100 lines with comments
and space. If you feel intimidated, focus on developing your project to step 6.
Here, you will begin to see your game come together and it gets easier.

Grading
----------
1 pt - The game correctly draws 16 cards on the canvas (horiz or as a grid).
1 pt - The cards appear in 8 unique pairs.
1 pt - The game ignores clicks on exposed cards.
1 pt - At the start of the game, a click on a card exposes that card.
1 pt - If one unpaired card is exposed, a click on a second unexposed card exposes
    that card.
1 pt - If two unpaired cards are exposed, a click on an unexposed card exposes
    the card that was clicked on and flips the two unpaired cards over.
1 pt - If all exposed cards are paired, a click on an unexposed card exposes the
    card clicked on and does not filp any cards.
1 pt - Cards paired by two clicks in the same turn remain exposed until the start
    of the next game.
1 pt - The game correctly updates and displays the number of turns in the current
    game in a label displayed in the control area. The counter may be incremented
    after either the first or second card is flipped during a turn.
1 pt - The game includes a Reset button that resets the turn counter and restarts
    the game.
1 pt - The deck is also randomly shuffled each time the Reset button is pressed,
    so that the cards are in a different order each game.
'''

##=================================================================

# Since I'm going back and re-implementing this, I will use my original version and
# update it with all that I've learned in the interim. The game will be stored in
# a class, and the GUI will be in a separate class. This is completely unnecessary
# for a task as simple as this, but I'm going to flex my skills a bit. The same
# basic functions will be lifted, and the same 8 colored cards from my Dropbox 
# acct will be used for the game instead of numbers.

# The final version submitted to Coursera will be everything below plus the import
# statements above. The following comments will apply to everything below as I
# re-work through it and encounter issues. These will not be broken up into
# pieces and placed in between code blocks. 

# The first major change--other than implementing two separate classes--is the
# draw handler. Before, each call to draw_image was written out. Here, two for
# loops will iterate through row and col. Also, the corresponding positions in which
# images are placed is computed in a much cleaner manner, and the index of the
# card at that position is also computed in a clear, clean way that utilizes these
# row and col values. 

# Another major difference is the storage and maniuplation of game variable
# and state changes. Here, the game class initializes everything that's needed
# and a host of getters and setters are implemented for use by the GUI. All
# changes to the game state are made through the calls to these methods by GUI.
# The row/col computations mentioned above can be used to index the opened
# and locked lists very easily--instead of creating a list of lists to store the 
# state of each card. Everything here is separated nicely.

# Additional features include orange squares placed around opened (but not locked)
# tiles, red squares placed around tiles when an incorrect pair results, and green
# squares placed around tiles when a match is made. These colored squares disappear
# once the next turn is started. Also, messages are added to convey game state.

TILE_WIDTH = 86
TILE_HEIGHT = 107
IMG_WH = (TILE_WIDTH, TILE_HEIGHT)
IMG_CTR = (TILE_WIDTH / 2, TILE_HEIGHT / 2)
BUF = 6
CANVAS_WIDTH = (TILE_WIDTH + BUF) * 4
CANVAS_HEIGHT = (TILE_HEIGHT + BUF) * 4

IMAGES = {
    0: simplegui.load_image("https://dl.dropboxusercontent.com/s/w3e8z6ielsojk8r/cardblank.jpg?dl=0"),
    1: simplegui.load_image("https://dl.dropboxusercontent.com/s/i5s2ayqiz2d5vyh/card1.jpg?dl=0"),
    2: simplegui.load_image("https://dl.dropboxusercontent.com/s/m1wkmp4jqjru4pv/card2.jpg?dl=0"),
    3: simplegui.load_image("https://dl.dropboxusercontent.com/s/bz7poe1lc1k739o/card3.jpg?dl=0"),
    4: simplegui.load_image("https://dl.dropboxusercontent.com/s/gxfprn8wfi1v2wh/card4.jpg?dl=0"),
    5: simplegui.load_image("https://dl.dropboxusercontent.com/s/vjajofzzv566tus/card5.jpg?dl=0"),
    6: simplegui.load_image("https://dl.dropboxusercontent.com/s/577rfznpjgxorey/card6.jpg?dl=0"),
    7: simplegui.load_image("https://dl.dropboxusercontent.com/s/4fh8ucd4nepgf74/card7.jpg?dl=0"),
    8: simplegui.load_image("https://dl.dropboxusercontent.com/s/0mr0ns4utla67li/card8.jpg?dl=0")
    }


class MemoryGame():

    def __init__(self):
    
        self._cards = range(1, 9) * 2
        random.shuffle(self._cards)
        self._opened = [False for index in range(16)]
        self._locked = [False for index in range(16)]
        self._turns = 0
        self._state = 0
        
    def clear(self):
        """
        Clear all variables and reset game.
        """
        random.shuffle(self._cards)
        self._opened = [False for index in range(16)]
        self._locked = [False for index in range(16)]
        self._turns = 0
        self._state = 0
        
    def get_card(self, index):
        """
        Return card at index.
        """
        return self._cards[index]
        
    def is_opened(self, index):
        """
        Return True if card at index is open, else False.
        """
        return self._opened[index]
        
    def is_locked(self, index):
        """
        Return True if card at index is locked, else False.
        """
        return self._locked[index]
        
    def get_turns(self):
        """
        Return number of turns taken in current game as string.
        """
        return str(self._turns)
        
    def get_state(self):
        """
        Return state of current game.
        """
        return self._state
        
    def set_opened(self, index):
        """
        Set card at index in opened list to True.
        """
        self._opened[index] = True
        
    def set_closed(self, index):
        """
        Set card at index in opened list to False.
        """
        self._opened[index] = False
        
    def set_locked(self, index):
        """
        Set card at index in locked list to True.
        """
        self._locked[index] = True
        
    def increment_turns(self):
        """
        Increase turn count by 1.
        """
        self._turns += 1
        
    def change_state(self):
        """
        Change state of game.
        """
        if self._state == 1:
            self._state = 2
        else:
            self._state = 1
            
    def check_win(self):
        """
        Check for end of game (all pairs are matched).
        """
        if False not in self._locked:
            return True
        else:
            return False
        
        
class MemoryGUI():

    def __init__(self, game):
        
        self._game = game
        self._hiscore = float("inf")
        self._winner = False
        self._win_color = "Black"
        
        self._first_card = 0
        self._first_index = -1
        self._second_card = 0
        self._second_index = -1
        self._choice_color = "Yellow"
        
        self._frame = simplegui.create_frame("Memory", CANVAS_WIDTH, CANVAS_HEIGHT)
        self._frame.add_button("--- RESET ---", self.new_game)
        self._turn_label = self._frame.add_label("Turns: 0")
        self._hiscore_label = self._frame.add_label("High Score: 0")
        self._frame.set_mouseclick_handler(self.click)
        self._frame.set_draw_handler(self.draw)
        self._win_timer = simplegui.create_timer(160, self.win_tick)
        self._choice_timer = simplegui.create_timer(450, self.choice_tick)
        self._choice_timer.start()
        self._frame.start()
        
    def new_game(self):
        """
        Start a new game.
        """
        score_string = self._game.get_turns()
        if int(score_string) < self._hiscore and self._winner:
            self._hiscore = int(score_string)
            self._hiscore_label.set_text("High Score: " + score_string)
        self._winner = False
        self._win_timer.stop()
        self._choice_timer.start()
        self.reset_choices()
        self._game.clear()
        self._turn_label.set_text("Turns: 0")
        
    def reset_choices(self):
        """
        Clear first and second card/index variables.
        """
        self._first_card = 0
        self._first_index = -1
        self._second_card = 0
        self._second_index = -1
        self._choice_color = "Yellow"
        
    def win_tick(self):
        """
        Timer for blinking winner message.
        """
        colors = ["Black", "Yellow", "Red", "Blue", "Green", "Pink", 
                  "Purple", "Orange", "Aqua", "White"]
        self._win_color = random.choice(colors)
        
    def choice_tick(self):
        """
        Timer for highlighting choices.
        """
        if self._choice_color == "Red":
            self._choice_color = "Red"
        elif self._choice_color == "Yellow":
            self._choice_color = "Black"
        elif self._choice_color == "Black":
            self._choice_color = "Yellow"
        
    def click(self, pos):
        """
        Mouseclick handler.
        """
        col = pos[0] / (TILE_WIDTH + BUF)
        row = pos[1] / (TILE_HEIGHT + BUF)
        index = col + 4 * row
        opened = self._game.is_opened(index)
        locked = self._game.is_locked(index)
        state = self._game.get_state()
        
        if state == 0 and not opened and not locked:
            self._game.set_opened(index)
            self._first_card = self._game.get_card(index)
            self._first_index = index
            self._game.change_state()
            
        elif state == 1 and not opened and not locked:
            self._game.set_opened(index)
            self._second_card = self._game.get_card(index)
            self._second_index = index
            if self._first_card == self._second_card:
                self._game.set_locked(self._first_index)
                self._game.set_locked(self._second_index)
            else:
                self._choice_color = "Red"
            self._game.increment_turns()
            self._turn_label.set_text("Turns: " + self._game.get_turns())
            self._game.change_state()
            
        elif state == 2 and not locked:
            if not self._game.is_locked(self._first_index):
                self._game.set_closed(self._first_index)
                self._game.set_closed(self._second_index)
            self.reset_choices()        
            self._game.set_opened(index)
            self._first_card = self._game.get_card(index)
            self._first_index = index
            self._game.change_state()
            
        if self._game.check_win():
            self._winner = True
            self._win_timer.start()
            self._choice_timer.stop()
        
    def draw(self, canvas):
        """
        Draw handler.
        """ 
        for row in range(4):
            for col in range(4):
                pos = (((TILE_WIDTH + BUF) / 2) + col * (TILE_WIDTH + BUF),
                       ((TILE_HEIGHT + BUF) / 2) + row * (TILE_HEIGHT + BUF))
                index = col + 4 * row
                if self._game.is_opened(index):
                    card = self._game.get_card(index)
                    if not self._game.is_locked(index):
                        canvas.draw_polygon([(pos[0] - IMG_CTR[0], pos[1] - IMG_CTR[1]), 
                                              (pos[0] + IMG_CTR[0], pos[1] - IMG_CTR[1]), 
                                              (pos[0] + IMG_CTR[0], pos[1] + IMG_CTR[1] + 1), 
                                              (pos[0] - IMG_CTR[0], pos[1] + IMG_CTR[1] + 1)], 
                                              6, self._choice_color)
                else:
                    card = 0
                canvas.draw_image(IMAGES[card], IMG_CTR, IMG_WH, pos, IMG_WH)
                
        if self._winner:
            canvas.draw_text("YOU'VE MATCHED", (8,184), 40, self._win_color)
            canvas.draw_text("ALL PAIRS!", (80, 300), 40, self._win_color)
                        
        
MemoryGUI(MemoryGame())

# Submitted URL: http://www.codeskulptor.org/#user40_SeB8gR2H29ByaAL_1.py

##=================================================================
##=================================================================