"""
Rice University / Coursera: Principles of Computing (Part 2)
Week 4: Project 4
Fifteen Puzzle
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# All import statements needed.

import simplegui

# Below is the link to the description of this assignment.

COURSE = "https://class.coursera.org/principlescomputing2-004/"
DESCRIPTION = COURSE + "wiki/view?page=fifteen_puzzle"

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
    
    #--------------------------------------------------
    # Helper to reposition tile for SIT and SC0T and return a move string
    def compute_tile_moves(self, curr_row, curr_col, target_row, target_col):
        """
        Moves the tile at curr_row, curr_col to the position target_row,
        target_col, then moves the zero tile to target_row, target_col - 1.
        """
        # Initialize test grid and moves variable.
        moves = ""
        
        # Standardized move addition from target_pos to curr_pos.
        # Note that up no up moves added if target row == current row.
        for dummy_move in range(target_row - curr_row):
            moves += "u"
        for dummy_move in range(target_col - curr_col):
            moves += "l"
        for dummy_move in range(curr_col - target_col):
            moves += "r"

        # Cycle target down into position, then move zero.
        if curr_col == target_col:
            for dummy_move in range(target_row - curr_row - 1):
                moves += "lddru"
                
            moves += "ld"
        # Move target right into target col then down, zero is in position at end.  
        elif curr_col < target_col:
            for dummy_move in range(target_col - curr_col - 1):
                moves += "drrul" if curr_row == 0 else "urrdl"

            for dummy_move in range(target_row - curr_row):
                moves += "druld"
        # Move target left into target col then down, zero is in position at end.
        elif curr_col > target_col:
            for dummy_move in range(curr_col - target_col - 1):
                moves += "dllur" if curr_row == 0 else "ulldr"

            moves += "dllu" if curr_row == 0 else "ulld"

            for dummy_move in range(target_row - curr_row):
                moves += "druld"

        return moves
    #--------------------------------------------------
    
    #--------------------------------------------------
    # Helper to remove useless moves in final move string.
    def remove_useless_moves(self, move_string):
        """
        Search a move string and remove all useless moves du, ud, lr, rl.
        """
        moves = "".join(move for move in move_string)
        bad_moves = ["ud", "du", "lr", "rl"]
        bad_moves_in_string = [move for move in bad_moves if move in moves]
        
        while len(bad_moves_in_string) > 0:
            for move in bad_moves:
                moves = moves.replace(move, "")
            bad_moves_in_string = [move for move in bad_moves if move in moves]
            
        return moves
    #--------------------------------------------------

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
        # Check for tile zero at (target_row, target_col)
        if self._grid[target_row][target_col] != 0:
            return False
        # Check that all tiles in target_row to the right of target_col are solved.
        for col in range(target_col + 1, self._width):
            if (target_row, col) != self.current_position(target_row, col):
                return False
        # Check that all tiles in rows target_row + 1 are solved.
        for row in range(target_row + 1, self._height):
            for col in range(self._width):
                if (row, col) != self.current_position(row, col):
                    return False
                    
        return True

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # Check lower row invariant and zero tile pos.
        assert self.lower_row_invariant(target_row, target_col), \
                "lower row invariant failed (pre SIT)"
        assert self._grid[target_row][target_col] == 0, \
                "zero tile not at target position"
        
        # Find current position of target tile and compute tile moves.
        curr_row, curr_col = self.current_position(target_row, target_col)
        moves = self.compute_tile_moves(curr_row, curr_col, target_row, target_col)
        
        # Update the grid with the computed moves and return the moves as a string.
        self.update_puzzle(moves)
        assert self.lower_row_invariant(target_row, target_col - 1), \
                "lower row invariant failed (post SIT)"
        return moves
        
    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # Check lower row invariant and zero tile pos.
        assert self.lower_row_invariant(target_row, 0), \
                "lower row invariant failed (pre SC0T)"
        assert self._grid[target_row][0] == 0, \
                "zero tile not at target position"
                
        curr_row, curr_col = self.current_position(target_row, 0)
        # Check if target tile is above the zero tile.
        if (curr_row, curr_col) == (target_row - 1, 0):
            moves = "u"
            
            for dummy_move in range(self._width - 1):
                moves += "r"
                
            self.update_puzzle(moves)
            assert self.lower_row_invariant(target_row - 1, self._width - 1), \
                    "lower row invariant failed (post SC0T)"
                    
            return moves
        
        # If the target tile is not above the zero tile, move the zero tile into
        # the new target position above the position target_row, target_col + 1.
        moves = "ur"
        self.update_puzzle("ur")
        curr_row, curr_col = self.current_position(target_row, 0)
        moves += self.compute_tile_moves(curr_row, curr_col, target_row - 1, 1)
        moves += "ruldrdlurdluurddlu"
        
        for dummy_move in range(self._width - 1):
            moves += "r"
        
        self.update_puzzle(moves[2:])
        assert self.lower_row_invariant(target_row - 1, self._width - 1), \
                "lower row invariant failed (post SC0T)"
                
        return moves

    ## Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # Check for tile zero at 1, target_col.
        if self._grid[0][target_col] != 0:
            return False
        # Check that all tiles in row 1 from target_col to the right are solved.
        for col in range(target_col, self._width):
            if (1, col) != self.current_position(1, col):
                return False
        # Check that all tiles in rows 2 to m are solved.
        for row in range(2, self._height):
            for col in range(self._width):
                if (row, col) != self.current_position(row, col):
                    return False
        # Check that all tiles in row 0 to the right of target_col are solved.
        for col in range(target_col + 1, self._width):
            if (0, col) != self.current_position(0, col):
                return False
                    
        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # Check for tile zero at 1, target_col.
        if self._grid[1][target_col] != 0:
            return False
        # Check that all tiles in row 1 to the right of target_col are solved.
        for col in range(target_col + 1, self._width):
            if (1, col) != self.current_position(1, col):
                return False
        # Check that all tiles in rows 2 to m are solved.
        for row in range(2, self._height):
            for col in range(self._width):
                if (row, col) != self.current_position(row, col):
                    return False
        # Check that all tiles in row 0 to the right of target_col are solved.
        for col in range(target_col + 1, self._width):
            if (0, col) != self.current_position(0, col):
                return False
                    
        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # Check row0 invariant and zero tile pos.
        assert self.row0_invariant(target_col), "row0 invariant failed (pre SR0T)"
        assert self._grid[0][target_col] == 0, "zero tile not at target position"
        
        # Check if target is at pos (0,j), move tiles accordingly.
        moves = "ld"
        self.update_puzzle("ld")
        curr_row, curr_col = self.current_position(0, target_col)
        if (curr_row, curr_col) != (0, target_col):
            moves += self.compute_tile_moves(curr_row, curr_col, 1, target_col - 1)
            moves += "urdlurrdluldrruld"
        
        # Update the grid with the computed moves and return the move string.
        self.update_puzzle(moves[2:])
        assert self.row1_invariant(target_col - 1), "row1 invariant failed (post SR0T)"
        return moves

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # Check row1 invariant and zero tile pos.
        assert self.row1_invariant(target_col), "row1 invariant failed (pre SR1T)"
        assert self._grid[1][target_col] == 0, "zero tile not at target position"
        
        # Find current pos of target tile and compute tile moves.
        curr_row, curr_col = self.current_position(1, target_col)
        moves = self.compute_tile_moves(curr_row, curr_col, 1, target_col)
        moves += "ur"
        
        # Update the grid with the computed moves and return the move string.
        self.update_puzzle(moves)
        assert self.row0_invariant(target_col), "row0 invariant failed (post SR1T)"
        return moves

    ## Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # Check row1 invariant and zero tile pos.
        assert self.row1_invariant(1), "row1 invariant failed (pre S22)"
        assert self._grid[1][1] == 0, "zero tile not at target position"
        
        # Move zero tile and check for 3 position.
        moves = "ul"
        self.update_puzzle("ul")
        if self._grid[0][1]  == 1:
            self.update_puzzle(moves[2:])
            return moves
        moves += "drul" if self._grid[1][0] == 1 else "rdlu"
        self.update_puzzle(moves[2:])
        return moves

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # Initialize solved status, target, and empty move string.
        moves = ""
        target_pos = (self._height - 1, self._width - 1)
        
        # Move the zero tile to position (m-1, n-1).
        zero_row, zero_col = self.current_position(0, 0)
        for dummy_move in range(zero_row, self._height - 1):
            moves += "d"
        for dummy_move in range(zero_col, self._width - 1):
            moves += "r"
            
        # Update puzzle with initial move string, as solution methods below will
        # update the puzzle on their own.
        self.update_puzzle(moves)
            
        # Solve for each row until target pos is (1, n-1).
        while target_pos != (1, self._width - 1):
            if target_pos[1] != 0:
                moves += self.solve_interior_tile(target_pos[0], target_pos[1])
                target_pos = (target_pos[0], target_pos[1] - 1)
            else:
                moves += self.solve_col0_tile(target_pos[0])
                target_pos = (target_pos[0] - 1, self._width - 1)
                
        # Solve for rightmost n-2 cols of remaining two rows.
        while target_pos != (1, 1):
            if target_pos[0] == 1:
                moves += self.solve_row1_tile(target_pos[1])
                target_pos = (target_pos[0] - 1, target_pos[1])
            else:
                moves += self.solve_row0_tile(target_pos[1])
                target_pos = (target_pos[0] + 1, target_pos[1] - 1)
        
        # Solve for remaining 2x2 grid.
        moves += self.solve_2x2()
        
        ## Remove useless successions.
        moves = self.remove_useless_moves(moves)
        
        return moves

##=================================================================

DIRECTIONS = '''
Overview
----------
This week's homework introduced you to the Fifteen puzzle and outlined the highlights
of building a solver for the puzzle. As described in the homework, the solution 
process for a puzzle of size m × n has three phases:

1.) Solve the bottom m−2 rows of the puzzle in a row by row manner from bottom to top. 
        Each individual row will be solved in a right to left order.
2.) Solve the rightmost n−2 columns of the top two rows of the puzzle (in a right to 
        left order). Each column consists of two unsolved positions and will be solved
        in a bottom to top order.
3.) Solve the upper left 2×2 portion of the puzzle directly.

As noted in the homework, we have provided a program template that includes a 
partially implemented Puzzle class that allows you to interact with a GUI designed to 
simulate the Fifteen puzzle. Your task for this mini-project is to write a collection 
of Puzzle methods that implement each phase of the solution process. Several of 
these methods will correspond to invariants designed to help guide you towards a 
correct implementation of the solver. The remaining methods are solution methods 
for portions of the puzzle. Note that each of these solution methods updates the 
puzzle and returns the move string associated with this update.

Testing Your Mini-Project
----------
The provided template includes stubs for the methods that you will need to implement 
for this mini-project. You should write tests for the Puzzle methods as you implement 
them. (Note that the initializer for a Puzzle object accepts an optional initial 
configuration for the puzzle that is specified as a 2D list of integers.) This 
mini-project is difficult. If you attempt to implement all of the methods before 
doing any testing, the mini-project will be impossible. Please take our advice and 
test as you go.

After you complete each Puzzle method, submit your code to the Owltest page
(http://codeskulptor.appspot.com/owltest?urlTests=poc.poc_fifteen_tests.py
&urlPylintConfig=poc.pylint_config.py&imports=%7Bpoc:(poc_fifteen_gui)%7D)
to confirm that your implementation of the method is correct. Follow the coding
guidelines for this class. Submit your code to the CourseraTest page for this
mini-project when your code is ready to submit.

Important Note: The tests in OwlTest are a different for this project in two ways. 
First, if you fail a test, you will not be given the correct answer. Instead, you 
will be given an input for which your answer was incorrect, and you will need to 
determine what is wrong. Second, the tests for the first two phases are not as 
comprehensive as normal. This is intentional. You need to run some of your own 
tests to convince yourself that you have things working correctly. If you do not, 
you will fail some of the phase three tests because of broken functions from the 
previous phases. These modifications are meant to get you thinking more about 
testing and correctness.

Phase One
----------
In this phase, your task is to implement three methods: one invariant method 
and two solution methods. The invariant method for this phase (as described in 
the problem #6 of the homework) is lower_row_invariant(i, j). This method should 
return True if the following three conditions are all true:
* Tile zero is positioned at (i,j).
* All tiles in rows i+1 or below are positioned at their solved location.
* All tiles in row i to the right of position (i,j) are positioned at their solved 
    location.
    
The image below (shown in text) shows a 4×4 puzzle for which lower_row_invariant(2, 2) 
is true with tile zero in position (2,2) and the blue tiles (not shown) in solved 
positions.
  4   2   3   7
  8   5   6 10
  9   1   0 11
12 13 14 15

We again remind you that you should implement and fully test LRI before proceeding.
In particular, we suggest that you test this method using OwlTest to confirm that your
implementation of this method is correct before proceeding. Next, you will implement
the two solution methods for this phase: solve_interior_tile (SIT) and solve_col0_tile
(SC0T).

The method SIT(i,j) is designed to solve the puzzle at position (i,j) where i > 1
and j > 0. Specifically, this method takes a puzzle for which LRI(i,j) is true and
repositions the tiles in the puzzle such that LRI(i, j-1) is true. To implement
SIT, we suggest that you review problem 8 from homework 4.

The second solution method SC0T(i) is designed to solve the problem at position 
(i,0) where i > 1. Specifically, this method takes a puzzle that satisfies the invariant
LRI(i,0) and repositions the tiles in the puzzle such that LRI(i-1, n-1) is true
when n is the width of the grid. Implementing SC0T is trickier than SIT since the
solution strategy for SIT(i,j) involved moving tile zero through column j-1. In the
case of the left column where j = 0, this solution process is not feasible.

Our recommended strategy for SC0T is to move the zero tile from (i,0) to (i-1,1) 
using the move string "ur". If you are lucky and the target tile (i.e. the tile being
solved for) is now at position (i,0), you can simply move tile zero to the end of row
i-1 and be done. However, if the target tile is not positioned at (i,0), we suggest 
following the solution strategy below:
* Reposition the target tile to position (i-1, 1) and the zero tile to position
    (i-1, 0) using a process similar to that of SIT.
* Then apply the move string for a 3x2 puzzle as described in problem #9 of
    homework 4 to bring the target tile into position (i,0).
* Finally, conclude by moving tile zero to the right end of row i-1.

Note the process for the first step is so similar to that of SIT that you may wish
to refactor your implementation to include a helper method position_tile that
is used by both tasks.

Note that the invariant method LRI can be extremely valuable as you test and
debug SIT and SC0T. Minimally, we recommend that you add assert statements
to your solution methods that verify that these methods are receiving a puzzle
in a proper input config and producing a puzzle with the proper output config.
Once you are confident that these methods are correct, use OwlTest to confirm.

Phase Two
----------
In phase two, you will solve the rightmost n - 2 cols of the remaining two rows,
one col at a time from right to left. Your task is to implement four methods: two
invariant methods and two solution methods. We recommend that you implement the
two invariant methods row1_invariant(j) and row0_invariant(j) first. These invariants
check whether the solution process has proceeded correctly to positoins (1,j) and
(0,j), respectively.

The invariant row1_invariant(j) should check whether tile zero is at (1, j) and whether
all positions either below or to the right of this position are solved. The invariant
row0_invariant(j) checks a similar condition, but additionally checks whether position
(1,j) is also solved. The images below show a pair of puzzles for which row1_invariant(2)
and row0_invariant(2) are true:

  4   6   1   3            4   2   0   3
  5   2   0   7            5   1   6   7
  8   9 10 11            8   9 10 11
12 13 14 15          12 13 14 15

Once these two invariant methods are implemented correctly, you should implement
corresponding solution methods solve_row1_tile(j) and solve_row0_tile(j). These
methods should solve for the tiles positioned at (1,j) and (0,j), respectively. These
solution methods are related to the invariant methods in a manner similar to that of
problem 7 on homework 4. In particular, the annotated execution trace for the solver
should have the form:
...
assert my_puzzle.row1_invariant(j)
my_puzzle.solve_row1_tile(j)
assert my_puzzle.row0_invariant(j)
my_puzzle.solve_row0_tile(j)
assert my_puzzle.row1_invariant(j-1)
...
where my_puzzle is the name of the puzzle being solved.

Implementing solve_row1_tile(j) should be straightforward using a method similar to 
that of solve_interior_tile (or using your helper method position_tile). To implement 
solve_row0_tile(j), we suggest that you use a method similar to that for 
solve_col0_tile. In particular, you should move the zero tile from position (0,j) to 
(1,j−1) using the move string "ld" and check whether target tile is at position (0,j). 
If not, reposition the target tile to position (1,j−1) with tile zero in position 
(1,j−2). At this point, you can apply the move string from problem #10 in the homework 
to complete the method.

Again, we recommend that you add assert statements to your solution methods that 
verify that the methods are receiving a puzzle in a proper input configuration and 
producing a puzzle with the proper output configuration. Once you are confident that 
these methods are correct, use OwlTest to confirm that they are correct.

Phase Three
----------
You are now ready to implement phase three and complete the mini-project. 
For this final phase, your task is to implement two solution methods: solve_2x2() 
and solve_puzzle(). The method solve_2x2() solves the final upper left 2×2 portion 
of the puzzle under the assumption that the remainder of the puzzle is solved 
(i.e, row1_invariant(1) is true). We recommend that you consult problems #3-5 in 
the homework for a suggested method.

When building test cases for your solver, note that not all puzzles generated by 
random placement of the tiles can be solved. For larger puzzles, everything but the 
upper left 2×2 portion of the puzzle can always be solved. To test this 2×2 portion 
of the solver, we recommend that you build your tests by applying a sequence of 
random moves to an unscrambled puzzle.

The final method solve_puzzle() takes a solvable Puzzle object and solves the puzzle. 
This method should call the various solution methods that you have implemented and 
join the move string returned by these methods to form a single move string that 
solves the entire puzzle. Observe the invariants associated with these solution 
methods link together to guarantee that each solution method receives the puzzle 
in the configuration necessary for the solution process. (Note that on the transition 
from phase one to phase two, the invariants lower_row_invariant(1, n - 1) and 
row1_invariant(n - 1) are identical.)

solve_puzzle should update the puzzle and return a solution string. Once you have 
implemented this method, clicking the "Solve" button in the GUI will call your solver 
to solve the puzzle.
'''

##=================================================================

# Phase One

# I will begin, as usual, by including all code from the template and GUI here. 
# The final version submitted to OwlTest will be of the Puzzle class implemented
# here. The use of the imported poc_fifteen_gui in the template is only at the end
# when the GUI is called, which is not required for the OwlTest submission.
# Changes will be made incrementally to the Puzzle class and test functions that
# call specific Puzzle configs and test components will be developed for each change.

# First, implement LRI(i,j). It checks for 3 conditions, described above. The method
# current_position(self, solved_row, solved_col) appears to be useful here such that
# if the method is called on a solved tile, the (row, col) returned by it should be equal
# to (solved_row, solved_col). For any (i,j), it returns the position of the tile that
# SHOULD BE at position (i,j) when the puzzle is solved. If the tile is in its solved
# position before the call, then returned indices will be the same as the input.

# Initial LRI attempt will be to traverse the grid starting with tile at (i, j+1)
# and moving left to right, top to bottom verifying with current_position
# that the tiles in those positions match those that should be there when
# the puzzle is solved. Beware that the first column traversed will vary in length.

## LRI_0
def lower_row_invariant(self, target_row, target_col):
    """
    Check whether the puzzle satisfies the specified invariant
    at the given position in the bottom rows of the puzzle (target_row > 1)
    Returns a boolean
    """
    # Check for tile zero at target row and col.
    if self._grid[target_row][target_col] != 0:
        return False
    # Check that all tiles in target_row to the right of target_col are solved.
    for col in range(target_col + 1, self._width):
        if (target_row, col) != self.current_position(target_row, col):
            return False
    # Check that all tiles in rows target_row + 1 are solved.
    for row in range(target_row + 1, self._height):
        for col in range(self._width):
            if (row, col) != self.current_position(row, col):
                return False
                
    return True

# OwlTest returned no errors for LRI_0!

# Second, implement SIT(i,j). It is designed to solve the puzzle at (i,j) where
# LRI(i,j) is true and reposition the tiles such that LRI(i, j-1) is true. It is
# suggested that we review question 8 from homework 4. In question 8, we were
# shown the boards (including the solution board):
#   Left                  Middle                Right                Solution
#   4 13   1   3       4   0   1   3        5   4   1   3       5   4   1   3
#   5 10   2   7       5 13   2   7        8   0   2   7     10   8   2   7
#   8 12   6 11       8 10   6 11      10 13   6 11     12   9   6 11
#   9   0 14 15       9 12 14 15        9 12 14 15       0 13 14 15

# The left grid is the starting config at SIT(3,1). The middle is the config after
# the zero moved to the target tile's current position (using "uuu"). The right
# is the config after the target tile was moved down one position towards the
# target position (using "lddru"). The solution is the config after "lddruld" to 
# move the target tile into the target position and move the zero to the left of it.

# Assuming the left to middle move was important, I assume that its beneficial to
# move the zero to the target tile's current position to begin. Then there are a 
# series of CCW movements around the target tile to move it into position. If the
# 13 was above the 15 (in place of the 11 in this example), then from the left config,
# a movement of "urr", "ulldr" would position the 13 two the left and over top of
# its target position, ending with the zero at where the 6 is in the example. One
# last move of "ullddru" would place the 13 into position. The zero would have to
# then move to the left of this position with "ld". 

# The docstring in the placeholder SIT method states that the correct tile is
# placed at the target position and that the puzzle is updated, and a string is
# returned. The update_puzzle(self, move_string) method takes a move string,
# initializes two variables zero_row and zero_col that correspond to the position
# of the zero tile, and then iterates through the move string, first checking that
# the moves do not take the tile off the grid, then swapping the value 0 with
# whatever is currently in the tile in which the zero will be moved, effectively
# changing the self._grid field.

# The SIT method must compute the necessary moves, update the grid using the
# move string, and then return the move string used to update the grid. First, the
# LRI must be asserted at the target_row and target_col. Second, it must find the
# moves. Third, it must update the grid. Fourth, it must return the move string. 
# As recommended in the directions for Phase One, I will implement a helper function
# compute_tile_moves to be used by SIT and SC0T. It will take a current position 
# (where the target tile is) and a target position (where it's to be moved so that it is
# in the solved position) to compute the necessary moves and return a move string.

# Using the example above, the 13 tile could be in four relative positions to the 
# zero: directly above it, to the left of it in the same row, to the left above it, 
# or to the right above it.

# The example above meets this first case, with 13 directly above 0. The moves
# taken to reposition the zero, from the left config to the solution config, were:
# "uuu", "lddru", "lddruld". In the third move string, "ld" was used to move the
# zero into the next target position after the 13 was in its solved position. The
# behavior follows the model: move "u" until you hit the current target tile pos,
# then "lddru" until the target tile is in the targte pos. Then "ld" to position zero.
# This is a CCW circle around the target tile.

# If the 13 were to the left of zero, it would move "l" until it hit the target tile's
# current position, then follow the sequence "urrdl" to move the target over
# to the right once more, and repeat that until the target is in its solved position.
# There would be no final "l" move to move zero, as it would be in the right place.

# If the 13 were above and to the left, the zero has a few options. First, it could
# make an L-shaped move to reach the curr_pos, then circle around it CW to drop
# it into the row, then circle CW in small 2x2 squares to move the target to the right.
# Or, it could make an inverted L-shaped move straight up and to the left to hit
# curr_pos, then make CCW moves to move it to the right until its directly above
# the target_pos, then make CCW circles to move it down, just as it would if the
# target tile were initially directly above the zero before running STI.

# If the 13 were above and to the right, the zero does not have two moves like
# in the case of the target being above and to the left. That backwards L-shape is
# illegal, as it would reposition the tiles to the right of target_pos, thereby causing
# the invariant LRI to fail. It could also not drop the 13 into the target_row wherever
# for the same reason. Instead, it would have to move straight up until it hit the
# curr_row, move to the right into curr_pos, and then pull the 13 into the overhead
# position. Note that CW circles would be used to do this (whereas CCW were used
# if the target were above and to the left).

# In all cases except for where target tile is to the left of zero, it seems that
# the easiest way to standardize the moves is to drag the target tile into target_col
# with either CCW or CW circles for above-left and above-right, respectively, and
# then use CCW circles to drop it down into target_pos. 

## Helper to reposition tile for SIT and SC0T and return a move string
def compute_tile_moves(self, curr_row, curr_col, target_row, target_col):
    """
    Moves the tile at curr_row, curr_col to the position target_row,
    target_col, then moves the zero tile to target_row, target_col - 1.
    """
    # Initialize test grid and moves variable.
    moves = ""
    
    # Standardized move addition from target_pos to curr_pos.
    # Note that up no up moves added if target row == current row.
    for dummy_move in range(target_row - curr_row):
        moves += "u"
    for dummy_move in range(target_col - curr_col):
        moves += "l"
    for dummy_move in range(curr_col - target_col):
        moves += "r"
    
    ## Many if then statements commented out and replaced with conditional
    ## expressions ("ternary operator") to avoid OwlTest too-many-branches warning.
    # Cycle target down into position, then move zero.
    if curr_col == target_col:
        for dummy_move in range(target_row - curr_row - 1):
            moves += "lddru"
            
        moves += "ld"
    # Move target right into target col then down, zero is in position at end.  
    elif curr_col < target_col:
        for dummy_move in range(target_col - curr_col - 1):
            moves += "drrul" if curr_row == 0 else "urrdl"
            # if curr_row == 0:
                # moves += "drrul"
            # else:
                # moves += "urrdl"
        for dummy_move in range(target_row - curr_row):
            moves += "druld"
    # Move target left into target col then down, zero is in position at end.
    elif curr_col > target_col:
        for dummy_move in range(curr_col - target_col - 1):
            moves += "dllur" if curr_row == 0 else "ulldr"
            # if curr_row == 0:
                # moves += "dllur"
            # else:
                # moves += "ulldr"
        moves += "dllu" if curr_row == 0 else "ulld"
        # if curr_row == 0:
            # moves += "dllu"
        # else:
            # moves += "ulld"
        for dummy_move in range(target_row - curr_row):
            moves += "druld"

    return moves

# Now I can implement the SIT method.

## SIT_0
def solve_interior_tile(self, target_row, target_col):
    """
    Place correct tile at target position
    Updates puzzle and returns a move string
    """
    # Check lower row invariant and zero tile pos.
    assert self.lower_row_invariant(target_row, target_col), \
            "lower row invariant failed (pre SIT)"
    assert self._grid[target_row][target_col] == 0, \
            "zero tile not at target position"
    
    # Find current position of target tile and compute tile moves.
    curr_row, curr_col = self.current_position(target_row, target_col)
    moves = self.compute_tile_moves(curr_row, curr_col, target_row, target_col)
    
    # Update the grid with the computed moves and return the moves as a string.
    self.update_puzzle(moves)
    assert self.lower_row_invariant(target_row, target_col - 1), \
            "lower row invariant failed (post SIT)"
    return moves

# OwlTest returned errors for SIT_0. Some of the curr_col variable names were 
# swapped with curr_row, but the rest of the logic was correct.

# Third, implement SC0T(i). Before executing SC0T, the invariant LRI(i, 0) is true,
# and after, LRI(i-1, n-1) is true where n = grid width. The recommended strategy 
# is to first move the zero tile "ur" and check if the target tile is in its solved
# pos. If so, you can move tile zero to the end of row i-1. If the target is NOT at
# (i,0), then: reposition the target tile to position (i-1, 1) and the zero tile to pos
# (i-1, 0) using a process similar to that of SIT. Then apply the move string for a
# 3x2 puzzle as described in homework 4 problem 9 to bring the target tile into
# pos (i,0). Finally, conclude by moving tile zero to the right end of row i-1.

# In the homework, the following moves were used to move 4 into the target pos:
# 2 4   reposition 4     1 2    then to finally move the 4       1 3
# 3 1   above 5 tile     0 4     into position (5 moves too)   2 0
# 0 5   with "uruld"     3 5     use "ruldrdlurdluurddlur"         4 5
# The first move places 4 above 5, or places target tile at (i-1, j+1). Then the
# move string does the following: "ruld" (CCW circle) moves 4 into (i-2, j); "rdlu"
# (CW circle) moves 5 up one row; "rdlu" moves 5 to the left in line with 4, and then
# down into pos (i,j); "u" moves 4 down on top of 5; "rddlu" moves 4 and 5 into
# solved positions; "r" moves the 0 into the next target (one "r" since zero only
# has to move one col over to get there). 

# The instructions for SC0T note that the first step is similar to that of SIT,
# and that we may wish to use the helper function compute_tile_moves to
# complete the first part of SC0T. The difference appears to be that the target pos
# passed to CTM in this case is (target_pos - 1, 1)--target_col not passed--the upper
# right diagonal spot from (i,j). Once those moves are computed, it is a matter of
# appending the move string "ruldrdlurdluurddlu", followed by the number of "r"
# moves to get 0 into the next target pos at (target_pos - 1, self._width -1).
# As the 0 will be at position (target_pos - 1, 0), the number of moves to the
# right is self._width - 1.

# A check for an up move solving for the target tile must be placed at the beginning
# of SC0T (as was recommended in the instructions) since the helper function would
# not recognize that it's solved and also would attempt to append a left move onto
# the move string (where i < 0). 

## SC0T_0
def solve_col0_tile(self, target_row):
    """
    Solve tile in column zero on specified row (> 1)
    Updates puzzle and returns a move string
    """
    # Check lower row invariant and zero tile pos.
    assert self.lower_row_invariant(target_row, 0), \
            "lower row invariant failed (pre SC0T)"
    assert self._grid[target_row][0] == 0, \
            "zero tile not at target position"
            
    curr_row, curr_col = self.current_position(target_row, 0)
    
    # Check if target tile is above the zero tile.
    if (curr_row, curr_col) == (target_row - 1, 0):
        moves = "u"
        
        for dummy_move in range(self._width - 1):
            moves += "r"
            
        self.update_puzzle(moves)
        assert self.lower_row_invariant(target_row - 1, self._width - 1), \
                "lower row invariant failed (post SC0T)"
                
        return moves
    
    # If the target tile is not above the zero tile, move the zero tile into
    # the new target position above the position target_row, target_col + 1.
    moves = "ur"
    moves += self.compute_tile_moves(curr_row, curr_col, target_row - 1, 1)
    moves += "ruldrdlurdluurddlu"
    
    for dummy_move in range(self._width - 1):
        moves += "r"
    
    self.update_puzzle(moves)
    assert self.lower_row_invariant(target_row - 1, self._width - 1), \
            "lower row invariant failed (post SC0T)"
            
    return moves

# OwlTest returned no errors for the implementation of SC0T. There are, however, 
# refactoring warnings for the compute_tile_move function, stating that there
# are too many branches (17/12). I will update the CTM helper function so that 
# the simple if then statements are replaced with conditional expressions.

# That worked. OwlTest returned no style errors. Phase One is complete.

##=================================================================

# Phase Two

# In this phase, four methods are implemented: row1_invariant(j) (R1I), row0_invariant(j)
# (R0I), solve_row1_tile(j) (SR1T), and solve_row0_tile(j) (SR0T). Using these four
# methods, the rightmost n - 2 cols will be solved for the remaining two rows, one col
# at a time. 

# R1I(j) should check whether tile zero is at (1,j) and whether all positions either
# below or to the right of this position are solved. R0I(j) checks a similar condition,
# but additionally checks whether position (1,j) is also solved. At first glance, R1I
# seems just like LRI, except that the target_row passed to it is 1. 

## R1I_0
def row1_invariant(self, target_col):
    """
    Check whether the puzzle satisfies the row one invariant
    at the given column (col > 1)
    Returns a boolean
    """
    # Check for tile zero at 1, target_col.
    if self._grid[1][target_col] != 0:
        return False
    # Check that all tiles in row 1 to the right of target_col are solved.
    for col in range(target_col + 1, self._width):
        if (1, col) != self.current_position(1, col):
            return False
    # Check that all tiles in rows 2 to m are solved.
    for row in range(2, self._height):
        for col in range(self._width):
            if (row, col) != self.current_position(row, col):
                return False
                
    return True
    
# OwlTest returned no errors for R1I(j). I will implement R0I in the same way,
# except the for loop that checks all tiles in row 1 will include target_col. In the
# example grid provided for R0I(2), it appears that there is an additional check
# for all tiles to the right of 0, which is positioned at (0,2) above the last target
# that has been solved (6 in that config). Assuming (i,j) is still pos (1,2) where
# 6 is, the check should iterate over row 0 to the right of target_col.

## R0I_0
def row0_invariant(self, target_col):
    """
    Check whether the puzzle satisfies the row zero invariant
    at the given column (col > 1)
    Returns a boolean
    """
    # Check for tile zero at 1, target_col.
    if self._grid[0][target_col] != 0:
        return False
    # Check that all tiles in row 1 from target_col to the right are solved.
    for col in range(target_col, self._width):
        if (1, col) != self.current_position(1, col):
            return False
    # Check that all tiles in rows 2 to m are solved.
    for row in range(2, self._height):
        for col in range(self._width):
            if (row, col) != self.current_position(row, col):
                return False
    # Check that all tiles in row 0 to the right of target_col are solved.
    for col in range(target_col + 1, self._width):
        if (0, col) != self.current_position(0, col):
            return False
                
    return True

# OwlTest returned an error for the tile zero check, which looked at
# self._grid[1][target_col] instead of at row 0--a cut and paste error. After
# the change, R0I now throws no errors with the test.

# Now that the invariants are complete, I will implement the solution methods
# starting with SR1T(j). The directions recommends using a method similar to that
# of SIT. To understand how the helper method CTM will work, I want to look at
# an example and solve for it.
#   4   6   1   3
#   5   2   0   7
#   8   9 10 11
# 12 13 14 15
# CTM, passed the current pos of 6 and target pos of 0, will first append to the
# move string "ul". 
#   4   0   6   3
#   5   2   1   7
#   8   9 10 11
# 12 13 14 15
# CTM will check for spatial relationship of curr_col and target_col. Since the two
# cols are next to each other, no moves are appended to move string to reposition
# the 6 above the target col as it's there already. Then for every step in range
# target row - current row (1, here), "druld" is appended to the move string. 
# The target tile is moved to its solved pos with zero to its left, shown below.
#   4   1   2   3
#   5   0   6   7
#   8   9 10 11
# 12 13 14 15

# I will implement SR1T(j) similarly to the SIT(i) solution method. The first statement
# will assert the row1 invariant and check the zero tile position being at (1, j).
# The next will execute CTM to find the move string needed. Finally, the row0
# invariant will be asserted and the moves returned. In the example above, the 3 tile
# was positioned above the 7. I'm not sure if this will always occur, or if this
# is a coincidence. This may be a source of error if OwlTest fails my implementation.

## SR1T_0
def solve_row1_tile(self, target_col):
    """
    Solve the tile in row one at the specified column
    Updates puzzle and returns a move string
    """
    # Check row1 invariant and zero tile pos.
    assert self.row1_invariant( target_col), "row1 invariant failed (pre SR1T)"
    assert self._grid[1][target_col] == 0, "zero tile not at target position"
    
    # Find current pos of target tile and compute tile moves.
    curr_row, curr_col = self.current_position(1, target_col)
    moves = self.compute_tile_moves(curr_row, curr_col, 1, target_col)
    
    # Update the grid with the computed moves and return the move string.
    self.update_puzzle(moves)
    assert self.row0_invariant(target_col), "row0 invariant failed (post SR1T)"
    return moves

# SR1T_0 failed. The assertion to row0 invariant threw an error. I add a '+ str(moves)'
# to the text returned upon failure, and the incorrect move string generated by
# SR1T_0 was "uldruld". This move string was expected. I assume that the 0 is, like
# in the example provided for Phase Two, supposed to be placed above the target pos
# before the row0 invariant is asserted. This would require removing the "ld" portion
# at the end of the move string, which requires a change to the move string returned
# by the helper function.

## SR1T_1
def solve_row1_tile(self, target_col):
    """
    Solve the tile in row one at the specified column
    Updates puzzle and returns a move string
    """
    # Check row1 invariant and zero tile pos.
    assert self.row1_invariant(target_col), "row1 invariant failed (pre SR1T)"
    assert self._grid[1][target_col] == 0, "zero tile not at target position"
    
    # Find current pos of target tile and compute tile moves.
    curr_row, curr_col = self.current_position(1, target_col)
    moves = self.compute_tile_moves(curr_row, curr_col, 1, target_col)
    moves += "ur"
    
    # Update the grid with the computed moves and return the move string.
    self.update_puzzle(moves)
    assert self.row0_invariant(target_col), "row0 invariant failed (post SR1T)"
    return moves
    
# OwlTest returned no errors for SR1T_1 after the change was made to append "ur"
# to the move string. I can only assume at this point, before implementation of the
# rest of the methods, that the 3 tile (or whichever is supposed to be at 0, width-1)
# will always be there, and that this zero position is the next target pos instead of
# the pos to the left of the last target pos. 

# Now I will implement SR0T(j). According to the provided annotated execution
# trace for these two solution methods, it should begin with a statement asserting
# the row0 variant at j, then compute the moves and update accordingly, and then
# assert the row1 invariant at j - 1. There is obviously a dependency here between
# these two functions, which might explain why the target pos after SR1T is not
# moved to the pos left of the last target. Maybe this is because in the example,
# that next position to the left of the last target pos is within the 2x2 section.

# To compute the moves in SR0T, the directions recommend using a method similar
# to that for SC0T. In particular, the zero tile should move from (0,j) to (1,j-1)
# using the move string "ld" and check whether the target tile is at pos (0,j). If not,
# the target tile is repositioned to (1, j-1) with tile zero in pos (1,j-2). Then 
# apply the move string from homework 4 question 10 to complete the method.

# From homework 4 question 10, we are given the following config and had to then
# find the move string which solved for target tile 4:
# 3 1 0     Failed check: target    3 4 1       Use move string       4 3 2
# 2 4 5     tile not at pos (0, j)    0 2 5       "urdlurrdluldrruld"      1 0 5
# The move string between the left and middle configs above, to reposition the
# target so that the 0 is in position (1,0) to the left of target at (1,1) appears
# to be "ldl". Since the instructions say to automatically append an "ld" move to
# the move string, the "l" is then what must be returned by the standardized
# move evaluation. If the 2 were at (0,0), the zero tile would have to follow move
# string (after the initial "ld") "lurdl". If 2 were at (0,1), zero would make the
# move "uld". It could also use the CW circle as in the previous case of 2 at
# (0, 0) and make the longer move "lurdlurdl". 

# To standardize this evaluation, first I must check if the CTM helper can be used
# to make this change before appending "urdlurrdluldrruld" to the move string.
# The target pos is (1, j-1), and the zero must be moved to its left, which is
# what CTM does. Here, j = 2. For this config:
# 2 4 1
# 3 0 5
# Running CTM(0, 0, 1, 1) where target_col = 2 (above the 5 is the target pos)
# will append one "u" and one "l" which creates this config:
# 0 2 1
# 3 4 5
# The conditional will execute for curr_col < target_col, and for curr_row == 0, 
# "drrul" will NOT be appended to the move string, but from "druld" will be appended
# once. The config below will result:
# 4 3 1
# 0 2 5
# So, it appears that CTM can be used to reposition the target and zero first.

## SR0T_0
def solve_row0_tile(self, target_col):
    """
    Solve the tile in row zero at the specified column
    Updates puzzle and returns a move string
    """
    # Check row0 invariant and zero tile pos.
    assert self.row0_invariant(target_col), "row0 invariant failed (pre SR0T)"
    assert self._grid[0][target_col] == 0, "zero tile not at target position"
    
    # Check if target is at pos (0,j), move tiles accordingly.
    moves = "ld"
    curr_row, curr_col = self.current_position(0, target_col)
    if (curr_row, curr_col) != (0, target_col):
        moves += self.compute_tile_moves(curr_row, curr_col, 1, target_col - 1)
        moves += "urdlurrdluldrruld"
    
    # Update the grid with the computed moves and return the move string.
    self.update_puzzle(moves)
    assert self.row1_invariant(target_col - 1)
    return moves

# OwlTest threw an error when the Puzzle class was passed the grid [[1, 2, 0, 3, 4 ], 
# [6, 5, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]], stating that the
# incorrect move string "lduldurdlurrdluldrruld" was returned by SR0T(2). That move
# string will create the following config (tested by calling the GUI with the initial config
# passed to the Puzzle class, then entering the string returned by SR0T_0):
#   1   6   5   3   4
#   2   0   7   8   9
# 10 11 12 13 14
# 15 16 17 18 19
# In place of the 5 tile should be the 2 tile. If you look at the initial grid, 
# a "ld" move will place the 2 in its solved pos and the zero will be in its
# necessary pos. In SR0T_0, the conditional checks for completion of moving the
# target tile to the target pos following the "ld" move. There must be an error
# in the conditional statement. Just beforehand, curr_row, curr_col is assigned
# to (0, 1). In SR0T(2), target_col = 2, so the conditional checks if (0, 1) !=
# (0, 2), which is correct; however, this does not take into account the "dl" move
# made by the zero tile. In fact, I placed the curr_row, curr_col assignment after
# moves was initialized to "dl" as if this were the case. This conditional should
# really look at (0, target_col - 1), which takes into account that zero tile move.

## SR0T_1
def solve_row0_tile(self, target_col):
    """
    Solve the tile in row zero at the specified column
    Updates puzzle and returns a move string
    """
    # Check row0 invariant and zero tile pos.
    assert self.row0_invariant(target_col), "row0 invariant failed (pre SR0T)"
    assert self._grid[0][target_col] == 0, "zero tile not at target position"
    
    # Check if target is at pos (0,j), move tiles accordingly.
    moves = "ld"
    curr_row, curr_col = self.current_position(0, target_col)
    if (curr_row, curr_col) != (0, target_col - 1):
        moves += self.compute_tile_moves(curr_row, curr_col, 1, target_col - 1)
        moves += "urdlurrdluldrruld"
    
    # Update the grid with the computed moves and return the move string.
    self.update_puzzle(moves)
    assert self.row1_invariant(target_col - 1), "row1 invariant failed (post SR0T)"
    return moves

# OwlTest did not return any errors for SRT_1.

##=================================================================

# Phase Three

# Finally, there are only two solution methods left to implement: one for the 2x2
# grid (simple), and one that joins all solution methods under one function so that
# when it is called, the GUI uses the returned move string to step through the
# grid with the zero tile and solve it. I will refer to these as S22 and SPUZ. 

# Note that in homework 4 question 3, the "rdlu" clockwise circle is demonstrated
# as needing 3 instances until the 2x2 grid of numbers is moved back into its 
# original config. Some examples are shown below.
# 0 2    "rdlu" x 1    0 1 | 0 3   "rdlu" x 2   0 1 | 0 1  "rdlu" x 0 as this is
# 3 1                      2 3 | 1 2                    2 3 | 2 3  already solved

# The reverse "drul" CCW circle can also be used:
# 0 3    "drul" x 1    0 1 | 0 2   "drul" x 2   0 1 |
# 1 2                      2 3 | 3 1                    2 3 |

# Note that the 1, 2, and 3 are always in a CCW order. Placing them in a 
# CW order ([[0, 3], [2, 1]]) makes the puzzle unsolvable. 
# The conditional seems like it can be written a few different ways (check for
# the position of any of the values 1-3, use "rdlu" or "drul" exclusively).
# Note that upon completion of the final SR0T call made toward solving the puzzle,
# the 0 should be in the bottom-right pos of the 2x2 grid. The only three possible
# configs of an up-until-then correctly solved puzzle are:
# 3 2      2 1       1 3 
# 1 0      3 0       2 0
# The only invariant that must be asserted prior to the S22 is the R1I(1). At this
# point, the rest of the puzzle but the 2x2 block should be solved. 

## I just noticed a potential error in my implementation of R1I(j): the method does
## not check for ALL tiles being solved to the right of (1,j)--only those in row 1. 
## According to the picture on the left in the example, the 3 is in 'blue', meaning
## it has been solved. This makes sense, as R1I(1) means that the tile at (0, 2)
## is solved, while my implementation does not check for that. R1L_1 below includes
## a for loop that checks tiles from (0, j+1) to (0, n-1). 

## R1I_1
def row1_invariant(self, target_col):
    """
    Check whether the puzzle satisfies the row one invariant
    at the given column (col > 1)
    Returns a boolean
    """
    # Check for tile zero at 1, target_col.
    if self._grid[1][target_col] != 0:
        return False
    # Check that all tiles in row 1 to the right of target_col are solved.
    for col in range(target_col + 1, self._width):
        if (1, col) != self.current_position(1, col):
            return False
    # Check that all tiles in rows 2 to m are solved.
    for row in range(2, self._height):
        for col in range(self._width):
            if (row, col) != self.current_position(row, col):
                return False
    # Check that all tiles in row 0 to the right of target_col are solved.
    for col in range(target_col + 1, self._width):
        if (0, col) != self.current_position(0, col):
            return False
                
    return True
    
## This implementation of R1L did not return an error in OwlTest, so I will use it.

# For the implementation of S22, first assert that zero is indeed at (1, 1), then
# move it "ul" to pos (0, 0). If the 3 is in the top right pos at (0, 1), append
# "drul" to the move string. If 3 is in the bottom left at (1, 0), append "rdlu".
# Otherwise, the puzzle is solved.

## S22_0
def solve_2x2(self):
    """
    Solve the upper left 2x2 part of the puzzle
    Updates the puzzle and returns a move string
    """
    # Check row1 invariant and zero tile pos.
    assert self.row1_invariant(1), "row1 invariant failed (pre S22)"
    assert self._grid[1][1] == 0, "zero tile not at target position"
    
    # Move zero tile and check for 3 position.
    moves = "ur"
    if self._grid[1][1]  == 3:
        self.update_puzzle(moves)
        return moves
    moves += "drul" if self._grid[0][1] == 3 else "rdlu"
    self.update_puzzle(moves)
    return moves

# OwlTest returned a error for puzzle config [[4, 3, 2], [1, 0, 5], [6, 7, 8]] passed
# to the GUI and it is obvious now that I implemented S22 for a 2x2 grid, not the 2x2
# portion of a potentially much larger grid (e.g. for a 4x5 grid, the remaining numbers
# would equal 0, 1, 5, and 6). I will modify the S22 method to look for placement
# of the 1, as before I arbitrarily chose the 3 tile (a good learning experience, though).
# I also initialized moves incorrectly, with an up-right move instead of an up-left one.

## S22_1
def solve_2x2(self):
    """
    Solve the upper left 2x2 part of the puzzle
    Updates the puzzle and returns a move string
    """
    # Check row1 invariant and zero tile pos.
    assert self.row1_invariant(1), "row1 invariant failed (pre S22)"
    assert self._grid[1][1] == 0, "zero tile not at target position"
    
    # Move zero tile and check for 3 position.
    moves = "ul"
    if self._grid[0][1]  == 1:
        self.update_puzzle(moves)
        return moves
    moves += "drul" if self._grid[1][0] == 1 else "rdlu"
    self.update_puzzle(moves)
    return moves

# OwlTest returned no errors! These mods effectively fixed the present issues.

# Finally, one last solution method to implement, one that ties everything above
# together into one single puzzle buster. This method will make use of the solution
# methods SIT(i, j), SC0T(j), SR1T(j), SR0T(j), and S22. The invariants were all
# incorporated into the solution methods, so references to them should not be
# necessary in solve_puzzle (SPUZ).

# The starting target pos will be (m - 1, n - 1). The zero tile will need to be
# moved to this pos, wherever it is in the initial config. Then the SIT and SC0T
# solution methods must be run until the target pos is at (1, n - 1). Then the
# SR1T and SR0T solution methods must be run until the target pos is at (1, 1).
# Then the S22 method is run once to complete the puzzle.

## SPUZ_0
def solve_puzzle(self):
    """
    Generate a solution string for a puzzle
    Updates the puzzle and returns a move string
    """
    # Initialize solved status, target, and empty move string.
    moves = ""
    target_pos = (self._height - 1, self._width - 1)
    
    # Move the zero tile to position (m-1, n-1).
    zero_row, zero_col = self.current_position(0, 0)
    for dummy_move in range(zero_row, self._height):
        moves += "d"
    for dummy_move in range(zero_col, self._width):
        moves += "r"
        
    # Update puzzle with initial move string, as solution methods below will
    # update the puzzle on their own.
    self.update_puzzle(moves)
        
    # Solve for each row until target pos is (1, n-1).
    while target_pos != (1, self._width - 1):
        if target_pos[1] != 0:
            moves += self.solve_interior_tile(target_pos[0], target_pos[1])
            target_pos = (target_pos[0], target_pos[1] - 1)
        else:
            moves += self.solve_col0_tile(target_pos[0], target_pos[1])
            target_pos = (target_pos[0] - 1, self._width - 1)
            
    # Solve for rightmost n-2 cols of remaining two rows.
    while target_pos != (1, 1):
        if target_pos[0] == 1:
            moves += self.solve_row1_tile(target_pos[1])
            target_pos = (target_pos[0] - 1, target_pos[1])
        else:
            moves += self.solve_row0_tile(target_pos[1])
            target_pos = (target_pos[0] + 1, target_pos[1] - 1)
    
    # Solve for remaining 2x2 grid.
    moves += self.solve_2x2()
    
    return moves

# After cleaning up a few minor errors in the code, OwlTest ultimately returned an
# error "Too many positional arguments for function call function "Puzzle.solve_puzzle"
# referring to the line in the first while loop, after the else keyword, where moves
# is appending the move string returned by solve_col0_tile. I fired up a solvable
# config and must step through this from the beginning to ensure that the move strings
# generated are accurate and the grid is effectively updated. I will comment out
# all lines and uncomment piece by piece, allowing the code to return the moves
# and including print statements to double check what is returned. SPUZ_1 will be
# updated below as I find errors.

FifteenGUI(Puzzle(5, 5, [[1,7,9,6,4], [10,5,3,0,14], [20,18,8,17,24],
                 [13,11,12,21,19], [16,22,2,15,23]]))
                 
# The target_pos and zero pos are returned accurately. The zero is moved into
# position at the bottom right of the grid.

# The initial "d" and "r" additions to moves added one too many moves in each
# direction. I subtracted 1 from the stop parameter and zero accurately repositioned.

# The call to self.update_puzzle(moves) appears to be oddly ignored, or at the
# very least superfluous. Commenting or uncommenting it leads to the same result:
# the zero tile repositions and moves is not updated. If uncommented, there are not
# even "move off grid" errors thrown. The update_puzzle method takes the move
# string and then for each direction in it, reassigns self._grid tiles accordingly.
# I think I am letting the slow progression of tile movements blind me from the
# instant return of my print statements, and I am ignoring the fact that the moves
# are returned at the very end and this move string is what is passed to the
# solution string. The problem may be that the while SPUZ is updating the
# final move string, the individual solution methods are already updating the
# puzzle and returning strings. 

# Removing the update_puzzle commands from the individual solution methods
# may throw an OwlTest error. Curiously, even though I pass this first move string
# of down/right movements to update_puzzle, there is no error thrown when the
# string is returned, passed to solution string, and the puzzle is updated with that.
# Logically, the individual updates should not affect things. I will run one while 
# statement, for lower rows, and see what happens.

# I passed the solve_col0_tile method a row arg when I should not have.
# The bottom row was effectively solved by the SIT method until the first
# column was hit. At that point, LRI failed at (4, 0). I also discovered here that
# update_puzzle does indeed have to be called after the initial down-right moves
# are appended to moves. Otherwise, LRI fails pre-SIT at the first call to SIT.
# The calls to solution methods are passed the CURRENT state of the grid, so it
# makes sense that as moves are calculated, they are passed to the update_puzzle
# method so that it is constantly updated. This is how the game logic is controlled.
#  The GUI updates the board based on what is returned by the SPUZ function. This
# is why it clones the board before computing the move string; it solves the board
# as is and takes from it that string, which is passed to the solution string. That
# clone must update itself as moves are made so that the individual solution
# methods are taking current configs of the puzzle and making accurate evals. 

# After changing the args passed to SC0T, the puzzle solved up until target tile
# for 10, at (2, 0). An assertion error was thrown post SC0T. Printing the grid
# after each move and focusing on the post-SC0T moves showed that after the
# final row to be solved by SC0T (row 2), the zero tile is then positioned at (2, 4)
# instead of at (1, 4). In the other two instances of SC0T executing on the puzzle,
# it is placed at the proper pos. After that final execution, the puzzle config is:
# [1, 7, 9, 3, 4]
# [2, 15, 8, 5, 6]
# [10, 12, 13, 14, 0]
# [11, 16, 17, 18, 19]
# [20, 21, 22, 23, 24]
# Beforehand, it looked fine:
# [1, 7, 9, 3, 4]
# [2, 10, 8, 5, 6]
# [0, 11, 12, 13, 14]
# [15, 16, 17, 18, 19]
# [20, 21, 22, 23, 24]
# The 15 and 11 tiles are also out of place. In fact, the 11 is in place of the 15,
# and the entire third row is shifted to the left one position. The zero tile is where
# the 14 WAS located. 
# The move string returned by that final SC0T move is "urldruldrdlurdluurddlurrrr".
# This corresponds to the initial "ur", the "ld" returned by CTM to position the
# 10 tile above the 11 tile, and the "ruldrdlurdluurddlu" string appended in every
# case, where 10 is supposed to be placed in the target pos, and then "rrrr" to
# move the zero tile over to the last col.

# That "ld" should be just an "l" move, according to the directions. Why did this
# not work here, but worked everywhere else? Let's look at CTM. With the config
# below, after SC0T(2), after the initial "ur" move and check, CTM takes 
# [1, 7, 9, 3, 4]
# [10, 0 8, 5, 6]
# [2, 11, 12, 13, 14]
# [15, 16, 17, 18, 19]
# [20, 21, 22, 23, 24]
# The first thing that sticks out is that 10 is initially at (1, 1). SC0T sets the
# current pos early on to check for target tile being above the target pos.
# Then the zero tile moves "ur" and moves are NOT updated, so when CTM is
# passed current pos and the modified target pos, it doesn't take into account
# whether or not that zero tile move up-right changed current pos. To fix this,
# I called self.update_puzzle("ur") to update the puzzle, reassigned current pos
# to wherever target tile is now, then changed the update_puzzle call at the bottom
# to take the parameter moves[2:] so that the first "ur" isn't passed to it. Below
# is SC0T_1 with print statements.

## SC0T_1
def solve_col0_tile(self, target_row):
    print "target_row:", target_row
    """
    Solve tile in column zero on specified row (> 1)
    Updates puzzle and returns a move string
    """
    # Check lower row invariant and zero tile pos.
    assert self.lower_row_invariant(target_row, 0), \
            "lower row invariant failed (pre SC0T)"
    assert self._grid[target_row][0] == 0, \
            "zero tile not at target position"
            
    curr_row, curr_col = self.current_position(target_row, 0)
    print "CURR POS", curr_row, curr_col
    # Check if target tile is above the zero tile.
    if (curr_row, curr_col) == (target_row - 1, 0):
        moves = "u"
        
        for dummy_move in range(self._width - 1):
            moves += "r"
            
        self.update_puzzle(moves)
        assert self.lower_row_invariant(target_row - 1, self._width - 1), \
                "lower row invariant failed (post SC0T)"
                
        return moves
    
    # If the target tile is not above the zero tile, move the zero tile into
    # the new target position above the position target_row, target_col + 1.
    moves = "ur"
    self.update_puzzle("ur")
    curr_row, curr_col = self.current_position(target_row, 0)
    print "CURR POS", curr_row, curr_col
    moves += self.compute_tile_moves(curr_row, curr_col, target_row - 1, 1)
    moves += "ruldrdlurdluurddlu"
    
    for dummy_move in range(self._width - 1):
        moves += "r"
    
    self.update_puzzle(moves[2:])
    print "SCOT MOVE:", moves
    print "TARGET_ROW:", target_row
    for item in self._grid:
        print item
    print ">>>>>"*3
    assert self.lower_row_invariant(target_row - 1, self._width - 1), \
            "lower row invariant failed (post SC0T)"
            
    return moves
    
# The next OwlTest error that is probably much like the recent one is a problem with
# the next while loop throwing an assertion error post-SC0T. I noticed the same
# bug in SR0T, after "ld" is appended to moves but the puzzle is not updated. 

## SR0T_2
def solve_row0_tile(self, target_col):
    """
    Solve the tile in row zero at the specified column
    Updates puzzle and returns a move string
    """
    # Check row0 invariant and zero tile pos.
    assert self.row0_invariant(target_col), "row0 invariant failed (pre SR0T)"
    assert self._grid[0][target_col] == 0, "zero tile not at target position"
    
    # Check if target is at pos (0,j), move tiles accordingly.
    moves = "ld"
    self.update_puzzle("ld")
    curr_row, curr_col = self.current_position(0, target_col)
    if (curr_row, curr_col) != (0, target_col - 1):
        moves += self.compute_tile_moves(curr_row, curr_col, 1, target_col - 1)
        moves += "urdlurrdluldrruld"
    
    # Update the grid with the computed moves and return the move string.
    self.update_puzzle(moves[2:])
    assert self.row1_invariant(target_col - 1), "row1 invariant failed (post SR0T)"
    return moves
    
# This actually did not solve the problem. This prevented a few more solved tiles
# than were returned with SR0T_1 and no updating after the move. This, however,
# does appear to be the proper implementation, so I will assume it is correct as I
# investigate. Now, there is an assertion error, post_SR0T row1 invariant failure.

# Found it! The update works, but the conditional in SR0T_2 checks for the target
# tile at (0, j - 1) instead of at (0, j). Removing this -1 allowed the solution
# method to return the correct move string.

## SR0T_3
def solve_row0_tile(self, target_col):
    """
    Solve the tile in row zero at the specified column
    Updates puzzle and returns a move string
    """
    # Check row0 invariant and zero tile pos.
    assert self.row0_invariant(target_col), "row0 invariant failed (pre SR0T)"
    assert self._grid[0][target_col] == 0, "zero tile not at target position"
    
    # Check if target is at pos (0,j), move tiles accordingly.
    moves = "ld"
    self.update_puzzle("ld")
    curr_row, curr_col = self.current_position(0, target_col)
    if (curr_row, curr_col) != (0, target_col ):
        moves += self.compute_tile_moves(curr_row, curr_col, 1, target_col - 1)
        moves += "urdlurrdluldrruld"
    
    # Update the grid with the computed moves and return the move string.
    self.update_puzzle(moves[2:])
    assert self.row1_invariant(target_col - 1), "row1 invariant failed (post SR0T)"
    return moves

# S22 needed to be updated in the same way.

## S22_2
def solve_2x2(self):
    """
    Solve the upper left 2x2 part of the puzzle
    Updates the puzzle and returns a move string
    """
    # Check row1 invariant and zero tile pos.
    assert self.row1_invariant(1), "row1 invariant failed (pre S22)"
    assert self._grid[1][1] == 0, "zero tile not at target position"
    
    # Move zero tile and check for 3 position.
    moves = "ul"
    self.update_puzzle("ul")
    if self._grid[0][1]  == 1:
        self.update_puzzle(moves[2:])
        return moves
    moves += "drul" if self._grid[1][0] == 1 else "rdlu"
    self.update_puzzle(moves[2:])
    return moves

# Below is the final implementation of SPUZ. It appears to work just fine.

## SPUZ_1
def solve_puzzle(self):
    """
    Generate a solution string for a puzzle
    Updates the puzzle and returns a move string
    """
    # Initialize solved status, target, and empty move string.
    moves = ""
    target_pos = (self._height - 1, self._width - 1)
    
    # Move the zero tile to position (m-1, n-1).
    zero_row, zero_col = self.current_position(0, 0)
    for dummy_move in range(zero_row, self._height - 1):
        moves += "d"
    for dummy_move in range(zero_col, self._width - 1):
        moves += "r"
        
    # Update puzzle with initial move string, as solution methods below will
    # update the puzzle on their own.
    self.update_puzzle(moves)
        
    # Solve for each row until target pos is (1, n-1).
    while target_pos != (1, self._width - 1):
        if target_pos[1] != 0:
            moves += self.solve_interior_tile(target_pos[0], target_pos[1])
            target_pos = (target_pos[0], target_pos[1] - 1)
        else:
            moves += self.solve_col0_tile(target_pos[0])
            target_pos = (target_pos[0] - 1, self._width - 1)
            
    # Solve for rightmost n-2 cols of remaining two rows.
    while target_pos != (1, 1):
        if target_pos[0] == 1:
            moves += self.solve_row1_tile(target_pos[1])
            target_pos = (target_pos[0] - 1, target_pos[1])
        else:
            moves += self.solve_row0_tile(target_pos[1])
            target_pos = (target_pos[0] + 1, target_pos[1] - 1)
    
    # Solve for remaining 2x2 grid.
    moves += self.solve_2x2()
    
    ## Remove useless successions.
    moves = self.remove_useless_moves(moves)
    
    return moves

# 100%! It works like a charm. Praise be to the 1s and 0s. There is one final
# challenge: return the shortest move string possible. One such method is to
# remove all useless successions ("du", "ud", "lr", "rl") where the zero tile moves
# in one direction by one tile, and then backwards in the opposite direction by one
# tile, effectively making no progress. I will implement a helper function that
# scans the move string for those moves and removes them. The challenge puzzle
# config and call to the GUI is at the very bottom.

# Note that simply iterating through the "bad moves" list and removing them from
# the move string may cause other bad moves to arise once the remaining moves
# shift to the left. The RUM function will have to loop through the move string
# multiple times until there are no bad moves found in the string.

## RUM_0
def remove_useless_moves(self, move_string):
    """
    Search a move string and remove all useless moves du, ud, lr, rl.
    """
    moves = "".join(move for move in move_string)
    bad_moves = ["ud", "du", "lr", "rl"]
    bad_moves_in_string = [move for move in bad_moves if move in moves]
    
    while len(bad_moves_in_string) > 0:
        for move in bad_moves:
            moves = moves.replace(move, "")
        bad_moves_in_string = [move for move in bad_moves if move in moves]
        
    return moves
            
## Best is 198: uuullldrruldrruldrulddrulddruluulldrruldrulddrulddrululddruuurrdl
## lurdlulddruldruldrdlurdluurddlurrrulllurrdlurrdldrululldrruldrulddrulldruurrdl
## lurdluldruldrdlurdluurddlurrulldrrurdluldrruldluldrrull

FifteenGUI(Puzzle(4, 4, [[15, 11, 8, 12], [14, 10, 9, 13], [2, 6, 1, 4], [3, 7, 5, 0]]))

##=================================================================
##=================================================================