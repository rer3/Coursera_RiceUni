"""
Rice University / Coursera: Algorithmic Thinking (Part 1)
Application 1-3
"""
'''
Question 3 (2 pts)

We next consider a different process for generating synthetic directed 
graphs. In this process, a random directed graph is generated iteratively, 
where in each iteration a new node is created, added to the graph, and 
connected to a subset of the existing nodes. This subset is chosen based 
on the in-degrees of the existing nodes. More formally, to generate a 
random directed graph in this process, the user must specify two 
parameters: n, which is the final number of nodes, and m (where m≤n), 
which is the number of existing nodes to which a new node is connected 
during each iteration. Notice that m is fixed throughout the procedure.

The algorithm starts by creating a complete directed graph on m nodes. 
(Note, you've already written the code for this part in the Project.) Then, 
the algorithm grows the graph by adding n−m nodes, where each new 
node is connected to m nodes randomly chosen from the set of existing 
nodes. As an existing node may be chosen more than once in an iteration, 
we eliminate duplicates (to avoid parallel edges); hence, the new node 
may be connected to fewer than m existing nodes upon its addition.

The full description of the algorithm for generating random directed graphs 
with this process is given below, and is called Algorithm DPA (note that the 
m in the input is a parameter that is specified to this algorithm, and it does 
not denote the total number of edges in the resulting graph). The notation
SIGxES x means the "sum of all elements x in set S." For example, if
S = {1, 7, 12}, then SIGxES x triple-equals 1 + 7 + 12 = 20. 

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

Notice that this algorithm is more complex than the ER algorithm. As a 
result, reasoning about the properties of the graphs that it generates 
analytically is not as simple. When such a scenario arises, we can implement 
the algorithm, run it, produce graphs, and visually inspect their in-degree 
distributions. In general, this is a powerful technique: When analytical 
solutions to systems are very hard to derive, we can simulate the systems 
and generate data that can be analyzed to understand the properties of the 
systems. 

For this question, we will choose values for n and m that yield a DPA graph 
whose number of nodes and edges is roughly the same to those of the 
citation graph. For the nodes, choosing n to be the number of nodes as the 
citation graph is easy. Since each step in the DPA algorithm adds m edges to 
the graph, a good choice for m is an integer that is close to the average 
out-degree of the physics citation graph.

For this question, provide numerical values for n and m that you will use in 
your construction of the DPA graph.
'''

## Choose an n for the DPA graph.
## The citation graph has 27,770 nodes, so n = 27,770 for the DPA graph.

## As instructed, a good choice for the DPA graph's m value is one close
## to the average out-degree of the citation graph. The citation graph will
## be loaded similar to App1-1, but the out-degrees will be computed for
## each node, then the average out-degree value for all nodes.

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

## Write code to compute out-degrees
def compute_out_degrees(digraph):
    """
    Returns a dictionary with the same set of keys as
    the digraph whose corresponding values are the
    number of edges whose tail matches that node.
    """
    out_degree_count = {}
    for key in digraph.keys():
        out_degree_count[key] = len(digraph[key])
    return out_degree_count

## Write code to compute average out-degree of a dict
## of node:out-degree-count items.

def compute_avg_out_degree(digraph):
    """
    Returns the average out-degree from a dict of
    node:out-degree-count items.
    """
    sum_out_deg = 0
    node_count = len(digraph.keys())
    for value in digraph.values():
        sum_out_deg += value
    avg_out_deg = sum_out_deg / node_count
    return avg_out_deg

## In retrospect, I realize that the total num of 
## out-degrees will always equal the total num of 
## in-degrees, which is the total number of edges.
## Since the average is taken, you include the nodes
## which have zero out-degrees when you calculate the
## average. Total edges is 352768 no matter which way
## you cut it. This code above is unnecessary when a 
## simple line could be added to the in-degree func. 

## Code provided for App1-1.
CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

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
    
    print "Loaded graph with " + str(len(graph_lines)) + " nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

# Load citation graph from URL
citation_graph = load_graph(CITATION_URL)
# Compute out-degrees of the citation graph
outdegs = compute_out_degrees(citation_graph)
# Compute the average out-degree
print compute_avg_out_degree(outdegs)

## ANSWER
'''
The citation graph has 27,770 nodes, so the DPA graph will also have n = 27,770 nodes. 

If m is to equal an integer close to the average out-degree of the citation graph, then m 
would be equal to the total number of out-degrees divided by the total number of nodes. 
The total number of out-degrees is equal to the total number of in-degrees, which is just 
the number of edges in the graph. You can divide the number of edges by the total 
number of nodes (and not just the nodes with either in- or out-degrees, since zero values 
are counted as well when calculating averages) to get 12. For the DPA graph, m = 12 edges.
'''