"""
Rice University / Coursera: Principles of Computing (Part 2)
Week 4: Homework 4
"""
#===========================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#===========================================================

# All import statements needed.

import simplegui

#-----------------------------------------------------------------
## Provided GUI at poc_fifteen_gui for Fifteen puzzle implementation.

# constants
TILE_SIZE = 60

class FifteenGUI:
    """
    Main GUI class
    """
    def __init__(self, puzzle):
        """
        Create frame and timers, register event handlers
        """
        self._puzzle = puzzle
        self._puzzle_height = puzzle.get_height()
        self._puzzle_width = puzzle.get_width()

        self._frame = simplegui.create_frame("The Fifteen puzzle",
                                             self._puzzle_width * TILE_SIZE,
                                             self._puzzle_height * TILE_SIZE)
        self._solution = ""
        self._current_moves = ""
        self._frame.add_button("Solve", self.solve, 100)
        self._frame.add_input("Enter moves", self.enter_moves, 100)
        self._frame.add_button("Print moves", self.print_moves, 100)
        self._frame.set_draw_handler(self.draw)
        self._frame.set_keydown_handler(self.keydown)
        self._timer = simplegui.create_timer(250, self.tick)
        self._timer.start()
        self._frame.start()

    def tick(self):
        """
        Timer for incrementally displaying computed solution
        """
        if self._solution == "":
            return
        direction = self._solution[0]
        self._solution = self._solution[1:]
        try:
            self._puzzle.update_puzzle(direction)
        except:
            print "invalid move:", direction

    def solve(self):
        """
        Event handler to generate solution string for given configuration
        """
        new_puzzle = self._puzzle.clone()
        self._solution = new_puzzle.solve_puzzle()

    def print_moves(self):
        """
        Event handler to print and reset current move string
        """
        print self._current_moves
        self._current_moves = ""

    def enter_moves(self, txt):
        """
        Event handler to enter move string
        """
        self._solution = txt

    def keydown(self, key):
        """
        Keydown handler that allows updates of puzzle using arrow keys
        """
        if key == simplegui.KEY_MAP["up"]:
            try:
                self._puzzle.update_puzzle("u")
                self._current_moves += "u"
            except:
                print "invalid move: up"
        elif key == simplegui.KEY_MAP["down"]:
            try:
                self._puzzle.update_puzzle("d")
                self._current_moves += "d"
            except:
                print "invalid move: down"
        elif key == simplegui.KEY_MAP["left"]:
            try:
                self._puzzle.update_puzzle("l")
                self._current_moves += "l"
            except:
                print "invalid move: left"
        elif key == simplegui.KEY_MAP["right"]:
            try:
                self._puzzle.update_puzzle("r")
                self._current_moves += "r"
            except:
                print "invalid move: right"

    def draw(self, canvas):
        """
        Draw the puzzle
        """
        for row in range(self._puzzle_height):
            for col in range(self._puzzle_width):
                tile_num = self._puzzle.get_number(row, col)
                if tile_num == 0:
                    background = "rgb(128, 128, 255)"
                else:
                    background = "Blue"
                tile = [[col * TILE_SIZE, row * TILE_SIZE],
                        [(col + 1) * TILE_SIZE, row * TILE_SIZE],
                        [(col + 1) * TILE_SIZE, (row + 1) * TILE_SIZE],
                        [col * TILE_SIZE, (row + 1) * TILE_SIZE]]
                canvas.draw_polygon(tile, 1, "White", background)
                canvas.draw_text(str(tile_num),
                                 [(col + .2) * TILE_SIZE,
                                  (row + 0.8) * TILE_SIZE],
                                 2 *  TILE_SIZE // 3, "White")

#-----------------------------------------------------------------
## Provided Fifteen puzzle template. It imports poc_fifteen_gui, which is
## contained in this doc, so references to the module have been removed.

"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """
    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    ## GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ## Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ## Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    ## Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    ## Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""


# Start interactive simulation (uncomment to run)
#FifteenGUI(Puzzle(4, 4))

##===========================================================

DIRECTIONS = '''
The Original Fifteen Puzzle
----------
For our initial mini-project, we will build a program that solves the Fifteen puzzle
(https://en.wikipedia.org/wiki/15_puzzle) which was popularized in the 1800s by
Loyd. The original version of the puzzle consists of 15 tiles numbered one to 
fifteen that lie on a 4x4 grid. Since there are 16 spaces in the grid, one space
is empty.

This verison of the puzzle starts in an initial configuration where the tiles
numbered one to four lie on the top row (left to right), tiles five to eight on
the next row down, then nine to twleve, then thirteen to fifteen on the bottom
row with the blank space starting in the lower right corner.

To manipulate the puzzle, the player can slide a tile adjacent to the blank space
into the blank space. Repeating this process scrambles the order of the tiles.
The challenge is to bring the tiles back into the initial configuration.

A Modified Version of the Fifteen Puzzle
----------
Before discussing how to solve the Fifteen puzzle, first we will make a minor
modification to the game design of the puzzle that simplifies reasoning about
the game. In the original, the tiles are numbered 1-15 with the blank space at the
lower right. In this version, the blank space can be viewed as logically
corresponding to the number 16.

From a computational POV, this design has two drawbacks: the tile numbers start
at one and the number logically associated with the blank space depends on the
size of the puzzle. A better design would be to start with the blank space in the
upper left-hand corner and associate the number zero with it. Now, the remaining
tiles are placed as usual in ascending order from left to right and top to bottom.

The program template (provided above) implements an interactive implementation
of this modified version of the Fifteen puzzle. Running the template initializes the
puzzle in its solved config with the blank space (represented by the light blue tile
with the number zero) in the upper left corner. You can use the arrow keys to swap
tile zero with its neighboring tiles. With a fairly small number of key presses, one
can scramble the board so that it is difficult to return the board to the solved
configuration. Your task for this week is to implement a solver for this version.

To begin, we suggest that you spend a few minutes examining the template in
detail. The main component of the template is a Puzzle class that provides the
functionality for our template. The contents of the board are represented as a 2D
list of numbers. In particular, note that the number of the tile current positioned
in the row row and column col of the puzzle is self._grid[row][col]. Here, row zero
is the topmost row and column zero is the leftmost column with indices increasing
from left to right and top to bottom.

Modeling Solutions to the Fifteen Puzzle
----------
Our goal for both the homework and mini-project will be to add several methods
to the Puzzle class that automatically solve the puzzle after it has been scrambled.
The solution will be a sequence of tile swaps between the tile zero and its neighbors.
At this point, we must make a critical decision: How will we represent solutions?

One possibility would be to record the path of tile zero as it moves through the
puzzle during the solution process. This choice is awkward for two reasons: the
position of tile zero is a pair of indices, which requires more indexing. Also,
building an inconsistent path for the tile is possible (i.e. a bug could lead to a
path that is not physically possible).

Instead, we have chosen to encode the path of tile zero as a string whose entries
are either 'l', 'r', 'u', or 'd'. These letters correspond to swaps of tile zero with
its left, right, up, and down neighbors, respectively. This design choice will allow
us to specify relative movements of tile zero without worrying about its position
and record these movements more compactly as a string.

Moreover, illegal movements such as attempting to swap tile zero across the border
of the puzzle can be handled easily, allowing for simpler debugging. To experiment
with this model, use the arrow keys to move tile zero around the puzzle and then
click the "Print moves" button. The corresponding movement string will be printed
in the console. We recommend that you use this functionality when creating
your own puzzle configs for testing.
'''

##===========================================================

def hw_401():
    """
    QUESTION 1: Understanding move string
    
    A 4x4 puzzle in its solved config is shown below. Which config is the result
    of applying the move string "drdr" to the puzzle? (Screenshots provided,
    here represented as four lines of four numbers)
      0   1   2   3
      4   5   6   7
      8   9 10 11
    12 13 14 15
    
    Option 1
      1   2   3   0
      4   5   6   7
      8   9 10 11
    12 13 14 15
     
     Option 2
      1   5   2   3
      4   6 10   7
      8   9   0 11
    12 13 14 15
     
     Option 3
      0   4   2   3
      5   1   6   7
      8   9 10 11
    12 13 14 15
     
     Option 4
      4   1   2   3
      5   9   6   7
      8 10   0 11
    12 13 14 15
    """
    # Option 1 is out because it corresponds to move string "rrr".
    # Option 3 is out because 0 must be in the initial 10 position for move
    # "drdr", regardless of orientation of the other numbers.
    
    # Options 2-4 have 0 in the correct position, but the other numbers are
    # different. An easy way to solve this is to think through the steps.
    # A "d" move swaps 0 with 4 since it is beneath it initially. Check if either
    # option has 4 in the (0,0) position. Option 4 does. But I have to be careful.
    # If the 0 hits that first position again, it will move the 4 and could place it
    # elsewhere. A "drdr" move goes (0,0) to (1,0) to (1,1) to (2,1) to (2,2).
    # Note that (0,0) is never encountered again, so 4 indeed should be in the
    # upper left corner.
    
    answer = " 4  1  2  3" + "\n"
    answer += " 5  9  6  7" + "\n"
    answer += " 8 10  0 11" + "\n"
    answer += "12 13 14 15"
    
    print "Question 401 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_401()

##===========================================================

def hw_402():
    """
    QUESTION 2
    
    Which move string updates the puzzle from the config shown on the left to
    the config shown on the right?
    Left                      Right
      1   2   3   7           5   1   2   7
      5   4   9   6           4   8   3   6
      8   0 10 11           0   9 10 11
    12 13 14 15         12 13 14 15
    
    Note that on the left, the tiles ten to fifteen are in their correct locations.
    On the right, tile nine has also been moved to its correct location. Hint:
    From the solved (initial) config, enter the move string:
    "ddrdrudlulurrrlldluurrrdllldr" in the input field to generate the left config.
    
    Option 1
    "ruldrul"
    
    Option 2
    "urrulllddruld"
    
    Option 3
    "urullddruld"
    
    Option 4
    "ruldrulld"
    """
    # This is simple. Since we are given the string to generate the left config, 
    # all I must do is enter all four options and see which leads to the right
    # config.
    
    # Call to GUI commented out after answer found.
    #FifteenGUI(Puzzle(4,4))
    
    # Option 1 is out. Option 2 is very close, but out. Ten bucks says it's option 4.
    # Option 3 appears to be correct. I will test option 4 to verify...and it's out.
    
    answer = "urullddruld"
    
    print "Question 402 Answer:"
    print answer
    print "-"*50
    print "\n"  
    
hw_402()

##===========================================================

def hw_403():
    """
    QUESTION 3: Solving a 2x2 puzzle
    
    For the next three problems, we will focus on exploring the behavior of a
    2x2 puzzle. The size of the puzzle is passed to the initializer for the Puzzle
    class as a height and a width. Modify the last line of the template to create
    a 2x2 puzzle.
    
    Now, from the solved config, enter the move string "rdlu" repeatedly. How
    many times do you need to enter this string to return the puzzle to its
    solved config?
    
    Options: 1, 5, 3, 4.
    """
    # I will initialize a 2x2 instance of the Puzzle to test this out.
    
    # Call to GUI commented out after answer found.
    #FifteenGUI(Puzzle(2,2))
    
    answer = 3
    
    print "Question 403 Answer:"
    print answer
    print "-"*50
    print "\n"  
    
hw_403()

##===========================================================

def hw_404():
    """
    QUESTION 4
    
    Starting from the config shown below, which move string returns the 2x2
    puzzle to its solved config?
    0 2
    3 1
    
    Option 1
    "dudu"
    
    Option 2
    ""
    
    Option 3
    "rdlu"
    
    Option 4
    "rdul"
    """
    # Option 1 is out because it simply swaps zero and three 4 times.
    # Option 2 is out because it does nothing, and the config here is not solved.
    # Option 3 applies the "rdlu" method from question 2 and works.
    # Option 4, to verify that it's incorrect, creates this same config shown here.
    
    answer = "rdlu"
    
    print "Question 404 Answer:"
    print answer
    print "-"*50
    print "\n"  
    
hw_404()
    
##===========================================================

def hw_405():
    """
    QUESTION 5
    
    For config shown below, which of the following move strings return the puzzle
    to its solved config?
    0 3
    1 2
    
    Option 1
    "drul"
    
    Option 2
    ""
    
    Option 3
    "rdul"
    
    Option 4
    "druldruldruldrul"
    """
    # Multiple options could be correct here.
    # Option 1 is correct, and it appears to be the reverse of the "rdlu" method.
    # Option 2 is out because this config here is not solved.
    # Option 3 creates the same config shown here.
    # Option 4 is long and should be investigated by calling the GUI and checking.
    
    # Call to GUI commented out after answer found.
    #FifteenGUI(Puzzle(2,2))
    
    # Option 4 is also correct. It applies the "drul" method, reverse of "rdlu",
    # and solves it with the first four moves. The next twelve moves rescramble
    # and resolve the puzzle.
    
    answer = "drul" + "\n"
    answer += "druldruldruldrul"
    
    print "Question 405 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_405()

##===========================================================

def hw_406():
    """
    QUESTION 6: The overall strategy for solving the Fifteen puzzle
    
    With the preliminaries out of the way, we now describe how to solve the general
    m x n version of the Fifteen puzzle. The solution process consists of repeatedly
    repositioning tiles into their solved positions in the puzzle. We refer to each
    instance of this process as "solving" for a tile at a specified position in the puzzle.
    
    The solution process has three phases:
    1.) We first solve the bottom m - 2 rows of the puzzle (in a bottom to top
        order) to reduce the problem to that of solving a 2 x n puzzle.
    2.) We then solve the rightmost n - 2 columns of the top two rows of the 
        puzzle (in a right to left order) to reduce the problem to that of solving
        a 2x2 puzzle.
    3.) Finally, we then solve this 2x2 puzzle based on the observations in 
        problems 3-5 here.
        
    Invariants for the Fifteen Puzzle
    -----
    In the next four problems, we will explore one particular strategy for
    implementing phase one. The key to this strategy will be to develop an
    invariant that reflects the state of the puzzle during phase one and then
    implement solution methods that maintain this invariant.
    
    Phase one will have one invariant lower_row_invariant(i, j) which is true 
    prior to solving for the tile at position (i,j) where i > j. This invariant
    consists of the following conditions:
    * Tile zero is positioned at (i, j).
    * All tiles in rows i + 1 or below are positioned at their solved location.
    * All tiles in row i to the right of position (i, j) are positioned at their
        solved location. 
        
    Problem: Which of the configs below satisfy the invariant 
    lower_row_invariant(2, 1)?
    
    Option 1
      4   1   7   2
      8   6   9   3
      5   0 10 11
    12 13 14 15
    
    Option 2
      1   2   6   3
      4   5 11 10
      8   0   9   7
    12 13 14 15
    
    Option 3
      2   4   6   5
      1 10   3   7
      8   9   0 11
    12 13 14 15
    
    Option 4
      8   1   2   3
      9   6   4   7
      5   0 10 11
    12 13 14 15
    """
    # There may be multiple correct answer to this problem.
    # Option 3 is out because 0 is not positioned at (2, 1), failing condition 1.
    # Option 2 is out because 10 and 11 are not positioned to the right of 0,
    # failing condition 3.
    # Options 1 and 4 both satisfy condition 2, with 12-15 in their solved locations.
    
    answer = " 4  1  7  2" + "\n"
    answer += " 8  6  9  3" + "\n"
    answer += " 5  0 10 11" + "\n"
    answer += "12 13 14 15" + "\n"
    answer += "-"*10 + "\n"
    answer += " 8  1  2  3" + "\n"
    answer += " 9  6  4  7" + "\n"
    answer += " 5  0 10 11" + "\n"
    answer += "12 13 14 15" + "\n"  
    
    print "Question 406 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_406()

##===========================================================

def hw_407():
    """
    QUESTION 7: Solving for tiles in the lower rows
    
    In phase one, we will implement two solution methods for positions in the
    lower rows. The method solve_interior_tile(i, j) will solve for all positions
    except for those in the left column (j > 0). The method solve_col0_tile(i)
    will solve for positions in the leftmost column.
    
    The solution method solve_interior_tile(i, j) is related to the invariants as
    follows: if the invariant lower_row_invariant(i, j) is true prior to execution
    of solve_interior_tile(i, j), the invariant lower_row_invariant(i, j-1) should
    be true after execution of this method. In short, the solution method should
    update the puzzle so the invariant is still true.
    
    Following the examples in the notes on invariants (https://class.coursera.org/
    principlescomputing2-004/wiki/view?page=invariants), the execution trace
    of the solver can be annotated with assertions of the form:
        ...
        assert my_puzzle.lower_row_invariant(i, j)
        my_puzzle.solve_interior_tile(i, j)
        assert my_puzzle.lower_row_invariant(i, j-1)
        ...
    where my_puzzle is the name of the puzzle being solved.
    
    Problem: Which annotated execution trace captures the relationship between
    the solution method solve_col0_tile and the invariant lower_row_invariant?
    Remember that once the entire ith row is solved, the solution process then
    proceeds to the rightmost column of the i-1st row. You may assume that
    the puzzle is m x n.
    
    Option 1
    ...
    assert my_puzzle.lower_row_invariant(i, 0)
    my_puzzle.solve_col0_tile(i)
    assert my_puzzle.lower_row_invariant(i - 1, n)
    ...
    
    Option 2
    ...
    assert my_puzzle.lower_row_invariant(i, 0)
    my_puzzle.solve_interior_tile(i, 0)
    assert my_puzzle.lower_row_invariant(i - 1, n - 1)
    ... 
    
    Option 3
    ...
    assert my_puzzle.lower_row_invariant(i, 0)
    my_puzzle.solve_col0_tile(i)
    assert my_puzzle.lower_row_invariant(i - 1, n -1)
    ... 
    
    Option 4
    ...
    assert my_puzzle.lower_row_invariant(i, 0)
    my_puzzle.solve_col0_tile(i)
    assert my_puzzle.lower_row_invariant(i, n - 1)
    ... 
    """
    # Let's break down what this is saying. Method solve_interior_tile(i,j) (SIT)
    # solves for all positions where j = 1 to m. Method solve_col0_tile(i) (SC0T)
    # solves for positions where j = 0. If lower_row_invariant(i, j) (LRI) is true
    # prior to SIT(i,j), then LRI(i,j-1) is true after SIT(i,j) is executed. Meaning,
    # SIT(i,j) should update the puzzle in a way where the invariant holds true.
    
    # That relationship manifests itself like so: if (i,j) is a spot at, say, (2,2)
    # on a 4x4 board, and LRI(2,2) is true--so all numbers in rows i+1 and beyond
    # as well as all numbers to the right of (i,j), or (i,j = j+1 to width)--then
    # after executing SIT(2,2), LRI(2,1) is true. Why? Because SIT(2,2) solved
    # for (2,2), placing the solved value in its rightful place. Now the focus is 
    # placed on (2,1) knowing that all values to the right of it (2,2) and (2,3), 
    # as well as all values in the rows below it are in their solved positions--
    # which is what the invariant LRI being true indicates. 
    
    # In the problem, the relationship referenced is that between solution method
    # SC0T and LRI, with a reminder that once the entire ith row is solved, the
    # solution process proceeds to the rightmost column of the i-1st row. This
    # means that after SC0T(2,0), the focus then proceeds to (1,3). We are then
    # asked to choose the annotated execution trace that captures this relationship.
    
    # Let's look at this assuming height = m and width = n. In my example, both
    # were equal to 4. After SC0T(2,0), I jumped focus to (i,j) = (1,3). Using the
    # height and width variables, the focus jumped to (i -1, n-1). But what about
    # LRI? LRI(2,0) was true before SC0T, so tiles (2,1), (2,2) and (2,3), as well
    # as all in row 3, were in order. After the focus jumps to row 1, there are no
    # tiles to the right of (i, j), but all tiles in the rows below are in their solved 
    # positions, which is all tiles from before plus the addition of (2,0).
    
    # The convention demonstrated in the SIT/LRI example appeared to show the
    # second call to LRI, after SIT, having indices that correspond to the initial
    # indices i and j. If (i, j) = (2,1) and SIT is executed on that tile, LRI(i, j-1) 
    # should hold true, which is just LRI(2,0) where i = 2 and j = 1. In fact, 
    # (i, j-1) is simply where the new focus is after solving a tile.
    
    # With that in mind, pertaining to the SC0T/LRI relationship, the first call 
    # should be to (i, j) which is really (i, 0) since you are at the first col where
    # j = 0. All options show these args being passed to the first LRI call. 
    # The SC0T method should be called on just i. Then the second call to LRI
    # should reflect the relationship between the new indices and the old. i was
    # 2 and became 1, a change of i - 1. j was 0 and become 3 (or n - 1). Note
    # that j jumping to the end of the row above is equivalent to a leftward (-1)
    # move, so this decrement representation is valid.
    
    # Option 1 is out because it passes n to LRI, an index outside of the grid's range.
    # Option 2 is out because SC0T takes one parameter, i, and not two.
    # Option 3 appears to be correct.
    # Option 4 is out because at tile (i, n-1), that, in my example, corresponds to
    # (2,3), which disregards tiles (2,0), (2,1) and (2,2) which were previously
    # in solved positions according to invariant rules. 
    
    answer = "..." + "\n"
    answer += "assert my_puzzle.lower_row_invariant(i, 0)" + "\n"
    answer += "my_puzzle.solve_col0_tile(i)" + "\n"
    answer += "assert my_puzzle.lower_row_invariant(i - 1, n -1)" + "\n"
    answer += "..."

    print "Question 407 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_407()
    
##===========================================================

def hw_408():
    """
    QUESTION 8: Implementing solve_interior_tile
    
    We are now ready to formulate the basic algm for solve_interior_tile(i, j).
    Given a target position (i, j), we start by finding the current position of
    the tile that should appear at this position to a solved puzzle. We refer to this
    tile as the target tile.
    
    While moving the target tile to the target position, we can leverage the fact
    that lower_row_invariant(i, j) is true prior to execution of 
    solve_interior_tile(i, j). First, we know that the zero tile is positioned at (i, j).
    Also, the target tile's current position (k, l) must be either above the target
    position (k < i) or on the same row to the left (i = k and l < j). 
    
    Our solution strategy will be to move the zero tile up and across to the target
    tile. Then we will move the target tile back to the target position by applying
    a series of cyclic moves to the zero tile that move the target tile back to the
    target position one position at a time. Our implementation of this strategy
    will have 3 cases depending on the relative horizontal positions of the zero
    tile and the target tile. 
    
    The 3 images below (text here) show an example in which the target tile
    (with number 13) is directly above the target position. The left image shows
    the config at the start of solve_interior_tile(3,1), the middle shows the config
    after the zero tile has been moved to the target tile's current position using
    the move string "uuu", and the right shows the config after the target tile
    has been moved down one position towards the target position using the 
    string "lddru". 
    Left                  Middle                Right
    4 13   1   3       4   0   1   3        5   4   1   3
    5 10   2   7       5 13   2   7        8   0   2   7
    8 12   6 11       8 10   6 11      10 13   6 11
    9   0 14 15       9 12 14 15        9 12 14 15
    
    Problem: Starting from the config on the right, which move string complete
    the solution process for this position and updates the puzzle to a config where
    lower_row_invariant(3, 0) is true?
    
    Option 1
    "lddru"
    
    Option 2
    "rddlu"
    
    Option 3
    "lddrulddru"
    
    Option 4
    "lddruld"
    """
    # I initialized a Puzzle instance with the config shown on the right. I will enter 
    # each option to find the correct answer. Since I am looking for a config where
    # LRI(3,0) is true, I want to see some permutation of the following (where
    # X in the grid below correspond to any other value not shown).
    
    EXPECTED = """
      X   X   X   X
      X   X   X   X
      X   X   X   X
    12 13 14 15
    """
    
    # Option 1 appears to be correct, as row 4 = [12, 13, 14, 15]. The other options
    # were verified to be incorrect. In option 1, the zero appeared to move in a
    # counter-clockwise path around the target tile in order to move it into the
    # target position. That the 12 was also moved into its solved position seemed
    # to be a coincidence, but I may find out otherwise further into this assignment.
    # Note that the "lddru" move string is the same used to move the 13 from position
    # (1, 1) to (2, 1). Using it to move 13 from (2, 1) to (3, 1) makes sense.
    
    # Call to GUI commented out after answer found.
    #FifteenGUI(Puzzle(4,4, [[5, 4, 1, 3], [8, 0, 2, 7], [10, 13, 6, 11], [9, 12, 14, 15]]))    
    
    ##################################################
    ## INCORRECT: No. This move string positions the target tile at the target
    ## position, but does not position the zero to the left of the target position.
    ##
    ## answer = "lddru"
    ##################################################
    
    # Having the entire last row in solved position is a situation where LRI(2,3) is
    # true, not where LRI(3,0) is true. In the later case, the 12 would not be in
    # its solved position, zero would be at (3,0). The correct answer was option 4.
        
    answer = "lddruld"

    print "Question 408 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_408()
    
##===========================================================

def hw_409():
    """
    QUESTION 9: Solving a 3 x 2 puzzle
    
    Our solution strategy for solve_interior_tile fails for positions in the leftmost
    column of the puzzle since we lack a free column on the left of the target
    position. For the leftmost column, the method solve_col0_tile will use a solution
    process that is similar to that of a 3x2 puzzle. 
    
    As a motivating example, imagine that we have used SIT(2,1) to position the
    five tile correctly. The example below shows a typical config that satisfies LRI(2,0):
    2 4
    3 1
    0 5
    
    The problem here is that, unless the four tile happens to be above the zero tile,
    there is no way to swap the four tile into its correct position without temporarily
    moving the five tile. In this case, the solution is to move the zero tile up and to
    the right and then reposition the four tile above the five tile with the zero tile to
    its left. The move string for this update can be generated in a manner similar
    to the process used in SIT. The config on the left below shows the result of
    this process:
    1 2      1 3
    0 4      2 0
    3 5      4 5
    
    From this left config we can apply a fixed move string that generates the config
    shown on the right in which the four and five tiles are at their desired locations
    while leaving the zero tile above the five tile.
    
    Problem: Which move string below updates the puzzle from the left config to
    the right config above?
    
    Option 1
    "ruldrdlurdluurddlur"
    
    Option 2
    "r"
    
    Option 3
    "druldruldru"
    
    Option 4
    "rdlurdlu"
    """
    # Like for the previous question, I will simply generate a puzzle with a grid
    # just like the config on the left and enter the four options to find the 
    # correct answer. 
    
    # Call to GUI commented out after answer found.
    #FifteenGUI(Puzzle(3,2,[[1,2], [0,4], [3,5]]))
    
    # Option 1 appears to be correct as row 3 = [4,5]. Options 3 and 4 were verified
    # to be incorrect (option 2 is obviously incorrect). They made simple CCW and
    # CW movements, respectively, in little 2x2 circles at the bottom of the grid.
    # Option 1 repositioned the 4 and 5 so that they were located in the first col
    # with 4 above 5, then 5 was lowered into position (2,0) with 4 at (1,0), then
    # 5 was moved back into its solved position and one move up dropped the 4
    # into the target position.
    
    answer = "ruldrdlurdluurddlur"

    print "Question 409 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_409()

##===========================================================

def hw_410():
    """
    QUESTION 10: Solving a 2 x 3 puzzle
    
    In phase two, we solve the top two rows of the puzzle, one column at a time
    from right to left. The basic strategy here is similar to that of solving a 3x2
    puzzle. In the config below, we have already positioned the 5 tile correctly,
    with the zero tile positioned above it.
    3 1 0
    2 4 5
    
    To solve the right column of the puzzle, we must correctly position the 2 tile
    next. The issue here is that, unless the 2 tile ends up to the left of the zero
    tile, there is no way to swap the 2 tile into its correct position without
    temporarily moving the five tile. 
    
    In this case, the solution is to move the zero tile over and down and then use
    a variant of SIT to position the 2 tile at (1,1) with the zero tile at (1,0). 
    3 4 1     4 3 2
    0 2 5     1 0 5
    
    From this left config, we can apply a fixed move string that generates the
    config shown on the right. In this config, the 2 and 5 tiles are in their
    desired positions with the zero tile positioned to the left of the 5 tile, 
    ready for the next step in the solution process.
    
    Problem: Which move string updates the left config into the right config?
    
    Option 1
    "urdlurrdluldrruld"
    
    Option 2
    "r"
    
    Option 3
    "urrdl"
    
    Option 4
    "urrd"
    """
    # Once again, I will modify the FifteenGUI call to instantiate a grid
    # configuration like the one on the left in the problem, then I will enter
    # each of the strings into the GUI to find the correct answer.
    
    # Option 1 was correct, again, and option 2 is obviously not, again.
    # Options 3 and 4 were verified to be incorrect as well.
    # Like in the 3x2 problem, the move string positioned the two adjacent
    # tiles, here the 2 and 5, next to each other, with the 2 to the left of the
    # 5. As the 5 was dropped into its rightful position at (1,2), the next move
    # to the left positioned 2 into the target position (0,2). 
    
    # Call to GUI commented out after answer found.
    #FifteenGUI(Puzzle(2,3,[[3, 4, 1], [0, 2, 5]]))
    
    answer = "urdlurrdluldrruld"

    print "Question 410 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_410()
    
##===========================================================
##===========================================================