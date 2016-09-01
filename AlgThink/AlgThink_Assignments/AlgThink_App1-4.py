"""
Rice University / Coursera: Algorithmic Thinking (Part 1)
Application 1-4
"""
'''
Your task for this question is to implement the DPA algorithm, 
compute a DPA graph using the values from Question 3, and 
then plot the in-degree distribution for this DPA graph. Creating 
an efficient implementation of the DPA algorithm from scratch is 
surprisingly tricky. The key issue in implementing the algorithm is 
to avoid iterating through every node in the graph when executing 
Line 6. Using a loop to implement Line 6 leads to implementations 
that require on the order of 30 minutes in desktop Python to 
create a DPA graph with 28000 nodes.

To avoid this bottleneck, you are welcome to use this provided 
code that implements a DPATrial class. The class has two methods:

__init__(num_nodes): Create a DPATrial object corresponding to 
a complete graph with num_nodes nodes.

run_trial(num_nodes): Runs num_nodes number of DPA trials 
(lines 4- 6). Returns a set of the nodes, computed with the correct 
probabilities, that are neighbors of the new node.

In the provided code, the DPATrial class maintains a list of node 
numbers that contains multiple instances of the same node number. 
If the number of instances of each node number is maintained in 
the same ratio as the desired probabilities, a call to random.choice() 
produces a random node number with the desired probability.

Using this provided code, implementing the DPA algorithm is fairly 
simple and leads to an efficient implementation of the algorithm. In 
particular, computing a DPA graph with 28000 nodes should take 
on the order of 10-20 seconds in CodeSkulptor. For a challenge, 
you are also welcome to develop your own implementation of the 
DPA algorithm that does not use this provided code. However, we 
recommend that you use desktop Python as your development 
environment since you are likely to encounter long running times.

Once you have created a DPA graph of the appropriate size, compute 
a (normalized) log/log plot of the points in the graph's in-degree 
distribution, and upload your plot in the box below using the "Attach 
a file" button. (Note that you do not need to upload or machine-grade 
your DPA code.) Your submitted plot will be assessed based on the 
answers to the following three questions:

Does the plot follow the formatting guidelines for plots?

Is the plot a log/log plot of a normalized distribution?

Is the content of the plot correct?
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

"""
Provided code for application portion of module 1

Helper class for implementing efficient version
of DPA algorithm
"""

class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) 
                              for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
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
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors

## From App1-3, n = 27,770 and m = 12.
## The algorithm looks like:
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

## From Project1, paste the make_complete_graph() func.

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

## Initial tests
# List comprehension test for two for loops without lists separating them
#test_comp = [node for node in range(5) for dummy_idx in range(3)]
#print test_comp
# Compared to the list comp when the first loop is isolated in a list
#test_comp = [[x for x in range(5)] for y in range(3)]
#print test_comp
# Create trial
#dpa = DPATrial(3)
#print dpa._node_numbers
#print dpa.run_trial(3)
#print dpa._node_numbers
#print dpa.run_trial(4)
#print dpa._node_numbers

'''
The DPATrial class can supplant line 6 as such: it starts out by creating
a list with num_node occurrences of each node, keeping the probability that
any such node is chosen the same. For example, if there are 3 nodes, p = 1/3,
and for 10 nodes, p = 1/10. This list of node_numbers is then updated with
the next node numm (4 and 11, respectively, in the aforementioned examples)
plus num_node randomly chosen nodes (unique values, which is why they are
entered into a set). This maintains the probability of each chosen node so
that it is now (total_indeg + 1)/(num_nodes + |V|). 

Note that the initial node_numbers list has this probability. For n = 3, you
have a list [0,0,0,1,1,1,2,2,2] with p = 1/3. This is equivalent to (using 0):
(2{indeg}+ 1)/(3{num_nodes}+ |V|{not sure about this one, let's figure it out}).
|V| must equal 6, but let's add a node and find out how this works. By adding
node 3, increasing num_nodes to 4, and randomly choosing neighbors 0, 1, and 2, 
the node_numbers are now [0,0,0,1,1,1,2,2,2,3,0,1,2]. The probabilities of 
choosing 0, 1, or 2 are 30.77%, while node 3's prob is 7.69%. Run another trial
to get [0,0,0,1,1,1,2,2,2,3,0,1,2,4,0,1]. You find that p = 31.25% for 0 and 1, 
p = 25% for 2, and p = 6.25% for 3 and 4. 

Testing the equation (indeg + 1) / (num_nodes + |V|) to solve for |V|, we can
see after adding node 3, for node 0, p = .3077 = (3 + 1)/(4 + |V|). Solve to
find |V| = 13 (roughly). 13, as you can clearly see, is the new length of the
list node_numbers. Let's solve for |V| after adding node 4. For node 4, you
get 0.0625 = (1 + 1)/(5 + |V|), and |V| = 27. The length of node_numbers is
16, so this does not make sense. We will have to come back to this and just 
take the professor's word that this holds for the DPA algorithm's prob func.
'''

## Write a function that executes the algorithm for n and m.
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

# Create DPA graph
graph = create_dpa_graph(28000, 12)
#for key, value in graph.items()[:200]:
#    print str(key) + ":" + str(value)

# Compute in-degree dist of DPA graph
indegdist = in_degree_distribution(graph)

# Normalize distribution
normdist = dict_to_normalized_lists(indegdist)

# Build loglog plot
plot = build_loglog_plot(normdist)

# Plot scatter of graph
simpleplot.plot_scatter("DPA Graph: Normalized In-Degree Distribution (log/log)",
                        700, 600, "log10(In-degree Number)", "log10(Normalized Distribution)",
                        [plot], ["n=28000, m=12"])
    
## ANSWER
## Graph attached, see file AlgThink_App1-4_Plot