'''
Graph exploration (that is, "visiting" the nodes and edges 
of a graph) is a powerful and necessary tool to elucidate 
properties of graphs and quantify statistics on them. For 
example, by exploring a graph, we can compute its degree 
distribution, pairwise distances among nodes, its connected 
components, and centrality measures of its nodes and edges. 
As we saw in the Homework and Project, breadth-first search 
can be used to compute the connected components of a graph.

In this Application, we will analyze the connectivity of a 
computer network as it undergoes a cyber-attack. In particular, 
we will simulate an attack on this network in which an increasing 
number of servers are disabled.  In computational terms, we will 
model the network by an undirected graph and repeatedly delete 
nodes from this graph. We will then measure the resilience of the 
graph in terms of the size of the largest remaining connected 
component as a function of the number of nodes deleted.

EXAMPLE GRAPHS
In this Application, you will compute resilience of several types 
of undirected graphs. We suggest that you begin by collecting and 
writing code to create the following 3 types of graphs:

An example computer network - The URL of the network is below, 
and code has been provided to load the file as an undirected graph
with 1239 nodes and 3047 edges. Note that this provided code includes
several useful helper functions that you should review.

ER graphs - If you have not implemented the pseudocode for creating
undirected ER graphs (I did, App1-2), you will need to implement this
code. 

UPA graphs - In App 1, you implemented pseudocode that created DPA
graphs. These graphs were directed (hence the D in DPA). In this App,
you will modify this code to generated undirected UPA graphs. This
code has also been provided by the instructor.
'''
######################################################
"""
Provided code for Application portion of Module 2
"""

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

# Desktop imports
#import matplotlib.pyplot as plt

# Provided code

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
    

# Code for loading computer network graph

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

##########################################################

## From App1-2, use code for creating ER graphs so that an
## undirected ER graph can be created.

class Graph:
    """
    Class to build a graph represented by its adjacency dict.
    """
    
    def __init__(self, num_nodes):
        """
        Create an adjacency dict with the specified number of 
        nodes and no edges.
        """
        self._node_count = num_nodes
        self._adjacency_dict = {}
        for node in range(num_nodes):
            self._adjacency_dict[node] = set([])
        
    def __str__(self):
        """
        Return a string representation of the graph's adjacency 
        dict.
        """
        adj_dict_string = ""
        for key, value in self._adjacency_dict.items():
            adj_dict_string += str(key) + ":" + str(value) + "\n"
        return adj_dict_string
    
    def adjacency_dict(self):
        """
        Return the adjacency dict of the graph.
        """
        return self._adjacency_dict
    
    def remove_edges(self):
        """
        Remove all edges from the adjacency matrix.
        """
        for node in range(self._node_count):
            self._adjacency_dict[node] = set([])
    
    def convert_to_undir_er_graph(self, probability):
        """
        Build an undirected ER graph based on the probability given.
        """
        self.remove_edges()
        for node_i in range(self._node_count):
            for node_j in range(self._node_count):
                if node_i != node_j:
                    if random.random() < probability:
                        self._adjacency_dict[node_i].add(node_j)
                        self._adjacency_dict[node_j].add(node_i)
                        
    def convert_to_dir_er_graph(self, probability):
        """
        Build a directed ER graph based on the probability given.
        """
        self.remove_edges()
        for node_i in range(self._node_count):
            for node_j in range(self._node_count):
                if node_i != node_j:
                    if random.random() < probability:
                        self._adjacency_dict[node_i].add(node_j)

#######################################################
"""
Provided code for application portion of module 2

Helper class for implementing efficient version
of UPA algorithm
"""

import random

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
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        ## Note that the below for loop is an addition due to the
        ## undirected nature of the graph, accounting for the
        ## inclusion of both nodes when adding a new node, instead
        ## of just including the new node once and its neighbors.
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors

##########################################################

## The create_dpa_graph(n, m) code from App1-4 can be used to create a UPA graph
## but there may be changes to be made. Recall that the algm was:
'''
Algorithm 3: DPA
Input: Number of nodes n (n >= 1); integer m (1 <= m <= n).
Output: A directed graph g = (V,E).
1. V <- {0, 1, ..., m - 1} // Start a graph on m nodes
2. E <- {(i,j): i,j EV, i != j} // Make the graph complete
3. for i <- m to n - 1 do
4.     totindeg = SIGjEV indeg(j) // sum of the in-degrees of existing nodes
5.     V' <- null
6.     Choose randomly m nodes from V and add them to V', where the 
        probability of choosing node j is (indeg(j) + 1) / (totindeg + |V|)\
        // The m nodes may not be distinct; hence |V'| <= m
7.		V <- V U {i} // new node i is added to set V
8.		E <- E U {(i,j):j E V'} // connect the new node to the randomly chosen
                                             node
9. return g = (V,E)
'''
## The UPA graph algm will add node i to the set of edges V' since the edge is undirected.
## Line 8 should be updated to include both j AND i, if I'm thinking of this correctly:
'''
8.     E <- E U {(i,j):i, j E V'} // might be incorrect syntax for this step
'''
## The make_complete_graph() function acts as a helper function to the create_dpa_graph()
## function, so it will be used by the create_dpa_graph() function as well.
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
## Note that the resulting dict for a complete directed graph will be a set of nodes as keys with
## each key's value a set of every other node in the graph, implicitly indicating two directed edges
## between all nodes, one edge pointed to one of the nodes, and the other edge pointed to the other
## node. For a complete undirected graph, this representation is still valid, but must be thought of as 
## one undirected edge pointing at both (or neither, rather) of the two nodes it connects. 

def create_dpa_graph(n = 0, m = 0):
    """
    Function to create a DPA graph with m initial nodes and n total nodes.
    All nine DPA algm steps will be identified where applicable.
    """
    # Step #1 - 2
    digraph = make_complete_graph(m)
    # Step #4 - 6 (part 1)
    trial = DPATrial(m)
    
    # Step #3
    for index in range(m, n):
    # Step #4 - 6 (part 2)
        new_neighbors = trial.run_trial(m)
    # Step #7 - 8
        digraph[index] = new_neighbors
        
    # Step 9
    return digraph
	
def create_upa_graph(n = 0, m = 0):
	"""
	Function to create a UPA graph with m initial nodes and n total nodes.
	"""
	## Same as create_dpa_graph for this chunk
	ugraph = make_complete_graph(m)
	trial = UPATrial(m)
	for index in range(m, n):
		new_neighbors = trial.run_trial(m)
		ugraph[index] = new_neighbors
		## Add new node (index) to the set associated with each node in new_neighbors
		## since we are adding undirected edges
		for node in new_neighbors:
			ugraph[node].add(index)
			
	return ugraph
		
###########
# TESTING #
###########
trial = UPATrial(3)
print trial._node_numbers
print trial.run_trial(3)
print trial._node_numbers

## Determine m value for UPA graph with 1239 nodes
n = 1239
m = 1
graph = create_upa_graph(n, m)
total_edges = 0
for value in graph.values():
    for item in value:
        total_edges += 0.5 # Incrementing by 1/2 because this graph is undirected
print total_edges
## m = 1, total edges = 1238
## m = 2, total edges is around 2460
## m = 3, total edges is around 3685