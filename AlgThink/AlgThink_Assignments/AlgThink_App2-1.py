"""
Rice University / Coursera: Algorithmic Thinking (Part 1)
Application 2-1
"""

'''
To begin our analysis, we will examine the resilience of the computer network
under an attack in which servers are chosen at random. We will then compare
the resilience of the network to the resilience of ER and UPA graphs of similar
size.

To begin, you should determine the probability p such that the ER graph computed
using this edge probability has approximately the same number of edges as the
computer network. Your choice for p should be consistent with considering each
edge in the undirected graph exactly once, not twice. Likewise, you should compute
an integer m such that the number of edges in the UPA graph is close to the number
of edges in the computer network. Remember that all 3 graphs being analyzed in
this App should have the same number of nodes and approximately the same number
of edges.

Next, you should write a function random_order that takes a graph and returns a list
of the nodes in the graph in some random order. Then, for each of the 3 graphs
(computer network, ER, UPA), compute a random attack order using random_order
and use this attack order in compute_resilience to compute the resilience of the graph.

Once you have computed the resilience for all 3 graphs, plot the results as 3 curves
combined in a single standard plot. Use a line plot for each curve. The horizontal axis
for your single plot should be the number of nodes REMOVED (ranging from zero to 
the number of nodes in the graph) while the vertical axis should be the size of the
largest connect component in the graphs resulting from the node removal. For this
question (and others) involving multiple curves in a single plot, please include a legend
in your plot that distinguishes the 3 curves. The text labels in this legend should include
the values for p and m that you used in computing the ER and UPA graphs, respecitively.
Both matplotlib and simpleplot support these capabilities.

Note that 3 graphs in this problem are large enough that using CodeSkulptor to calculate
compute_resilience for these graphs will take on the order of 3-5 minutes per graph. When
using CodeSkulptor, we suggest that you compute resilience for each graph separately
and save the results. You can then plot the result of all 3 calculations using simpleplot. 

Once you are satisfied with your plot, upload your plot blah blah blah Coursera usage stuff.
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

## First determine probability p for ER graph to return an undirected ER graph with
## a number of edges comparable to the 3047 edges in the network graph with 
## 1239 nodes. Note that iterating through all 1239 nodes should result in 3047 edges
## in the ER graph. The ER algm assigns an edge to a set of nodes if the random number 
## generated in range (0, 1] is less than the specified probability from 0 to 1, with a p of
## 0 resulting in no edges and a p of 1 resulting in a complete graph. 
##
## Note that num of edges in a complete ungraph with n nodes will be (n(n-1))/ 2. For
## n = 1239, max edges = 766941. An ungraph with 1239 nodes and 3047 edges has
## only .39739 % of its max possible edges present. Therefore, p = 0.0039739. 
##
## When the Graph class's convert_to_undir_er_graph() method was used on a ugraph,
## the number of nodes with p = 0.004 was around 6000. Why? Lowering p to 0.002
## halved the edges to around 3000 where we want it to be. This could be a mistake, as
## a simulation (shown below) produces the predicted outcome of 3000 edges at p = .004.
## This sim also produces numbers of edges that are not integers, which is impossible since
## there are not "half edges". 
# import math
# import random
# import codeskulptor
# codeskulptor.set_timeout(60)
# n = 1239
# p = .004
# max_edges = (n * (n - 1)) / 2.0
# edges = 0
# for i in range(n):
    # for j in range(n):
        # if i != j:
            # if random.random() < p:
                # edges += .5
# print "num edges:", edges
# print "max edges:", max_edges
# print "percent of:", round(edges / max_edges, 3)
## 
## Creating a graph with the following statements and incrementing a global EDGES
## by 0.5 each time an edge is made by convert_to_undir_er_graph() produces 3000 too.
# http://www.codeskulptor.org/#user40_JIW4kufI9l_2.py
# ergraph = Graph(1239)
# ergraph.convert_to_undir_er_graph(.004)
# print EDGES
##
## I will stick with p = 0.004. At this time, I will work on a better code to traverse the adjacency
## dictionary and produces the total number of edges, as my previous attempt was mistaken.
## 
## I was wrong. When I adjusted the convert method to check for existence of node j in the
## value set for node i, thereby eliminating duplicate edges (that are obfuscated by the nature
## of the set() type), I was able to return the same same of edges by incrementing EDGES by
## 1 each time a linkage was made (that would theoretically not be duplicated) as I did by
## iterating through the values of the adjacency list, adding the lengths, and halving them. 
## But why p = 0.002 when 0.002 * 766941 = 1534? 
##
## The code used below generates a probability that's twice the specified p:
# n = 100
# p = .1
# MAX_EDGES = (n * (n - 1)) / 2.0
# ergraph = Graph(n)
# ergraph.convert_to_undir_er_graph(p)
# print "nodes:", len(ergraph._adjacency_dict)
# new_edges = 0
# for key, value in ergraph._adjacency_dict.items():
    # print "new_edges", new_edges, "+ len(value)", len(value)
    # print "key:", key, "value:", value
    # new_edges += len(value)
    # print "new_edges:", new_edges
# EDGES = new_edges / 2.0
# print EDGES
# print MAX_EDGES
# print "P:", EDGES / MAX_EDGES
##
## When p = .1, the EDGES / MAX_EDGES value is .2. I don't understand, I thought that perhaps
## because you traverse the i,j pairs twice each that you would then double your probability of
## making a link, but that doesn't hold for every p value. I will just attempt to use p = 0.002 since
## that creates around 3000 edges.
##
#############################################################
## This is incorrect, apparently. p = 0.004 is in fact correct. I guess when you use p = 0.002, you 
## are counting each possible edge twice, which is inconsistent with the pseudocode for creating
## an undirected ER graph! Although, I did not seem to count every edge twice, since I divided
## by 2 to get a total that was still twice as much as when I used 0.004. So this is weird...
#############################################################

## Then, compute an integer m such that the number of edges in the UPA graph is close
## to the number of edges (3047) in the computer network. For me, this integer m is not
## intuitive, so I will compute several UPA graphs with several m values, find the number of
## edges in each, and compare those values to the corresponding m values. For the DPA
## graph, I ran several tests, shown below, where a = create_dpa_graph(n, m) and b = edges:
## a = (100, 5), b = 424
## a = (100, 10), b = 759
## a = (200, 5), b = 883
## a = (200, 10), b = 1609
## a = (300, 5), b = 1340
## a = (300, 10), b = 2417
## a = (400, 5), b = 1856
## a = (400, 10), b = 3371
## a = (500, 5), b = 2301
## a = (500, 10), b = 4122
##
## Doubling m doubles the number of edges, on average, as expected, since you are making twice 
## as many connections (or trying to, since nodes chosen more than once are only counted once).
## Increasing n increasing the total edges by n * m, again on average. Starting from (100, 5) and going
## to (500, 5), the values increased by roughly 460, 460, 500, and 440. When m = 10, the same
## jumps were 850, 800, 960, and 750, or roughly 100 * 10 = 1000. 
##
## We know that n = 1239, so now we must compute an m that results in 3047 edges. Using that same
## analysis, a = (1239, m) starting with lower values of m, and running each ten times to improve
## the accuracy of results, we get:
## m = 1, total edges always eqals 1238 (no uncertainty since no chance of choosing same node twice)
## m = 2, total edges were 2451, 2457, 2451, 2456, 2448, 2448, 2438, 2449, 2447, 2453
## m = 3, total edges were 3610, 3606, 3636, 3629, 3625, 3631, 3628, 3642, 3617, 3647
## m = 4, total edges were 4698, 4725, ... and higher
## 
## This may not hold for UPA, though I suspect it will since the number of edges will be similar, the
## only difference will be in the implementation to represent a shared edge instead of a directed
## one each time an edge is added between two nodes. With m = 3, the total edges were only
## slightly closer on average (+563) than with m = 2 (-597), thus I will choose m = 3 if the analysis
## with the UPATrial and create_upa_graph implementation produces similar results. 
##
## As expected, for the UPA graph, m = 2 had total edges hovering around 2470, and m = 3 had 
## total edges around 3685. In this case, the total edges for m = 2 were closer (-577 vs. +638).
## Therefore, I will choose m = 2, and I imagine 2 OR 3 could work for this analysis. 

## Next write a function random_order that takes a graph and returns a list of the nodes in the graph
## in some random order.

def random_order(graph):
	"""
	Returns nodes in graph in a random order.
	"""
	all_nodes = [key for key in graph.keys()]
	random.shuffle(all_nodes)
	return all_nodes
	
## Then for each of the 3 graphs, compute a random attack using random_order and use this
## attack order in compute_resilience to compute the resilience of the graph. Below are the four
## functions from Module #1 Project #2 used to compute resilience of a graph.

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
network_order = random_order(network)
network_res = compute_resilience(network, network_order)
print network_res ## see below

erugraph = Graph(1239)
erugraph.convert_to_undir_er_graph(.002)
erugraph_order = random_order(erugraph.adjacency_dict())
erugraph_res = compute_resilience(erugraph.adjacency_dict(), erugraph_order)
print erugraph_res ## see below

upagraph = create_upa_graph(1239, 2)
upagraph_order = random_order(upagraph)
upagraph_res = compute_resilience(upagraph, upagraph_order)
print upagraph_res ## see below

network_res = 
	[1239, 1238, 1234, 1233, 1232, 1231, 1230, 1229, 1228, 1226, 1225, 1221, 1220, 1219, 1218, 
     1217, 1211, 1199, 1198, 1197, 1196, 1195, 1194, 1193, 1192, 1191, 1185, 1183, 1182, 1181, 
     1180, 1099, 1098, 1097, 1096, 1096, 1092, 1091, 1090, 1089, 1088, 1087, 1084, 1083, 1082, 
     1081, 1080, 1078, 1077, 1076, 1075, 1074, 1073, 1071, 1071, 1070, 1070, 1069, 1068, 1067, 
     1064, 1063, 1062, 1061, 1060, 1059, 1058, 1057, 1057, 1056, 1055, 1054, 1053, 1052, 1051, 
     1050, 1050, 1050, 1049, 1049, 1048, 1047, 1046, 1043, 1041, 1040, 1039, 1038, 1037, 1036, 
     1035, 1034, 1034, 1033, 1032, 1031, 1030, 1029, 1028, 1026, 1025, 1024, 1023, 1022, 1021, 
     1020, 1019, 1018, 1017, 1016, 1015, 1014, 1013, 1012, 1011, 1011, 1010, 1009, 1008, 1007, 
     1006, 1005, 1004, 1003, 1002, 1001, 1000, 999, 999, 998, 995, 994, 992, 991, 990, 989, 988, 
     987, 986, 985, 984, 983, 983, 982, 981, 980, 979, 978, 977, 976, 969, 967, 966, 965, 963, 
     962, 960, 959, 958, 957, 956, 956, 955, 954, 950, 949, 947, 946, 945, 944, 943, 942, 941, 
     940, 939, 938, 937, 936, 936, 935, 935, 935, 934, 932, 931, 931, 931, 930, 930, 929, 927, 
     927, 927, 926, 925, 924, 923, 922, 922, 921, 919, 918, 917, 916, 915, 914, 909, 908, 905, 
     904, 903, 902, 901, 900, 899, 898, 898, 897, 895, 894, 893, 892, 892, 891, 890, 888, 876, 
     875, 873, 872, 872, 871, 866, 865, 864, 863, 862, 861, 860, 858, 849, 848, 847, 846, 842, 
     840, 840, 840, 838, 837, 836, 830, 829, 818, 817, 816, 815, 814, 814, 812, 811, 810, 809, 
     806, 806, 805, 804, 804, 803, 802, 801, 801, 800, 799, 798, 798, 797, 796, 795, 794, 794, 
     790, 789, 787, 786, 785, 783, 783, 779, 779, 775, 774, 773, 772, 771, 769, 768, 767, 766, 
     766, 765, 764, 763, 762, 762, 761, 756, 755, 754, 753, 751, 751, 750, 750, 749, 748, 747, 
     747, 746, 745, 744, 743, 742, 741, 736, 735, 734, 734, 733, 732, 731, 731, 731, 730, 729, 
     728, 727, 726, 726, 724, 723, 722, 719, 718, 717, 716, 715, 714, 713, 712, 709, 706, 705, 
     704, 703, 699, 698, 697, 696, 695, 694, 693, 693, 692, 691, 690, 689, 689, 688, 687, 686, 
     685, 683, 683, 682, 681, 680, 678, 678, 676, 669, 668, 667, 666, 666, 665, 665, 663, 662, 
     661, 661, 660, 659, 658, 657, 656, 654, 653, 653, 652, 651, 650, 649, 649, 648, 647, 637, 
     637, 636, 635, 634, 634, 634, 631, 630, 629, 627, 626, 623, 622, 621, 620, 619, 618, 618, 
     612, 611, 610, 609, 608, 607, 606, 605, 604, 603, 602, 597, 596, 595, 594, 594, 593, 592, 
     591, 590, 589, 588, 587, 587, 586, 585, 585, 585, 584, 584, 583, 582, 581, 580, 579, 578, 
     577, 577, 577, 576, 576, 575, 574, 573, 573, 573, 572, 571, 570, 569, 568, 563, 562, 562, 
     561, 560, 559, 558, 557, 556, 555, 555, 554, 554, 553, 552, 552, 551, 550, 549, 549, 548, 
     548, 547, 547, 535, 534, 534, 533, 533, 533, 532, 531, 528, 528, 527, 527, 526, 525, 524, 
     523, 522, 522, 521, 517, 516, 515, 514, 514, 514, 513, 512, 512, 511, 510, 509, 492, 491, 
     490, 490, 489, 486, 484, 484, 483, 482, 481, 480, 479, 478, 477, 477, 476, 475, 474, 473, 
     473, 473, 472, 471, 470, 470, 469, 466, 466, 466, 465, 465, 465, 464, 463, 462, 461, 460, 
     459, 459, 458, 457, 456, 455, 454, 453, 452, 451, 450, 449, 449, 449, 449, 449, 449, 448, 
     447, 446, 445, 445, 444, 443, 443, 442, 440, 439, 439, 438, 438, 437, 436, 435, 425, 425, 
     424, 423, 420, 420, 419, 418, 418, 412, 409, 409, 408, 408, 408, 407, 407, 405, 404, 403, 
     403, 402, 401, 401, 401, 401, 400, 399, 398, 397, 397, 396, 396, 396, 395, 394, 387, 386, 
     386, 385, 385, 385, 385, 385, 384, 383, 381, 380, 380, 380, 380, 379, 378, 378, 377, 377, 
     375, 375, 374, 373, 373, 372, 372, 372, 372, 372, 371, 370, 370, 370, 369, 368, 368, 367, 
     366, 365, 364, 361, 361, 360, 359, 358, 358, 358, 358, 357, 357, 356, 354, 353, 353, 353, 
     352, 351, 350, 350, 350, 350, 349, 349, 349, 348, 347, 346, 345, 345, 343, 343, 342, 342, 
     336, 335, 333, 332, 331, 330, 330, 330, 330, 329, 328, 327, 326, 322, 321, 320, 320, 319, 
     318, 316, 315, 314, 310, 307, 306, 306, 305, 304, 303, 303, 301, 300, 300, 300, 299, 299, 
     298, 297, 297, 295, 294, 294, 293, 293, 293, 292, 291, 291, 291, 289, 287, 286, 286, 286, 
     284, 283, 283, 282, 281, 281, 280, 279, 278, 277, 276, 275, 274, 274, 273, 272, 272, 271, 
     271, 269, 268, 264, 264, 264, 264, 264, 264, 263, 263, 262, 262, 250, 250, 250, 250, 250, 
     250, 250, 247, 247, 245, 245, 245, 245, 244, 233, 231, 231, 229, 228, 228, 228, 227, 226, 
     226, 226, 225, 225, 225, 225, 225, 225, 222, 222, 219, 216, 215, 215, 215, 215, 215, 215, 
     215, 215, 214, 213, 213, 213, 212, 212, 212, 210, 210, 209, 208, 207, 207, 204, 203, 203, 
     202, 199, 196, 194, 194, 193, 192, 192, 191, 190, 190, 189, 187, 186, 185, 185, 184, 183, 
     182, 181, 181, 180, 179, 168, 168, 167, 167, 167, 167, 166, 166, 166, 166, 165, 165, 164, 
     164, 164, 164, 163, 162, 161, 161, 160, 159, 158, 158, 156, 155, 154, 154, 154, 152, 151, 
     151, 151, 143, 143, 143, 133, 133, 132, 132, 132, 132, 132, 132, 131, 131, 131, 131, 128, 
     128, 127, 127, 127, 126, 124, 124, 124, 123, 122, 122, 121, 120, 120, 120, 120, 120, 120, 
     119, 119, 119, 119, 119, 119, 119, 113, 111, 107, 107, 93, 93, 93, 93, 92, 90, 90, 90, 90, 
     89, 89, 87, 87, 87, 85, 85, 84, 84, 84, 84, 83, 83, 83, 83, 83, 82, 82, 81, 80, 80, 79, 79, 
     78, 78, 77, 77, 77, 76, 76, 76, 76, 76, 76, 75, 74, 74, 74, 58, 57, 57, 57, 57, 57, 57, 57, 
     57, 57, 57, 57, 57, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 53, 53, 53, 53, 53, 52, 
     51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 49, 49, 49, 48, 47, 47, 46, 46, 46, 46, 46, 
     46, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 25, 25, 25, 24, 24, 24, 24, 24, 24, 23, 23, 
     23, 23, 23, 23, 23, 22, 22, 13, 13, 13, 13, 13, 13, 13, 11, 11, 11, 11, 11, 11, 11, 11, 11, 
     11, 11, 11, 11, 11, 11, 11, 11, 11, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 7, 7, 7, 7, 7, 
     7, 7, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 
     5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 
     2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

erugraph_res = 
	[1228, 1227, 1226, 1225, 1224, 1223, 1222, 1221, 1220, 1219, 1217, 1215, 1214, 1212, 1211, 
     1210, 1209, 1208, 1207, 1206, 1204, 1203, 1202, 1201, 1200, 1199, 1198, 1197, 1196, 1195, 
     1194, 1194, 1193, 1192, 1191, 1190, 1189, 1188, 1187, 1186, 1185, 1184, 1183, 1182, 1181, 
     1180, 1179, 1178, 1177, 1176, 1175, 1174, 1173, 1172, 1171, 1170, 1168, 1167, 1166, 1165, 
     1164, 1163, 1162, 1161, 1160, 1159, 1158, 1157, 1156, 1155, 1154, 1151, 1150, 1149, 1146, 
     1145, 1144, 1143, 1142, 1141, 1140, 1139, 1138, 1137, 1136, 1135, 1134, 1133, 1132, 1131, 
     1130, 1129, 1128, 1127, 1126, 1125, 1124, 1123, 1122, 1121, 1120, 1119, 1118, 1117, 1116, 
     1115, 1114, 1113, 1112, 1111, 1110, 1109, 1108, 1107, 1106, 1105, 1104, 1102, 1101, 1100, 
     1099, 1098, 1097, 1096, 1095, 1094, 1093, 1092, 1091, 1090, 1089, 1088, 1087, 1086, 1085, 
     1084, 1083, 1082, 1081, 1080, 1079, 1078, 1077, 1076, 1075, 1074, 1073, 1072, 1071, 1070, 
     1070, 1067, 1067, 1066, 1065, 1064, 1063, 1062, 1061, 1060, 1059, 1058, 1057, 1056, 1055, 
     1054, 1053, 1052, 1051, 1050, 1049, 1048, 1047, 1046, 1045, 1044, 1043, 1041, 1040, 1038, 
     1037, 1036, 1035, 1034, 1033, 1032, 1031, 1030, 1029, 1028, 1026, 1025, 1024, 1023, 1022, 
     1021, 1020, 1019, 1018, 1017, 1016, 1015, 1014, 1013, 1012, 1010, 1009, 1008, 1007, 1006, 
     1005, 1005, 1004, 1003, 1002, 1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989,
     988, 987, 986, 985, 984, 983, 982, 981, 980, 979, 978, 977, 974, 973, 972, 971, 970, 969, 
     967, 966, 965, 964, 963, 962, 961, 959, 958, 957, 956, 955, 954, 952, 951, 950, 949, 948, 
     947, 946, 945, 943, 942, 941, 940, 939, 938, 937, 936, 935, 934, 933, 932, 931, 931, 929, 
     928, 927, 926, 925, 924, 922, 921, 920, 918, 917, 916, 914, 913, 912, 911, 909, 908, 907, 
     906, 905, 902, 901, 900, 899, 898, 898, 897, 896, 895, 894, 893, 892, 891, 890, 889, 888, 
     887, 886, 885, 884, 883, 882, 881, 879, 878, 877, 876, 875, 874, 873, 872, 871, 870, 869, 
     868, 867, 866, 865, 864, 863, 862, 861, 860, 859, 858, 857, 856, 855, 854, 853, 849, 848, 
     847, 846, 845, 844, 843, 842, 841, 840, 839, 837, 836, 835, 834, 831, 830, 829, 828, 827, 
     826, 825, 824, 823, 822, 820, 819, 818, 818, 817, 816, 814, 813, 812, 811, 810, 809, 808, 
     807, 806, 805, 803, 802, 801, 798, 797, 796, 795, 794, 793, 790, 789, 788, 787, 787, 786, 
     785, 784, 782, 780, 779, 779, 778, 777, 775, 774, 773, 772, 771, 770, 769, 768, 766, 765, 
     764, 763, 763, 762, 761, 760, 760, 759, 758, 755, 754, 753, 752, 751, 750, 749, 748, 746, 
     746, 745, 744, 743, 742, 741, 740, 739, 738, 735, 734, 733, 732, 731, 730, 729, 728, 727, 
     726, 725, 724, 722, 721, 720, 719, 718, 718, 717, 716, 715, 714, 712, 711, 710, 709, 709, 
     708, 706, 703, 702, 700, 699, 698, 696, 695, 694, 693, 692, 691, 690, 688, 687, 686, 684, 
     684, 683, 682, 681, 681, 680, 680, 679, 679, 678, 677, 674, 673, 667, 665, 662, 661, 660, 
     659, 658, 658, 657, 656, 655, 654, 653, 653, 652, 650, 649, 648, 647, 646, 645, 644, 643, 
     642, 641, 640, 639, 638, 637, 636, 635, 634, 633, 632, 632, 632, 631, 630, 629, 628, 627, 
     624, 622, 621, 620, 620, 619, 618, 617, 616, 615, 614, 613, 609, 608, 606, 605, 604, 603, 
     602, 600, 599, 596, 594, 593, 592, 591, 590, 589, 588, 587, 586, 585, 584, 582, 581, 580, 
     579, 578, 577, 576, 575, 574, 573, 573, 572, 571, 570, 568, 567, 566, 561, 560, 559, 559, 
     558, 557, 556, 553, 552, 552, 549, 548, 547, 546, 545, 544, 542, 541, 540, 539, 538, 537, 
     536, 535, 534, 533, 532, 529, 528, 527, 524, 523, 520, 520, 519, 519, 518, 517, 517, 516, 
     515, 514, 513, 512, 511, 510, 508, 506, 505, 504, 504, 503, 502, 501, 500, 500, 498, 494, 
     493, 492, 490, 489, 489, 489, 485, 482, 482, 480, 479, 477, 476, 475, 474, 473, 471, 470, 
     469, 468, 467, 466, 466, 466, 466, 464, 463, 463, 461, 460, 459, 458, 456, 451, 450, 449, 
     448, 446, 443, 439, 438, 437, 433, 432, 431, 430, 428, 427, 426, 425, 424, 423, 422, 421, 
     421, 421, 420, 419, 419, 416, 416, 415, 415, 414, 412, 410, 408, 407, 406, 405, 402, 396, 
     395, 394, 394, 392, 392, 390, 390, 389, 388, 387, 384, 383, 383, 382, 381, 380, 379, 379, 
     378, 377, 376, 375, 375, 375, 375, 374, 374, 374, 373, 372, 368, 368, 362, 361, 360, 354, 
     353, 352, 352, 352, 351, 347, 347, 347, 346, 342, 341, 341, 340, 337, 336, 333, 333, 333, 
     332, 317, 316, 315, 313, 311, 310, 309, 306, 305, 305, 299, 299, 293, 292, 292, 291, 291, 
     291, 290, 290, 290, 289, 288, 287, 287, 286, 286, 286, 284, 283, 282, 282, 282, 282, 282, 
     281, 280, 280, 280, 276, 276, 274, 273, 272, 268, 266, 265, 264, 264, 263, 263, 260, 260, 
     259, 258, 258, 258, 257, 256, 256, 256, 256, 255, 254, 253, 249, 249, 246, 246, 245, 245, 
     244, 241, 241, 237, 236, 235, 234, 233, 227, 226, 224, 224, 223, 210, 210, 209, 199, 193, 
     193, 192, 192, 192, 191, 191, 191, 190, 190, 189, 187, 186, 185, 184, 184, 183, 182, 181, 
     180, 180, 180, 180, 180, 179, 179, 177, 176, 175, 175, 175, 173, 173, 171, 161, 160, 160, 
     160, 158, 157, 157, 157, 154, 153, 153, 153, 153, 139, 136, 136, 135, 135, 125, 125, 125, 
     125, 124, 116, 116, 112, 112, 112, 112, 112, 112, 111, 110, 110, 110, 110, 110, 99, 94, 94, 
     94, 94, 93, 93, 93, 93, 93, 93, 93, 93, 90, 90, 89, 89, 89, 89, 89, 89, 88, 88, 88, 88, 88, 
     88, 88, 88, 88, 87, 86, 86, 86, 85, 85, 85, 84, 84, 84, 84, 84, 84, 84, 84, 84, 82, 82, 82, 
     81, 48, 48, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 36, 36, 
     36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 24, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 12, 
     12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 
     12, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 6, 6, 6, 6, 6, 6, 6, 6, 
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 
     5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 
     4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
     3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 
     2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

upagraph_res = 
	[1239, 1238, 1237, 1236, 1235, 1234, 1233, 1232, 1231, 1230, 1229, 1228, 1227, 1226, 1225, 
     1224, 1223, 1222, 1221, 1220, 1219, 1218, 1217, 1216, 1215, 1214, 1213, 1212, 1211, 1210, 
     1209, 1208, 1207, 1206, 1205, 1204, 1203, 1202, 1200, 1199, 1198, 1197, 1196, 1195, 1194, 
     1193, 1192, 1191, 1190, 1189, 1188, 1187, 1186, 1185, 1184, 1183, 1182, 1181, 1180, 1179, 
     1178, 1177, 1176, 1175, 1174, 1173, 1172, 1171, 1170, 1169, 1168, 1167, 1166, 1165, 1164, 
     1163, 1162, 1161, 1160, 1159, 1158, 1157, 1156, 1155, 1153, 1152, 1151, 1150, 1149, 1148, 
     1147, 1146, 1144, 1143, 1142, 1141, 1140, 1139, 1138, 1137, 1136, 1135, 1134, 1133, 1131, 
     1130, 1129, 1128, 1127, 1126, 1125, 1124, 1123, 1121, 1120, 1119, 1118, 1117, 1116, 1115, 
     1114, 1112, 1110, 1109, 1108, 1107, 1106, 1105, 1104, 1103, 1102, 1101, 1100, 1099, 1097, 
     1096, 1095, 1092, 1091, 1090, 1089, 1088, 1087, 1086, 1085, 1083, 1082, 1081, 1078, 1077, 
     1076, 1075, 1074, 1072, 1071, 1070, 1068, 1067, 1066, 1064, 1062, 1061, 1060, 1059, 1058, 
     1057, 1056, 1055, 1054, 1053, 1052, 1051, 1050, 1049, 1048, 1047, 1046, 1045, 1044, 1043, 
     1042, 1041, 1040, 1040, 1039, 1037, 1036, 1035, 1034, 1033, 1032, 1031, 1030, 1029, 1028, 
     1026, 1024, 1023, 1022, 1021, 1020, 1019, 1018, 1017, 1016, 1015, 1014, 1013, 1012, 1011, 
     1010, 1009, 1008, 1007, 1006, 1005, 1004, 1003, 1002, 1001, 1000, 997, 996, 993, 992, 991,
     990, 989, 988, 987, 986, 985, 984, 984, 983, 982, 981, 980, 979, 978, 975, 974, 972, 971, 
     970, 969, 968, 967, 966, 965, 962, 960, 959, 958, 957, 956, 955, 954, 953, 952, 951, 949, 
     948, 947, 946, 945, 944, 943, 942, 941, 939, 938, 937, 936, 935, 934, 933, 932, 932, 931, 
     930, 929, 928, 927, 926, 925, 924, 923, 922, 921, 920, 919, 918, 914, 913, 912, 911, 910, 
     909, 907, 906, 905, 904, 903, 902, 901, 900, 899, 893, 892, 891, 890, 888, 887, 886, 885, 
     884, 883, 882, 881, 878, 877, 876, 875, 874, 873, 872, 870, 867, 866, 865, 864, 863, 861, 
     860, 858, 857, 856, 855, 853, 852, 849, 849, 849, 848, 847, 846, 845, 844, 843, 841, 840, 
     838, 836, 835, 834, 833, 832, 831, 830, 829, 828, 827, 826, 825, 823, 822, 821, 820, 819, 
     818, 817, 815, 814, 813, 812, 810, 809, 808, 807, 806, 805, 802, 801, 800, 799, 798, 797, 
     796, 795, 794, 792, 791, 790, 788, 787, 786, 786, 785, 783, 782, 782, 780, 778, 777, 775, 
     774, 773, 770, 768, 766, 765, 764, 764, 763, 763, 762, 761, 760, 757, 756, 755, 754, 753, 
     752, 750, 749, 748, 747, 747, 745, 744, 743, 742, 741, 740, 739, 738, 737, 733, 732, 731, 
     730, 727, 723, 722, 716, 715, 714, 712, 709, 707, 705, 704, 703, 702, 702, 701, 700, 699, 
     698, 696, 693, 692, 692, 691, 690, 689, 686, 685, 684, 683, 682, 681, 680, 674, 673, 671, 
     670, 667, 666, 665, 662, 661, 660, 657, 655, 653, 651, 650, 649, 648, 646, 644, 643, 642, 
     642, 642, 640, 639, 638, 637, 636, 635, 631, 630, 626, 623, 622, 622, 618, 616, 615, 614, 
     614, 613, 609, 608, 607, 606, 605, 604, 601, 600, 599, 598, 597, 596, 595, 594, 593, 592, 
     588, 588, 587, 578, 574, 573, 572, 571, 570, 569, 568, 568, 567, 566, 566, 565, 563, 562, 
     561, 559, 557, 556, 555, 553, 552, 547, 546, 545, 542, 541, 541, 541, 538, 537, 536, 526, 
     521, 519, 518, 517, 517, 515, 514, 513, 513, 513, 512, 511, 509, 508, 508, 507, 506, 506, 
     505, 505, 503, 502, 501, 498, 498, 496, 493, 492, 486, 486, 468, 467, 467, 466, 465, 463, 
     463, 463, 461, 461, 458, 457, 456, 455, 453, 452, 452, 448, 447, 447, 447, 446, 445, 443, 
     437, 437, 436, 435, 434, 432, 431, 429, 428, 422, 414, 413, 412, 412, 412, 412, 412, 412, 
     411, 410, 409, 409, 408, 399, 398, 397, 397, 396, 396, 396, 395, 395, 391, 390, 389, 389, 
     388, 387, 386, 385, 385, 384, 383, 383, 383, 382, 381, 380, 379, 368, 366, 365, 364, 362, 
     362, 361, 357, 357, 357, 355, 352, 352, 348, 348, 346, 346, 342, 342, 342, 341, 340, 340, 
     339, 338, 333, 320, 320, 319, 318, 317, 317, 317, 317, 316, 315, 314, 314, 313, 312, 311, 
     311, 311, 310, 305, 305, 303, 298, 298, 297, 297, 297, 296, 296, 296, 296, 293, 293, 293, 
     293, 293, 292, 289, 288, 288, 287, 286, 286, 286, 286, 282, 282, 282, 271, 271, 271, 271, 
     269, 268, 268, 267, 266, 266, 266, 265, 265, 265, 264, 264, 264, 263, 262, 258, 257, 257, 
     257, 257, 256, 256, 255, 255, 254, 254, 251, 245, 245, 242, 242, 242, 242, 241, 241, 241, 
     239, 238, 236, 236, 235, 234, 233, 233, 230, 230, 230, 228, 228, 227, 227, 227, 226, 220, 
     220, 218, 218, 217, 217, 217, 216, 214, 210, 209, 209, 208, 208, 208, 207, 207, 197, 197, 
     189, 189, 188, 186, 186, 186, 186, 180, 180, 173, 173, 173, 172, 172, 172, 171, 171, 171, 
     160, 160, 158, 157, 157, 157, 156, 156, 156, 156, 155, 148, 138, 136, 135, 135, 135, 135, 
     133, 133, 133, 133, 132, 132, 132, 132, 132, 132, 132, 132, 127, 127, 122, 122, 122, 121, 
     116, 114, 114, 113, 113, 113, 113, 113, 112, 112, 112, 112, 112, 112, 112, 112, 112, 102, 
     102, 102, 101, 101, 101, 101, 101, 100, 99, 98, 96, 91, 91, 91, 91, 88, 88, 88, 88, 88, 88, 
     78, 74, 71, 71, 71, 71, 71, 71, 71, 71, 69, 67, 67, 67, 67, 67, 67, 67, 67, 67, 66, 66, 66, 
     66, 66, 66, 65, 65, 65, 65, 65, 65, 65, 65, 63, 63, 63, 63, 63, 62, 56, 55, 55, 55, 55, 55, 
     55, 55, 55, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 17, 17, 17, 17, 17, 17, 17, 17, 17, 14, 
     14, 14, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 12, 12, 12, 12, 11, 11, 11, 11, 11, 11, 
     11, 11, 11, 11, 11, 11, 11, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 
     10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 
     8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 
     7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 
     5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 
     4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 
     2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
     2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
	 
## Plot the 3 resilience lists

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

simpleplot.plot_lines("Graph Resilience Using Random Attack Order on All Nodes", 
                      700, 600, "No. of Nodes Removed", "Size of Largest CC Left", 
                      [netplot, eruplot, upaplot], False,
                      ["Network Graph", "ER Graph (p=0.002)", "UPA Graph (m=2)"])
					  
## ANSWER
# See AlgThink_App2-1_Plot