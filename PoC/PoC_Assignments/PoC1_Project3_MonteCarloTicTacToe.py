"""
Rice University / Coursera: Principles of Computing (Part 1)
Week 3: Project 3
Monte Carlo Tic-Tac-Toe
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# All import statements needed.

import codeskulptor
import random
import simplegui
codeskulptor.set_timeout(60)

# Below is the link to the description of this assignment.

COURSE = "https://class.coursera.org/principlescomputing1-004/"
DESCRIPTION = COURSE + "wiki/view?page=tictactoemc"

#-----------------------------------------------------------------
## Provided template for Monte Carlo Tic-Tac-Toe Player (commented out).

# """
# Monte Carlo Tic-Tac-Toe Player
# """

# import random
# import poc_ttt_gui
# import poc_ttt_provided as provided

# # Constants for Monte Carlo simulator
# # You may change the values of these constants as desired, but
# #  do not change their names.
# NTRIALS = 1         # Number of trials to run
# SCORE_CURRENT = 1.0 # Score for squares played by the current player
# SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# # Add your functions here.



# # Test game with the console or the GUI.  Uncomment whichever 
# # you prefer.  Both should be commented out when you submit 
# # for testing to save time.

# # provided.play_game(mc_move, NTRIALS, False)        
# # poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

#-----------------------------------------------------------------
## Provided TTTBoard class, constants, and helper functions. Module called
## poc_ttt_provided.

"""
Provided Code for Tic-Tac-Toe
"""

# Constants
EMPTY = 1
PLAYERX = 2
PLAYERO = 3 
DRAW = 4

# Map player constants to letters for printing
STRMAP = {EMPTY: " ",
          PLAYERX: "X",
          PLAYERO: "O"}

class TTTBoard:
    """
    Class to represent a Tic-Tac-Toe board.
    """

    def __init__(self, dim, reverse = False, board = None):
        """
        Initialize the TTTBoard object with the given dimension and 
        whether or not the game should be reversed.
        """
 
        self._dim = dim
        self._reverse = reverse
        if board == None:
            # Create empty board
            self._board = [[EMPTY for dummycol in range(dim)] 
                           for dummyrow in range(dim)]
        else:
            # Copy board grid
            self._board = [[board[row][col] for col in range(dim)] 
                           for row in range(dim)]
            
    def __str__(self):
        """
        Human readable representation of the board.
        """
        rep = ""
        for row in range(self._dim):
            for col in range(self._dim):
                rep += STRMAP[self._board[row][col]]
                if col == self._dim - 1:
                    rep += "\n"
                else:
                    rep += " | "
            if row != self._dim - 1:
                rep += "-" * (4 * self._dim - 3)
                rep += "\n"
        return rep

    def get_dim(self):
        """
        Return the dimension of the board.
        """
        return self._dim
    
    def square(self, row, col):
        """
        Returns one of the three constants EMPTY, PLAYERX, or PLAYERO 
        that correspond to the contents of the board at position (row, col).
         """
        return self._board[row][col]

    def get_empty_squares(self):
        """
        Return a list of (row, col) tuples for all empty squares
        """
        empty = []
        for row in range(self._dim):
            for col in range(self._dim):
                if self._board[row][col] == EMPTY:
                    empty.append((row, col))
        return empty

    def move(self, row, col, player):
        """
        Place player on the board at position (row, col).
        player should be either the constant PLAYERX or PLAYERO.
        Does nothing if board square is not empty.
        """
        if self._board[row][col] == EMPTY:
            self._board[row][col] = player

    def check_win(self):
        """
        Returns a constant associated with the state of the game
            If PLAYERX wins, returns PLAYERX.
            If PLAYERO wins, returns PLAYERO.
            If game is drawn, returns DRAW.
            If game is in progress, returns None.
        """
        board = self._board
        dim = self._dim
        dimrng = range(dim)
        lines = []

        # rows
        lines.extend(board)

        # cols
        cols = [[board[rowidx][colidx] for rowidx in dimrng]
                for colidx in dimrng]
        lines.extend(cols)

        # diags
        diag1 = [board[idx][idx] for idx in dimrng]
        diag2 = [board[idx][dim - idx -1] 
                 for idx in dimrng]
        lines.append(diag1)
        lines.append(diag2)

        # check all lines
        for line in lines:
            if len(set(line)) == 1 and line[0] != EMPTY:
                if self._reverse:
                    return switch_player(line[0])
                else:
                    return line[0]

        # no winner, check for draw
        if len(self.get_empty_squares()) == 0:
            return DRAW

        # game is still in progress
        return None
            
    def clone(self):
        """
        Return a copy of the board.
        """
        return TTTBoard(self._dim, self._reverse, self._board)

def switch_player(player):
    """
    Convenience function to switch players.
    
    Returns other player.
    """
    if player == PLAYERX:
        return PLAYERO
    else:
        return PLAYERX

def play_game(mc_move_function, ntrials, reverse = False):
    """
    Function to play a game with two MC players.
    """
    # Setup game
    board = TTTBoard(3, reverse)
    curplayer = PLAYERX
    winner = None
    
    # Run game
    while winner == None:
        # Move
        row, col = mc_move_function(board, curplayer, ntrials)
        board.move(row, col, curplayer)

        # Update state
        winner = board.check_win()
        curplayer = switch_player(curplayer)

        # Display board
        print board
        print
        
    # Print winner
    if winner == PLAYERX:
        print "X wins!"
    elif winner == PLAYERO:
        print "O wins!"
    elif winner == DRAW:
        print "Tie!"
    else:
        print "Error: unknown winner"

#-----------------------------------------------------------------
## Provided TTT GUI at poc_ttt_gui, with constants and function to run
## the game. Import statements commented out.

"""
Tic Tac Toe GUI code.
"""

# import simplegui
# import poc_ttt_provided as provided

GUI_WIDTH = 400
GUI_HEIGHT = GUI_WIDTH
BAR_WIDTH = 5

class TicTacGUI:
    """
    GUI for Tic Tac Toe game.
    """
    def __init__(self, size, aiplayer, aifunction, ntrials, reverse=False):
        # Game board
        self._size = size
        self._bar_spacing = GUI_WIDTH // self._size
        self._turn = PLAYERX
        self._reverse = reverse

        # AI setup
        self._humanplayer = switch_player(aiplayer)
        self._aiplayer = aiplayer
        self._aifunction = aifunction
        self._ntrials = ntrials
        
        # Set up data structures
        self.setup_frame()

        # Start new game
        self.newgame()
        
    def setup_frame(self):
        """
        Create GUI frame and add handlers.
        """
        self._frame = simplegui.create_frame("Tic-Tac-Toe",
                                             GUI_WIDTH,
                                             GUI_HEIGHT)
        self._frame.set_canvas_background('White')
        
        # Set handlers
        self._frame.set_draw_handler(self.draw)
        self._frame.set_mouseclick_handler(self.click)
        self._frame.add_button("New Game", self.newgame)
        self._label = self._frame.add_label("")

    def start(self):
        """
        Start the GUI.
        """
        self._frame.start()

    def newgame(self):
        """
        Start new game.
        """
        self._board = TTTBoard(self._size, self._reverse)
        self._inprogress = True
        self._wait = False
        self._turn = PLAYERX
        self._label.set_text("")
        
    def drawx(self, canvas, pos):
        """
        Draw an X on the given canvas at the given position.
        """
        halfsize = .4 * self._bar_spacing
        canvas.draw_line((pos[0]-halfsize, pos[1]-halfsize),
                         (pos[0]+halfsize, pos[1]+halfsize),
                         BAR_WIDTH, 'Black')
        canvas.draw_line((pos[0]+halfsize, pos[1]-halfsize),
                         (pos[0]-halfsize, pos[1]+halfsize),
                         BAR_WIDTH, 'Black')
        
    def drawo(self, canvas, pos):
        """
        Draw an O on the given canvas at the given position.
        """
        halfsize = .4 * self._bar_spacing
        canvas.draw_circle(pos, halfsize, BAR_WIDTH, 'Black')
        
    def draw(self, canvas):
        """
        Updates the tic-tac-toe GUI.
        """
        # Draw the '#' symbol
        for bar_start in range(self._bar_spacing,
                               GUI_WIDTH - 1,
                               self._bar_spacing):
            canvas.draw_line((bar_start, 0),
                             (bar_start, GUI_HEIGHT),
                             BAR_WIDTH,
                             'Black')
            canvas.draw_line((0, bar_start),
                             (GUI_WIDTH, bar_start),
                             BAR_WIDTH,
                             'Black')
            
        # Draw the current players' moves
        for row in range(self._size):
            for col in range(self._size):
                symbol = self._board.square(row, col)
                coords = self.get_coords_from_grid(row, col)
                if symbol == PLAYERX:
                    self.drawx(canvas, coords)
                elif symbol == PLAYERO:
                    self.drawo(canvas, coords)
                
        # Run AI, if necessary
        if not self._wait:
            self.aimove()
        else:
            self._wait = False
                
    def click(self, position):
        """
        Make human move.
        """
        if self._inprogress and (self._turn == self._humanplayer):        
            row, col = self.get_grid_from_coords(position)
            if self._board.square(row, col) == EMPTY:
                self._board.move(row, col, self._humanplayer)
                self._turn = self._aiplayer
                winner = self._board.check_win()
                if winner is not None:
                    self.game_over(winner)
                self._wait = True
                
    def aimove(self):
        """
        Make AI move.
        """
        if self._inprogress and (self._turn == self._aiplayer):
            row, col = self._aifunction(self._board, 
                                        self._aiplayer, 
                                        self._ntrials)
            if self._board.square(row, col) == EMPTY:
                self._board.move(row, col, self._aiplayer)
            self._turn = self._humanplayer
            winner = self._board.check_win()
            if winner is not None:
                self.game_over(winner)        
            
    def game_over(self, winner):
        """
        Game over
        """
        # Display winner
        if winner == DRAW:
            self._label.set_text("It's a tie!")
        elif winner == PLAYERX:
            self._label.set_text("X Wins!")
        elif winner == PLAYERO:
            self._label.set_text("O Wins!") 
            
        # Game is no longer in progress
        self._inprogress = False

    def get_coords_from_grid(self, row, col):
        """
        Given a grid position in the form (row, col), returns
        the coordinates on the canvas of the center of the grid.
        """
        # X coordinate = (bar spacing) * (col + 1/2)
        # Y coordinate = height - (bar spacing) * (row + 1/2)
        return (self._bar_spacing * (col + 1.0/2.0), # x
                self._bar_spacing * (row + 1.0/2.0)) # y
    
    def get_grid_from_coords(self, position):
        """
        Given coordinates on a canvas, gets the indices of
        the grid.
        """
        posx, posy = position
        return (posy // self._bar_spacing, # row
                posx // self._bar_spacing) # col


def run_gui(board_size, ai_player, ai_function, ntrials, reverse=False):
    """
    Instantiate and run the GUI
    """
    gui = TicTacGUI(board_size, ai_player, ai_function, ntrials, reverse)
    gui.start()

##=================================================================

DIRECTIONS = '''
Overview
----------
Tic-Tac-Toe is a simple children's game played on a 3x3 grid. Players alternate turns
placing an "X" or an "O" in an empty grid square. First to get 3 in a row wins. The
game can always end in a tie if both players have great strategy. Reverse TTT is a
fun variant of the game. 

For this assignment, your task is to implement machine player logic for TTT.
Specifically, your machine player will use a Monte Carlo sim to decide its next
move. We will provide both a console-based interface to the game where your machine
player will player against itself and a graphical user interface where you can play
against your machine player. Although the game is played on a 3x3 grid, your version
should be able to handle any square grid. We will continue to use grid conventions.

For this project, we will provide you with a complete implementation of a TTT
Board class. However, for your part of the project, we will provide only a very
minimal amount of starting code. We will also dispense with the phased description
of the implementation process so that your coding task for this project is a more
realistic example of the software development process.

Provided Code
----------
We have provided a TTTBoard class. This class keeps track of the current state of
the game board. You should familiarize yourself with the interface to the TTTBoard
class in the poc_ttt_provided module. The provided module also has a
switch_player(player) function that returns the other player (PLAYERX or PLAYERO),
and a play_game(mc_move_function, ntrials, reverse) function that uses the
mc_move_function you provide to play a game with two machine players on a
3x3 board. The play_game function will print the moves in the game to the console.
Finally, the provided module defines the constants EMPTY, PLAYERX, PLAYERO, and
DRAW for you to use in your code. The provided TTTBoard class and GUI use these
constants, so you will need to use them in your code as well.

At the At the bottom of the template, there are example calls to the GUi and console
game player. You may uncomment and modify these during the development of your
machine player to actually use it in the game. The run_gui function takes five args:
dim of the board, which player the machine player will be, a move function, the 
number of trials per move, and a reverse arg indicating whethre or not you want to
play normal (False) or reverse (True) game.

Testing
----------
As always, testing is a critical part of the process of building your project.
Remember you should be testing each function as you write it. Don't try to implement
all of the functions and then test. You will have lots of errors that all interact in
strange ways. Submit your code to this OwlTest page to test it: http://codeskulptor.
appspot.com/owltest?urlTests=poc.poc_tttmc_tests.py&urlPylintConfig=poc.pylint_config.
py&imports=%7Bpoc:(poc_ttt_provided,%20poc_ttt_gui)%7D. Follow Pylint style.

Machine Player Strategy
----------
Your machine player should use a Monte Carlo sim to choose the next move from a
given TTT board pos. The general idea is to play a collection of games with random
moves starting from the position, and then use the results of these games to compute
a good move. When you win one of these random games, you want to favor the squares
in which you played (in hopes of choosing a winning move) and avoid the squares in 
which your opponent played. Conversely, when you lose one of these random games,
you want to favor the squares in which your opponent played (to block your opponent)
and avoid the squares in which you played. In short, squares in which the winning
player played in these random games should be favored over squares in which the
losing player played.

Here is an outline of this sim:
1.) Start with the current board you are given ("board").
2.) Repeat for the desired number of trials:
    A. Set the current board to be "board" (clone it).
    B. Play an entire game on this board by just randomly choosing a move for
        each player.
    C. Score the resulting board.
    D. Add the scores to a running total across all trials.
3.) To select a move, randomly choose one of the empty squares on the board that
    has the max score.
    
These steps should be relatively straightforward except for step 2C, scoring the board.
Scores are kept for each square on the board. The way you assign a score to a square
depends on who won the game. If the game was a tie, then all squares should receive
a score of 0, since that game will not help you determine a winning strategy. If the
current player (the player for which your code is currently selecting a move) won the
game, each square that matches the current player should get a positive score
(corresponding to SCORE_CURRENT in the template, which is the scoring value for the
current player) and each square that matches the other player should get a negative
score (-SCORE_OTHER). Conversely, if the current player lost the game, each square
that matches the current player should get a negative score (-SCORE_CURRENT) and
each square that matches the other player should get a positive score (SCORE_OTHER).
All empty squares should get a score of 0.

Note that you want to select a final move from the total scores across all tiles, so
in step 2D you are adding the scores from 2C to the running total of all scores. Higher
scores indicates squares that are more likely to be played by the current player in
winning games and lower scores indicate squares that are more likely to be played
in losing games.

Implementation
----------
Your task is to implement the following 4 functions: mc_trial, mc_update_scores,
get_best_move, and mc_move. These 4 core functions should do the following:
* mc_trial(board, player): This func takes a current board and the next player to
    move. The func should play a game starting with the given player by making
    random moves, alternating between players. The func should return when the
    game is over. The modified board will contain the state of the game, so the
    func does not return anything. In other words, the func should modify the
    board input.
* mc_update_scores(scores, board, player): This func takes a grid of scores (a 
    list of lists) with the same dim as the TTT board, a board from a completed
    game, and which player the machine player is. The func should score the
    completed board and update the scores grid. As the func updates the scores
    grid directly, it does not return anything.
* get_best_move(board, scores): This func takes a current board and a grid of
    scores. The func should find all of the empty squares with the max score and
    randomly return one of them as (row, col) tuple. It is an error to call this func
    with a board that has no empty squares (there is no poss next move), so your
    func may do whatever it wants in that case. The case where the board is full
    will not be tested.
* mc_move(board, player, trials): This func takes a current board, which player the
    machine player is, and the number of trials to run. The func should use the 
    Monte Carlo sim described above to return a move for the machine player in
    the form of a (row, col) tuple. Be sure to use the other funcs you've written.
    
You may add helper funcs if desired. The signature of the 4 funcs above must match
the provided description as they will be tested by the machine grader. Once you have
working code, you will want to experiment with the values of NTRIALS, SCORE_CURRENT,
and SCORE_OTHER to get a good machine player. You must use these constant names,
as the machine grader will assume they are defined in your file. Further, the final
test will be whether your player selects obvious good next moves.
'''

##=================================================================

# A lot of freedom was given for this project. I began by testing the TTTBoard class
# using the code below (commented out here). 

# print "Create a new board and test __str__()"
# print "-"*10
# myboard = TTTBoard(3)
# print myboard
# print "Literal representation of _board: " + str(myboard._board)
# print "\n"
# print "Return dimension with get_dim()"
# print "-"*10
# print myboard._dim
# print "\n"
# print "Return constant corresponding to a board position"
# print "-"*10
# print "Board at (0, 0): " + str(myboard.square(0, 0))
# print "Board at (0, 1): " + str(myboard.square(0, 1))
# print "Board at (1, 1): " + str(myboard.square(1, 1))
# print "Board at (1, 2): " + str(myboard.square(1, 2))
# print "Board at (2, 2): " + str(myboard.square(2, 2))
# print "Board at (2, 0): " + str(myboard.square(2, 0))
# print "\n"
# print "Return a list of empty squares with get_empty_squares()"
# print "-"*10
# print myboard.get_empty_squares()
# print "\n"
# print "Place player on the board at position with move()"
# print "-"*10
# myboard.move(1,1,PLAYERX)
# myboard.move(1,1,PLAYERO)
# myboard.move(1,2,PLAYERO)
# myboard.move(0,1,PLAYERX)
# myboard.move(2,1,PLAYERO)
# myboard.move(0,2,PLAYERX)
# myboard.move(2,0,PLAYERO)
# print myboard
# print "\n"
# print "Check for a winner with check_win()"
# print "-"*10
# print "Winner yet? " + str(myboard.check_win())
# print "myboard.move(0,0,PLAYERX)"
# myboard.move(0,0,PLAYERX)
# print "Winner yet? " + str(myboard.check_win())
# print myboard
# print "\n"
# print "Return a copy of the board with clone()"
# print "-"*10
# newboard = myboard.clone()
# print newboard
# print "\n"
# print "Switch player with switch_player()"
# print "-"*10
# print "Switch from PLAYERX(2) to PLAYERO (3)"
# print "Other player:", switch_player(PLAYERX)
# print "\n"

# Gameplay testing did not occur there, but with the project code, once the func
# mc_move_function was written. This applies to the GUI class as well.

# The first step in implementing the necessary functions for this project was to
# create a class for the scoreboard. When initialized, it creates a field for the
# scoreboard and fills it with zero values. Two methods were written, one to
# update a score in the board, and one to return the entire scoreboard for use
# in the four core functions.

class Scoreboard:
    """
    Class to track player scores for a TTT game board.
    """
    def __init__(self, board):
        dim = board.get_dim()
        self._scoreboard = [[0 for dummy_row in range(dim)] for dummy_col in range(dim)]
        
    def update_score(self, row, col, value):
        """
        Update the score of a square on the scoreboard by a value.
        """
        self._scoreboard[row][col] += value
        
    def get_score(self, row, col):
        """
        Return the score of a square in the scoreboard.
        """
        return self._scoreboard[row][col]
        
    def get_scoreboard(self):
        """
        Return the scoreboard.
        """
        return self._scoreboard
        
# A big problem with this implementation in OwlTest was a list of scores being
# expected as passed to the core functions, where here I'm using a class to store
# and modify the scores. While I'd prefer to use the methods above, I ended
# up using only get_scoreboard() and then modifying the scores in that grid with
# [row][col] references to those indices. It's not ideal, but OwlTest fails otherwise.
        
# First, I implemented mc_trial(board, player). This was a fairly simple function
# that assigned player moves to random empty squares until a draw (full) or win.
# Note that all references to "provided" module are removed here, but in the
# submitted version were included in the appropriate references to constants/methods.

def mc_trial(board, player):
    """
    Takes a TTT game board and current player and computes a
    trial run of a TTT game.
    """
    winner = None
    while winner == None:
        dim = board.get_dim()
        row, col = random.randrange(dim), random.randrange(dim)
        if board.square(row, col) == EMPTY:
            board.move(row, col, player)
            player = switch_player(player)
        winner = board.check_win()

# Testing for this particular function was minimal, as it was very straightforward.
# When testing for bugs, print statements were added which identified the winner
# before the call to check_win.

# Next, mc_update_scores was implemented to update a grid of scores. The machine
# player is passed to it, and the SCORE_CURRENT value corresponds to it (conversely,
# SCORE_OTHER corresponds to either another machine player or to the human player).
# This function first checks for the winner (a draw is ignored as square scores in 
# the event of one are updated by zero) and then updates the scores accordingly.
# Note that the scores being passed to this function are contained in a list of lists,
# so they are directly referenced with row/col indices and updated (vs. using the
# Scoreboard class's methods, which I would like to have had the option to do...).

def mc_update_scores(scores, board, player):
    """
    Takes a grid of scores, a completed TTT game board, and which player the
    machine player is to score the game board and update the scores grid.
    """
    dim = board.get_dim()
    
    if board.check_win() == player:
        for row in range(dim):
            for col in range(dim):
                if board.square(row, col) == player:
                    scores[row][col] += SCORE_CURRENT
                elif board.square(row, col) == switch_player(player):
                    scores[row][col] -= SCORE_OTHER
                    
    elif board.check_win() == switch_player(player):
        for row in range(dim):
            for col in range(dim):
                if board.square(row, col) == switch_player(player):
                    scores[row][col] += SCORE_OTHER
                elif board.square(row, col) == player:
                    scores[row][col] -= SCORE_CURRENT
                    
# To test this out, I initialized a TTTBoard (taken from the tests above), a scoreboard,
# and identified PLAYERX as the machine player. Uncomment to run.

# print "Testing mc_update_scores(scores, board, player)"
# print "-"*10
# SCORE_CURRENT = 2.0
# SCORE_OTHER = 1.0
# myboard = TTTBoard(3)
# myboard.move(1,1,PLAYERX)
# myboard.move(1,1,PLAYERO)
# myboard.move(1,2,PLAYERO)
# myboard.move(0,1,PLAYERX)
# myboard.move(2,1,PLAYERO)
# myboard.move(0,2,PLAYERX)
# myboard.move(2,0,PLAYERO)
# myboard.move(0,0,PLAYERX)
# print myboard
# print "\n"
# scores = Scoreboard(myboard)
# print scores.get_scoreboard()
# print "\n"
# mc_update_scores(scores.get_scoreboard(), myboard, PLAYERX)
# print scores.get_scoreboard()
# print "\n"

# The scores [[2.0, 2.0, 2.0], [0, 2.0, -1.0], [-1.0, -1.0, 0]] were returned. The
# function appeared to be successful, since the X squares were updated with scores
# of 2.0 and the O squares with scores of -1.0. 

# Next, get_best_move was implemented. This was a bit tricky, but not too 
# complicated. My preferred method of identifying and sorting squares with the
# maximum score was to pair scores with coords, sort the scores, pick out all
# of the top scores, and return a random choice from the top scoring squares.
# The directions mention the scenario when no moves can be made and that that
# should return an error. We did not cover that up to this point, so I simply wrote
# a conditional to look for no moves left that returns from the function a string.

def get_best_move(board, scores):
    """
    Takes a current TTT board and a grid of scores, find all empty squares with
    max score, and randomly returns one as (row, col) tuple.
    """
    dim = board.get_dim()
    empty_squares = []
    
    for row in range(dim):
        for col in range(dim):
            if board.square(row, col) == EMPTY:
                score = scores[row][col]
                empty_squares.append([score, (row, col)])
                
    # Check if there are no empty squares left.
    if len(empty_squares) == 0:
        return "Board is full."
        
    empty_squares = sorted(empty_squares, reverse = True)
    hi_score = empty_squares[0][0]
    hi_score_squares = [square for square in empty_squares if square[0] == hi_score]
    
    return random.choice(hi_score_squares)[1]
    
# I will pass a test board and test scores to this function to simply check if 
# it returns the best move based on the scores provided.

# print "Testing get_best_move(board, scores)"
# print "-"*10
# myboard = TTTBoard(3)
# myboard.move(1,1,PLAYERX)
# myboard.move(1,2,PLAYERO)
# myboard.move(0,1,PLAYERX)
# myboard.move(2,1,PLAYERO)
# print myboard
# scores = [[4, 4, 2], [4, 5, 5], [3, 9, 2]]
# print get_best_move(myboard, scores)
# print "\n"

# That code returns either [4, (0,0)] or [4, (1,0)], which are the best open moves.
# It appears that the code is successful. However, I did find a bug in the return
# statement--I returned the entire list, score and tuple all, instead of just the
# tuple. Fixed by adding a reference to the second element, [1].

# Finally, mc_move must be implemented. This uses the other 3 core functions
# (as well as the Scoreboard class that is largely unnecessary here) to return
# a move based on Monte Carlo sims and scoreboard updates. First the board
# must be cloned so that it can be modified, then a scoreboard must be initialized.
# Then for the number of trials specified by "trials", the board must run through
# a randomized game, the scores must be updated, and a new board must be
# initialized to run all over again.

def mc_move(board, player, trials):
    """
    Takes a current board, the identity of the machine player, and the number
    of trials to run of a Monte Carlo sim to return a move as a (row, col) tuple.
    """
    test_board = board.clone()
    test_scores = Scoreboard(test_board)
    
    for dummy_trial in range(trials):
        mc_trial(test_board, player)
        mc_update_scores(test_scores.get_scoreboard(), test_board, player)
        test_board = board.clone()
        
    return get_best_move(board, test_scores.get_scoreboard())
    
# Now the game can be tested with the console or GUI. The constants below will
# be updated as testing progresses.

# NTRIALS = 1
# SCORE_CURRENT = 1.0
# SCORE_OTHER = 1.0 

# Uncomment to run.
# play_game(mc_move, NTRIALS, False)

# The game appears to run successfully. Games are run until completion without
# error. As long as this continues to run properly, I can focus on improving the 
# three constants so that X never loses. As of now, X appears to win more than 
# O, but not every time. Though O is also using the mc_move logic to compute the
# best move, X goes first and so should never lose. At best, all games should end
# in draws. I will tweak constants to see what results I get. To measure results, 
# I played games until O never wins. I set the timeout to 15 seconds and modified
# the play_game function to return the winner instead of printing the board.

# Uncomment to run.
def o_loss_test1(mc_move_function, ntrials, reverse = False):
    """
    Function to play a game with two MC players.
    """
    # Setup game
    board = TTTBoard(3, reverse)
    curplayer = PLAYERX
    winner = None
    
    # Run game
    while winner == None:
        # Move
        row, col = mc_move_function(board, curplayer, ntrials)
        board.move(row, col, curplayer)

        # Update state
        winner = board.check_win()
        curplayer = switch_player(curplayer)
        
    return winner

# print "Play games until O never wins (manual)"
# print "-"*10
# winner = None
# its = 0
# while winner != PLAYERO:
    # winner = o_loss_test1(mc_move, NTRIALS, False)
    # its += 1
# print "It took", its, "iterations for O to win"

# Below are the results where n = NTRIALS, x = SCORE_CURRENT, y = SCORE_OTHER.
# The numbers indicate how many games were played until O won, and TO indicates
# a timeout where O did not win at all. Draws count as non-win for O.

# n = 20, x = 1, o = 1 -> 17, 04, 08, TO, 03, 02, TO, 03, 01, 08
# n = 30, x = 1, o = 1 -> 07, TO, 17, TO, 07, TO, TO, TO, 15, 09
# n = 40, x = 1, o = 1 -> 03, TO, TO, 06, TO, TO, TO, TO, TO, TO
#---------------------------------------------------------------
# n = 20, x = 3, o = 2 -> 25, 09, 01, 10, 04, 14, 05, 03, TO, 04
# n = 30, x = 3, o = 2 -> 09, TO, 13, 19, TO, 05, 01, TO, TO, 05
# n = 40, x = 3, o = 2 -> 08, TO, 08, TO, TO, TO, TO, 07, TO, TO
#---------------------------------------------------------------
# n = 20, x = 4, o = 1 -> 04, 20, 03, 16, TO, 01, 06, 24, 22, 04
# n = 30, x = 4, o = 1 -> 01, 04, 13, 09, 19, 08, 14, 14, 12, 05
# n = 40, x = 4, o = 1 -> 02, 05, 11, 04, TO, 04, TO, 13, 14, TO
#---------------------------------------------------------------
# n = 20, x = 7, o = 1 -> 04, 18, 03, 13, 04, 02, 04, 11, 02, 01
# n = 30, x = 7, o = 1 -> 13, 05, 05, 10, TO, 14, 04, 17, 04, 15
# n = 40, x = 7, o = 1 -> 11, TO, 18, 08, 04, 08, TO, 04, 01, 15
#---------------------------------------------------------------
# n = 20, x = 1, o = 7 -> 17, 12, TO, TO, 14, 16, TO, TO, TO, 02
# n = 30, x = 1, o = 7 -> TO, TO, TO, TO, TO, TO, TO, TO, TO, TO
# n = 40 will not be tried.

# That work was completed manually, but I will write code that updates a list
# of data computationally (a much better method of measuring results).
# I will rewrite the o_loss_test function to itself play games until O does not
# win, then return the number of iterations taken. I will have to set an arbitrary
# limit to avoid timeouts (timeout set for 60 seconds here) since there are
# 3 separate loops running a total of 3900 times. The max its to run will
# first be set at 100, but if this times out often, I will lower it in increments
# of 20. The results will be analyzed and the best values will be further tested.

def o_loss_test2(mc_move_function, ntrials, reverse = False):
    """
    Function to play a game with two MC players.
    """
    its = 0
    winner = None
    while winner != PLAYERO and its < 30:
        board = TTTBoard(3, reverse)
        curplayer = PLAYERX
        winner = None
        while winner == None:
            row, col = mc_move_function(board, curplayer, ntrials)
            board.move(row, col, curplayer)
            winner = board.check_win()
            curplayer = switch_player(curplayer)
        its += 1
        
    return its

# print "Play games until O never wins"
# print "-"*10
# results = []
# for n in range(1, 40):
    # for x in range(1, 11):
        # SCORE_CURRENT = x
        # for y in range(1, 11):
            # SCORE_OTHER = y
            # iterations = o_loss_test2(mc_move, n, reverse = False)
            # results.append([iterations, n, x, y])
# print results

# I should've referenced my manual entries to see that the max number of
# its to get an O win in the highest iteration cases was around 20. The final
# max its in o_loss_test2 was 20. This still timed out. I reset the max its
# to 30 and ran this code in chunks instead of across the entirety of my ranges.

# print "Play games until O never wins"
# print "-"*10
# results = []
# for n in range(1, 11):
    # for x in range(1, 11):
        # SCORE_CURRENT = x
        # for y in range(1, 11):
            # SCORE_OTHER = y
            # iterations = o_loss_test2(mc_move, n, reverse = False)
            # results.append([iterations, n, x, y])
# print results

# Again with the time limit error...I will only look at ranges of x and y
# separately. In fact, I will look at a very simple base case to make sure
# that this code works.

# results = []
# for n in range(1, 2):
    # for x in range(1, 2):
        # SCORE_CURRENT = x
        # for y in range(1, 2):
            # SCORE_OTHER = y
            # iterations = o_loss_test2(mc_move, n, reverse = False)
            # results.append([iterations, n, x, y])
# print results

# The list [[1, 1, 1, 1]] was returned. Now I will increase the ranges from inner-
# most nested loop y outward to n until it times out again.

# results = []
# for n in range(1, 2):
    # for x in range(1, 3):
        # SCORE_CURRENT = x
        # for y in range(1, 3):
            # SCORE_OTHER = y
            # iterations = o_loss_test2(mc_move, n, reverse = False)
            # results.append([iterations, n, x, y])
# results = sorted(results, reverse = True)
# for item in results:
    # print item

# When all 3 ranges were set to [1,6), the best results were: [30, 5, 3, 4] and
# [28, 3, 1, 5]. This is odd since the disparity between x and y is vastly different
# (1 vs. 4), but somewhat holds when you see that n was 5 vs. 3. Two more trials
# allowed O to win less even though the x and y values were so close. The lowest 
# scores (i.e. least its to an O win) occurred whenever n was low or x < y.

# Let's look at what the scoring system is doing. It takes a completed board and
# scores it +winner for every winner square and -loser for every loser square. 
# The scores grow at two different rates if x and y are different. If x is set very 
# high, then you get results where x-win squares are scored a lot higher than
# x-loss squares. Let's look at those sets of data, holding x equal to 10 and
# looping over y values from 1 to 10. n will be in range [1,6).

# results = []
# for n in range(1, 6):
    # x = SCORE_CURRENT = 10
    # for y in range(1, 11):
        # SCORE_OTHER = y
        # iterations = o_loss_test2(mc_move, n, reverse = False)
        # results.append([iterations, n, x, y])
# results = sorted(results, reverse = True)
# for item in results:
    # print item

# Strangely, [21, 3, 10, 1] and [17, 2, 10, 10] were the highest scores, where the
# x/y disparities were at polar opposites to each other (and with only 1 extra trial).
# It seems like CodeSkulptor is ill-equipped to computationally handle the statements
# necessary to really tease out the best values. It seems, though, that the x/y
# disparity and its effect on O winning can be lumped into general groups where
# disparity is either very low, medium, or very high. 

# results = []
# for n in range(1,6):
    # for x in range(1, 11):
        # SCORE_CURRENT = x
        # for addition in range(1, 8, 3):
            # y = SCORE_OTHER = x + addition
            # iterations = o_loss_test2(mc_move, n, reverse=False)
            # results.append([iterations, n, x, y])
# results = sorted(results, reverse = True)
# for item in results:
    # print item

# The best: [30, 5, 8, 15] and [30, 5, 6, 13], where n was at its max, and the
# disparity was around 1:2 for x:y. This corresponds to a growth rate of x-win
# squares at half the speed of o-win squares (where x would have to block o).
# Let's keep x and y at 1:2 and play with varying values of n (1 to 30).

# results = []
# for n in range(20, 21):
    # x = SCORE_CURRENT = 1
    # y = SCORE_OTHER = 2
    # iterations = o_loss_test2(mc_move, n, reverse=False)
    # results.append([iterations, n, x, y])
# results = sorted(results, reverse = True)
# for item in results:
    # print item

# 30 and 20 trials timed out. I must, unfortunately, manually adjust the n
# value and record the results (like I did before). I will set the max attempts
# in o_loss_test to 50 since I am running one call at a time.

def o_loss_test3(mc_move_function, ntrials, reverse = False):
    """
    Function to play a game with two MC players.
    """
    its = 0
    winner = None
    while winner != PLAYERO and its < 50:
        board = TTTBoard(3, reverse)
        curplayer = PLAYERX
        winner = None
        while winner == None:
            row, col = mc_move_function(board, curplayer, ntrials)
            board.move(row, col, curplayer)
            winner = board.check_win()
            curplayer = switch_player(curplayer)
        its += 1
        
    return its

# n = 10
# x = SCORE_CURRENT = 1
# y = SCORE_OTHER = 2
# iterations = o_loss_test3(mc_move, n, reverse=False)
# print "# Took", iterations, "iterations where n, x, y =", n, x, y

# Took 12 iterations where n, x, y = 10 1 2
# Took 43 iterations where n, x, y = 20 1 2
# Took 50 iterations where n, x, y = 30 1 2
#
# Took 4 iterations where n, x, y = 10 1 3
# Took 13 iterations where n, x, y = 10 1 4
# Took 13 iterations where n, x, y = 10 1 5
# Took 5 iterations where n, x, y = 10 1 6
# Took 1 iterations where n, x, y = 10 1 7
# Took 1 iterations where n, x, y = 10 2 1
# Took 18 iterations where n, x, y = 10 3 1
# Took 2 iterations where n, x, y = 10 4 1
# Took 8 iterations where n, x, y = 10 5 1
# Took 2 iterations where n, x, y = 10 6 1
# Took 5 iterations where n, x, y = 10 7 1
#
# Took 50 iterations where n, x, y = 20 1 2
# Took 25 iterations where n, x, y = 20 1 3
# Took 41 iterations where n, x, y = 20 1 4
# Took 50 iterations where n, x, y = 20 1 5
# Took 50 iterations where n, x, y = 20 1 6
# Took 12 iterations where n, x, y = 20 1 7
#
# Took 3 iterations where n, x, y = 20 2 1
# Took 4 iterations where n, x, y = 20 3 1
# Took 7 iterations where n, x, y = 20 4 1
# Took 14 iterations where n, x, y = 20 5 1
# Took 1 iterations where n, x, y = 20 6 1
# Took 9 iterations where n, x, y = 20 7 1

# From the above data, it appears that the growth rate of o-win squares being
# higher than that of x-win squares greatly affects the efficacy of the function
# to block o wins. This puts emphasis on blocking squares in which o in known to
# win vs. squares in which x is known to win. Defense is the key to winning (or 
# here, simply not losing) when Monte Carlo sims are used to determine best move.
# At 20 trials, a 1:5 ratio of x:y appeared to be the best. I will test this out via
# the GUI.

# Uncomment to run.
# NTRIALS = 20
# SCORE_CURRENT = 1.0
# SCORE_OTHER = 5.0 

# run_gui(3, PLAYERX, mc_move, NTRIALS, False)

# Works like a charm!

##=================================================================
##=================================================================