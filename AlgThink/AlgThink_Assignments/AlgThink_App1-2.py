"""
Rice University / Coursera: Algorithmic Thinking (Part 1)
Application 1-2
"""
'''
Question 2 (3 pts)

In Homework 1, you saw Algorithm ER for generating random graphs 
and reasoned analytically about the properties of the ER graphs 
it generates. Consider the simple modification of the algorithm 
to generate random directed graphs: For every ordered pair of 
distinct nodes (i,j), the modified algorithm adds the directed 
edge from i to j with probability p.

For this question, your task is to consider the shape of the 
in-degree distribution for an ER graph and compare its shape to 
that of the physics citation graph. In the homework, we considered 
the probability of a specific in-degree, k, for a single node.  
Now, we are interested in the in-degree distribution for the 
entire ER graph. To determine the shape of this distribution, 
you are welcome to compute several examples of in-degree 
distributions or determine the shape mathematically.

Once you have determined the shape of the in-degree distributions 
for ER graphs, compare the shape of this distribution to the shape 
of the in-degree distribution for the citation graph. When 
answering this question, make sure to address the following points:

Is the expected in-degree the same for every node in an ER graph? 
Please answer yes or no and include a short explanation for your 
answer.

What does the in-degree distribution for an ER graph look like? 
You may either provide a plot (linear or log/log) of the degree 
distribution for a small value of n or a short written description 
of the shape of the distribution.

Does the shape of the in-degree distribution plot for ER look 
similar to the shape of the in-degree distribution for the 
citation graph? Provide a short explanation of the similarities 
or differences. Focus on comparing the shape of the two plots as 
discussed in the class page on "Creating, formatting, and 
comparing plots".
'''

## Import modules and set timeout to 50 sec
import urllib2
import simpleplot
import codeskulptor
import math
import time
import random
codeskulptor.set_timeout(50)

## Set seed for reproducibility
RANDOM_SEED = 1
random.seed(RANDOM_SEED)

## Enter compute_in_degrees() and in_degree_distribution() 
## functions from Project #1 for use here.
def compute_in_degrees(digraph):
    """
    Returns a dictionary with the same set of keys as
    the parameter digraph whose corresponding values
    are the number of edges whose head matches that
    particular node.
    """
    nodes = set([key for key in digraph.keys()])
    edges = []
    for edge in digraph.values():
        edges.extend([set_item for set_item in edge])
    
    in_degree_count = {}
    for node in nodes:
        in_degree_count[node] = 0
    for edge in edges:
        in_degree_count[edge] += 1
        
    return in_degree_count

def in_degree_distribution(digraph):
    """
    Returns a dictionary whose keys correspond to in-degrees
    of the parameter digraph and whose values are the number
    of nodes with that in-degree. 
    """
    in_degree_count = compute_in_degrees(digraph)
    all_in_degrees = [value for value in in_degree_count.values()]
    unique_in_degrees = set([value for value in 
                             in_degree_count.values()])
    
    in_degree_dist = {}
    for in_degree in unique_in_degrees:
        in_degree_dist[in_degree] = 0
    for in_degree in all_in_degrees:
        in_degree_dist[in_degree] += 1

    return in_degree_dist
    
## Write helper functions for normalization of dist data.
## Taken from App 1-1.
def dict_to_normalized_lists(a_dict):
    """
    Function that converts a dictionary to a list of [sorted key, 
    normal_value] lists.
    """
    normal_list = []
    keys = sorted(a_dict.keys())
    normvals = normalize_list([a_dict[key] for key in keys])
    for index in range(len(keys)):
        normal_list.append([keys[index], normvals[index]])
    return normal_list

def normalize_list(a_list):
    """
    Function that normalizes a list of data.
    """
    if len(a_list) <1:
        return float('nan')
    divisor = float(sum(a_list))
    return [item / divisor for item in a_list]

## Write a function to build the log/log plot.
## Taken from App 1-1.
def build_loglog_plot(normdata):
    """
    Build loglog plot from normalized dict data.
    """
    plot = []
    for index in range(len(normdata)):
        if normdata[index][0] > 0 and normdata[index][1] > 0:
            plot.append([math.log(normdata[index][0], 10), 
                         math.log(normdata[index][1],10)])
    return plot
    
## Write a Graph class to create a graph with
## the necessary attributes.

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

#print "~"*20
#print "UNDIRECTED GRAPHS"
#print "~"*20
#graph_1 = Graph(50)
#graph_1.convert_to_undir_er_graph(.2)
#print graph_1
#print "~"*20
#graph_2 = Graph(100)
#graph_2.convert_to_undir_er_graph(.2)
#print graph_2
#print "~"*20
#print "DIRECTED GRAPHS"
#print "~"*20
digraph_1 = Graph(300)
digraph_1.convert_to_dir_er_graph(.3)
#print digraph_1
#print "~"*20
digraph_2 = Graph(300)
digraph_2.convert_to_dir_er_graph(.6)
#print digraph_2
digraph_3 = Graph(300)
digraph_3.convert_to_dir_er_graph(.9)
digraph_0 = Graph(300)
digraph_0.convert_to_dir_er_graph(.1)

## Test undirected graphs
#digraph_0.convert_to_undir_er_graph(.1)
#digraph_1.convert_to_undir_er_graph(.3)
#digraph_2.convert_to_undir_er_graph(.6)
#digraph_3.convert_to_undir_er_graph(.9)

# Compute in-degree dist of digraphs
indegdist_1 = in_degree_distribution(digraph_1.adjacency_dict())
indegdist_2 = in_degree_distribution(digraph_2.adjacency_dict())
indegdist_3 = in_degree_distribution(digraph_3.adjacency_dict())
indegdist_0 = in_degree_distribution(digraph_0.adjacency_dict())

# Normalize distributions
normdist_1 = dict_to_normalized_lists(indegdist_1)
normdist_2 = dict_to_normalized_lists(indegdist_2)
normdist_3 = dict_to_normalized_lists(indegdist_3)
normdist_0 = dict_to_normalized_lists(indegdist_0)

# Compute log/log plots from normalized dist lists
plot_1 = build_loglog_plot(normdist_1)
plot_2 = build_loglog_plot(normdist_2)
plot_3 = build_loglog_plot(normdist_3)
plot_0 = build_loglog_plot(normdist_0)

# Scatter plots
simpleplot.plot_scatter("ER Digraphs: Normalized In-degree Distribution (log/log)", 
                        700, 600, "log10(In-degree Number)", "log10(Normalized Distribution)", 
                        [plot_0, plot_1, plot_2,plot_3],
                       ["p = .1", "p = .3", "p = .6", "p = .9"])
                       
## ANSWER
'''
1.) The expected in-degree is not the same for every node in an ER 
graph. The normalized distribution from one in-degree number to the
next is not constant.

2.) The in-degree distribution for an ER digraph plot looks like an inverted 
parabola when probability p is low (below 0.5) and a spike when probability 
p is high (above 0.5). The in-degree numbers increased along with probability 
that an edge would be made between 2 nodes. See attached graph. It appears 
to follow a Poisson distribution. For each of the ER digraphs in the attached file, 
n = 300. It is of note that increasing n from 300 to 700 (not shown) decreased 
the spread of each curve, creating narrower spikes. 

3.) The ER digraph plot shape differs greatly from the citation digraph shape. 
In the ER plot, as the in-degree number increases, so does the distribution, 
but only until a maximum point is reached at roughly the halfway point; 
then as the in-degree number increases from there on, the distribution decreases. 
In the citation plot, the first in-degree number has the highest distribution, and 
then there is a gradual decrease in distribution as the in-degree number increases.
'''
## Graph attached, see file AlgThink_App1-2_Plot