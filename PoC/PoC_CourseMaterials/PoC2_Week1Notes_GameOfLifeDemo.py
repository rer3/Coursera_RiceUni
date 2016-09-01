"""
Rice University / Coursera: Principles of Computing (Part 2)
Week 1: Class Notes
Game of Life Demo
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# All import statements needed.

import simplegui

#-----------------------------------------------------------------
## Provided Grid class and constants.

EMPTY = 0
FULL = 1

class Grid:
    """
    Implementation of 2D grid of cells
    Includes boundary handling
    """
    def __init__(self, grid_height, grid_width):
        """
        Initializes grid to be empty, take height and width of grid as parameters
        Indexed by rows (left to right), then by columns (top to bottom)
        """
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._cells = [[EMPTY for dummy_col in range(self._grid_width)] 
                       for dummy_row in range(self._grid_height)]
                
    def __str__(self):
        """
        Return multi-line string represenation for grid
        """
        ans = ""
        for row in range(self._grid_height):
            ans += str(self._cells[row])
            ans += "\n"
        return ans
    
    def get_grid_height(self):
        """
        Return the height of the grid for use in the GUI
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Return the width of the grid for use in the GUI
        """
        return self._grid_width

    def clear(self):
        """
        Clears grid to be empty
        """
        self._cells = [[EMPTY for dummy_col in range(self._grid_width)]
                       for dummy_row in range(self._grid_height)]
                
    def set_empty(self, row, col):
        """
        Set cell with index (row, col) to be empty
        """
        self._cells[row][col] = EMPTY
    
    def set_full(self, row, col):
        """
        Set cell with index (row, col) to be full
        """
        self._cells[row][col] = FULL
    
    def is_empty(self, row, col):
        """
        Checks whether cell with index (row, col) is empty
        """
        return self._cells[row][col] == EMPTY
 
    def four_neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col)
        """
        ans = []
        if row > 0:
            ans.append((row - 1, col))
        if row < self._grid_height - 1:
            ans.append((row + 1, col))
        if col > 0:
            ans.append((row, col - 1))
        if col < self._grid_width - 1:
            ans.append((row, col + 1))
        return ans

    def eight_neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col) as well as
        diagonal neighbors
        """
        ans = []
        if row > 0:
            ans.append((row - 1, col))
        if row < self._grid_height - 1:
            ans.append((row + 1, col))
        if col > 0:
            ans.append((row, col - 1))
        if col < self._grid_width - 1:
            ans.append((row, col + 1))
        if (row > 0) and (col > 0):
            ans.append((row - 1, col - 1))
        if (row > 0) and (col < self._grid_width - 1):
            ans.append((row - 1, col + 1))
        if (row < self._grid_height - 1) and (col > 0):
            ans.append((row + 1, col - 1))
        if (row < self._grid_height - 1) and (col < self._grid_width - 1):
            ans.append((row + 1, col + 1))
        return ans
    
    def get_index(self, point, cell_size):
        """
        Takes point in screen coordinates and returns index of
        containing cell
        """
        return (point[1] / cell_size, point[0] / cell_size)

#-----------------------------------------------------------------
## Provided GolGui class, constants, and run_gui() function.

# Global constants
CELL_SIZE = 10
EMPTY = 0 
FULL = 1

class GolGui:
    """
    Container for interactive content
    """    
    def __init__(self, game):
        """ 
        Create frame and timers, register event handlers
        """
        self.game = game
        self._grid_height = self.game.get_grid_height()
        self._grid_width = self.game.get_grid_width()
        self._frame = simplegui.create_frame("Interactive Game of Life demo", 
                                             self._grid_width * CELL_SIZE,  self._grid_height * CELL_SIZE)
        self._frame.set_canvas_background("White")
        self._frame.add_button("Clear all", self.clear, 100)
        self._frame.add_button("Step", self.step, 100)
        self._frame.add_button("Ten steps", self.ten_steps, 100)
        self._frame.set_mousedrag_handler(self.add_cell_index)
        self._frame.set_draw_handler(self.draw)
        #--------------------------------------------------
        # Timer for running the simulation, with buttons.
        self._timer = simplegui.create_timer(500, self.ticker)
        self._frame.add_button("Timer On/Off", self.ticker_controller, 100)
        #--------------------------------------------------       
        
    #--------------------------------------------------
    # Button for timer and timer event handler.
    def ticker_controller(self):
        """
        Turn ticker on and off.
        """
        if self._timer.is_running():
            self._timer.stop()
        else:
            self._timer.start()
            
    def ticker(self):
        """
        Run one step of the sim.
        """
        self.step()
    #--------------------------------------------------
    
    def start(self):
        """
        Start frame
        """
        self._frame.start()
                       
    def clear(self):
        """ 
        Event handler for button that clears everything
        """
        self.game.clear()
            
    def step(self):
        """ 
        Event handler for button that updates current game
        """
        self.game.update_gol()

    def ten_steps(self):
        """ 
        Event handler for button that updates current game by 10 steps
        """
        for dummy_idx in range(10):
            self.game.update_gol()
            
    def add_cell_index(self, click_position):
        """ 
        Event handler to add new cell index to the index queue
        """
        cell_index = self.game.get_index(click_position, CELL_SIZE)
        self.game.set_full(cell_index[0], cell_index[1])    
        
    def draw_cell(self, canvas, row, col, color = "Cyan"):
        """
        Draw a cell in the grid
        """
        upper_left = [col * CELL_SIZE, row * CELL_SIZE]
        upper_right = [(col + 1) * CELL_SIZE, row * CELL_SIZE]
        lower_right = [(col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE]
        lower_left = [col * CELL_SIZE, (row + 1) * CELL_SIZE]
        canvas.draw_polygon([upper_left, upper_right, lower_right, lower_left], 1, "Black", color)
    
    def draw_grid(self, canvas, color = "Cyan"):
        """
        Draw entire grid
        """
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if not self.game.is_empty(row, col):
                    self.draw_cell(canvas, row, col, color)
    
    def draw(self, canvas):
        """
        Handler for drawing grid
        """        
        self.draw_grid(canvas)

            
# Start interactive simulation    
def run_gui(game):
    """
    Encapsulate frame
    """
    gui = GolGui(game)
    gui.start()

#-----------------------------------------------------------------
## Provided GameOfLife class, constants, and run_gui() function call.

# constants
EMPTY = 0 
FULL = 1

class GameOfLife(Grid):
    """
    Extend Grid class to support Game of Life
    """
    def update_gol(self):
        """
        Function that performs one step of the Game of Life
        """
        
        updated_grid = [[self.update_cell(row, col) \
                            for col in range(self.get_grid_width())] \
                            for row in range(self.get_grid_height())]
        
        for col in range(self.get_grid_width()):
            for row in range(self.get_grid_height()):
                if updated_grid[row][col] == EMPTY:
                    self.set_empty(row, col)
                else:
                    self.set_full(row, col)
                    
    def update_cell(self, row, col):
        """
        Function that computes the update for one cell in the Game of Life
        """
        # compute number of living neighbors
        neighbors = self.eight_neighbors(row, col)
        living_neighbors = 0
        for neighbor in neighbors:
            if not self.is_empty(neighbor[0], neighbor[1]):
                living_neighbors += 1
            
        # logic for Game of life        
        if (living_neighbors == 3) or (living_neighbors == 2 and not self.is_empty(row, col)):
            return FULL
        else:
            return EMPTY
            

# run gui        
#run_gui(GameOfLife(30, 40))

##=================================================================

# Testing Grounds

# Let's take a look at how this works. The first thing I want to do is add a timer
# that executes a step every 0.5-1.0 seconds. The Ten Steps calculation is very
# computationally intensive in Chrome, and that timing seems to be conducive
# to running the program smoothly. The timer will be added to GolGui.

# Uncomment to run.
#run_gui(GameOfLife(30,40))

# That sim stills runs slowly (but the timer works). I will look at a smaller grid.

# Uncomment to run.
#run_gui(GameOfLife(20,10))

# Changing the GOL logic so that the conditional looks for 2 living neighbors
# allows the sim to run indefinitely. Setting that to 4 living neighbors cauess
# the living cells to disappear very quickly. The 3 neighbor check is a happy
# medium. 

##=================================================================
##=================================================================