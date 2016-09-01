"""
Coursera / Rice University
Algorithmic Thinking (Part 1)
Application 1
Final Version
"""
#################################################
#################################################
# This is a cleaned up and combined version of AlgThink_App1-1, 
# AlgThink_App1-2, AlgThink_App1-3, AlgThink_App1-4, and AlgThink_App1-5.
# All code for this assignment is shown below with only essential imports.
# Some comments may have been left to provide context.
# Distinct sections/questions are enclosed in ## containers.
# All computations done in Desktop python to avoid runtime issues.
# Code provided by Rice University has been modified whenever applicable.
# Questions enclosed in functions precede a call to their function.
#################################################

## All import statements needed.

import math
import matplotlib.pyplot as plt
import random
import time
import urllib2
random.seed(1)

## Enter compute_in_degrees() and in_degree_distribution() functions from
## Project 1 for use in Application 1.

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
    unique_in_degrees = set([value for value in in_degree_count.values()])
    
    in_degree_dist = {}
    for in_degree in unique_in_degrees:
        in_degree_dist[in_degree] = 0
    for in_degree in all_in_degrees:
        in_degree_dist[in_degree] += 1

    return in_degree_dist
	
## Code below was provided for 1-1.

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
	
## Write helper functions for normalization of list data.

def normalize_list(a_list):
    """
    Function that normalizes a list of data.
    """
    if len(a_list) <1:
        return float('nan')
    divisor = float(sum(a_list))
    return [item / divisor for item in a_list]

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

## Write a function to build the log/log plot. Modified to account
## for Desktop Python use instead of CodeSkulptor use.

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
	
## Write a Graph class to create a graph with the necessary attributes in 1-2.

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
						
						
## Provided code for DPATrial class, used to implement efficient version of
## DPA algm in 1-4.

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
		
		
## From Project 1, use the make_complete_graph() function in 1-4.

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
#################################################

# Many helper functions are created here that will be used for subsequent
# questions. Plotting functions will need to be used differently for use in
# Desktop Python (PyCharm IDE).

def app_101():
	'''
	QUESTION 1

	For this question, your task is to load a provided citation graph for 
	27,770 high energy physics theory papers. This graph has 352,768 edges. 
	You should use the following code to load the citation graph as a dictionary. 
	In CodeSkulptor, loading the graph should take 5-10 seconds. (For an extra 
	challenge, you are welcome to write your own function to create the citation 
	graph by parsing this text representation of the citation graph.)

	Your task for this question is to compute the in-degree distribution for this 
	citation graph. Once you have computed this distribution, you should normalize 
	the distribution (make the values in the dictionary sum to one) and then compute 
	a log/log plot of the points in this normalized distribution. How you create 
	this point plot is up to you. You are welcome to use a package such as matplotlib 
	for desktop Python, use the simpleplot module in CodeSkulptor, or use any other 
	method that you wish. This class page on "Creating, formatting, and comparing 
	plots" gives an overview of some of the options that we recommend for creating 
	plots.

	Since simpleplot does not support direct log/log plotting, you may simulate 
	log/log plotting as shown in this example from the PoC video on "Plotting data". 
	However, be sure to include an indication on the labels for the horizontal and 
	vertical axes that you are plotting the log of the values and note the base that 
	you are using. (Nodes with in-degree zero can be ignored when computing the 
	log/log plot since log(0)=-INF).

	Once you have created your plot, upload your plot in the box below using 
	"Attach a file" button (the button is disabled under the 'html' edit mode; 
	you must be under the 'Rich' edit mode for the button to be enabled). Please 
	review the class guidelines for formatting and comparing plots on the "Creating, 
	formatting, and comparing plots" class page. These guidelines cover the basics 
	of good formatting practices for plots. Your plot will be assessed based on the 
	answers to the following three questions:

	Does the plot follow the formatting guidelines for plots?
	Is the plot that of a normalized distribution on a log/log scale?
	Is the content of the plot correct?
	'''
	
	# Write helper functions for normalization of list data, add to shared classes/functions.
	# Write a function to build the log/log plot, add to shared classes/functions.
	# Load graph, compute in-degree distribution, normalize it, and create log/log plot.
	
	citation_graph = load_graph(CITATION_URL)
	in_deg_dist = in_degree_distribution(citation_graph)
	norm_dist  = dict_to_normalized_lists(in_deg_dist)
	norm_dist_plot = build_loglog_plot(norm_dist)
	
	# Plot using matplotlib module.
	
	x_val = [norm_dist_plot[idx][0] for idx in range(len(norm_dist_plot))]
	y_val = [norm_dist_plot[idx][1] for idx in range(len(norm_dist_plot))]
	
	fig = plt.figure(figsize = (8, 7), dpi = 100)
	scatter = plt.scatter(x_val, y_val, color='r')
	plt.title("Citation Graph: Normalized In-degree Distribution (log/log)")
	plt.xlabel("log10(In-degree Number")
	plt.ylabel("log10(Normalized Distribution")
	plt.show()

## ANSWER
#app_101()
# See AlgThink_1-1_Plot or AlgThink_1-1_Plot_HiRes
#################################################

# Use many of the same shared functions. Though the Graph class will only be
# used by 1-2, it will be placed in the shared area due to its size and nature.

def app_102():
	'''
	QUESTION 2
	
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
	
	# For this, I created 4 graphs using p = .1, .3, .6, and .9, n = 300.
	
	digraph_0 = Graph(300)
	digraph_0.convert_to_dir_er_graph(.1)
	digraph_1 = Graph(300)
	digraph_1.convert_to_dir_er_graph(.3)
	digraph_2 = Graph(300)
	digraph_2.convert_to_dir_er_graph(.6)
	digraph_3 = Graph(300)
	digraph_3.convert_to_dir_er_graph(.9)
	
	# Compute in-degree dist for each, normalize them, and create log/log plots.
	
	indegdist_0 = in_degree_distribution(digraph_0.adjacency_dict())
	indegdist_1 = in_degree_distribution(digraph_1.adjacency_dict())
	indegdist_2 = in_degree_distribution(digraph_2.adjacency_dict())
	indegdist_3 = in_degree_distribution(digraph_3.adjacency_dict())
	
	normdist_0 = dict_to_normalized_lists(indegdist_0)
	normdist_1 = dict_to_normalized_lists(indegdist_1)
	normdist_2 = dict_to_normalized_lists(indegdist_2)
	normdist_3 = dict_to_normalized_lists(indegdist_3)

	plot_0 = build_loglog_plot(normdist_0)
	plot_1 = build_loglog_plot(normdist_1)
	plot_2 = build_loglog_plot(normdist_2)
	plot_3 = build_loglog_plot(normdist_3)
	
	# Plot using matplotlib module.
	
	x_val_0 = [plot_0[idx][0] for idx in range(len(plot_0))]
	y_val_0 = [plot_0[idx][1] for idx in range(len(plot_0))]
	x_val_1 = [plot_1[idx][0] for idx in range(len(plot_1))]
	y_val_1 = [plot_1[idx][1] for idx in range(len(plot_1))]
	x_val_2 = [plot_2[idx][0] for idx in range(len(plot_2))]
	y_val_2 = [plot_2[idx][1] for idx in range(len(plot_2))]
	x_val_3 = [plot_3[idx][0] for idx in range(len(plot_3))]
	y_val_3 = [plot_3[idx][1] for idx in range(len(plot_3))]
	
	fig = plt.figure(figsize = (8, 7), dpi = 100)
	scatter_0 = plt.scatter(x_val_0, y_val_0, color='r', label="p = .1")
	scatter_1 = plt.scatter(x_val_1, y_val_1, color='g', label="p = .3")
	scatter_2 = plt.scatter(x_val_2, y_val_2, color='b', label="p = .6")
	scatter_3 = plt.scatter(x_val_3, y_val_3, color='p', label="p = .9")
	plt.legend()
	plt.title("ER Digraphs: Normalized In-degree Distribution (log/log)")
	plt.xlabel("log10(In-degree Number")
	plt.ylabel("log10(Normalized Distribution")
	plt.show()
	
	answer = "See string in function."
	
	"""
	1.) Yes. The ER algorithm treats each node in the graph in the same manner. 	
	So the expected in-degree for each node must be the same. In fact, the 
	in-degree 	distribution is the same for each node.

	2.) The in-degree distribution for an ER digraph plot looks like an inverted 
	parabola when probability p is low (below 0.5) and a spike when probability 
	p is high (above 0.5). The in-degree numbers increased along with probability
	that an edge would be made between 2 nodes. See attached graph. It appears 
	to follow a Poisson distribution. For each of the ER digraphs in the attached file, 
	n = 300. It is of note that increasing n from 300 to 700 (not shown) decreased 
	the spread of each curve, creating narrower spikes. 

	3.) The ER digraph plot shape differs greatly from the citation digraph shape. 
	In the ER plot, as the in-degree number increases, so does the distribution, 
	but only until a maximum point is reached at roughly the halfway point; then 
	as the in-degree number increases from there on, the distribution decreases. 
	In the citation plot, the first in-degree number has the highest distribution, and 
	then there is a gradual decrease in distribution as the in-degree number increases.
	"""
	
	return answer
	
## ANSWER
#app_102()
# See AlgThink_App1-2_Plot or AlgThink_App1-2_Plot_HiRes
#################################################

# Question 1-3 is text-only, and the answer will be a returned string.

def app_103():
	'''
	QUESTION 3
	
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
	
	answer = "See string in function."
	
	"""
	The citation graph has 27,770 nodes, so the DPA graph will also have 
	n = 27,770 nodes. 

	If m is to equal an integer close to the average out-degree of the citation 
	graph, then m would be equal to the total number of out-degrees divided 
	by the total number of nodes. The total number of out-degrees is equal to 
	the total number of in-degrees, which is just the number of edges in the 
	graph. You can divide the number of edges by the total number of nodes 
	(and not just the nodes with either in- or out-degrees, since zero values 
	are counted as well when calculating averages) to get 12. For the DPA 
	graph, m = 12 edges.
	"""
	
	return answer
		
## ANSWER
#app_103()
#################################################

# Once again, the functions written for 1-4 will be added to the bottom of the shared
# class/function area. This includes a provided DPATrial class, as well as a function
# from Project 1.

def app_104():
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
	
	# Remember from 1-3 that m = 12, n = 27770
	# Write a function that executes the DPA algorithm for n and m.
	# For the pseudocode, reference the OneNote file or AlgThink_App1-4.py.
	
	def create_dpa_graph(n = 0, m = 0):
		"""
		Function to create a DPA graph with m initial nodes and n total nodes.
		All nine DPA algm steps will be identified where applicable.
		"""
		digraph = make_complete_graph(m)
		trial = DPATrial(m)
		
		for index in range(m, n):
			new_neighbors = trial.run_trial(m)
			digraph[index] = new_neighbors
			
		return digraph
	
	# Create a DPA graph with m = 12 and n = 28000, compute in-degrees,
	# normalize distribution, and build a log/log plot. 
	
	graph = create_dpa_graph(28000, 12)
	indegdist = in_degree_distribution(graph)
	normdist = dict_to_normalized_lists(indegdist)
	plot = build_loglog_plot(normdist)
	
	# Plot scatter of graph using matplotlib module.
	
	x_val = [plot[idx][0] for idx in range(len(plot))]
	y_val = [plot[idx][1] for idx in range(len(plot))]
	
	fig = plt.figure(figsize = (8, 7), dpi = 100)
	scatter = plt.scatter(x_val, y_val, color='r', label="n=28000, m=12")
	plt.title("DPA Graph: Normalized In-Degree Distribution (log/log)")
	plt.legend()
	plt.xlabel("log10(In-degree Number")
	plt.ylabel("log10(Normalized Distribution")
	plt.show()
		
## ANSWER
#app_104()
# See AlgThink_App1-4_Plot or AlgThink_App1-4_Plot_HiRes
#################################################
	
# Question 1-5 is text-only, and the answer will be a returned string.

def app_105():
	'''
	In this last problem, we will compare the in-degree distribution for 
	the citation graph to the in-degree distribution for the DPA graph 
	as constructed in Question 4. In particular, we will consider whether 
	the shape of these two distributions are similar and, if they are 
	similar, what might be the cause of the similarity.

	To help you in your analysis, you should consider the following three 
	phenomena:

	The "six degrees of separation" phenomenon,
	The "rich gets richer" phenomenon, and
	The "Hierarchical structure of networks" phenomenon.

	If you're not familiar with these phenomena, you can read about them 
	by conducting a simple Google or Wikipedia search. Your task for this 
	problem is to consider how one of these phenomena might explain the 
	structure of the citation graph or, alternatively, how the citations patterns 
	follow one of these phenomena. 

	When answering this question, please include answers to the following:

	Is the plot of the in-degree distribution for the DPA graph similar to that of 
	the citation graph? Provide a short explanation of the similarities or differences. 
	Focus on the various properties of the two plots as discussed in the class page 
	on "Creating, formatting, and comparing plots".

	Which one of the three social phenomena listed above mimics the behavior of 
	the DPA process? Provide a short explanation for your answer.

	Could one of these phenomena explain the structure of the physics citation 
	graph? Provide a short explanation for your answer.
	'''
	
	answer = "See string in function."
	
	"""
	1.) The plot of the in-degree distribution for the DPA graph is indeed similar to 
	that 	of the citation graph. Both plots begin with the first in-degree number at 
	the maximum distribution and then gradually decrease in distribution as the 
	in-degree number increases. At very high in-degree numbers, the plot becomes 
	"dirtier" and the somewhat continuous 	best fit line splits into multiple lines.

	2.) The "rich gets richer" phenomenon mimics the DPA process. The DPA graph 
	begins as a complete digraph with m  nodes. With each node addition up to n 
	nodes, the algorithm chooses m random nodes from the existing set of nodes 
	to which the new node is linked. The probability of choosing a node via this 
	process is directly related to the number of in-degrees that each existing node 
	has, since the numerator of the probability function is the number of in-degrees 
	that an existing node (j) has, plus 1. As the number of in-degrees of a 
	particular node increases, so does the probability of that node being chosen in 
	the next node addition. This effect is compounded with each addition. 

	3.) This "rich gets richer" phenomenon could explain the structure of the 
	physics citation graph very easily. Scientific research has always been built 
	on the foundation of all research that has come before it. Certain underlying 
	principles in a particular field (like physics theory) will be discovered when 
	repeated study is applied to the data that stem from their existence. 
	Subsequent research studies will refer to these principles as a basis for their 
	new approaches and experiments. Slowly over time, as evidence builds 
	toward newer theories, more principles are revealed, and these new principles 
	become popular, more modern points of reference--although often they do 
	not entirely supplant the originally-discovered, "fundamental" principles. An 
	example in the field of Physics is Newton's laws of motion, laying the 
	foundation for classical mechanics. These principles lead to the understanding 
	of projectile motion, which eventually leads to the understanding of rocket 
	ships and ultimately space travel and beyond. 
	"""
	
	return answer
		
## ANSWER
#app_105()
#################################################
#################################################