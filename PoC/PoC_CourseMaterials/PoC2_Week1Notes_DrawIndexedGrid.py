"""
Rice University / Coursera: Principles of Computing (Part 2)
Week 1: Class Notes
Draw Indexed Grid
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
## Provided constants and draw() and run_gui() functions.

CELL_SIZE = 50
GRID_HEIGHT = 6
GRID_WIDTH = 9
CANVAS_HEIGHT = CELL_SIZE * GRID_HEIGHT
CANVAS_WIDTH  = CELL_SIZE * GRID_WIDTH

# Handler to draw on canvas
def draw(canvas):
    """
    Draw the grid
    """
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            polygon = [[col * CELL_SIZE, row * CELL_SIZE], 
                       [col * CELL_SIZE, (row + 1) * CELL_SIZE], 
                       [(col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE], 
                       [(col + 1) * CELL_SIZE, (row) * CELL_SIZE]]
            canvas.draw_polygon(polygon, 1, "Black")
            text_pos = [(col + 0.1) * CELL_SIZE, (row + 0.8) * CELL_SIZE]
            canvas.draw_text(str(row) + "," + str(col), text_pos, 0.6 * CELL_SIZE, "Black")
                                
def run_gui(): 
    """
    Create a frame and assign draw handler
    """
    frame = simplegui.create_frame("Indexed grid", CANVAS_WIDTH, CANVAS_HEIGHT)
    frame.set_canvas_background("White")
    frame.set_draw_handler(draw)
    
    # Start the frame animation
    frame.start()

# Commented out for testing purposes.
#run_gui()

##=================================================================

# Testing Grounds

# Change the size of the cell to see what changes occur.
CELL_SIZE = 100
#run_gui()

# The canvas size did not change. Changing the CELL_SIZE constant at the top
# of the code does, however, work. This is because the canvas constants are
# set up top and not reassigned after CELL_SIZE is changed.
CANVAS_HEIGHT = CELL_SIZE * GRID_HEIGHT
CANVAS_WIDTH  = CELL_SIZE * GRID_WIDTH
#run_gui() # Success!

# Now let's change grid constants, remembering to recompute canvas constants.
GRID_HEIGHT = 3
GRID_WIDTH = 4
CANVAS_HEIGHT = CELL_SIZE * GRID_HEIGHT
CANVAS_WIDTH  = CELL_SIZE * GRID_WIDTH
#run_gui() # Success!

#Testing a large grid to see how the index numbers run into each other.
GRID_HEIGHT = 23
GRID_WIDTH = 35
CANVAS_HEIGHT = CELL_SIZE * GRID_HEIGHT
CANVAS_WIDTH  = CELL_SIZE * GRID_WIDTH
#run_gui()

# When resizing, remember to change the cell size to accommodate, though 
# indices will still run into each other as this code is not built for greater than
# 9x9 grid dimensions.
CELL_SIZE = 40
GRID_HEIGHT = 23
GRID_WIDTH = 35
CANVAS_HEIGHT = CELL_SIZE * GRID_HEIGHT
CANVAS_WIDTH  = CELL_SIZE * GRID_WIDTH
#run_gui()

def draw(canvas):
    """
    Draw the grid
    """
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            polygon = [[col * CELL_SIZE, row * CELL_SIZE], 
                       [col * CELL_SIZE, (row + 1) * CELL_SIZE], 
                       [(col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE], 
                       [(col + 1) * CELL_SIZE, (row) * CELL_SIZE]]
            canvas.draw_polygon(polygon, 1, "Black")
            text_pos = [(col + 0.1) * CELL_SIZE, (row + 0.8) * CELL_SIZE]
            canvas.draw_text(str(row) + "," + str(col), text_pos, 0.35 * CELL_SIZE, "Black")
            
#run_gui() 

# The new draw function works for two-digit by two-digit indices, but not for 
# one-digit by one-digit indices. Unfortunately, the text width can only be found
# (in CodeSkulptor) with the command 'frame.get_canvas_textwidth' and the
# frame can't be accessed from inside the draw handler. Creating a frame inside
# the handler, even without the start() method, will create that frame as a window.
# An alternative method will have to be devised to better center the indices.

##=================================================================
##=================================================================