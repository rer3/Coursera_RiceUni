"""
Rice University / Coursera: Principles of Computing (Part 2)
Week 3: Project 3
Tic-Tac-Toe - Minimax
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# All import statements needed.

import codeskulptor
import simplegui
codeskulptor.set_timeout(60)

# Below is the link to the description of this assignment.

COURSE = "https://class.coursera.org/principlescomputing1-004/"
DESCRIPTION = COURSE + "wiki/view?page=tictactoemm"

#-----------------------------------------------------------------
## Provided TicTacGUI class, constants, and run_gui function (poc_ttt_gui).

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


#-----------------------------------------------------------------
## Provided TTTBoard class, constants, and switch_player and play_game functions
## (poc_ttt_provided).

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

##=================================================================

DIRECTIONS = '''
Overview
----------
We have previously seen Tic-Tac-Toe in part 1 of this class. In this assignment, we 
are going to revisit the game and develop an alternative strategy to play the game.

For this assignment, your task is to implement a machine player for Tic-Tac-Toe 
that uses a Minimax strategy to decide its next move. You will be able to use the 
same console-based interface and graphical user interface to play the game as you 
did before. Although the game is played on a 3×3 grid, your version should be able to 
handle any square grid (however, the time it will take to search the tree for larger 
grid sizes will be prohibitively slow). We will continue to use the same grid 
conventions that we have used previously.

This project does not require you to write a lot of code. It does, however, bring 
together a lot of concepts that we have previously seen in the class. We would like 
you to think about how these concepts are coming together to enable you to build 
a relatively complex machine player with very little code. Further, you should think 
about the situations in which Minimax or Monte Carlo might produce better/worse 
machine players for games other than Tic-Tac-Toe.

Provided Code
----------
We have provided a TTTBoard class for you to use. This class keeps track of the 
current state of the game board. You should familiarize yourself with the interface 
to the TTTBoard class in the poc_ttt_provided module. The provided module also 
has a switch_player(player) function that returns the other player (PLAYERX or 
PLAYERO). The provided module defines the constants EMPTY, PLAYERX, PLAYERO, 
and DRAW for you to use in your code. The provided TTTBoard class and GUI use 
these same constants, so you will need to use them in your code, as well.

At the bottom of the provided template, there are example calls to the GUI and 
console game player. You may uncomment and modify these during the development 
of your machine player to actually use it in the game. Note that these are the 
same calls we used previously for your Monte Carlo strategy, so they take an 
ntrials parameter. You can pass anything you want as ntrials, since you will not 
be using it for Minimax. In order to allow us to use the same infrastructure, we 
have also provided a move_wrapper function in the template that you can pass 
to play_game and run_gui. This wrapper simply translates between the inputs and 
outputs of your function and those that were expected if you were implementing 
a Monte Carlo player.

Testing your mini-project
----------
As you implement your machine player, we suggest that you build your own collection 
of tests using the poc_simpletest module that we have provided. Please review this 
page for an overview of the capabilities of this module. These tests can be organized 
into a separate test suite that you can import and run in your program as we 
demonstrated for Solitaire Mancala. To facilitate testing on the first few mini-
projects, we will create a thread in the forums where students may share and refine
their test suites for each mini-project.

IMPORTANT: In this project, you will use Minimax to search the entire game tree. 
If you start with an empty Tic-Tac-Toe board, it will take a long time for your 
strategy to search the tree. Therefore, we strongly suggest that you write tests
that start with a partially full board. This will allow your code to run much faster 
and will lead to a more pleasant development and debugging experience.

Finally, submit your code (with the calls to play_game and run_gui commented out) 
to this Owltest page. This page will automatically test your mini-project. It will run 
faster if you comment out the calls to play_game and run_gui before submitting. 
Note that trying to debug your mini-project using the tests in OwlTest can be very 
tedious since they are slow and give limited feedback. Instead, we strongly suggest
 that you first test your program using your own test suite and the provided GUI. 
 Programs that pass these tests are much more likely to pass the OwlTest tests.

Remember that OwlTest uses Pylint to check that you have followed the coding style 
guidelines for this class. Deviations from these style guidelines will result in 
deductions from your final score. Please read the feedback from Pylint closely. 
If you have questions, feel free to consult this page and the class forums.

When you are ready to submit your code to be graded formally, submit your code 
to the CourseraTest page for this mini-project that is linked on the main assignment page.

Machine Player Strategy
----------
Your machine player should use a Minimax strategy to choose the next move from 
a given Tic-Tac-Toe position. As the objective of this assignment is to help you 
bring together what you have learned, we ask that you do not search for pseudo-
code to implement Minimax. At this point in the class, we hope that you can use 
the examples in the lectures and an English language description and be able to
 implement Minimax.

The general idea on Minimax is to search the entire game tree alternating between 
minimizing and maximizing the score at each level. For this to work, you need to 
start at the bottom of the tree and work back towards the root. However, instead 
of actually building the game tree to do this, you should use recursion to search the 
tree in a depth-first manner. Your recursive function should call itself on each child 
of the current board position and then pick the move that maximizes (or minimizes, 
as appropriate) the score. If you do this, your recursive function will naturally 
explore all the way down to the bottom of the tree along each path in turn, leading 
to a depth first search that will implement Minimax. The following page describes 
the process in more detail.

As you recursively call your minimax function, you should create a copy of the board 
to pass to the next level. When the function returns, you no longer need that copy of 
the board. In this manner, you are dynamically constructing the part of the game 
tree that you are actively looking at, but you do not need to keep it around.

For this mini-project, you need only implement one function:

* mm_move(board, player): This function takes a current board and which player 
    should move next. The function should use Minimax to return a tuple which is a 
    score for the current board and the best move for the player in the form of a 
    (row, column) tuple. In situations in which the game is over, you should return 
    a valid score and the move (-1, -1). As (-1, -1) is an illegal move, it should only 
    be returned in cases where there is no move that can be made.
    
You should start from this code that imports the Tic-Tac-Toe class and a wrapper 
function to enable you to play the game. You may add extra helper functions if so desired.

Hints
----------
You do not need to write a lot of code to implement Minimax, but it can be difficult 
to get everything working correctly. Here are some hints that may help you out:

* Do not forget the base case in your recursive function. Think carefully about when 
    you can return with an answer immediately.
* Remember to make a copy of the board before you recursively call your function. 
    If you do not, you will modify the current board and you will not be searching the 
    correct tree.
* The SCORES dictionary is useful. You should use it to score a completed board. For 
    example, the score of a board in which X has won should be SCORES[provided.PLAYERX]. 
    If the game is a draw, you should score the board as 0.
* In Minimax, you need to alternate between maximizing and minimizing. Given the SCORES 
    that we have provided you with, player X is always the maximizing player and play O 
    is always the minimizing player. You can use an if-else statement to decide when to 
    maximize and when to minimize. But, you can also be more clever by noticing that if 
    you multiply the score by SCORES[player] then you can always maximize. Why? 
    Because this has the effect of negating player O's scores allowing you to maximize 
    instead of minimize for player O.
* Minimax can be slow when there are a lot of moves to explore. The way we have set 
    up the scoring, you do not always need to search everything. If you find a move 
    that yields a winning score (+1 for X or -1 for O), you know that you cannot do 
    any better by continuing to search the other possible moves from the current board. 
    So, you can just return immediately with the score and move at that point. This will 
    significantly speed up the search.
'''

##=================================================================

# Write a function mm_move(board, player) that computes "minimax" 
# scores for TTT boards. PLAYERX pursues maximum scores and PLAYERO
# pursues minimum scores. Use recursion to perform a depth first search
# on each board configuration, terminating when there is a winner or draw.

# The mm_move implementation takes advantage of a dictionary called
# MEMORY to store computed scores for board configurations to improve
# running time. The recursive function has a base case equal to a finished
# game with a winner (PLAYERX, PLAYERO, DRAW) and no more moves.
# If no moves, a square (-1, -1) is returned, which is an illegal move.

# Start with the base case where there is a winner and no move can be made.
# This check can be done with a call to board.check_win(). If there is no winner,
# proceed with the recursive call. First initialize best_score with a placeholder
# that is the extreme opposite of the player score (so if player == X, the score
# must be init'd to -INF since we are looking for the largest score for X). Then
# for each empty square in the board: clone the board, move the player to the
# empty square, check the "memory" for the board config score (or make a recursive
# call to mm_move with the new board and update the memory), and then check
# against certain conditions.

# For player X, if the computed score of the board config is greater than the
# best score (starting out at -INF), best_score must be updated along with the
# associated best_square. The opposite is true for player O, where best_score is
# updated with the config score if it is less than best_score. If the config score is
# equal to the player score, that signifies a win and the function can return the
# move as it is arbitrary whether other moves exist that can lead to a win.
# This repeats for every empty move in the board, and then the best score and
# the associated best square are returned.

# There must be a trick to combining a best_score/best_square update that affects
# player X and O equally so that two separately conditionals need not be used. 
# Instinctually, I want to write two statements (if player == PLAYERX, if player ==
# PLAYER O), but it is hinted at that this can be done in one single statement.
# I have to identify how a config score can be compared to best score the same
# way for both players. It's obvious that X = 1 and O = -1 is a good start. Since
# for X, score > best score means updating best score, and for O score < best
# score means updating best score, I could integrate the player score into that
# computation in a way that makes a generic "score > best score" work. By
# multiplying player score by both sides, player X's check is unchanged as player
# X's score is +1, but player O, with a score of -1, would see a change such that
# its largest value between score and best score would be swapped. If the starting
# best_score is INF, and it's looking for a smaller number, it wants score < INF. 
# If score = 0, and both sides are multiplied by -1, that changes the expression
# to 0 > -INF, or score * player score > best score * player score.

# SCORING VALUES - DO NOT MODIFY
SCORES = {PLAYERX: 1,
          DRAW: 0,
          PLAYERO: -1}
          
# Initialize a "memory" variable to store scores for board configurations.

MEMORY = {}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """ 
    # Check for the base case.
    winner = board.check_win()
    if winner != None:
        return SCORES[winner], (-1, -1)
    else:
        if player == PLAYERX:
            best_score = float("-inf")
        elif player == PLAYERO:
            best_score = float("inf")
        best_square = (-1, -1)
        # Iterate over each potential move. Reference MEMORY or
        # execute recursive call with updated board and other player.
        for square in board.get_empty_squares():
            test_board = board.clone()
            test_board.move(square[0], square[1], player)
            if str(test_board) in MEMORY:
                score = MEMORY[str(test_board)]
            else:
                score, dummy_square = mm_move(test_board, switch_player(player))
                MEMORY[str(test_board)] = score
            # Return if winning move, otherwise update score accordingly.   
            if score == SCORES[player]:
                return score, square
            if score * SCORES[player] > best_score * SCORES[player]:
                best_score = score
                best_square = square
                
    return best_score, best_square
        
def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer. Uncomment when submitting to OwlTest.

#play_game(move_wrapper, 1, False)        
#run_gui(3, PLAYERO, move_wrapper, 1, False)

##=================================================================
##=================================================================