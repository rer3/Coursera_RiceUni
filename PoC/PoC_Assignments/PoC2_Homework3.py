"""
Rice University / Coursera: Principles of Computing (Part 2)
Week 3: Homework 3
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
## Provided NodeList class and run_example function:

"""
Recursive class definition for a non-empty list of nodes
"""

# Counter added for Question 2.
COUNT = 0

class NodeList:
    """
    Basic class definition for non-empty lists using recursion
    """
    def __init__(self, val):
        """
        Create a list with one node
        """
        self._value = val
        self._next = None
     
    def append(self, val):
        """
        Append a node to an existing list of nodes
        """
        # Added to increase COUNT:
        global COUNT
        COUNT += 1
            
        if self._next == None:
            new_node = NodeList(val)
            self._next = new_node
        else:
            self._next.append(val)
            
    def __str__(self):
        """
        Build standard string representation for list
        """
        if self._next == None:
            return "[" + str(self._value) + "]"
        else:
            rest_str = str(self._next)
            rest_str = rest_str[1:]
            return "[" + str(self._value) + ", " + rest_str
    

def run_example():
    """
    Create some examples
    """
    node_list = NodeList(2)
    node_list.append(3)
    node_list.append(4)
    print node_list
    
    sub_list = NodeList(5)
    sub_list.append(6)
    
    node_list.append(sub_list)
    print node_list
    
# Commented out as not to change COUNT for Question 2.
#run_example()

#-----------------------------------------------------------------
## Provided poc_draw_tree module for drawing the Tree class.

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
## Provided implementation of Tree class and run_examples function.

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

    
def run_examples():
    """
    Create some trees and apply various methods to these trees
    """
    tree_a = Tree("a", [])
    tree_b = Tree("b", [])
    print "Tree consisting of single leaf node labelled 'a'", tree_a
    print "Tree consisting of single leaf node labelled 'b'", tree_b
    
    tree_cab = Tree("c", [tree_a, tree_b])
    print "Tree consisting of three node", tree_cab
    
    tree_dcabe = Tree("d", [tree_cab, Tree("e", [])])
    print "Tree consisting of five nodes", tree_dcabe
    print 
    
    my_tree = Tree("a", [Tree("b", [Tree("c", []), Tree("d", [])]), 
                         Tree("e", [Tree("f", [Tree("g", [])]), Tree("h", []), Tree("i", [])])])
    print "Tree with nine nodes", my_tree
    
    print "The tree has", my_tree.num_nodes(), "nodes,", 
    print my_tree.num_leaves(), "leaves and height",
    print my_tree.height()

    #TreeDisplay(my_tree)
             
#run_examples()

#-----------------------------------------------------------------
## Provided poc_nav_tree_template with NavTree class and run_examples().
## The code has been modified as poc_tree (Tree class) is not imported here.

class NavTree(Tree):
    """
    Recursive definition for navigable trees plus extra tree methods
    """
    def __init__(self, value, children, parent = None):
        """
        Create a tree whose root has specific value (a string)
        children is a list of references to the roots of the children.  
        parent (if specified) is a reference to the tree's parent node
        """
        Tree.__init__(self, value, children)
        self._parent = parent
        for child in self._children:
            child._parent = self          
    
    def set_parent(self, parent):
        """
        Update parent field
        """
        self._parent = parent
               
    def get_root(self):
        """
        Return the root of the tree
        """
        ## Question 3 answer goes below.
        if self._parent is None:
            return self
        else:
            return self._parent.get_root()

    def depth(self):
        """
        Return the depth of the self with respect to the root of the tree
        """
        ## Question 4 answer goes below
        if self._parent is None:
            return 0
        else:
            return self._parent.depth() + 1
    

def run_examples():
    """
    Create some trees and apply various methods to these trees
    """
    tree_a = NavTree("a", [])
    tree_b = NavTree("b", [])
    tree_cab = NavTree("c", [tree_a, tree_b]) 
    tree_e = NavTree("e", [])
    tree_dcabe = NavTree("d", [tree_cab, tree_e])
    
    print "This is the main tree -", tree_dcabe
    print "This is tree that contains b -", tree_b.get_root()
    
    # Commented out since it is provided in this document.
    #import poc_draw_tree
    TreeDisplay(tree_dcabe)

    print "The node b has depth", tree_b.depth()
    print "The node e has depth", tree_e.depth()
             
#run_examples()

# Expect output

#This is the main tree - [d, [c, [a], [b]], [e]]
#This is tree that contains b - [d, [c, [a], [b]], [e]]
#The node b has depth 2
#The node e has depth 1

#-----------------------------------------------------------------
## Provided poc_arith_expression module. References to poc_tree and poc_draw_tree
## removed as they're provided in this doc. Constants and run_example() included.

"""
Python class definition for creation and 
evaluation of arithmetic expressions
"""

# Use dictionary of lambdas to abstract function definitions

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
    
    TreeDisplay(one_plus_two_times_three)
    print one_plus_two_times_three.evaluate()
    
#run_example()

##=================================================================

def hw_301():
    """
    QUESTION 1: Lists as recursive data structures
    
    In Python, lists are primarily iterative data structures that are processed using
    loops. However, in other languages such as Lisp and Scheme, lists are treated
    primarily as recursive data structures and processed recursively. 
    
    The NodeList class and run_example function provided above defines a class
    NodeList that recursively creates a non-empty list of nodes. Note that a 
    reference to the next node in the list is stored in the _next file of a NodeList
    object. What value is stored in the _next field to signal that there are no more 
    nodes in the list?
    """
    # The self._next field is given a default of None. When a new node is
    # appended to the list, this field referenced a new instance of NodeList
    # with its _value field referencing the node number and its _next field
    # assigned to None. It is clearly the last node as its _next references
    # None instead of another instance of NodeList.
    
    answer = "None"
    
    print "Question 301 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_301()

##=================================================================

def hw_302():
    """
    QUESTION 2
    
    Observe that the method append for the NodeList class is defined recursively.
    Given an existing list of n nodes (created as a NodeList object), how many 
    calls to append are evaluated when appending a new node to the end of the
    list? Count only the calls performed during the process of appending of this
    (n + 1)st node to the list, not those performed during the process of creating
    the original n-node input list.
    
    Enter the answer as a math expression in n below.
    """
    # Write a function that creates increasingly bigger instances of NodeList that
    # update a global counter when adding the (n + 1)st node. Print results in a
    # clear manner so that a series dependent on n can be identified.
    
    global COUNT
    
    nodes = NodeList(0)
    
    for num in range(1, 10):
        start = COUNT
        nodes.append(num)
        end = COUNT
        total = end - start
        print "At addition of", num + 1, "-th node, count change was", total
        print "With COUNT starting at", start, "and ending at", end
        print "-----"
        
    # Adding node 2 increased COUNT by 1. Adding node 3 increased COUNT by 2. 
    # Adding node 4 increased COUNT by 3. And so on until adding node 10 
    # increased COUNT by 9. Given an existing list of n nodes, adding a new node
    # would evaluate n calls to append.
    
    answer = "n"
    
    print "Question 302 Answer:"
    print answer
    print "-"*50
    print "\n"
        
hw_302()

##=================================================================

def hw_303():
    """
    QUESTION 3: Navigating trees
    
    Our implementation (in the shared area above) of the Tree class includes a
    list of references to the subtrees associated with the root node. These 
    references allow Tree methods to recursively traverse the tree downward
    from the root node to its children and then to its children's children and so 
    on.
    
    In some situations, the ability to traverse a tree in the opposite direction
    (upward) is also useful. The provided NavTree class is a subclass of Tree
    that includes a _parent field. Methods in the NavTree class use this field
    to traverse from a node in a given tree to its parent node and so on. Note
    that in this representation, the root node of the given tree has value None
    in its _parent field to indicate that the node has no parent.
    
    Based on the provided code for the NavTree class, which of the following
    implementations of def get_root(self): returns the root of the tree
    containing the subtree referenced by self?
    
    Option 1
    if self._parent is None:
        return self
    else:
        return self._parent.get_root()
        
    Option 2
    if self is None:
        return self
    else:
        return self._parent.get_root()
        
    Option 3
    if self._parent is None:
        return self
    else:
        return get_root(self._parent)
        
    Option 4
    return self._parent.get_root()
    """
    # Option 2 is out because self will not be None.
    # Option 3 is out because the call to get_root() is incorrect.
    # Option 4 is out because None has no attribute get_root().
    
    answer = "if self._parent is None:" + "\n"
    answer += "    return self" + "\n"
    answer += "else:" + "\n"
    answer += "    return self._parent.get_root()"
    
    print "Question 303 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_303()

##=================================================================

def hw_304():
    """
    QUESTION 4
    
    Given a tree, the depth of a node in that tree is the number of edges that
    connect the node to the root of the tree. In the NavTree class provided, the
    nodes "b" and "e" have depths two and one, respectively, in the tree
    tree_dcabe.
    
    Starting from this provided code, which of the following implementations of
    def depth(self): returns the depth of the node referenced by self? Remember
    that the depth should be computed with respect to largest tree that contains
    self.
    
    Option 1
    if self._parent is None:
        return 0
    else:
        return self._parent.depth() + 1
        
    Option 2
    if self._parent is None:
        return 0
    else:
        return self._parent.depth()
        
    Option 3
    if self._parent is None:
        return 0
    else:
        return depth(self._parent)
        
    Option 4
    return self._parent.depth() + 1
    """
    # Option 2 is out because it will only ever return 0.
    # Option 3 is out because the method call is incorrect (and it mirrors option 1).
    # Option 4 is out because None has no attribute depth().
    
    answer = "if self._parent is None:" + "\n"
    answer += "    return 0" + "\n"
    answer += "else:" + "\n"
    answer += "    return self._parent.depth() + 1"
    
    print "Question 304 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_304()

##=================================================================

def hw_305():
    """
    QUESTION 5
    
    As defined in the math notes on trees, a full binary tree is a tree in which
    each internal node has exactly two children. A full binary tree is perfect if
    every leaf in the tree has the same depth.
    
    How many leaves does a perfect binary tree of height n have? Try some 
    examples and look for a simple expression in n that reproduces the values
    generated by the examples. Enter the answer below as an expression in n.
    """
    # Write code to build increasingly larger binary trees and return the number
    # of leaves on each one. These will be in the form of print statements that
    # will be analyzed for a sequence. This tree will be built from the ground up.
    # The tree will be 4 levels stemming from the root, with 16 leaves.
    
    CHARACTERS = [chr(ord("a") + char_num) for char_num in range(26)]
    
    # Create 16 leaves (instances of the Tree class with no children).
    level4_nodes = []   
    for char in CHARACTERS[:16]:
        level4_nodes.append(Tree(char * 4, []))
        
    print "Level 4 Node Height:", level4_nodes[0].height()
    print "Level 4 Node Num Leaves:", level4_nodes[0].num_leaves()
    
    # Create 8 parent nodes for the 16 leaves. Remove the first two nodes from
    # the level4_nodes list and add them as children to each new parent.
    level3_nodes = []
    for char in CHARACTERS[:8]:
        level3_nodes.append(Tree(char * 3, [level4_nodes.pop(), level4_nodes.pop()]))
        
    print "Level 3 Node Height:", level3_nodes[0].height()
    print "Level 3 Node Num Leaves:", level3_nodes[0].num_leaves()
        
    # Repeat with 4 parents, then 2 parents, and then a root node. Use TreeDisplay
    # to visualize the full binary tree and verify a correct configuration.
    
    level2_nodes = []
    for char in CHARACTERS[:4]:
        level2_nodes.append(Tree(char * 2, [level3_nodes.pop(), level3_nodes.pop()]))
        
    print "Level 2 Node Height:", level2_nodes[0].height()
    print "Level 2 Node Num Leaves:", level2_nodes[0].num_leaves()
        
    level1_nodes = []
    for char in CHARACTERS[:2]:
        level1_nodes.append(Tree(char, [level2_nodes.pop(), level2_nodes.pop()]))
        
    print "Level 1 Node Height:", level1_nodes[0].height()
    print "Level 1 Node Num Leaves:", level1_nodes[0].num_leaves()
        
    full_binary = Tree("R", [level1_nodes.pop(), level1_nodes.pop()])
    
    print "Root Node Height:", full_binary.height()
    print "Root Node Num Leaves:", full_binary.num_leaves()
    print "-----"
    
    # Success! A full binary tree is drawn. Uncomment to display tree.
    #TreeDisplay(full_binary)
    
    # Now I will go back through the above code and add statements to print
    # height and num of leaves for the first element in each list (before all elems
    # are popped) since it will be the same for all elems in the list.
    
    # From levels 4 to root, the height: num_leaves associations were:
    # 0: 1, 1: 2, 2: 4, 3: 8, 4: 16. This is a power of 2 series. 2**0 = 1, 
    # 2**1 = 2, 2**2 = 4, etc. Remember that height = n in this case.
    
    answer = "2**n"
    
    print "Question 305 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_305()

##=================================================================

def hw_306():
    """
    QUESTION 6
    
    How many nodes (both internal and leaf) does a perfect binary tree of height
    n have?
    
    To answer this question, you can either try some examples and look for pattern
    in n or convert your answer for question #5 into a sum and use one of the 
    formulas on this page:  (https://class.coursera.org/principlescomputing2-004
    wiki/view?page=arithmetic_sums) to reduce the sum to a single expression
    in n. 
    
    Enter the answer as a math expression in n.
    """
    # A quick look at paper notes shows the following sequence (height: nodes):
    # 0: 1, 1: 3, 2: 7, 3: 15, 4: 31, 5: 63. As n increases by 1, 2**n nodes are
    # added to the tree. The expression must evaluate to 1 at height (n) = 0, and
    # 2**0 = 1, but 2**1 = 2, when we see that at height of 1 the number of
    # nodes is 3, and 2**2 = 4 but at height of 2 we see 7. We must refer to an
    # arithmetic sum. From that link, the sum 2**(n+1) - 1 fits this sequence.
    # At each height, the num nodes is always 1 short of 2**(height + 1).
    
    answer = "2**(n+1) - 1"
    
    print "Question 306 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_306()

##=================================================================

def hw_307():
    """
    QUESTION 7: Applications to genealogy
    
    Trees are extremely important tools for modeling genealogical data. One simple
    example is modeling the descendants of an important individual (let's call him
    "Luay XIV"). The root of the tree is labelled "Luay XIV" and its subtrees 
    correspond to the descendants of the biological children of Luay XIV.
    
    If Luay and his descendants each have a maximum of four children and the
    height of Luay XIV's tree of descendants is three, what is the maximal number
    of descendants in Luay's tree? (Exclude Luay in this count.) Enter the answer
    as a whole number.
    """
    # The tree can be visualized as 3 levels like those described in question 5. At
    # the root you have Luay, level 1 has 4 children, level 2 has 4**2 children,
    # and level 3 has 4**3 children. A very simple mathematical expression can
    # solve this problem. Not counting Luay, you can find it using the general
    # expression (created for much more difficult but similar problems) below:
    
    NUM_OFFSPRING = 4
    TREE_HEIGHT = 3
    DESCENDANTS = 0
    
    # This will only work if every descendant has the same number of children.
    for children in range(1, TREE_HEIGHT + 1):
        DESCENDANTS += NUM_OFFSPRING ** children
    
    answer = DESCENDANTS
    # 84 descendants.
    
    print "Question 307 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_307()

##=================================================================

def hw_308():
    """
    QUESTION 8
    
    Trees can also be used to model the ancestors of an individual (let's call him
    Charles II"). In this model, the role of parent and child is reversed. The root
    of the tree is labelled "Charles II" and has two subtrees corresponding to 
    the ancestors of Charles II's parents. 
    
    Note that ancestor tress are necessarily binary trees. However, the curious
    case of the real-life Charles II (link: http://blogs.discovermagazine.com/gnxp/
    2009/04/inbreeding-the-downfall-of-the-spanish-hapsburgs/#.U78ABpRdVPZ)
    illustrates a complication of modeling genealogical data using trees. This image
    (http://blogs.discovermagazine.com/gnxp/files/777px-Carlos_segundo80.png)
    shows the ancestor tree for Charles II going back several generations. (Charles
    is at the bottom.) Note that his family, the Hapsburgs, suffered from serious
    in-breeding. As a result, Charles II's family tree is not actually a tree, but
    more of a "family graph."
    
    In the case of modeling ancestors, in-breeding violates the condition that
    every node in a tree (but the root) should have a single parent node. In the
    case of Charles II's ancestor tree, several of his ancestors have multiple
    biological children who themselves are ancestors of Charles. 
    
    Note our basic Tree class (above) is fully capable of modeling Charles II's
    ancestors (even in the presence of in-breeding) since there is no check of
    the single-parent condition when an instance of the Tree class is created.
    However, the lack of this check will cause several of the methods for the
    Tree class to possibly return incorrect ancestors. Select the Tree methods
    below that may return an incorrect answer when an instance of the Tree
    class has multiple parents.
    
    Option 1
    num_leaves
    
    Option 2
    children
    
    Option 3
    height
    
    Option 4
    num_nodes
    """
    # Option 4 is the first obvious correct choice, as this assumes nodes are unique.
    # Option 1 is out because leaves are leaves, and internal nodes would be the
    # most affected by this multiple-parent condition.
    # Option 2 is out because the children method simply iterates over the specified
    # children, which would be unaffected by the condition.
    # Option 3 is tricky at first glance, but as it relates (no pun intended) to the
    # parent-child relationship to generate its answer, this seems like another
    # correct choice. I think of an example of a person bearing children with a
    # relative that's two levels up at the grandparents' sibling level. This might skew
    # the height computation enough.
    
    ##################################################
    ## INCORRECT: no note.
    ##
    ## answer = "height, num_nodes"
    ##################################################
    
    # The height method is actually unaffected. In retrospect, this makes sense, 
    # as the largest height is always going to be returned, which accounts for
    # parent-child pathways which would be shorter in cases of in-breeding.
    # The num_leaves method would be affected. This too makes sense, as
    # some leaves may be connected to the same parent.
    
    answer = "num_leaves, num_nodes"
    
    print "Question 308 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_308()

##=================================================================

def hw_309():
    """
    QUESTION 9: Tree traversal
    
    A tree traversal (or tree search) is a recursive method for visiting and
    processing all of the nodes in a tree. In the provided Tree class, the __str__
    method performs a tree traversal to generate a string representation for a
    tree. In particular, this method creates a string representation for the root
    node's associated value and then appends the string representations for each
    subtree (which are recursively computed using the str method) to this string.
    
    Consider a change to the __str__ method in which line 32 
    (ans += str(self._value) is moved after the for loop in lines 34-36 (and the
    commas are repositioned appropriately). In this modified version, the root's
    value is appended to the string representations for the root's sub-trees. Using
    this modified code, what is the string representation for the tree below?
    
    Using the normal Tree string format, it looks like: [d, [c, [a], [b]], [e]]. 
    
    Option 1
    [[[a], [b], c], [e], d]
    
    Option 2
    [d, [c, [a], [b]], [e]]
    
    Option 3
    [[a, b, c], [e], d]
    
    Option 4
    [[[[a, b], c], e], [d]]
    """
    # The cleanest way to solve this problem is to first write the modified version
    # of the Tree class below for use in this problem. The unused methods will be
    # removed from this modified version.
    
    # The described tree would normally be instantiated with the statement below.
    # Modify this to instead create instances of the following TreeMod class.
    
    tree_norm = Tree("d", [Tree("c", [Tree("a", []), Tree("b", [])]), Tree("e", [])])
    
    # Tree class modified as described in the problem:
    
    class TreeMod:
        """
        Modified version of Tree class
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
            
            ## Line 32 used to be here.
     
            for child in self._children:
                ans += str(child)
                ## This comma used to occur prior to the line above.
                ans += ", "
            ## New position of line 32.
            ans += str(self._value)
            return ans + "]"

        def children(self):
            """
            Generator to return children
            """
            for child in self._children:
                yield child
            
            
    tree_mod = TreeMod("d", [TreeMod("c", [TreeMod("a", []), \
                        TreeMod("b", [])]), TreeMod("e", [])])
    
    answer = tree_mod
    # Option 1 is printed: [[[a], [b], c], [e], d]
    
    # I executed this statement and know that Option 1 is the answer. But why?
    # The normal string representation is [d, [c, [a], [b]], [e]], but the modified
    # version is [[[a], [b], c], [e], d]. This actually makes perfect sense, as the
    # original code begins with the root and then appends the children. The mod
    # code begins with the children and appends the root as it returns from
    # recursive calls. 
    
    print "Question 309 Answer:"
    print answer 
    print "-"*50
    print "\n"
    
hw_309()

##=================================================================

def hw_310():
    """
    QUESTION 10
    
    In the case of binary trees, the two subtrees of a node are usually referred to
    as the left subtree and the right subtree. For binary trees, there are 3 common
    types of tree traversals:
    
    *Pre-order traversals - process root, process left subtree, process right sub
    *Post-order traversals - process left sub, process right sub, process root
    *In-order traversals - process left sub, process root, process right sub
    
    Examine the implementation of the __str__ method for the ArithmeticExpression
    class provided. What type of tree traversal does the __str__ method for this
    class implement?
    
    Options 1-4 are the 3 traversals, or 'None of the above'.
    """
    # The method first initializes a variable ans = "(", then appends the string
    # representation of the first child, then the string rep of the _value field
    # which corresponds to the operator (and is the root, here), then the string
    # rep of the second child, and finally a ")" at the end. This appears to be a
    # straightforward implementation of an in-order traversal, as the left sub,
    # then the root, then the right sub is appended to the string.
    
    answer = "In-order traversal"
    
    print "Question 310 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_310()

##=================================================================
##=================================================================