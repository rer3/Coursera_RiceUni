"""
Rice University / Coursera: Algorithmic Thinking (Part 1)
Application 1-1
"""
'''
Provided code for Application portion of Module 1

Imports physics citation graph 
Question 1 (4 pts)

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

## Enter compute_in_degrees() and in_degree_distribution() functions from
## Project #1 for use here.
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

## Write helper functions for normalization of dist data.
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

# Load graph from URL
citation_graph = load_graph(CITATION_URL)
# Compute in-degree distribution of graph
indegdist = in_degree_distribution(citation_graph)
# Normalize the distribution
normdist = dict_to_normalized_lists(indegdist)
# Compute a log/log plot of the points in the distribution
nordisplot = build_loglog_plot(normdist)
simpleplot.plot_scatter("Citation Graph: Normalized In-degree Distribution (log/log)", 700, 600, 
                        "log10(In-degree Number)", "log10(Normalized Distribution)", [nordisplot])
                        
## ANSWER
## See file AlgThink_App1-1_Plot