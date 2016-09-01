"""
Rice University / Coursera: Principles of Computing (Part 1)
Week 2: Project 2
2048 Game
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# All import statements needed.

import codeskulptor
import math
import random
import simplegui

# Below is the link to the description of this assignment.

COURSE = "https://class.coursera.org/principlescomputing1-004/"
DESCRIPTION = COURSE + "wiki/view?page=2048"

#-----------------------------------------------------------------
## Provided 2048 GUI class, constants, and run_gui function
## (poc_2048_gui).

# Tile Images
IMAGENAME = "assets_2048.png"
TILE_SIZE = 100
HALF_TILE_SIZE = TILE_SIZE / 2
BORDER_SIZE = 45

# Directions
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

class GUI:
    """
    Class to run game GUI.
    """
    def __init__(self, game):
        self._rows = game.get_grid_height()
        self._cols = game.get_grid_width()
        self._frame = simplegui.create_frame('2048',
                        self._cols * TILE_SIZE + 2 * BORDER_SIZE,
                        self._rows * TILE_SIZE + 2 * BORDER_SIZE)
        self._frame.add_button('New Game', self.start)
        self._frame.set_keydown_handler(self.keydown)
        self._frame.set_draw_handler(self.draw)
        self._frame.set_canvas_background("#BCADA1")
        self._frame.start()
        self._game = game
        url = codeskulptor.file2url(IMAGENAME)
        self._tiles = simplegui.load_image(url)
        self._directions = {"up": UP, "down": DOWN,
                            "left": LEFT, "right": RIGHT}

    def keydown(self, key):
        """
        Keydown handler
        """
        for dirstr, dirval in self._directions.items():
            if key == simplegui.KEY_MAP[dirstr]:
                self._game.move(dirval)
                break

    def draw(self, canvas):
        """
        Draw handler
        """
        for row in range(self._rows):
            for col in range(self._cols):
                tile = self._game.get_tile(row, col)
                if tile == 0:
                    val = 0
                else:
                    val = int(math.log(tile, 2))
                canvas.draw_image(self._tiles,
                    [HALF_TILE_SIZE + val * TILE_SIZE, HALF_TILE_SIZE],
                    [TILE_SIZE, TILE_SIZE],
                    [col * TILE_SIZE + HALF_TILE_SIZE + BORDER_SIZE,
                     row * TILE_SIZE + HALF_TILE_SIZE + BORDER_SIZE],
                    [TILE_SIZE, TILE_SIZE])

    def start(self):
        """
        Start the game.
        """
        self._game.reset()


def run_gui(game):
    """
    Instantiate and run the GUI.
    """
    gui = GUI(game)
    gui.start() 

#-----------------------------------------------------------------
## Merge code from Project 1.

def merge(line):
    """
    Function that merges a single row or column in 2048. 
    A left-merged list with trailing zeros is returned.
    """
    # Slide nonzeros to the left.
    slid = [num for num in line if num != 0]
    
    # Combine like pairs.
    for idx in range(len(slid) - 1):
        if slid[idx] == slid[idx+1] and slid[idx] != 0:
            slid[idx] *= 2
            slid[idx+1] = 0
    
    merged = [num for num in slid if num != 0]
    return merged + [0] * (len(line) - len(merged))

#-----------------------------------------------------------------
## Provided code for 2048 game (poc_2048_template). References to
## poc_2048_gui removed as the GUI class is included in this doc.

"""
Clone of 2048 game.
"""

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

## Merge code placed here in template, found above in shared area.

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        """
        Create a TwentyFortyEight object
        """
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()
        self._initial_tiles = {UP: [(0, col) for col in range(self._grid_width)],
                               DOWN: [(self._grid_height - 1, col) for col in \
                                      range(self._grid_width)],
                               LEFT: [(row, 0) for row in range(self._grid_height)],
                               RIGHT: [(row, self._grid_width - 1) for row in \
                                      range(self._grid_height)]} 

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0]*self._grid_width for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        row = random.randrange(0, self._grid_height)
        col = random.randrange(0, self._grid_width)
        value = random.choice([4] + [2]*9)
        
        if self._grid[row][col] == 0:
            self._grid[row][col] = value
        else:
            self.new_tile()

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        board = ""
        for row in range(self._grid_height):
            board += str(self._grid[row]) + "\n"
        return board

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # Initialize variables.
        grid_changed = False
        len_line = self._grid_height if direction == 1 or direction == 2 \
                   else self._grid_width
        grid_coords = []
        merged_lines = []
        
        # Iterate through initial tiles and merge the divergent lines.
        for origin in self._initial_tiles[direction]:
            line_coords = []
            unmerged_line = []
            for idx in range(len_line):
                tile_pos = (origin[0] + idx * OFFSETS[direction][0],
                            origin[1] + idx * OFFSETS[direction][1])
                line_coords.append(tile_pos)
                unmerged_line.append(self._grid[tile_pos[0]][tile_pos[1]])
            grid_coords.append(line_coords)
            merged_lines.append(merge(unmerged_line))
            
        # Check for a change in the grid.
        for line in grid_coords:
            for pos in line:
                old_tile = self._grid[pos[0]][pos[1]]
                new_tile = merged_lines[grid_coords.index(line)][line.index(pos)]
                if old_tile != new_tile:
                    self._grid[pos[0]][pos[1]] = new_tile
                    grid_changed = True
                    
        if grid_changed:
            self.new_tile()


#run_gui(TwentyFortyEight(4, 4))

##=================================================================

DIRECTIONS = '''
Overview
----------
2048 is a simple grid-based numbers game. The rules are described here:
https://class.coursera.org/principlescomputing1-004/wiki/2048_Game.
For this assignment, your task is to complete the implementation of a version of
the 2048 game. Since we will provide a GUI for the game, your task is to implement
the game logic in terms of a TwentyFortyEight class in Python. Familiarize yourself
with grid conventions we will use in this course: 
https://class.coursera.org/principlescomputing1-004/wiki/grids. The template for
this assignment is provided here. The signature of the functions, classes, and methods
in this file must remain unchanged, but you may add any additional code that you need.

Testing Your Project
----------
Testing is a critical part of the process of building your mini-project. Remember
to be testing each method as you write it. Build your own collection of tests. Note
that template uses a GUI, which is created and run by the last line of the template.
When testing with the GUI, it is important to point out that just because it seems
like your game plays reasonably does not mean that you code is correct. You can
easily have subtle errors that are hard to see by casually playing the game. 

Submit your code to the OwlTest page. Follow the style guidelines. When finished,
submit code to the CourseraTest page.

Phase One
----------
You should paste your merge function from the previous mini-project into this
template for this mini-project. 

Phase Two
----------
In the template, we have provided the skeleton of a TwentyFortyEight class. You
should first implement the game initialization, which consist of the following methods:
* __init__(self, grid_height, grid_width): This method takes the height and width of
    the grid and creates the initial 2048 board. You should store the height and width
    of the grid for use in other methods and then call the reset method to create an
    initial grid of the proper size.
* reset(self): This method should create a grid of height x width zeros and then use
    the new_tile method to add two initial tiles. This method will be called by 
    __init__ to create the initial grid. It will also be called by the GUi to start a 
    new game, so the point of this method is to reset any state of the game, such as
    the grid, so that you are ready to play again.
* new_tile(self): This method should randomly select an empty grid square (one that
    currently has a value of 0) if one exists and place a new tile in that square. The
    new tile should have the value 2 90% of the time and the value 4 10% of the time.
    You should implement this by selecting a tile randomly with that proportion, not by
    guaranteeing that every 10th tile is a 4.

You will also need to implement the following helper methods, which will help you
develop and test the above methods. Further, they are used by both GUI and OwlTest.

* get_grid_height(self): This method should return the height of the grid. It will be
    used by the GUI to determine the size of the board.
* get_grid_width(self): This method should return grid width.
* __str__(self): This method should return a human readable string representing
    your 2048 board. You may format this string however you would like. This method
    will be helpful to you as you develop and debug your code and will be used by
    OwlTest to display your game board when there are errors.
* set_tile(self, row, col, value): This method should set the tile at position
    (row,col) in the grid to value. This method will be helpful to you as you test
    your code with different configurations and will be used by OwlTest for the
    same purpose. Note that the rows of the grid are indexed from top to bottom
    starting at zero while the columns are indexed left to right.
* get_tile(self, row, col): Return the value of the tile at position (row, col).

You should test all of these methods as you develop them. Note, however, that
your reset method will not be completely correct until after you implement new_tile.
You can still call new_tile from reset before you implement it, it will just not add any
tiles. During testing, you will want to use the set_tile method so that you can start
with different board states.

Phase Three
----------
You are now ready to implement the final method: move. It is where the real logic
of the game goes. This method should slide all of the tiles in the given direction. The
direction argument will be one of the constants UP, DOWN, LEFT, or RIGHT. There are
many ways of implementing the move method. Here is one approach that will help
you avoid writing separate pieces of code for each direction.

For each direction, we recommend pre-computing a list of the indices for the initial
tiles in that direction. Initial tiles are those whose values appear first in the list
passed to the merge function. For example, the initial tiles for the UP direction
lie along the top row of the grid and in a 4x4 grid have indices [(0,0), (0,1), (0,2),
(0,3)]. Since these lists of indices will be used throughout the game, we recommend
computing them once in the __init__method and then storing them in a dictionary
where the keys are the direction constants (UP, DOWN, LEFT, and RIGHT).

With this dictionary computed, the move method can be implemented as follows:
give a direction, iterate over the list of initial tiles for that direction, and perform
the following 3 steps for each initial tile:
1.) Use the direction in the provided OFFSETS dict to iterate over the entries of
    the associated row or col starting at the specified initial tile. Retrieve the
    tile values from those entries and store them in a temporary list.
2.) Use your merge function to merge the tile values in this temp list.
3.) Iterate over the entries in the row or col again and store the merged tile values
    back into the grid.
    
To illustrate this process, consider updating the state of the game via method 
call move(UP) in the config below:
4 2 2 2
0 0 2 8
4 2 2 8
0 2 0 4

Following our outline above, we retrive the list of initial tiles [(0,0), (0,1),
(0,2), (0,3)] for the top row of the grid and use the direction (1,0) associated
with UP to iterate over the grid indices for each column. For the second col, these
indices are [(0,1), (1,1), (2,1), (3,1)]. Using these indices, we can create a temp
list [2,0,2,2] that holds the tile values in the col, apply merge to compute the
merged list [4,2,0,0], and finally copy the new merged tile values back into
the grid. This sequence of operations yields the grid shown below.
8   4   4   2
0   2   2 16
0   0   0   4
0   0   0   0

If you have done this correctly, a single call to the move method should slide all 
of the tiles in the given direction. All that remains is that you must determine
if any tiles have moved. You can easily do this when you put the line back into
the grid. For each element, check if it has changed and keep track of whether any
tiles have changed. If so, you should add a new tile to the grid, by calling your
new_tile method. Now you are ready to run the GUi and play 2048!

Note that you do not write any logic to determine whether the user has won or
lost the game. This assignment does not require this step.
'''

##=================================================================

# Phase One

# The merge function from Project 1 replaced the stub for the merge function in the
# provided template above. 

##=================================================================

# Phase Two

# First implement __init__. The height and width will need to be stored in variables.
# The initial grid will have to be created (a 2D list). Then call the reset method.
# It is also recommended in Phase Three (I'm jumping the gun here) to pre-compute
# a list of the indices for the initial tiles in each direction. I will initialize
# this list here.

def __init__(self, grid_height, grid_width):
    """
    Create a TwentyFortyEight object
    """
    self._grid_height = grid_height
    self._grid_width = grid_width
    self.reset()
    self._initial_tiles = {UP: [(0, col) for col in range(self._grid_width)],
                           DOWN: [(self._grid_height - 1, col) for col in \
                                  range(self._grid_width)],
                           LEFT: [(row, 0) for row in range(self._grid_height)],
                           RIGHT: [(row, self._grid_width - 1) for row in \
                                  range(self._grid_height)]}      

# Before testing anything, I'll implement the reset and new_tile methods due to the
# dependencies. The reset method should simply create the grid with 0 values in it
# and call new_tile twice.

def reset(self):
    """
    Reset the game so the grid is empty except for two
    initial tiles.
    """
    self._grid = [[0]*self._grid_width for dummy_row in range(self._grid_height)]
    self.new_tile()
    self.new_tile()

# The new_tile method simply chooses a random row and col, checks to see if it is
# empty (if not, choose another one until an empty one is found), and then
# sets the tile's value. To ensure that it chooses 4 10% of the time and 2 90% of
# the time, the list of numbers from which to randomly choose must have one 4
# for every nine 2's. The proportion is 10/90.

def new_tile(self):
    """
    Create a new tile in a randomly selected empty
    square.  The tile should be 2 90% of the time and
    4 10% of the time.
    """
    row = random.randrange(0, self._grid_height)
    col = random.randrange(0, self._grid_width)
    value = random.choice([4] + [2]*9)
    
    if self._grid[row][col] == 0:
        self._grid[row][col] = value
    else:
        self.new_tile()

# Although it may be easier to implement __str__ before testing instances of the
# TwentyFortyEight class out, I will return the specific fields to verify that the
# methods are functioning properly. Uncomment to run.

# print "Testing __init__, reset(), new_tile()"
# grid = TwentyFortyEight(4,4)
# for item in grid._grid:
    # print item
# print "-"*10

# grid.new_tile()
# grid.new_tile()
# for item in grid._grid:
    # print item
# print "-"*10

# grid.reset()
# for item in grid._grid:
    # print item
# print "-"*10
# print "\n"

# The new_tile method does not appear to be adding new tiles to a grid. 
# SOLVED: I put an equality "==" operator instead of an assignment operator
# "=" in the new_tile statement that assigns the value to the row,col in the grid.

# Next, the helper methods must be implemented. The two getters are simple for
# grid dims are simple, as are the setter and getter for tiles. The __str__ method
# is straightforward.

def get_grid_height(self):
    """
    Get the height of the board.
    """
    return self._grid_height

def get_grid_width(self):
    """
    Get the width of the board.
    """
    return self._grid_width
    
def __str__(self):
    """
    Return a string representation of the grid for debugging.
    """
    board = ""
    for row in range(self._grid_height):
        board += str(self._grid[row]) + "\n"
    return board

def set_tile(self, row, col, value):
    """
    Set the tile at position row, col to have the given value.
    """
    self._grid[row][col] = value

def get_tile(self, row, col):
    """
    Return the value of the tile at position row, col.
    """
    return self._grid[row][col]

# I will test these methods out now using a series of differently sized grids.
# Uncomment to run tests.

# print "Testing __str__, getters, setters"
# grid1 = TwentyFortyEight(4,4)
# print grid1
# print "height:", grid1.get_grid_height()
# print "width:", grid1.get_grid_width()
# print "Set tile (2,2) to 42"
# grid1.set_tile(2, 2, 42)
# print grid1
# print "Tile at (3,3) is:", grid1.get_tile(3,3)
# print "-"*10

# grid2 = TwentyFortyEight(7,7)
# print grid2
# print "height:", grid2.get_grid_height()
# print "width:", grid2.get_grid_width()
# # Testing out of range assignments.  Success, rcvd IndexError.
# #grid2.set_tile(7,7,42)
# #grid2.get_tile(7,7)
# print "-"*10
# print "\n"

# The helper methods appear to function properly as well.

##=================================================================

# Phase Three

# Finally, the move method must be implemented. The self._initial_tiles field will
# be referenced here to avoid writing separate pieces of code for each direction.
# This will be the list of origin points from which to build the lists that will 
# be merged. The direction in the provided OFFSETS dictionary will be used to
# iterate over the entries of the row/col starting at the specified origin/initial tile.
# these lists will be stored in a separate, temporary list which is passed to the
# merge function. Then the grid is updated.

# Remember to check if the grid is changed by making the move. If not, then
# new tiles are not added. Initialize a ref var for the line length (which is 
# dependent on direction of move). Iterate through the initial tiles and from
# each origin, iterate through the rest of the line diverging from it. Store both
# the line values and the line coords in temporary lists. Then, merge the line
# values and store the new values in a merged_lines list. Store the associated
# line coords in a grid_coords list. This will allow the grid to be updated with
# the new values placed in the right positions. Finally, check the grid for any
# changes. 

def move(self, direction):
    """
    Move all tiles in the given direction and add
    a new tile if any tiles moved.
    """
    # Initialize variables.
    grid_changed = False
    len_line = self._grid_height if direction == 1 or direction == 2 \
               else self._grid_width
    grid_coords = []
    merged_lines = []
    
    # Iterate through initial tiles and merge the divergent lines.
    for origin in self._initial_tiles[direction]:
        line_coords = []
        unmerged_line = []
        for idx in range(len_line):
            tile_pos = (origin[0] + idx * OFFSETS[direction][0],
                        origin[1] + idx * OFFSETS[direction][1])
            line_coords.append(tile_pos)
            unmerged_line.append(self._grid[tile_pos[0]][tile_pos[1]])
        grid_coords.append(line_coords)
        merged_lines.append(merge(unmerged_line))
        
    # Check for a change in the grid.
    for line in grid_coords:
        for pos in line:
            old_tile = self._grid[pos[0]][pos[1]]
            new_tile = merged_lines[grid_coords.index(line)][line.index(pos)]
            if old_tile != new_tile:
                self._grid[pos[0]][pos[1]] = new_tile
                grid_changed = True
                
    if grid_changed:
        self.new_tile()
        
# OwlTest was used to verify the success of this implementation. No errors were
# returned. Now for the final test (uncomment to run).

#run_gui(TwentyFortyEight(4, 4))
#run_gui(TwentyFortyEight(6,6))

# It's a success. The challenge going forward is to implement a solver function
# that computes a series of moves that solves the game. Also, methods and fields
# need to be added to the class to track game progress.

##=================================================================
##=================================================================