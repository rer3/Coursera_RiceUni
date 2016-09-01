"""
Rice University / Coursera: Principles of Computing (Part 2)
Week 1: Class Notes
WildFire Class (using BreadthFirstSearch)
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
##Provided Queue class.

class Queue:
    """
    A simple implementation of a FIFO queue.
    """
    def __init__(self):
        """ 
        Initialize the queue.
        """
        self._items = []

    def __len__(self):
        """
        Return the number of items in the queue.
        """
        return len(self._items)
    
    def __iter__(self):
        """
        Create an iterator for the queue.
        """
        for item in self._items:
            yield item

    def __str__(self):
        """
        Return a string representation of the queue.
        """
        return str(self._items)

    def enqueue(self, item):
        """
        Add item to the queue.
        """        
        self._items.append(item)

    def dequeue(self):
        """
        Remove and return the least recently inserted item.
        """
        return self._items.pop(0)

    def clear(self):
        """
        Remove all items from the queue.
        """
        self._items = []

#-----------------------------------------------------------------
## Provided WildFire GUI, constants, and run_gui() function.

# Global constants
CELL_SIZE = 10
EMPTY = 0 
FULL = 1


class WildFireGUI:
    """
    Container for interactive content
    """    
    def __init__(self, wildfire):
        """ 
        Create frame and timers, register event handlers
        """
        self._fire = wildfire
        self._grid_height = self._fire.get_grid_height()
        self._grid_width = self._fire.get_grid_width()
        self._frame = simplegui.create_frame("Interactive BFS demo", 
                                            self._grid_width * CELL_SIZE, self._grid_height * CELL_SIZE)
        self._frame.set_canvas_background("White")
        self._frame.add_button("Clear all", self.clear, 100)
        self._frame.add_button("Step", self.step, 100)
        self._frame.add_button("Ten steps", self.ten_steps, 100)
        self._frame.set_mouseclick_handler(self.add_cell_index)
        self._frame.set_draw_handler(self.draw)
        
    def start(self):
        """
        Start frame
        """
        self._frame.start()
        
    def clear(self):
        """ 
        Event handler for button that clears everything
        """
        self._fire.clear()
        
    def step(self):
        """ 
        Event handler for button that add cells to the boundary of the fire
        """
        if self._fire.boundary_size() > 0:
            self._fire.update_boundary()
        else:
            print "Click in the canvas to cells to the boundary of the fire"

    def ten_steps(self):
        """ 
        Event handler for button that updates the fire boundary by 10 steps
        """
        for dummy_idx in range(10):
            if self._fire.boundary_size() > 0:
                self._fire.update_boundary()
            
    def add_cell_index(self, click_position):
        """ 
        Event handler to add new cell index to the fire boundary
        """
        cell_index = self._fire.get_index(click_position, CELL_SIZE)
        self._fire.set_full(cell_index[0], cell_index[1])
        self._fire.enqueue_boundary(cell_index[0], cell_index[1])
    
    def draw_cell(self, canvas, row, col, color = "Yellow"):
        """
        Draw a cell in the grid
        """
        upper_left = [col * CELL_SIZE, row * CELL_SIZE]
        upper_right = [(col + 1) * CELL_SIZE, row * CELL_SIZE]
        lower_right = [(col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE]
        lower_left = [col * CELL_SIZE, (row + 1) * CELL_SIZE]
        canvas.draw_polygon([upper_left, upper_right, lower_right, lower_left], 1, "Black", color)
    
    def draw_grid(self, canvas, color = "Yellow"):
        """
        Draw entire grid
        """
        for col in range(self._grid_width):
            for row in range(self._grid_height):
                if not self._fire.is_empty(row, col):
                    self.draw_cell(canvas, row, col, color)
             
    def draw(self, canvas):
        """
        Handler for drawing grid
        """        
        self.draw_grid(canvas)
        
        for cell in self._fire.fire_boundary():
            self.draw_cell(canvas, cell[0], cell[1], "Orange")
      
      
# Start interactive simulation    
def run_gui(wildfire):
    """
    Encapsulate frame
    """
    gui = WildFireGUI(wildfire)
    gui.start()

#-----------------------------------------------------------------
## Provided WildFire class, constants, and run_gui() function call.

# constants
EMPTY = 0 
FULL = 1


class WildFire(Grid):
    """
    Class that models a burning wild fire using a grid and a queue
    The grid stores whether a cell is burned (FULL) or unburned (EMPTY)
    The queue stores the cells on the boundary of the fire
    """
    def __init__(self, grid_height, grid_width, queue = Queue()):
        """
        Override initializer for Grid, add queue to store boundary of fire
        """
        Grid.__init__(self, grid_height, grid_width)
        self._fire_boundary = queue

    def clear(self):
        """
        Set cells to be unburned and the fire boundary to be empty
        """
        Grid.clear(self)
        self._fire_boundary.clear()  


    def enqueue_boundary(self, row, col):
        """
        Add cell with index (row, col) the boundary of the fire
        """
        self._fire_boundary.enqueue((row, col))
    
    def dequeue_boundary(self):
        """
        Remove an element from the boundary of the fire
        """
        return self._fire_boundary.dequeue()
    
    def boundary_size(self):
        """
        Return the size of the boundary of the fire
        """
        return len(self._fire_boundary)

    def fire_boundary(self):
        """
        Generator for the boundary of the fire
        """
        for cell in self._fire_boundary:
            yield cell
        # alternative syntax
        #return (cell for cell in self._fire_boundary)
    
    def update_boundary(self):
        """
        Function that spreads the wild fire using one step of BFS
        Updates both the cells and the fire_boundary
        """
        cell = self._fire_boundary.dequeue()
        neighbors = self.four_neighbors(cell[0], cell[1])
        #neighbors = self.eight_neighbors(cell[0], cell[1])
        for neighbor in neighbors:
            if self.is_empty(neighbor[0], neighbor[1]):
                self.set_full(neighbor[0], neighbor[1])
                self._fire_boundary.enqueue(neighbor)

                
# run gui to visualize wildfire                
#run_gui(WildFire(30, 40))

##=================================================================

# Uncomment to run.
#run_gui(WildFire(30,40))

##=================================================================
##=================================================================