"""
Rice University / Coursera: Principles of Computing (Part 2)
Week 1: Homework 1
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

#-----------------------------------------------------------------
## Provided code for sorting strings.

"""
Sorting a list of strings using an alphabetical grid
"""

# constants
NUM_CHARS = 26
CHARACTERS = [chr(ord("a") + char_num) for char_num in range(NUM_CHARS)] 


def order_by_letter(string_list, letter_pos):
    """
    Takes a list of strings and order them alphabetically 
    using the letter at the specified position
    """
    buckets = [[] for dummy_idx in range(NUM_CHARS)]
    for string in string_list:
        char_index = ord(string[letter_pos]) - ord("a")
        buckets[char_index] += [string]
       
    answer = []
    for char_index in range(NUM_CHARS):
        answer += buckets[char_index]
    ## Alternative syntax for the above 2 lines:
    # for item in buckets:
        # answer.extend(item)
    return answer

def string_sort(string_list, length):
    """
    Order a list of strings of the specific length in ascending alphabetical order
    """
    for position in range(length -1 , -1, -1):
        string_list = order_by_letter(string_list, position)
    return string_list

def run_example():
    """
    Example of string sort
    """
    string_length = 3
    test_list = ["".join([random.choice(CHARACTERS) for _ in range(string_length)]) 
                 for dummy_index in range(50)]
    print "Unsorted string list is", test_list
    print "Sorted string list is", string_sort(test_list, string_length)
     
#run_example()

#-----------------------------------------------------------------
## Provided implementation of Grid class (poc_grid).

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
## Provided poc_wildfire_gui for WildFire demo, includes run_gui function.

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
## Provided code for Queue class, modified for question 10.

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
        # Uncomment next line and comment out modded line to use original method.
        # self._items.append(item)
        
        #--------------------------------------------------
        # Modification to mirror Stack's push method.
        self._items.insert(0, item)
        #--------------------------------------------------

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
## Provided code for WildFire class with module references removed.

"""
Simulation of wild fire using breadth first search (BFS)
Click in the canvas to add cells to the boundary of the fire
"""

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

#-----------------------------------------------------------------
## Provided Stack class. Original return statements commented out.
## My implementation of each method shown under original statements.

"""
Stack class
"""

class Stack:
    """
    A simple implementation of a FILO stack.
    """
    def __init__(self):
        """ 
        Initialize the stack.
        """
        #pass
        self._items = []

    def __len__(self):
        """
        Return number of items in the stack.
        """
        #return 0
        return len(self._items)

    def __str__(self):
        """
        Returns a string representation of the stack.
        """
        #return ""
        return str(self._items)

    def push(self, item):
        """
        Push item onto the stack.
        """        
        #pass
        self._items.insert(0, item)

    def pop(self):
        """
        Pop an item off of the stack
        """
        #return 0
        return self._items.pop(0)

    def clear(self):
        """
        Remove all items from the stack.
        """
        #pass
        self._items = []

##=================================================================

def hw_101():
    """
    QUESTION 1: Growth of functions
    
    Review the math notes on the growth of functions (https://class.coursera.org/
    principlescomputing2-004/wiki/view?page=fun_growth). Which of the following
    functions grows at the same rate as (1/2)*n**2 - 5*n + 20?
    
    Option 1
    n
    
    Option 2
    n**3
    
    Option 3
    n*log(n)
    
    Option 4
    n**2
    """
    # Knowing from asymptotic analysis of algorithms that quadratic expressions
    # will be affected most by the highest order term as n approaches INF, you
    # can reduce the problem's expression to n**2, which is option 4.
    
    answer = "n**2"
    
    print "Question 101 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_101()

##=================================================================

def hw_102():
    """
    QUESTION 2
    
    Many algorithms for sorting a list of numbers use comparisons (like greater
    than or less than) to determine the sorted order of the list. The problem of
    building fast sorting algorithms using comparisons is well-studied. In fact,
    we will consider a very elegant sorting algorithm of this type next week.
    
    The fastest algms for sorting a list of size n share a bound (specified as a
    simple expression in n) for minimal number of comparisons required to sort
    any list of length n. Use a web search engine to look up this estimate and
    select the answer below that grows at the same rate as this expression.
    """
    # A quick lookup showed that n*log(n) comparisons is the correct answer.
    # Comparison sorts require some multiple of that expression to sort a list.
    
    answer = "n*log(n)"
    
    print "Question 102 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_102()

##=================================================================

def hw_103():
    """
    QUESTION 3
    
    Review this week's practice activity on sorting strings (in shared area above).
    The activity discusses a grid-based method for sorting strings that does not
    require comparisons. Given a list of n three-letter words, which expression
    grows at the same rate as the number of statements executed during this sort?
    
    Option 1
    n*log(n)
    
    Option 2
    n
    
    Option 3
    log(n)
    
    Option 4
    n**2
    """
    # The string sorting function provided appears to be linearly dependent on the
    # number of words in the list. The order_by_letter for loop that iterates through
    # the string list is affected by this increase, and its statements both occur at
    # a constant time (two assignments). With each new string in the list, there
    # would be two more statements executed. 
    
    answer = "n"
    
    print "Question 103 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_103()

##=================================================================

def hw_104():
    """
    QUESTION 4: Stacks and queues
    
    Consider a stack in which we have performed n pushes followed by n pops.
    Which of the following are true statements concerning this sequence of ops?
    
    Option 1
    The first element pushed onto the stack is the first element popped off.
    
    Option 2
    The last element pushed onto the stack is the last element popped off.
    
    Option 3
    The first element pushed onto the stack is the last element popped off.

    Option 4
    The last element pushed onto the stack is the first element popped off.
    """
    # A stack is not FIFO, instead it adds to the top and takes from the top.
    # Knowing this, options 3-4 are correct.
    
    answer = "The first elem pushed onto the stack is the last elem popped off."
    answer += "\n"
    answer += "The last elem pushed onto the stack is the first elem popped off."
    
    print "Question 104 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_104()

##=================================================================

def hw_105():
    """
    QUESTION 5
    
    Consider a queue in which we have performed n enqueues followed by n dequeues.
    Which of the following are true statements concerning this sequence of ops?
    
    Option 1
    The first element enqueued into the queue is the last element dequeued out.
    
    Option 2
    The last element enqueued into the queue is the last element dequeued out.
    
    Option 3
    The last element enqueued into the queue is the first element dequeued out.
    
    Option 4
    The first element enqueued into the queue is the first element dequeued out.
    """
    # A queue is FIFO (and LILO). Knowing that, options 2 and 4 are correct.
    
    answer = "The last elem enqueued is the last elem dequeued."
    answer += "\n"
    answer = "The first elem enqueued is the first elem dequeued."
    
    print "Question 105 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_105()

##=================================================================

def hw_106():
    """
    QUESTION 6: 2D grids
    
    Review the provided Grid class (above). In this implementation, the methods
    four_neighbors and eight_neighbors treat the boundaries of the grid as being
    impassable.
    
    An alternative approach is to treat cells with the same row index on the left
    and right boundaries as being adjacent and cells with the same column index
    on the top and bottom boundaries as being adjacent. The thick lines in the 
    figure below (on HW site, not found here) indicate that the cells (1, 0) and 
    (1, 8) are horizontally adjacent, while the cells (0, 6) and (5, 6) are vertically
    adjacent.
    
    Which of the following code fragments correctly computes four_neighbors
    when the top/bottom rows and left/right columns are treated as adjacent?
    
    Option 1
    up = (row - 1) % self._grid_height
    down = (row + 1) % self._grid_height
    left = (col - 1) % self._grid_width
    right = (col + 1) % self._grid_width
    return [[up, col], [down, col], [row, left], [row, right]]
    
    Option 2
    up = (row - 1) % (self._grid_height - 1)
    down = (row + 1) % (self._grid_height - 1)
    left = (col - 1) % (self._grid_width - 1)
    right = (col + 1) % (self._grid_width - 1)
    return [[up, col], [down, col], [row, left], [row, right]]  
    
    Option 3
    up = (row - 1) % (self._grid_height + 1)
    down = (row + 1) % (self._grid_height + 1)
    left = (col - 1) % (self._grid_width + 1)
    right = (col + 1) % (self._grid_width + 1)
    return [[up, col], [down, col], [row, left], [row, right]]  
    
    Option 4
    up = (row - 1) % self._grid_width
    down = (row + 1) % self._grid_width
    left = (col - 1) % self._grid_height
    right = (col + 1) % self._grid_height
    return [[up, col], [down, col], [row, left], [row, right]]
    """
    # Options 2 and 3 can be disregarded off the bat because we want to use the
    # modulo operation on the height/width, not on those values plus or minus 1.
    # Option 3 is out because rows correspond to grid height (e.g. 4 rows means
    # a grid height of 4), and this option swaps height and width in the expressions.
    # Option 1 is left, and is clearly correct.
    
    answer = "up = (row - 1) % self._grid_height" + "\n"
    answer += "down = (row + 1) % self._grid_height" + "\n"
    answer += "left = (col - 1) % self._grid_width" + "\n"
    answer += "right = (col + 1) % self._grid_width" + "\n"
    answer += "return [[up, col], [down, col], [row, left], [row, right]]"
    
    print "Question 106 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_106()

##=================================================================

def hw_107():
    """
    QUESTION 7: Breadth first search
    
    Consider the wildfire demo provided (above) from lecture. Which line in the 
    implementation of update_boundary checks whether the fire can spread to an
    unburned cell?
    
    Option 1
    neighbors = self.four_neighbors(cell_index[0], cell_index[1])
    
    Option 2
    if self.is_empty(neighbor[0], neighbor[1]):
    
    Option 3
    for neighbor in neighbors:
    
    Option 4
    self.set_full(neighbor[0], neighbor[1])
    """
    # The key word here is "check", regardless of what it checks for, and all
    # options but 2 do not check for anything. Option 1 is an assignment, and
    # option 3 is a for loop. Option 4 could be tricky since it is a function call
    # that may or may not perform a check, but a quick look at the Grid.set_full
    # method shows a simple assignment with no check.
    
    answer = "if self.is_empty(neighbor[0], neighbor[1]):"
    
    print "Question 107 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_107()

##=================================================================

def hw_108():
    """
    QUESTION 8
    
    Consider the case in which one steps through the entire breadth first search
    of the grid in the wildfire demonstration. Which of the following expressions
    grows at the same rate as the number of statements executed during the
    breadth first search? Assume the grid has size m-by-n. 
    
    Option 1
    m*n
    
    Option 2
    m + n
    
    Option 3
    m**2 * n**2
    
    Option 4
    2**(m+n)
    """
    # In the WildFire class/demo, the fire slowly overtakes every single cell in
    # the grid with each BFS step. There is no indication that other factors affect
    # the number of statements executed as significantly as grid size.
    
    answer = "m * n"
    
    print "Question 108 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_108()

##=================================================================

def hw_109():
    """
    QUESTION 9
    
    Complete the implementation of the Stack class provided above. Once complete,
    uncomment the test code (provided in this question instead of at the end of the
    above code) and enter the number printed out.
    """
    # My implementation is above, in the shared area. The "pass" statements originally
    # in the Stack class template were commented out.
    
    # Test code from the provided Stack class module.
    my_stack = Stack()
    my_stack.push(72)
    my_stack.push(59)
    my_stack.push(33)
    my_stack.pop()
    my_stack.push(77)
    my_stack.push(13)
    my_stack.push(22)
    my_stack.push(45)
    my_stack.pop()
    my_stack.pop()
    my_stack.push(22)
    my_stack.push(72)
    my_stack.pop()
    my_stack.push(90)
    my_stack.push(67)
    while len(my_stack) > 4:
        my_stack.pop()
    my_stack.push(32)
    my_stack.push(14)
    my_stack.pop()
    my_stack.push(65)
    my_stack.push(87)
    my_stack.pop()
    my_stack.pop()
    my_stack.push(34)
    my_stack.push(38)
    my_stack.push(29)
    my_stack.push(87)
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    # Item stored as var instead of being printed here.
    #print my_stack.pop()
    
    answer = my_stack.pop()
    # 77
    
    print "Question 109 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_109()

##=================================================================

def hw_110():
    """
    QUESTION 10
    
    Take the provided Queue class (above) and modify the enqueue and dequeue
    methods to behave like the push and pop methods for your Stack class.
    
    Save this modded class definition. Take the WildFire demo and import this
    modified definition for the Queue class at the top of the demo code. In
    CodeSkulptor, the modified import statement would have the form:
    import userXX_XXXXX as poc_queue (unnecessary here, all code is in this doc).
    
    Now, run this modified demo and add a single cell in the middle of the canvas
    to the boundary queue prior to starting the search. Which of the images
    correspond to a possible state of the grid during the resulting depth first search?
    """
    # First I will modify the Queue class above so that enqueue mirrors Stack's
    # push method (the dequeue method is the same as Stack's pop method
    # already). Then I will run the WildFire demo from here.
    
    # Uncomment to run
    #run_gui(WildFire(30, 40))
    
    # Running the WildFire GUI showed a horizontal traversal of the grid that
    # reversed its direction once it hit a vertical boundary (0 or grid width). 
    # Once it reached the bottom, it traversed the grid backwards, retracing its
    # path and "consuming" the boundary cells. When it hit the origin, it continued
    # traversing in the same way until it reached the top, the backtracked again.
    
    # Since the images can't be shown here, the answer will simply state which 
    # of the 4 provided images appeared to match behavior exhibited by this program.
    
    answer = "a, b, d"
    
    print "Question 110 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_110()

##=================================================================
##=================================================================