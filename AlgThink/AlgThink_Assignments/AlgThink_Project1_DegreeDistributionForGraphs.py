"""
Rice University / Coursera: Algorithmic Thinking (Part 1)
Project 1: Degree Distribution for Graphs
"""

EX_GRAPH0 = {0:set([1,2]),
             1:set([]),
             2:set([])}

EX_GRAPH1 = {0:set([1,4,5]),
             1:set([2,6]),
             2:set([3]),
             3:set([0]),
             4:set([1]),
             5:set([2]),
             6:set([])}

EX_GRAPH2 = {0:set([1,4,5]),
             1:set([2,6]),
             2:set([3,7]),
             3:set([7]),
             4:set([1]),
             5:set([2]),
             6:set([]),
             7:set([3]),
             8:set([1,2]),
             9:set([0,3,4,5,6,7])}

def make_complete_graph(num_nodes):
    """
    Returns a complete graph with the number of nodes specified by
    the num_nodes parameter.
    """
    # Create an empty dict.
    complete_graph = {}
    
    # For no nodes, return the empty dict.
    if num_nodes <= 0: 
        return complete_graph
    
    ## This appears to be O(n^2) running time, so the initial code
    ## will be used.
    #all_node_groups = []
    #for node_group in range(num_nodes):
    #    all_node_groups.append(set([node for node in range(num_nodes) 
    #                                if node != node_group]))
    #for key in range(num_nodes):
    #    complete_graph[key] = all_node_groups[key]
     
    # Add each key from 0 to (num_nodes - 1) to the dict and set
    # its value to a set of all other nodes but itself.
    for key in range(num_nodes):
        nodes = [node for node in range(num_nodes) if node != key]
        complete_graph[key] = set(nodes)

    return complete_graph

def compute_in_degrees(digraph):
    """
    Returns a dictionary with the same set of keys as
    the parameter digraph whose corresponding values
    are the number of edges whose head matches that
    particular node.
    """
    # Create a set of unique nodes and a list of all edges in the graph.
    nodes = set([key for key in digraph.keys()])
    edges = []
    for edge in digraph.values():
        edges.extend([set_item for set_item in edge])
    
    # Create a dict with each key equal to a node with initial val=0.
    # For each occur. of the node in the list of all edges, incr by 1.
    in_degree_count = {}
    for node in nodes:
        in_degree_count[node] = 0
    for edge in edges:
        in_degree_count[edge] += 1
    
    ## The below code, while cleaner, is much slower than the 4 lines above.
    ## It goes through the for loop n times, each time running m times. The
    ## running time is (sum of 1 to n) * m. Above, it runs through n times,
    ## then it runs through m times, separately, O(n + m) vs. O(n^2).
    # Create a dict with each key equal to a node and each key's value
    # equal to the num of times it appears in the list of all edges.
    #for node in nodes:
    #    in_degree_count[node] = edges.count(node)
        
    return in_degree_count

def in_degree_distribution(digraph):
    """
    Returns a dictionary whose keys correspond to in-degrees
    of the parameter digraph and whose values are the number
    of nodes with that in-degree. 
    """
    # Compute a dict of in-degrees for the graph, from it create a list 
    # of all in-degrees and a set of  unique in-degrees.
    in_degree_count = compute_in_degrees(digraph)
    all_in_degrees = [value for value in in_degree_count.values()]
    unique_in_degrees = set([value for value in in_degree_count.values()])
    
    # Create a dict with each key equal to a unique in-degree with init val=0.
    # For each occur. of the in-degree in the list of all in-degrees incr by 1.
    in_degree_dist = {}
    for in_degree in unique_in_degrees:
        in_degree_dist[in_degree] = 0
    for in_degree in all_in_degrees:
        in_degree_dist[in_degree] += 1
    
    ## Rewrote the above 4 lines to match what was done in the previous func
    ## to attain O(n + m) running time.
    # Create a dict with each key equal to a unique in-degree and each key's
    # value equal to the num of times it appears in the list of all in-degrees.
    #for in_degree in unique_in_degrees:
    #    in_degree_dist[in_degree] = all_in_degrees.count(in_degree)
    
    return in_degree_dist

##################################
# TESTING GROUNDS REMOVED FROM FINAL CODE #
##################################
print "Print example sets"
for key, value in EX_GRAPH0.items():
    print str(key) + ":" + str(value)
print
for key, value in EX_GRAPH1.items():
    print str(key) + ":" + str(value)
print
for key, value in EX_GRAPH2.items():
    print str(key) + ":" + str(value)
print
print
print "Make complete graphs"
print make_complete_graph(-5)
print make_complete_graph(5)
print
print
print "Compute in-degrees"
print compute_in_degrees(EX_GRAPH0)
print compute_in_degrees(EX_GRAPH1)
print compute_in_degrees(EX_GRAPH2)
print
print
print "Compute in-degree distribution"
print in_degree_distribution(EX_GRAPH0)
print in_degree_distribution(EX_GRAPH1)
print in_degree_distribution(EX_GRAPH2)