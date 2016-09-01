"""
Rice University / Coursera: Algorithmic Thinking (Part 1)
Application 2-4
"""

'''
To continue our analysis of the computer network, we will examine its 
resilience under an attack in which servers are chosen based on their connectivity. 
We will again compare the resilience of the network to the resilience of ER and 
UPA graphs of similar size.

Using targeted_order (or fast_targeted_order), your task is to compute a targeted 
attack order for each of the three graphs (computer network, ER, UPA) from 
Question 1. Then, for each of these three graphs, compute the resilience of the 
graph using compute_resilience. Finally, plot the computed resiliences as three 
curves (line plots) in a single standard plot. As in Question 1, please include a legend 
in your plot that distinguishes the three plots. The text labels in this legend should 
include the values for p and m that you used in computing the ER and UPA graphs, 
respectively.

Once you are satisfied with your plot, upload your plot in the box below using 
"Attach a file" button (the button is disabled under the 'html' edit mode; you must 
be under the 'Rich' edit mode for the button to be enabled). Your plot will be assessed 
based on the answers to the following three questions:

Does the plot follow the formatting guidelines for plots?

Does the plot include a legend? Does this legend indicate the values for p and m used in 
ER and UPA, respectively?

Do the three curves in the plot have the correct shape?
'''

## Resilience will be computed on the desktop due to runtime

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
#codeskulptor.set_timeout(120)

## Use fast_targeted_order from App2-3

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

	## Changed this line from the previous one since the node numbers in the
	## Network Graph are not continuous from 0 to 1238, instead they range
	## from 0 to 1300+ and skip node numbers in between. This new code works.
    for node in graph.keys():
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
	
## Create the graphs from App2-1

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
        self._items.append(item)

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

def bfs_visited(ugraph, start_node):
	"""
	Takes undirected graph ugraph and the node start_node and
	returns the set consisting of all nodes that are visited by a BFS
	that starts at start_node.
	"""
	stack = Queue()
	visited = [start_node]
	stack.enqueue(start_node)
	while len(stack) > 0:
		ref_node = stack.dequeue()
		for neighbor in ugraph[ref_node]:
			if neighbor not in visited:
				visited.append(neighbor)
				stack.enqueue(neighbor)
	return set(visited)

def cc_visited(ugraph):
	"""
	Takes undirected graph ugraph and returns a list of sets where
	each set consists of all nodes in a connected component, and 
	each CC in the graph only has one set.
	"""
	rem_nodes = [key for key in ugraph.keys()]
	conn_comps = []
	while len(rem_nodes) > 0:
		ref_node = random.choice(rem_nodes)
		visited = bfs_visited(ugraph, ref_node)
		conn_comps.append(set(visited))
		for node in visited:
			rem_nodes.remove(node)
	return conn_comps
	
def largest_cc_size(ugraph):
    """
    Takes the undirected graph ugraph and returns the size of the
    largest connected component in ugraph.
    """
    conn_comps = cc_visited(ugraph)
    if len(conn_comps) == 0:
        return 0
    max_len = max([len(comp) for comp in conn_comps])
    return max_len
	
def compute_resilience(ugraph, attack_order):
    """
    Takes the undirected graph ugraph and a list of nodes attack_order
    and iterates through the nodes in attack_order. For each node in the
    list, the given node and its edges are removed from the graph and 
    then the size of the largest resulting CC is computed.
    """
    conn_comps = [largest_cc_size(ugraph)]
    for node in attack_order:
        ugraph.pop(node)
        for edge_set in ugraph.values():
            edge_set.discard(node)
        conn_comps.append(largest_cc_size(ugraph))
    return conn_comps
	
## Now all 3 graphs must be created. The below code will create each graph.
## NETWORK GRAPH

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
	
## ER GRAPH using p = 0.002. 

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
        global EDGES
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
						
## UPA graph using m = 2

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
	
## Compute a random attack order and resilience for each graph
NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"
network = load_graph(NETWORK_URL)
network_order = fast_targeted_order(network)
network_res = compute_resilience(network, network_order)
print network_res ## see below

erugraph = Graph(1239)
erugraph.convert_to_undir_er_graph(.002)
erugraph_order = fast_targeted_order(erugraph.adjacency_dict())
erugraph_res = compute_resilience(erugraph.adjacency_dict(), erugraph_order)
print erugraph_res ## see below

upagraph = create_upa_graph(1239, 2)
upagraph_order = fast_targeted_order(upagraph)
upagraph_res = compute_resilience(upagraph, upagraph_order)
print upagraph_res ## see below

network_res = [1239, 1158, 1150, 1148, 1142, 1136, 1129, 1127, 1124, 
               1120, 1119, 1110, 1109, 1101, 1100, 1069, 1068, 1066, 
               1065, 1064, 1055, 1050, 1049, 1047, 1037, 1035, 1034, 
               1031, 1025, 1024, 1019, 1012, 1011, 1007, 1003, 990, 
               989, 985, 962, 938, 935, 934, 929, 926, 924, 908, 863, 
               860, 817, 810, 783, 782, 764, 701, 694, 672, 519, 516, 
               496, 478, 476, 476, 461, 461, 457, 410, 407, 375, 370, 
               333, 333, 333, 311, 311, 311, 309, 297, 294, 281, 279, 
               216, 216, 215, 212, 212, 174, 174, 174, 174, 172, 162, 
               162, 162, 162, 159, 159, 159, 156, 156, 156, 156, 154, 
               127, 127, 127, 127, 82, 82, 82, 80, 70, 65, 65, 65, 65, 
               65, 65, 65, 65, 65, 65, 62, 62, 62, 62, 62, 62, 62, 55, 
               55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 54, 54, 54, 
               54, 46, 46, 46, 46, 43, 43, 43, 43, 42, 42, 42, 42, 28, 
               28, 28, 28, 28, 28, 20, 20, 20, 20, 20, 20, 16, 16, 16, 
               16, 16, 16, 16, 16, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 
               9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 7, 7, 7, 
               7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 
               6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 
               5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 
               4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
               2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
               2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
               2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
               1, 1, 1, 1, 1, 1, 1, 1, 0]

erugraph_res = [1229, 1227, 1225, 1223, 1222, 1220, 1219, 1218, 1217, 
                1216, 1215, 1214, 1212, 1211, 1210, 1209, 1208, 1207, 
                1206, 1205, 1204, 1203, 1202, 1201, 1200, 1199, 1198, 
                1196, 1195, 1194, 1193, 1192, 1191, 1190, 1189, 1188, 
                1187, 1186, 1185, 1184, 1183, 1182, 1181, 1180, 1179, 
                1178, 1177, 1176, 1175, 1174, 1173, 1172, 1171, 1170, 
                1169, 1168, 1166, 1165, 1164, 1163, 1162, 1161, 1160, 
                1159, 1158, 1157, 1156, 1155, 1154, 1153, 1152, 1151, 
                1150, 1149, 1148, 1147, 1146, 1145, 1144, 1143, 1142, 
                1141, 1140, 1139, 1138, 1137, 1136, 1135, 1134, 1133, 
                1132, 1131, 1130, 1129, 1128, 1127, 1126, 1125, 1123, 
                1122, 1121, 1119, 1118, 1117, 1116, 1115, 1114, 1113, 
                1111, 1110, 1109, 1108, 1107, 1106, 1105, 1104, 1102, 
                1101, 1100, 1098, 1096, 1095, 1094, 1093, 1092, 1091, 
                1090, 1089, 1088, 1087, 1086, 1085, 1083, 1082, 1080, 
                1079, 1077, 1076, 1074, 1073, 1071, 1070, 1069, 1068, 
                1067, 1066, 1065, 1064, 1063, 1062, 1060, 1059, 1058, 
                1057, 1056, 1055, 1054, 1053, 1052, 1050, 1049, 1048, 
                1046, 1045, 1044, 1042, 1041, 1038, 1037, 1036, 1035, 
                1034, 1033, 1031, 1030, 1029, 1027, 1026, 1025, 1024, 
                1023, 1022, 1019, 1018, 1017, 1016, 1014, 1013, 1012, 
                1011, 1010, 1009, 1008, 1007, 1005, 1004, 1003, 1002,
                1001, 1000, 999, 998, 997, 995, 994, 993, 992, 991, 
                990, 989, 988, 986, 985, 983, 982, 981, 979, 977, 
                976, 975, 974, 973, 972, 971, 970, 968, 967, 966, 
                965, 962, 961, 960, 959, 957, 956, 954, 951, 950, 
                949, 948, 946, 945, 944, 943, 942, 941, 940, 939, 
                937, 936, 935, 934, 933, 931, 926, 925, 923, 921, 
                919, 917, 916, 913, 912, 910, 909, 908, 905, 904, 
                903, 902, 900, 899, 897, 895, 894, 893, 892, 891, 
                890, 889, 887, 886, 885, 884, 882, 879, 876, 874, 
                865, 864, 862, 861, 860, 858, 856, 854, 852, 849, 
                847, 844, 843, 836, 834, 832, 829, 828, 826, 823, 
                822, 819, 817, 812, 811, 810, 808, 807, 804, 803, 
                802, 800, 799, 797, 794, 793, 792, 789, 784, 783, 
                782, 781, 780, 778, 775, 774, 773, 771, 767, 761, 
                757, 755, 751, 745, 743, 741, 730, 726, 717, 715, 
                711, 710, 707, 705, 701, 700, 695, 685, 680, 678, 
                677, 673, 671, 670, 666, 664, 653, 651, 640, 638, 
                637, 634, 630, 623, 616, 611, 608, 607, 600, 591, 
                588, 580, 579, 572, 565, 563, 557, 553, 544, 517, 
                514, 506, 503, 502, 481, 476, 475, 423, 373, 361, 
                297, 297, 291, 288, 259, 259, 255, 255, 163, 160, 
                114, 99, 99, 99, 99, 99, 99, 99, 81, 81, 81, 81, 
                81, 81, 81, 81, 81, 56, 56, 56, 56, 56, 56, 39, 
                39, 39, 39, 39, 39, 39, 31, 31, 31, 31, 31, 31, 
                29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 
                29, 29, 29, 29, 29, 24, 24, 24, 24, 24, 24, 24, 
                24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 19, 19, 
                19, 19, 19, 15, 15, 15, 15, 15, 15, 11, 11, 11, 
                11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 
                10, 10, 10, 10, 10, 10, 10, 8, 8, 8, 8, 8, 8, 8, 
                8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 
                7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 
                7, 7, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 
                4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 
                4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 
                3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
                2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 0]

upagraph_res = [1239, 1238, 1237, 1236, 1235, 1230, 1227, 1224, 
                1221, 1219, 1218, 1216, 1214, 1212, 1210, 1209, 
                1207, 1205, 1204, 1202, 1201, 1200, 1199, 1191, 
                1189, 1187, 1186, 1184, 1182, 1179, 1175, 1173, 
                1170, 1169, 1168, 1166, 1165, 1163, 1158, 1156, 
                1153, 1152, 1151, 1150, 1147, 1144, 1143, 1141, 
                1139, 1135, 1134, 1131, 1129, 1126, 1124, 1122, 
                1120, 1116, 1114, 1113, 1110, 1107, 1103, 1102, 
                1100, 1097, 1095, 1091, 1088, 1084, 1082, 1080, 
                1078, 1074, 1072, 1063, 1057, 1054, 1045, 1043, 
                1038, 1035, 1032, 1026, 1023, 1015, 1014, 1011, 
                1009, 1006, 1002, 1000, 998, 996, 995, 992, 989, 
                986, 984, 980, 978, 976, 974, 970, 965, 962, 960, 
                958, 951, 949, 947, 945, 938, 935, 933, 928, 927, 
                923, 921, 913, 908, 901, 900, 897, 895, 892, 890, 
                887, 885, 884, 883, 881, 874, 872, 870, 868, 861, 
                857, 845, 839, 836, 826, 819, 816, 812, 809, 808, 
                805, 799, 785, 774, 760, 745, 741, 728, 725, 713, 
                702, 700, 697, 694, 688, 677, 670, 656, 650, 642, 
                637, 629, 627, 624, 617, 617, 614, 612, 608, 525, 
                521, 272, 272, 246, 246, 231, 231, 231, 231, 231, 
                231, 221, 221, 214, 214, 209, 209, 209, 209, 209, 
                205, 201, 201, 201, 123, 123, 123, 123, 123, 104, 
                104, 68, 68, 68, 68, 68, 68, 48, 48, 48, 48, 48, 
                48, 48, 41, 41, 41, 36, 36, 36, 36, 36, 36, 36, 
                36, 36, 36, 36, 29, 29, 29, 29, 29, 29, 29, 29, 
                29, 29, 24, 20, 20, 20, 20, 20, 20, 20, 20, 20, 
                20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 
                20, 20, 20, 20, 18, 18, 13, 13, 13, 13, 13, 13, 
                13, 13, 13, 13, 13, 13, 13, 10, 10, 10, 10, 10, 
                10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 
                9, 9, 9, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 
                7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 
                7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 
                6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 
                6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 
                5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 
                4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
                3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
                2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 0]
				
def convert_res_to_points(res_list):
    """
    Converts a resilience list to a series of points
    """
    nodes_in_graph = len(res_list)
    point_list = []
    for i in range(nodes_in_graph):
        point_list.append((i, res_list[i]))
    return point_list

#print len(network_res)
#print len(erugraph_res)
#print len(upagraph_res)

netplot = convert_res_to_points(network_res)
eruplot = convert_res_to_points(erugraph_res)
upaplot = convert_res_to_points(upagraph_res)

#print netplot
#print eruplot
#print upaplot

simpleplot.plot_lines("Graph Resilience Using Fast Targeted Attack Order on All Nodes", 
                      700, 600, "No. of Nodes Removed", "Size of Largest CC Left", 
                      [netplot, eruplot, upaplot], False,
                      ["Network Graph", "ER Graph (p=0.002)", "UPA Graph (m=2)"])
					  
## ANSWER
# See AlgThink_App2-4_Plot