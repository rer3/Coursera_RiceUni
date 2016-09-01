"""
Coursera / Rice University: Principles of Computing (Part 2)
Week 1: Project 1
Zombie Apocalypse 
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

COURSE = "https://class.coursera.org/principlescomputing2-004/"
DESCRIPTION = COURSE + "wiki/view?page=zombie"

#-----------------------------------------------------------------
## Provided Grid class poc_grid. 

"""
Grid class
"""

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
## Provided Queue class poc_queue.

"""
Queue class
"""

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
## Provided ApocalypseGUI class poc_zombie_gui, global constants,
## and run_gui() function.

"""
Zombie Apocalypse mini-project
Click "Mouse click" button to toggle items added by mouse clicks
Zombies have four way movement, humans have eight way movement
"""

# Global constants
EMPTY = 0
FULL = 1
HAS_ZOMBIE = 2
HAS_HUMAN = 4
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7
CELL_COLORS = {EMPTY: "White",
               FULL: "Black",
               HAS_ZOMBIE: "Red",
               HAS_HUMAN: "Green",
               HAS_ZOMBIE|HAS_HUMAN: "Purple"}

NAME_MAP = {OBSTACLE: "obstacle",
            HUMAN: "human",
            ZOMBIE: "zombie"}

# GUI constants
CELL_SIZE = 10
LABEL_STRING = "Mouse click: Add "


class ApocalypseGUI:
    """
    Container for interactive content
    """
    def __init__(self, simulation):
        """
        Create frame and timers, register event handlers
        """
        self._simulation = simulation
        self._grid_height = self._simulation.get_grid_height()
        self._grid_width = self._simulation.get_grid_width()
        self._frame = simplegui.create_frame("Zombie Apocalypse simulation",
                                             self._grid_width * CELL_SIZE,
                                             self._grid_height * CELL_SIZE)
        self._frame.set_canvas_background("White")
        self._frame.add_button("Clear all", self.clear, 200)
        self._item_type = OBSTACLE
        label = LABEL_STRING + NAME_MAP[self._item_type]
        self._item_label = self._frame.add_button(label,
                                                  self.toggle_item, 200)
        self._frame.add_button("Humans flee", self.flee, 200)
        self._frame.add_button("Zombies stalk", self.stalk, 200)
        
        #--------------------------------------------------
        # Buttons to turn on and off the automatic simulation.
        self._frame.add_button("Start simulation", self.start_sim, 200)
        self._frame.add_button("End simulation", self.end_sim, 200)
        
        # Timer to manage automatic simulation.
        self.timer = simplegui.create_timer(300, self.auto_sim)
        #--------------------------------------------------
        
        self._frame.set_mouseclick_handler(self.add_item)
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
        self._simulation.clear()

    def flee(self):
        """
        Event handler for button that causes humans to flee zombies by one cell
        Diagonal movement allowed
        """
        zombie_distance = self._simulation.compute_distance_field(ZOMBIE)
        self._simulation.move_humans(zombie_distance)

    def stalk(self):
        """
        Event handler for button that causes zombies to stack humans by one cell
        Diagonal movement not allowed
        """
        human_distance = self._simulation.compute_distance_field(HUMAN)
        self._simulation.move_zombies(human_distance)

    def toggle_item(self):
        """
        Event handler to toggle between new obstacles, humans and zombies
        """
        if self._item_type == OBSTACLE:
            self._item_type = ZOMBIE
            self._item_label.set_text(LABEL_STRING + NAME_MAP[ZOMBIE])
        elif self._item_type == ZOMBIE:
            self._item_type = HUMAN
            self._item_label.set_text(LABEL_STRING + NAME_MAP[HUMAN])
        elif self._item_type == HUMAN:
            self._item_type = OBSTACLE
            self._item_label.set_text(LABEL_STRING + NAME_MAP[OBSTACLE])

    def add_item(self, click_position):
        """
        Event handler to add new obstacles, humans and zombies
        """
        row, col = self._simulation.get_index(click_position, CELL_SIZE)
        if self._item_type == OBSTACLE:
            if not self.is_occupied(row, col):
                self._simulation.set_full(row, col)
        elif self._item_type == ZOMBIE:
            if self._simulation.is_empty(row, col):
                self._simulation.add_zombie(row, col)
        elif self._item_type == HUMAN:
            if self._simulation.is_empty(row, col):
                self._simulation.add_human(row, col)

    def is_occupied(self, row, col):
        """
        Determines whether the given cell contains any humans or zombies
        """
        cell = (row, col)
        human = cell in self._simulation.humans()
        zombie = cell in self._simulation.zombies()
        return human or zombie

    def draw_cell(self, canvas, row, col, color="Cyan"):
        """
        Draw a cell in the grid
        """
        upper_left = [col * CELL_SIZE, row * CELL_SIZE]
        upper_right = [(col + 1) * CELL_SIZE, row * CELL_SIZE]
        lower_right = [(col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE]
        lower_left = [col * CELL_SIZE, (row + 1) * CELL_SIZE]
        canvas.draw_polygon([upper_left, upper_right,
                             lower_right, lower_left],
                            1, "Black", color)

    def draw_grid(self, canvas, grid):
        """
        Draw entire grid
        """
        for col in range(self._grid_width):
            for row in range(self._grid_height):
                status = grid[row][col]
                if status in CELL_COLORS:
                    color = CELL_COLORS[status]
                    if color != "White":
                        self.draw_cell(canvas, row, col, color)
                else:
                    if status == (FULL | HAS_HUMAN):
                        raise ValueError, "human moved onto an obstacle"
                    elif status == (FULL | HAS_ZOMBIE):
                        raise ValueError, "zombie moved onto an obstacle"
                    elif status == (FULL | HAS_HUMAN | HAS_ZOMBIE):
                        raise ValueError, "human and zombie moved onto an obstacle"
                    else:
                        raise ValueError, "invalid grid status: " + str(status)

    def draw(self, canvas):
        """
        Handler for drawing obstacle grid, human queue and zombie queue
        """
        grid = [[FULL] * self._grid_width for
                dummy_row in range(self._grid_height)]
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._simulation.is_empty(row, col):
                    grid[row][col] = EMPTY
        for row, col in self._simulation.humans():
            grid[row][col] |= HAS_HUMAN
        for row, col in self._simulation.zombies():
            grid[row][col] |= HAS_ZOMBIE
        self.draw_grid(canvas, grid)
        
    #--------------------------------------------------
    # Button handlers for starting and ending the automatic simulation.
    def start_sim(self):
        """
        Handler for turning on the automatic simulation.
        """
        self.timer.start()
        
    def end_sim(self):
        """
        Handler for turning off the automatic simulation.
        """
        self.timer.stop()
        
    # Timer for automatic simulation.
    def auto_sim(self):
        """
        Automatically moves zombies and humans every half second.
        """
        self.flee()
        self.stalk()
    #--------------------------------------------------


# Start interactive simulation
def run_gui(sim):
    """
    Encapsulate frame
    """
    gui = ApocalypseGUI(sim)
    gui.start()

##=================================================================

DIRECTIONS = '''
Overview
----------
In this mini-project, we will create a simulation of zombies and humans interacting 
on a grid. As in the movies, our zombies are hungry for human brains. As a result, 
zombies chase humans and humans flee from zombies. To keep our simulation manageable, 
the positions of the zombies and humans will be restricted to a grid. In our 
simulation, zombies are not very agile and can only move up, down, left or right in 
one step of the simulation. On the other hand, humans are more agile and can move 
in these four directions as well as the four neighboring diagonal directions. If a 
zombie catches a human by positioning itself in the same cell, the zombie enjoys 
some delicious human brains. Being a Computer Scientist, the human has plenty of 
brains to spare and continues to live on in our simulation.

To enhance the realism of our simulation, some of the cells in this grid will be marked 
as impassable and restrict zombie/human movement so that they can not move through 
these cells. Our task in this simulation is to implement an Apocalypse class that 
encapsulates the core mechanisms of this simulation and that interacts with a GUI 
that we have created for visualizing the simulation in CodeSkulptor. This Apocalpyse 
class is a sub-class of the Grid class and inherits the Grid class methods. Passable 
cells in the grid correspond to EMPTY cells while FULL cells are impassable. Humans 
and zombies can only inhabit passable cells of the grid. However, several humans 
and zombies may inhabit the same grid cell.

This Apocalpyse class also includes two lists, one for zombies and one for humans. 
Note that the entries in each list are cell indices of the form (row, col) that 
represent the position of zombies/humans in the grid. Each step in the simulation 
will either update the positions of the zombies based on the state of the grid and 
the position of the humans or update the positions of the humans based on the 
state of the grid and the position of the zombies.

Testing Your Code
----------
Your task is to implement the Apocalypse class described in detail below. Remember
to test each method as you implement it using the testing philosophy discussed
in class. You are also welcome to experiment with your simulation code in 
CodeSkulptor using our provided GUI. Note that the template contains two lines of
the form:
* import poc_zombie_gui
* poc_zombie_gui.run_gui(Apocalypse(30, 40))
that will load, create and run our GUI in CodeSkulptor. Once you are confident
that your implementation works, test your code using the OwlTest test suite.

Remember that OwlTest uses Pylint to check that you have following the style
guidelines for this class. Deviations will result in deductions. Submit your final
code to the CourseraTest page for this mini-project.

Phase One
----------
In phase one, we will implement the basic methods for the Apocalypse class. We suggest
that you start from the provided template. Note that the class is a subclass of the 
Grid class and inherits all of its methods.

The template contains an implementation of the __init__ method for the Apocalypse
class. The initializer takes two required args grid_height and grid_width. The init
also takes 3 options args obstacle_list, zombie_list, and human_list which are lists 
of cells that initially contain obstacles, zombies and humans, respectively. For
phase one, your task is to implement the remaining seven methods:
* clear(self): Reset all cells in the grid to be passable and reinitialize the human
    and zombie lists to be empty. Remember that you can use the clear method from
    the Grid class to clear the grid of impassable cells. Examine the implementation of
    the __init__ method for how to call this method.
* add_zombie(self, row, col): Add a zombie to the zombie list at the supplied row
    and column.
* num_zombies(self): Return the number of zombies in the zombie list.
* zombies(self): Generator that allows you to iterate over zombies in the zombie
    list. Here, a zombie is a tuple of the form (row, col) indicating the zombie's
    location in the grid. The generator MUST yield the zombies in the order they were
    added (even if they have moved). Remember that you can use a generator to
    implement this method in one or two lines of code.
* add_human(self, row, col): Add a human to the human list at the row, col.
* num_humans(self): Return the number of humans in the human list.
* humans(self): Generator that allows you to iterate over humans in the human list.
    The generator MUST yield the humans in the order they were added.
    
Once you have implemented these methods, you should be able to add zombies (red)
and humans (green) by toggling the button labelled "Mouse click: ..." and then clicking
on the canvas. Cells that are occupied by both zombies and humans are purple.

Phase Two
----------
Phase two is the core of this project. Your task will be to compute a simple
approximation of the distance from each cell in the grid to the nearest zombie
or human. This distance will correspond to the length of the shortest sequence
of adjacent grid cells (a path) from the cell to a zombie. This 2D array of integer
distances is a distance field. The image below shows an example of two zombies on
a 4x6 grid and the distances from each cell in the grid to the nearest zombie. Note
that in this diagram, we are using the cell's four neighbors when determining whether
cells are adjacent. Since no image is included, the 0 cells are zombies, and the
other cells correspond to empty or full cells adjacent to them.
5 4 3 3 2 1
4 3 2 2 1 0
3 2 1 2 2 1
2 1 0 1 2 2

Observe that the distances in this example grow in a manner strikingly similar to
the order in which cells are visited during breadth-first search (BFS). This observation
is not a coincidence. In fact, this distance field was computed using BFS. To compute
the distance field, start by recalling the description of BFS:
    while boundary is not empty:
        current_cell <- dequeue boundary
        for all neighbor_cell of current_cell:
            if neighbor_cell is not visited:
                add_neighbor_cell to visited
                enqueue neighbor_cell onto boundary

This description can be modified to compute a distance field during BFS as follows:
* Create a new grid "visited" of the same size as the original grid and initialize
    its cells to be empty.
* Create a 2D list "distance_field" of the same size as the original grid and initialize
    each of its entries to be the product of the height times the width of the grid.
    This value is larger than any possible distance.
* Create a queue boundary that is a copy of either the zombie list or the human
    list. For cells in the queue, initialize "visited" to be FULL and "distance_field"
    to be zero. We recommend you use our Queue class.
* Finally, implement a modified version of BFS described above. For each
    neighbor_cell in the inner loop, check whether the cell has not been visited
    and is passable. If so, update the visited grid and the boundary queue as
    specified. In this case, also update the neighbor's distance to be the distance
    to current_cell plus one: distance_field[current_cell[0]][current_cell[1]] + 1.
    
This method computes distances in exactly the order that the wildfire spreads. when
a neighbor_cell is added to the queue, the neighbor's distance from a start position
is just the distance to the cell current_cell plus the one step to the neighbor.
Working from the outline above, your task in phase two is to implement the method
compute_distance_field as specified below:
* comptue_distance_field(self, entity_type): This method returns a 2D distance field
    computed using the four-way distance of entities of the given type (either ZOMBIE
    or HUMAN). Note that entries of the computed distance fields should be zero at the
    entities in the specified list. Non-zero distances should be computed using the
    shortest path computation based on BFS. These shortest paths should avoid
    impassable cells.
    
Finally, if you are having trouble converting our English description into Python, 
remember that the update_boundary() method from the WildFireDemo implements
one step of BFS.

Phase Three
----------
In phase three, your task is to implement two final methods that update the positions
of the zombies and humans, respectively.
* move_humans(self, zombie_distance_field): This method updates the entries in the
    human list to model humans avoiding zombies. Each human either stays in its 
    current cell or moves to a neighboring cell to maximize its distance from the
    zombies. Specifically, humans move to a cell that maximizes their distance from the
    zombies according to the supplied zombie_distance_field. In the case where several
    cells share the same maximal distance, we recommend choosing among these cells
    at random.
* move_zombies(self, human_distance_field): This method updates the entries in the
    zombie list to model zombies chasing humans. Each zombie either stays in its current
    cell or moves to a neighboring cell to minimize its distance to the humans. It 
    uses the human_distance_field passed to this method to compute best move. Choose
    the best move at random if several moves share the same maximal value.
    
Once you have successfully implemented the three methods in phase two and three,
the buttons in the GUI "Zombies stalk" and "Humans flee" should work. Zombies should
stalk humans and humans should flee zombies. We encourage you to spend some time
testing/experimenting with the simulation using our GUI. Once your code works, submit
it to Owltest for grading.

Just for fun! Observations from the simulation
----------
At a distance, zombies are quite good at finding humans (even ones hiding in 
buildings) since breadth-first search always searches the interiors of buildings 
(provided there is an entrance). The human distance field decreases steadily and 
always reaches zero at a delicious human brain. Humans, on the other hand, aren't 
so smart while fleeing since they greedily maximize the local distance away from the 
nearest zombies on each step. As a result, humans often run to the nearest corner 
of a building and cower as the zombies approach. (Hey, this is a pretty realistic 
simulation!)

However, in close quarters, humans have a large advantage since they can move 
diagonally. Unless cornered by multiple zombies, humans can easily out-maneuver a 
single zombie and avoid having their brains eaten. For packs of zombies inhabiting a 
single cell, the strategy for breaking ties in move_zombies is important. When the 
pack has a choice between moving to two neighboring cells that minimize distance, 
always choosing the one cell or the other causes the zombies to stay in clumped in a 
single cell. Having each zombie choose between the two cells at random causes the 
pack to tend to disperse.

This situation arises when the pack is chasing a human that is fleeing diagonally (say 
down and left). There are two directions (down or left) that are available to the 
zombies that minimize the distance to the human. Instead of having all of the zombies 
move in the same direction, each zombie should choose one of the two optimal 
directions randomly. With the random approach, some zombies go down and some 
zombies go left and the pack of zombies tends to spread out. This behavior makes 
the zombies more likely to catch the human when he/she ends up huddled in a corner.

There are several other interesting scenarios in the simulation that we will let you 
explore on your own. For example, you might consider creating a "zombie-proof" 
building that exploits the human's ability to move diagonally between obstacles. 
Feel free to post interesting scenarios that you discover in the forum. So, have 
fun and enjoy some "Brains!"
'''

##=================================================================

## From the template poc_zombie_template. References to "poc_XX" modules removed
## as all code is provided in this doc. This template includes global constants, a 
## completed __init__() method, and stubs for the remaining methods implemented for
## this assignment. Methods will be upated with code as the assignment is completed.

"""
Student portion of Zombie Apocalypse mini-project
"""

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7

class Apocalypse(Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        Grid.clear(self)
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        # Initialize a new grid and a 2D list in which to store the distance field.
        visited = Grid(self.get_grid_height(), self.get_grid_width())
        distance_field = [[self.get_grid_height() * self.get_grid_width() 
                          for dummy_col in range(self.get_grid_width())] 
                          for dummy_row in range(self.get_grid_height())]
        
        # Create an instance of Queue for the boundary, which is the list of entities.
        boundary = Queue()
        if entity_type == HUMAN:
            for human in self.humans():
                boundary.enqueue(human)
        elif entity_type == ZOMBIE:
            for zombie in self.zombies():
                boundary.enqueue(zombie)
        else:
            print "Invalid entry"
        
        # For each cell in the queue, set visited to full and distance field entry to 0.
        for cell in boundary:
            visited.set_full(cell[0], cell[1])
            distance_field[cell[0]][cell[1]] = 0
        
        # BFS based on pseudocode from class.
        while len(boundary) > 0:
            cell = boundary.dequeue()
            neighbors = self.four_neighbors(cell[0], cell[1])
            for neighbor in neighbors:
                if self.is_empty(neighbor[0], neighbor[1]):
                    if visited.is_empty(neighbor[0], neighbor[1]):
                        visited.set_full(neighbor[0], neighbor[1])
                        boundary.enqueue(neighbor)
                        if distance_field[cell[0]][cell[1]] + \
                        1 < distance_field[neighbor[0]][neighbor[1]]:
                            distance_field[neighbor[0]][neighbor[1]] = \
                            distance_field[cell[0]][cell[1]] + 1
                        
        return distance_field
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        # Queue up humans and identify value of obstacles.
        people = Queue()
        for human in self.humans():
            people.enqueue(human)
        blocked_cell = self.get_grid_height() * self.get_grid_width()
        
        while len(people) > 0:
            brain = people.dequeue()
            moves = self.eight_neighbors(brain[0], brain[1])
            move_scores = {}
            
            for move in moves:
                score = zombie_distance_field[move[0]][move[1]]
                if score != blocked_cell and score != 0:
                    move_scores[move] = score
                    
            # Check for no possible moves.
            if len(move_scores) == 0:
                continue
                
            # Randomly choose move from best move(s), update brain.
            best_moves = []
            for key, value in move_scores.items():
                if value == sorted(move_scores.values(), reverse = True)[0]:
                    best_moves.append(key)
            best_move = random.choice(best_moves)
            self._human_list[self._human_list.index(brain)] = \
            (best_move[0], best_move[1])
                    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        horde = Queue()
        for zombie in self.zombies():
            horde.enqueue(zombie)
        blocked_cell = self.get_grid_height() * self.get_grid_width()
        
        while len(horde) > 0:
            zed = horde.dequeue()
            
            # Check if zed is already eating brains; if so, skip iteration.
            if human_distance_field[zed[0]][zed[1]] == 0:
                continue
            
            moves = self.four_neighbors(zed[0], zed[1])
            move_scores = {}
            for move in moves:
                score = human_distance_field[move[0]][move[1]]
                if score != blocked_cell:
                    move_scores[move] = score
                    
            # Check for no possible moves.
            if len(move_scores) == 0:
                continue
                
            # Randomly choose move from best move(s), update zed.
            best_moves = []
            for key, value in move_scores.items():
                if value == sorted(move_scores.values())[0]:
                    best_moves.append(key)
            best_move = random.choice(best_moves)
            self._zombie_list[self._zombie_list.index(zed)] = \
            (best_move[0], best_move[1])

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

# run_gui(Apocalypse(30, 40))

##=================================================================

# Phase One

# The seven basic methods will be implemented first. The template is above; it will
# be filled in as methods are developed and verified as successful. These are very
# simple and require very little discussion, with the exception of clear. Since the
# Grid class is initialized in the __init__ for subclass Apocalypse, the sub has access
# to the methods of the superclass. Call Grid.clear(self) to set all cells in the grid
# to empty, but don't forget to empty the zombie and human lists.

def clear(self):
    """
    Set cells in obstacle grid to be empty
    Reset zombie and human lists to be empty
    """
    Grid.clear(self)
    self._zombie_list = []
    self._human_list = []
    
def add_zombie(self, row, col):
    """
    Add zombie to the zombie list
    """
    self._zombie_list.append((row, col))
            
def num_zombies(self):
    """
    Return number of zombies
    """
    return len(self._zombie_list)
      
def zombies(self):
    """
    Generator that yields the zombies in the order they were
    added.
    """
    for zombie in self._zombie_list:
        yield zombie

def add_human(self, row, col):
    """
    Add human to the human list
    """
    self._human_list.append((row, col))
    
def num_humans(self):
    """
    Return number of humans
    """
    return len(self._human_list)

def humans(self):
    """
    Generator that yields the humans in the order they were added.
    """
    for human in self._human_list:
        yield human
        
# Initialize an instance of Apocalypse and test the methods. Uncomment to run.

# obstacles = [(1,1), (2,2), (3,3), (4,4), (5,5)]
# zombies = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5)]
# humans = [(5,0), (5,1), (5,2), (5,3), (5,4)]
# my_apoc = Apocalypse(6, 6, obstacles, zombies, humans)
# print my_apoc
# print "-"*10

# print my_apoc.zombies()
# for zombie in my_apoc.zombies():
    # print zombie
# print "Zombies:", my_apoc.num_zombies()
# my_apoc.add_zombie(2,0)
# my_apoc.add_zombie(2,1)
# for zombie in my_apoc.zombies():
    # print zombie
# print "Zombies:", my_apoc.num_zombies()
# print "-"*10

# print my_apoc.humans()
# for human in my_apoc.humans():
    # print human
# print "Humans:", my_apoc.num_humans()
# my_apoc.add_human(4,1)
# my_apoc.add_human(4,2)
# my_apoc.add_human(4,3)
# for human in my_apoc.humans():
    # print human
# print "Humans:", my_apoc.num_humans()
# print "-"*10

# my_apoc.clear()
# print my_apoc
# print my_apoc.zombies()
# for zombie in my_apoc.zombies():
    # print zombie
# print "Zombies:", my_apoc.num_zombies()
# print my_apoc.humans()
# for human in my_apoc.humans():
    # print human
# print "Humans:", my_apoc.num_humans()

# All tests were successful. 

##=================================================================

# Phase Two

# The compute_distance_field method takes an entity_type, either zombie or human.
# The resulting distance field treats the entity as a zero and must draw a path, using
# the four neighbors of each cell, from those entities. The BFS pseudocode is a
# reference point from which to implement this function. The directions are clear
# as well on how to proceed.

# First initialize an instance of the Grid class with the same dimensions as the
# original grid. Use the get methods for height and width values. Create the 2D
# list distance field and set each entry to be height x width. This is the list that
# will be filled in and returned.

# Create the queue "boundary" that is a copy of the zombie or human list, depending
# on which is the entity. Use a conditional to determine which to reference. Use an
# instance of the Queue class here as FIFO will need to be followed when iterating
# over entities in the boundary. For each entity, set the cell in the Grid instance 
# "visited" to full (as they have been visited), and in the distance field set
# these entries to zero (as they are the origin points for the paths). 

# Implement BFS. The boundary not being empty is simply len(boundary) > 0. Use
# a while loop, as stated. Initialize a current cell to a dequeued boundary element.
# Compute its neighbors using the self.four_neighbors(cell[0], cell[1]) call. Iterate
# through the neighbors first checking if the cell is empty, then if the cell in
# the visited grid is empty. If both return True, set that cell in the visited grid 
# to full (as it has just been visited) and add it to the boundary queue (as it is
# now a boundary, the neighbors of which must be searched). Finally, update the
# distance field to be the cell value + 1, but first check to make sure that this
# value is less than what is currently in the distance field entry. These entries
# begin at h x w so that every value will evaluate to being less than that value;
# however, if a neighbor of this cell has already evaluated it and it is given a
# smaller value (i.e. there is a closer entity to it influencing the value), then
# the lesser value remains in the entry.

def compute_distance_field(self, entity_type):
    """
    Function computes and returns a 2D distance field
    Distance at member of entity_list is zero
    Shortest paths avoid obstacles and use four-way distances
    """
    # Initialize a new grid and a 2D list in which to store the distance field.
    visited = Grid(self.get_grid_height(), self.get_grid_width())
    distance_field = [[self.get_grid_height() * self.get_grid_width() 
                      for dummy_col in range(self.get_grid_width())] 
                      for dummy_row in range(self.get_grid_height())]
    
    # Create an instance of Queue for the boundary, which is the list of entities.
    boundary = Queue()
    if entity_type == HUMAN:
        for human in self.humans():
            boundary.enqueue(human)
    elif entity_type == ZOMBIE:
        for zombie in self.zombies():
            boundary.enqueue(zombie)
    else:
        print "Invalid entry"
    
    # For each cell in the queue, set visited to full and distance field entry to 0.
    for cell in boundary:
        visited.set_full(cell[0], cell[1])
        distance_field[cell[0]][cell[1]] = 0
    
    # BFS based on pseudocode from class.
    while len(boundary) > 0:
        cell = boundary.dequeue()
        neighbors = self.four_neighbors(cell[0], cell[1])
        for neighbor in neighbors:
            if self.is_empty(neighbor[0], neighbor[1]):
                if visited.is_empty(neighbor[0], neighbor[1]):
                    visited.set_full(neighbor[0], neighbor[1])
                    boundary.enqueue(neighbor)
                    if distance_field[cell[0]][cell[1]] + \
                    1 < distance_field[neighbor[0]][neighbor[1]]:
                        distance_field[neighbor[0]][neighbor[1]] = \
                        distance_field[cell[0]][cell[1]] + 1
                    
    return distance_field

# Initialize the same game as in Phase One and print the distance field for each
# zombies and humans, then cross reference with the two lists of either entity.
# Uncomment all relevant code blocks to run.

# print "Basic testing"
# obstacles = [(1,1), (2,2), (3,3), (4,4), (5,5)]
# zombies = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5)]
# humans = [(5,0), (5,1), (5,2), (5,3), (5,4)]
# my_apoc = Apocalypse(6, 6, obstacles, zombies, humans)
# print my_apoc

# print "Zombies"
# for zombie in my_apoc.zombies(): print zombie
# print "Humans"
# for human in my_apoc.humans(): print human
# print "-"*10

# print "Human Distance Field"
# for item in my_apoc.compute_distance_field(HUMAN): print item
# print "Zombie Distance Field"
# for item in my_apoc.compute_distance_field(ZOMBIE): print item
# print "-"*10
# print "\n"

# The distance fields show 0 values for an entity and 36 (h x w) for obstacles.
# The example above lists zombies and humans across from each other in opposite 
# edges, top and bottom. A diagonal line bisects the grid, with only (0,0) allowing
# passage for a four-neighbor move (and distance field computation). It seems that
# with a zombie blocking (0,0), there are values less than 36 computed for the
# dead ends around the diagonal obstacle line. I will do two things with this next 
# test: remove zombies from the passage so that there are no 0 values blocking
# the path from zombie to human. I will also create an obstacle circle to see what
# is computed for the value in its center.

# print "Obstacles enclosing cells"
# obstacles = [(2,1), (2,2), (2,3), (3,1), (3,3), (4,1), (4,2), (4,3)]
# my_apoc = Apocalypse(6, 6, obstacles, zombies, humans)
# print "Human Distance Field"
# for item in my_apoc.compute_distance_field(HUMAN): print item
# print "Zombie Distance Field"
# for item in my_apoc.compute_distance_field(ZOMBIE): print item
# print "-"*10
# print "\n"

# The enclosed cells do not get touched by the BFS, which is expected. The
# distance fields are much more accurate without blockage. One more round
# of tests: how does this react when you place human and zombie on the same
# cell, human and obstacle on the same cell, and zombie and obstacle on the same
# cell. The first probably does nothing as that game config is expected, the latter two
# should act in the same way.

# print "Zombie on top of human"
# obstacles = [(2,2)]
# zombies = [(0,0)]
# humans = [(0,0), (0,1)]
# my_apoc = Apocalypse(3,3, obstacles, zombies, humans)
# print "Human Distance Field"
# for item in my_apoc.compute_distance_field(HUMAN): print item
# print "Zombie Distance Field"
# for item in my_apoc.compute_distance_field(ZOMBIE): print item
# print "-"*10
# print "\n"

# When a zombie and human are on top of one another, the distance field does not
# take this into account. It simply zeros the entities and counts moving away from
# them. The decision to move or not (e.g. if you are a zombie already eating those
# sweet human brains) is probably to be governed by the move function below.

# print "Obstacle on top of human and zombie"
# obstacles = [(0,0)]
# my_apoc = Apocalypse(3,3, obstacles, zombies, humans)
# print my_apoc
# print "Human Distance Field"
# for item in my_apoc.compute_distance_field(HUMAN): print item
# print "Zombie Distance Field"
# for item in my_apoc.compute_distance_field(ZOMBIE): print item
# print "-"*10
# print "\n"

# The distance field does not react to an obstacle on a human on a zombie, either.
# that's unsurprising, as the entity is considered the origin anyway, and that cell
# becomes a zero. I try one example with the obstacle on the human but not
# on the zombie. 

# print "Obstacle on top of human NOT zombie"
# obstacles = [(1,1)]
# zombies = [(2,2)]
# humans = [(1,1)]
# my_apoc = Apocalypse(3,3, obstacles, zombies, humans)
# print my_apoc
# print "Human Distance Field"
# for item in my_apoc.compute_distance_field(HUMAN): print item
# print "Zombie Distance Field"
# for item in my_apoc.compute_distance_field(ZOMBIE): print item
# print "-"*10
# print "\n"

# In the human distance field, the human became zero and the rest of the cells
# were numbered going away from it. In the zombie distance field, the human
# finally showed up as a 9 since there was no zombie on it this time. In this
# last test, we'll see what happens when a zombie or human is enclosed within
# an obstacle.

# print "Obstacles enclosing a zombie"
# obstacles = [(2,1), (2,2), (2,3), (2,4), (2,5), (3,1), (3,5), (4,1), (4,2), 
             # (4,3), (4,4), (4,5)]
# zombies = [(3,3)]
# humans = [(0,0)]
# my_apoc = Apocalypse(6,6, obstacles, zombies, humans)
# print my_apoc
# print "Human Distance Field"
# for item in my_apoc.compute_distance_field(HUMAN): print item
# print "Zombie Distance Field"
# for item in my_apoc.compute_distance_field(ZOMBIE): print item
# print "-"*10
# print "\n"

# The human distance field behaved as expected, not able to breach the obstacles
# to get to the 3 empty cells within. The zombie distance field did not breach and
# did not assign a value to any cell outside of its enclosure. Everything seems okay.

##=================================================================

# Phase Three

# The two move functions must compute distance fields for each entity in the entity
# list (human or zombie), then determine the best move based on that field. The
# tied-at-best moves will be chosen from at random. Also remember that humans
# can move in 8 directions, while zombies can only move in 4. Conditionals will 
# have to check for a move being on a zombie (for a human) or on top of an
# obstacle (for either entity) and prohibit those moves. Zombies already eating
# brains do not have to move.

# Move scores will be maintained in a dictionary for easy reference and
# updating. If there are no moves to make, the dictionary will not be updated,
# and so there are no moves to be made. The loop must continue (operative
# word) to the next entity in the list and compute move scores for that one.

def move_humans(self, zombie_distance_field):
    """
    Function that moves humans away from zombies, diagonal moves
    are allowed
    """
    # Queue up humans and identify value of obstacles.
    people = Queue()
    for human in self.humans():
        people.enqueue(human)
    blocked_cell = self.get_grid_height() * self.get_grid_width()
    
    while len(people) > 0:
        brain = people.dequeue()
        moves = self.eight_neighbors(brain[0], brain[1])
        move_scores = {}
        
        for move in moves:
            score = zombie_distance_field[move[0]][move[1]]
            if score != blocked_cell and score != 0:
                move_scores[move] = score
                
        # Check for no possible moves.
        if len(move_scores) == 0:
            continue
            
        # Randomly choose move from best move(s), update brain.
        best_moves = []
        for key, value in move_scores.items():
            if value == sorted(move_scores.values(), reverse = True)[0]:
                best_moves.append(key)
        best_move = random.choice(best_moves)
        self._human_list[self._human_list.index(brain)] = \
        (best_move[0], best_move[1])
                
def move_zombies(self, human_distance_field):
    """
    Function that moves zombies towards humans, no diagonal moves
    are allowed
    """
    horde = Queue()
    for zombie in self.zombies():
        horde.enqueue(zombie)
    blocked_cell = self.get_grid_height() * self.get_grid_width()
    
    while len(horde) > 0:
        zed = horde.dequeue()
        
        # Check if zed is already eating brains; if so, skip iteration.
        if human_distance_field[zed[0]][zed[1]] == 0:
            continue
        
        moves = self.four_neighbors(zed[0], zed[1])
        move_scores = {}
        for move in moves:
            score = human_distance_field[move[0]][move[1]]
            if score != blocked_cell:
                move_scores[move] = score
                
        # Check for no possible moves.
        if len(move_scores) == 0:
            continue
            
        # Randomly choose move from best move(s), update zed.
        best_moves = []
        for key, value in move_scores.items():
            if value == sorted(move_scores.values())[0]:
                best_moves.append(key)
        best_move = random.choice(best_moves)
        self._zombie_list[self._zombie_list.index(zed)] = \
        (best_move[0], best_move[1])
        
# Start up gui for simulation and test it out. Uncomment to run.

obstacles = [(10,10), (11,11), (12,12), (12,15), (12,16)]
zombies = [(0,0), (0,3), (0,17), (5,17), (6,4)]
humans = [(4, 18), (5,18), (6,18)]
run_gui(Apocalypse(20, 20, obstacles, zombies, humans))

# I made one error: in the conditional checking value == sorted(move_scores.values()),
# I set reverse = True and looked at the value at index 0, which is the highest score. 
# I always returned moves for the zombies that maximized the score instead of minimizing
# it, which caused them to run away from the humans instead of pursuing them. After
# fixing this, the code seemed to run just fine.

##=================================================================

# Testing Grounds

# I want to implement my own function to run the sim. Instead of relying on manually
# moving the zombies and humans, I want to make moves every second for each one,
# first the zombies, then the humans. I will add a timer to the GUI code that
# executes the flee and stalk code automatically. I'll add another button to execute
# this new feature.

# The per-second speed is too slow. I modified the timer to update every 300 ms.

# It's pretty cool. Some future updates might be to have a human compute whether
# or not the four neighbors around it are filled with obstacles, in which case it is
# in his/her best interest to stay put. Humans that overlap with zombies (and are
# essentially feasted upon) could turn into zombies. The former feature would be
# simple to implement, but the latter requires some thought.

# Before each human move, a check the zombie distance field could check for all
# zero values. If one is found in a cell that corresponds to the human's current
# position, that human would be removed from self._humans and a new zombie
# added via the relevant method. Though the humans and zombies are enqueued
# into and dequeued from a completely new queue when distances are computed,
# moves are updated by finding that specific entity in the queue and changing it
# (specifically, changing its tuple to a different tuple). Removing a human this way
# would change the list and normally could screw up an iteration through the list,
# but because a separate list is being iterated through to compute distances,
# amending this original list of humans might be possible. 
    
##=================================================================
##=================================================================