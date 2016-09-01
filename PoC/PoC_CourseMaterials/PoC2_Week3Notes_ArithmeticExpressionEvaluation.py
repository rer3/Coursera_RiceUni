"""
Rice University / Coursera: Principles of Computing (Part 2)
Week 3: Class Notes
Arithmetic Expression Evaluation
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
## Provided TreeDisplay class and constants for drawing tree:

NODE_HEIGHT = 100
NODE_WIDTH = 100

class TreeDisplay:
    """
    Class to display a given tree on the canvas
    """
    def __init__(self, tree):
        """
        Create GUI
        """
        self._tree = tree
        self._canvas_width, self._canvas_height = self.get_box_size(tree)
        self._frame = simplegui.create_frame("Draw a tree", self._canvas_width, self._canvas_height)
        self._frame.set_canvas_background("White")
        self._frame.set_draw_handler(self.draw)
        self._frame.start()
         
    def get_box_size(self, tree):
        """
        Recursive function to compute height and width
        of the bounding box for a tree
        """
        current_subtree_widths = 0
        tree_height = 0
        for child in tree.children():
            child_width, child_height = self.get_box_size(child)
            current_subtree_widths += child_width
            tree_height = max(tree_height, child_height)                            
        subtree_width = max(NODE_WIDTH, current_subtree_widths)
        tree_height = NODE_HEIGHT + tree_height
        return subtree_width, tree_height

    def draw_tree(self, canvas, tree, pos):
        """ 
        Recursively draw a tree on the canvas
        pos is the position of the upper left corner of the bounding box
        """
        # compute horizontal position for left boundary of each subtree
        horiz_boundaries = [pos[0]]
        for child in tree.children():
            child_width, dummy_child_height = self.get_box_size(child)
            horiz_boundaries.append(horiz_boundaries[-1] + child_width)
            
        # draw lines from root to children, must draw first                    
        width = max(NODE_WIDTH, horiz_boundaries[-1] - horiz_boundaries[0])
        root_center = [pos[0] + width / 2, pos[1] + NODE_HEIGHT / 2]
        for idx in range(len(horiz_boundaries) - 1):
            child_center = [(horiz_boundaries[idx] + horiz_boundaries[idx + 1]) / 2, 
                             pos[1] + 3 * NODE_HEIGHT / 2]
            canvas.draw_line(root_center, child_center, 3, "Black")
                       
        # draw root
        canvas.draw_circle(root_center, NODE_HEIGHT / 4, 2, "Black", "LightGreen")
        text_pos = [root_center[0] - NODE_HEIGHT / 12, root_center[1] + NODE_HEIGHT / 12]
        canvas.draw_text(tree.get_value(), text_pos, NODE_HEIGHT / 4, "Black") 

        #draw children
        for child, bndry in zip(tree.children(), horiz_boundaries):
            self.draw_tree(canvas, child, [bndry, pos[1] + NODE_HEIGHT])
        
    def draw(self, canvas):
        """
        Draw handler for tree drawing
        """
        self.draw_tree(canvas, self._tree, [0, 0])

#-----------------------------------------------------------------
## Provided Tree class WITHOUT run_examples() function:

"""
Python definition of basic Tree class

IMPORTANT:  Some class methods assume that instances of the Tree class
always have a single parent (or no parent for the root). See problem #8
on homework #3 for more details.
"""

class Tree:
    """
    Recursive definition for trees plus various tree methods
    """
    def __init__(self, value, children):
        """
        Create a tree whose root has specific value (a string)
        Children is a list of references to the roots of the subtrees.  
        """
        self._value = value
        self._children = children
        
    def __str__(self):
        """
        Generate a string representation of the tree
        Use an pre-order traversal of the tree
        """
        ans = "["
        ans += str(self._value)
                   
        for child in self._children:
            ans += ", "
            ans += str(child)
        return ans + "]"

    def get_value(self):
        """
        Getter for node's value
        """
        return self._value

    def children(self):
        """
        Generator to return children
        """
        for child in self._children:
            yield child
                    
    def num_nodes(self):
        """
        Compute number of nodes in the tree
        """
        ans = 1
        for child in self._children:
            ans += child.num_nodes()
        return ans
    
    def num_leaves(self):
        """
        Count number of leaves in tree
        """
        if len(self._children) == 0:
            return 1
        
        ans = 0
        for child in self._children:
            ans += child.num_leaves()
        return ans

    def height(self):
        """
        Compute height of a tree rooted by self
        """
        height = 0
        for child in self._children:
            height = max(height, child.height() + 1)
        return height

#-----------------------------------------------------------------
## Provided ArtithmeticExpression class and constants with run_example() function:

OPERATORS = {"+" : (lambda x, y : x + y), 
            "-" : (lambda x, y : x - y),
            "*" : (lambda x, y : x * y),
            "/" : (lambda x, y : x / y),
            "//" : (lambda x, y : x // y),
            "%" : (lambda x, y : x % y)}


class ArithmeticExpression(Tree):
    """
    Basic operations on arithmetic expressions
    """
    def __init__(self, value, children, parent = None):
        """
        Create an arithmetic expression as a tree
        """
        Tree.__init__(self, value, children)
        
    def __str__(self):
        """
        Generate a string representation for an arithmetic expression
        """
        if len(self._children) == 0:
            return str(self._value)
        ans = "("
        ans += str(self._children[0])
        ans += str(self._value)
        ans += str(self._children[1])
        ans += ")"
        return ans
        
    def evaluate(self):
        """
        Evaluate the arithmetic expression
        """
        if len(self._children) == 0:
            if "." in self._value:
                return float(self._value)
            else:
                return int(self._value)
        else:
            function = OPERATORS[self._value]
            left_value = self._children[0].evaluate()
            right_value = self._children[1].evaluate()
            return function(left_value, right_value) 


def run_example():
    """
    Create and evaluate some examples of arithmetic expressions
    """
    one = ArithmeticExpression("1", [])
    two = ArithmeticExpression("2", [])
    three = ArithmeticExpression("3", [])
    print one
    print one.evaluate()
    
    one_plus_two = ArithmeticExpression("+", [one, two])
    print one_plus_two
    print one_plus_two.evaluate()
    
    one_plus_two_times_three = ArithmeticExpression("*", [one_plus_two, three])
    print one_plus_two_times_three
    
    ##import poc_draw_tree
    TreeDisplay(one_plus_two_times_three)
    print one_plus_two_times_three.evaluate()
    
#run_example()

##=================================================================

# Testing Grounds

def run_my_example():
    """
    Create and evaluate a lengthy arithmetic expression.
    """
    # I want to create the expression: 4 + 6 * 3 / 2 - 27 * 2.
    # I have to manually identify the components using the standard order of
    # operations: multiply and division > addition and subtraction.
    # I then need to rewrite the expression for use with this class as:
    # 4 + ((6 * 3) / 2) - (27 * 2).
    # These are the components that will be assigned to varialbes to get
    # the correct answer, which is -41.
    
    # Create instances with single integers using ArithmeticExpression class.
    
    two = ArithmeticExpression("2", [])
    three = ArithmeticExpression("3", [])
    four = ArithmeticExpression("4", [])
    six = ArithmeticExpression("6", [])
    twentyseven = ArithmeticExpression("27", [])
    
    # Create instances where those instances in component expressions.
    # These instances will be built in order of operation, and the variable names
    # will be truncated with * = "m", / = "d", + = "a", and - = "s". A leading
    # underscore will be used to allow variable names to begin with numbers.
    
    _6m3 = ArithmeticExpression("*", [six, three])
    _6m3d2 = ArithmeticExpression("/", [_6m3, two])
    _27m2 = ArithmeticExpression("*", [twentyseven, two])
    _4a6m3d2 = ArithmeticExpression("+", [four, _6m3d2])
    answer = ArithmeticExpression("-", [_4a6m3d2, _27m2])
    
    print answer.evaluate()
    TreeDisplay(answer)
    
run_my_example()

##=================================================================
##=================================================================