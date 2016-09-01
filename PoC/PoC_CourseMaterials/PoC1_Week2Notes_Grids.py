"""
Rice University / Coursera: Principles of Computing (Part 1)
Week 2: Class Notes
Grids
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
## Provided code for grid traversal (poc_grid_traversal).

"""
Create a rectagular grid and iterate through 
a subset of its cells in a specified direction
"""

GRID_HEIGHT = 4
GRID_WIDTH = 6

# Create a rectangular grid using nested list comprehension 
# Inner comprehension creates a single row
EXAMPLE_GRID = [[row + col for col in range(GRID_WIDTH)]
                           for row in range(GRID_HEIGHT)]

def traverse_grid(start_cell, direction, num_steps):
    """
    Function that iterates through the cells in a grid
    in a linear direction
    
    Both start_cell is a tuple(row, col) denoting the
    starting cell
    
    direction is a tuple that contains difference between
    consecutive cells in the traversal
    """
    for step in range(num_steps):
        row = start_cell[0] + step * direction[0]
        col = start_cell[1] + step * direction[1]
        print "Processing cell", (row, col), 
        print "with value", EXAMPLE_GRID[row][col] 

def run_example():
    """
    Run several example calls of traverse_grid()
    """
    print "Print out values in grid"
    for row in range(GRID_HEIGHT):
        print EXAMPLE_GRID[row]
    print
    
    print "Traversing first row"
    traverse_grid((0, 0), (0, 1), GRID_WIDTH)
    print
    
    print "Traversing second column"
    traverse_grid((0, 1), (1, 0), GRID_HEIGHT)
    print
    
    print "Traversing second column in reverse order"
    traverse_grid((GRID_HEIGHT - 1, 1), (-1, 0), GRID_HEIGHT)
    print
    
    print "Traversing diagonal"
    traverse_grid((0, 0), (1, 1), min(GRID_WIDTH, GRID_HEIGHT))
  
# Uncomment to run.
#run_example()

##=================================================================

class Gridz:
    """
    Class to perform the same functions as this example,
    but now encapsulated
    """
    
    def __init__(self):
        """
        Create a new Gridz object
        """
        self.CELL_SIZE = 50
        self.GRID_HEIGHT = 6
        self.GRID_WIDTH = 9
        self.CANVAS_HEIGHT = self.CELL_SIZE * self.GRID_HEIGHT
        self.CANVAS_WIDTH  = self.CELL_SIZE * self.GRID_WIDTH

    # Handler to draw on canvas
    def draw(self, canvas):
        """
        Draw the grid
        """
        for row in range(self.GRID_HEIGHT):
            for col in range(self.GRID_WIDTH):
                polygon = [[col * self.CELL_SIZE, row * self.CELL_SIZE], 
                           [col * self.CELL_SIZE, (row + 1) * self.CELL_SIZE], 
                           [(col + 1) * self.CELL_SIZE, (row + 1) * self.CELL_SIZE], 
                           [(col + 1) * self.CELL_SIZE, (row) * self.CELL_SIZE]]
                canvas.draw_polygon(polygon, 1, "Black")
                text_pos = [(col + 0.1) * self.CELL_SIZE, (row + 0.7) * self.CELL_SIZE]
                canvas.draw_text(str(row) + "," + str(col), text_pos, 0.6 * self.CELL_SIZE, "Black")

    def run_gui(self): 
        """
        Create a frame and assign draw handler
        """
        frame = simplegui.create_frame("Indexed grid", self.CANVAS_WIDTH, self.CANVAS_HEIGHT)
        frame.set_canvas_background("White")
        frame.set_draw_handler(self.draw)

        # Start the frame animation
        frame.start()

gridz = Gridz()
gridz.run_gui()

##=================================================================
##=================================================================