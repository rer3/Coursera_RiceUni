"""
Rice University / Coursera: Principles of Computing (Part 2)
Week 3: Class Notes
Trees
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
## Provided Tree class with run_examples() function:

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
    print "Tree consisting of three nodes", tree_cab
    
    tree_dcabe = Tree("d", [tree_cab, Tree("e", [])])
    print "Tree consisting of five nodes", tree_dcabe
    print 
    
    my_tree = Tree("a", [Tree("b", [Tree("c", []), Tree("d", [])]), 
                         Tree("e", [Tree("f", [Tree("g", [])]), Tree("h", []), Tree("i", [])])])
    print "Tree with nine nodes", my_tree
    
    print "The tree has", my_tree.num_nodes(), "nodes,", 
    print my_tree.num_leaves(), "leaves and height",
    print my_tree.height()
    
    ## Original import statement and function call.
    #import poc_draw_tree
    #poc_draw_tree.TreeDisplay(my_tree)
    
    TreeDisplay(my_tree)
                
# Uncomment to run code
#run_examples()

##=================================================================

# Testing Grounds

def run_my_example():
    """
    Create my tree and apply various methods to it. 
    """
    # My tree should have a height of 6, nodes a through q, and 7 leaves.
    # Node a connects to b, c; b to d, e, f; f to g; g to h; h to i, j; 
    # i to k, l; c to m; m to n; n to o, p; p to q.
    
    # First with all parents and nodes identified as explicit args:
    
    my_tree = Tree("a", [Tree("b", [Tree("d", []), Tree("e", []), 
                        Tree("f", [Tree("g", [Tree("h", [Tree("i", [Tree("k", []),
                        Tree("l", [])]), Tree("j", [])])])])]), Tree("c", [Tree("m",
                        [Tree("n", [Tree("o", []), Tree("p", [Tree("q", [])])])])])])

    #TreeDisplay(my_tree) # Success!
    
    # Now with each leaf assigned to a variable and my_tree built from the
    # ground up. I'll start with leaves, then move to internal nodes up to the root.
    
    t_q, t_o, t_j, t_l, t_k, t_e, t_d = Tree("q", []), Tree("o", []), Tree("j", []), \
                                        Tree("l", []), Tree("k", []), Tree("e", []), Tree("d", [])
    t_i = Tree("i", [t_k, t_l])
    t_h = Tree("h", [t_i, t_j])
    t_g = Tree("g", [t_h])
    t_f = Tree("f", [t_g])
    t_b = Tree("b", [t_d, t_e, t_f])
    t_p = Tree("p", [t_q])
    t_n = Tree("n", [t_o, t_p])
    t_m = Tree("m", [t_n])
    t_c = Tree("c", [t_m])
    my_tree = Tree("a", [t_b, t_c])
    
    #TreeDisplay(my_tree) # Success!
    
    print "The tree has", my_tree.num_nodes(), "nodes,", 
    print my_tree.num_leaves(), "leaves and height",
    print my_tree.height()
    
    # Both representations can become convoluted with enough nodes.
    
run_my_example()

##=================================================================
##=================================================================