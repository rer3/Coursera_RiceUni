"""
Rice University / Coursera: Algorithmic Thinking (Part 1)
Application 2-3
"""

'''
In the next three problems, we will consider attack orders in which the 
nodes being removed are chosen based on the structure of the graph. 
A simple rule for these targeted attacks is to always remove a node of
maximum (highest) degree from the graph. The function 
targeted_order(ugraph) in the provided code takes an undirected graph 
ugraph and iteratively does the following:

Computes a node of the maximum degree in ugraph. If multiple nodes 
have the maximum degree, it chooses any of them (arbitrarily).

Removes that node (and its incident edges) from ugraph.

Observe that targeted_order continuously updates ugraph and always 
computes a node of maximum degree with respect to this updated graph. 
The output of targeted_order is a sequence of nodes that can be used as 
input to compute_resilience.

As you examine the code for targeted_order, you feel that the provided 
implementation of targeted_order is not as efficient as possible. In particular, 
much work is being repeated during the location of nodes with the maximum 
degree. In this question, we will consider an alternative method (which we will 
refer to as fast_targeted_order) for computing the same targeted attack order. 
Here is a pseudo-code description of the method:

Algorithm 1: FastTargetedOrder
Input: Graph g = (V, E), with V = {0, 1, ..., n - 1}
Output: An ordered list L of the nodes in V in decreasing order of their degrees.
1.   for k <- 0 to n - 1 do
2.       DegreeSets[k] <- null   // DegreeSets[k] is a set of all nodes whose degree is k
3.   for i <- 0 to n - 1 do
4.       d <- degree(i)   // d is the degree of node i
5.       DegreeSets[d] <- DegreeSets[d] U {i}   // Adds node i to null set in DegreeSets[d]
6.   L <- []    // L is initialized to an empty list
7.   i <- 0    // Initialize an index variable for list L
8.   for k <- n - 1 downto 0 do    // Start with degree k equal to maximum node degree possible
9.       while DegreeSets[k] != null do    // While set of nodes with that degree is not empty
10.         Let u be an arbitrary element in DegreeSets[k]    // Choose a random element u in the set
11.         DegreeSets[k] <- DegreeSets[k] - {u}    // Remove element u from set for degree k
12.         foreach neighbor v of u do    // Find each neighbor v of u and do to each the following
13.             d <- degree(v)    // Find degree d of node v
14.             DegreeSets[d] <- DegreeSets[d] - {v}    // Remove node v from the set for that degree
15.             DegreeSets[d - 1] <- DegreeSets[d - 1] U {v} // Add nove v to degree d - 1 (since u removed)
16.         L[i] <- u    // Add node u to list L
17.         i <- i + 1    // Increment index variable
18.         Remove node u from g    // Node u has been dealt with
19. return L

In Python, this method creates a list degree_sets whose kth element is the set of nodes of degree k.
The method then iterates through the list degree_sets in order of decreasing degree. When it 
encounters a non-empty set, the nodes in this set must be of maximum degree. The method then
repeatedly chooses a node from this set, deletes that node from the graph, and updates degree_sets
appropriately.

For this question, your task is to implement fast_targeted_order and then analyze the running time
of these two methods on UPA graphs of size n with m = 5. Your analysis should be both mathematical
and empirical and include the following:

Determine big-O bounds of the worst-case running times of targeted_order and fast_targeted_order
as a function of the number of nodes n in the UPA graph.

Compute a plot comparing the running times of these methods on UPA graphs of increasing size.

Since the number of edges in these UPA graphs is always less than 5n (due to the choice of m = 5),
your big-O bounds for both functions should be expressions in n. You should also assume that all
of the set operations used in fast_targeted_order are O(1).

Next, run these two functions on a sequence of UPA graphs with n in range(10, 1000, 10) and m=5
and use the time module to compute the running times of these functions. Then, plot these running times
(vertical axis) as a function of the number of nodes n (horizontal axis) using a standard plot. Your plot
should consist of two curves showing the results of your timings. Remember to format your plot 
appropriately and include a legend. The title of your plot should indicate the implementation of Python
(desktop vs. CodeSkulptor) used to generate the timing results.

Your answer to this question will be assessed according to the following 3 items:

What are tight upper bounds on the worst case running times of targeted_order and fast_targeted_order?
Use big-O notation to express your answers (which should be simple).

Does the plot follow the formatting guidelines for plots? Is there a legend, and does the title include the
implementation of Python used to compute the timings?

Are the shapes of the timing curves in the plot correct?
'''
# general imports
import urllib2
import random
import time
import math

## Set seed for reproducibility
RANDOM_SEED = 1
random.seed(RANDOM_SEED)

# CodeSkulptor import
import simpleplot
import codeskulptor
codeskulptor.set_timeout(120)

## Below is the code provided for this question. Note that delete_node()
## is mimicked in the targeted_order() function.
def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)

def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order
	
## Below is my implementation of fast_targeted_order based on the algm steps.
## The block commented out is the function with notes and print statements.

# def fast_targeted_order(inp_graph):
    # """
    # Computes a targeted attack order consisting of
    # nodes of maximal degree.
    # """
    # graph = copy_graph(inp_graph)
    # num_nodes = len([key for key in graph.keys()])
    
    # # Steps 1-2
    # degree_sets = {}
    # for degree in range(num_nodes):
        # degree_sets[degree] = set()

    # # Steps 3-5
    # for node in range(num_nodes):
        # node_degree = len(graph[node])
        # degree_sets[node_degree].add(node)
    # print "degree_sets after update:", degree_sets
    # print
        
    # # Steps 6-7
    # attack_order = []
    # order_index = 0
    
    # # Step 8
    # for degree in range(num_nodes - 1, -1, -1):
        # # Step 9
        # while len(degree_sets[degree]) > 0:
            # # Steps 10-11
            # print "degree:", degree
            # node = degree_sets[degree].pop()
            # print "random node:", node
            # print "degree sets:", degree_sets
            # print "-"*30
            # # Steps 12-15
            # for neighbor in graph[node]:
                # print "neighbor:", neighbor
                # neighbor_degree = len(graph[neighbor])
                # print "neighbor degree:", neighbor_degree
                # degree_sets[neighbor_degree].remove(neighbor)
                # degree_sets[neighbor_degree - 1].add(neighbor)
                # print "updated degree set:", degree_sets
                # print "FINISH FOR LOOP FOR NEIGHBOR"
                # print "*"*30
            # # Steps 16-18
            # attack_order.append(node)
            # order_index += 1
            # delete_node(graph, node)
            # print "graph without node:", graph
            # print "FINISH WHILE LOOP FOR DEGREE"
            # print
    # # Step 19
    # return attack_order
	
def fast_targeted_order(inp_graph):
    """
    Computes a targeted attack order consisting of
    nodes of maximal degree.
    """
    graph = copy_graph(inp_graph)
    num_nodes = len([key for key in graph.keys()])
    degree_sets = {}
	
    for degree in range(num_nodes):
        degree_sets[degree] = set()

    for node in range(num_nodes):
        node_degree = len(graph[node])
        degree_sets[node_degree].add(node)
        
    attack_order = []
    order_index = 0
    
    for degree in range(num_nodes - 1, -1, -1):
        while len(degree_sets[degree]) > 0:
		
            node = degree_sets[degree].pop()
			
            for neighbor in graph[node]:
                neighbor_degree = len(graph[neighbor])
                degree_sets[neighbor_degree].remove(neighbor)
                degree_sets[neighbor_degree - 1].add(neighbor)
				
            attack_order.append(node)
            order_index += 1
            delete_node(graph, node)
			
    return attack_order
	
## Running time will be analyzed with time.time() statements. 
## Below is code from App 2-1 for UPA graphs.

class UPATrial:
    """
    Simple class to encapsulate optimizated trials for the UPA 
    algorithm
    
    Maintains a list of node numbers with multiple instance 
    of each number. The number of instances of each node number 
    are in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for 
    each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) 
                              for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that each node number
        appears in correct ratio
        
        Returns:
        Set of nodes
        """
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        self._node_numbers.append(self._num_nodes)

        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        
		self._node_numbers.extend(list(new_node_neighbors))
        self._num_nodes += 1
        
		return new_node_neighbors
		
def make_complete_graph(num_nodes):
    """
    Returns a complete graph with the number of nodes specified by
    the num_nodes parameter.
    """
    complete_graph = {}
    if num_nodes <= 0: 
        return complete_graph
    for key in range(num_nodes):
        nodes = [node for node in range(num_nodes) if node != key]
        complete_graph[key] = set(nodes)
    return complete_graph
	
def create_upa_graph(n = 0, m = 0):
	"""
	Function to create a UPA graph with m initial nodes and n total nodes.
	"""
	ugraph = make_complete_graph(m)
	trial = UPATrial(m)
	for index in range(m, n):
		new_neighbors = trial.run_trial(m)
		ugraph[index] = new_neighbors
		for node in new_neighbors:
			ugraph[node].add(index)
			
	return ugraph

## Several UPA graphs will be made of size n = 10 to n = 1000, incrementing
## n by 10 nodes each time to make 99 graphs. In this loop, run each function
## on each returned graph and append n and both running times to a list.
targeted_runtimes = []
fast_targeted_runtimes = []
m = 5
for n in range(10, 1000, 10):
    graph = create_upa_graph(n, m)
    
    start = time.time()
    targeted_order(graph)
    end = time.time()
    runtime = end - start
    targeted_runtimes.append((n, runtime))
    
    start = time.time()
    fast_targeted_order(graph)
    end = time.time()
    runtime = end - start
    fast_targeted_runtimes.append((n, runtime))
    
simpleplot.plot_lines("CodeSkulptor Running Times of Targeted and Fast Targeted Ordering of UPA Graphs (m=5)", 
                      700, 600, "No. of Nodes", "Running Time in Seconds", 
                      [targeted_runtimes, fast_targeted_runtimes], False,
                      ["Targeted", "Fast Targeted"])
					  
## Answer
# See AlgThink_App2-3_Plot for resulting plot
'''
The tight upper bound on the worst-case running time of targeted_order is O(n^2). 
The tight upper bound on the worst-case running time of fast_targeted_order is O(n). 
'''