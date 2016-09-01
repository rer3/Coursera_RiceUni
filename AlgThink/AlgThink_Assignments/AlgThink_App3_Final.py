"""
Coursera / Rice University
Algorithmic Thinking (Part 2)
Application 3
Final Version
"""
#################################################
#################################################
# This is a cleaned up version of AlgThink_App3-3.py.
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

## Provided Cluster class:

class Cluster:
    """
    Class for creating and merging clusters of counties
    """
    
    def __init__(self, fips_codes, horiz_pos, vert_pos, population, risk):
        """
        Create a cluster based the models a set of counties' data
        """
        self._fips_codes = fips_codes
        self._horiz_center = horiz_pos
        self._vert_center = vert_pos
        self._total_population = population
        self._averaged_risk = risk
        
        
    def __repr__(self):
        """
        String representation assuming the module is "alg_cluster".
        """
        rep = "alg_cluster.Cluster("
        rep += str(self._fips_codes) + ", "
        rep += str(self._horiz_center) + ", "
        rep += str(self._vert_center) + ", "
        rep += str(self._total_population) + ", "
        rep += str(self._averaged_risk) + ")"
        return rep


    def fips_codes(self):
        """
        Get the cluster's set of FIPS codes
        """
        return self._fips_codes
    
    def horiz_center(self):
        """
        Get the averged horizontal center of cluster
        """
        return self._horiz_center
    
    def vert_center(self):
        """
        Get the averaged vertical center of the cluster
        """
        return self._vert_center
    
    def total_population(self):
        """
        Get the total population for the cluster
        """
        return self._total_population
    
    def averaged_risk(self):
        """
        Get the averaged risk for the cluster
        """
        return self._averaged_risk
           
    def copy(self):
        """
        Return a copy of a cluster
        """
        copy_cluster = Cluster(set(self._fips_codes), self._horiz_center, self._vert_center,
                               self._total_population, self._averaged_risk)
        return copy_cluster

    def distance(self, other_cluster):
        """
        Compute the Euclidean distance between two clusters
        """
        vert_dist = self._vert_center - other_cluster.vert_center()
        horiz_dist = self._horiz_center - other_cluster.horiz_center()
        return math.sqrt(vert_dist ** 2 + horiz_dist ** 2)
        
    def merge_clusters(self, other_cluster):
        """
        Merge one cluster into another
        The merge uses the relatively populations of each
        cluster in computing a new center and risk
        
        Note that this method mutates self
        """
        if len(other_cluster.fips_codes()) == 0:
            return self
        else:
            self._fips_codes.update(set(other_cluster.fips_codes()))
 
            # compute weights for averaging
            self_weight = float(self._total_population)                        
            other_weight = float(other_cluster.total_population())
            self._total_population = self._total_population + other_cluster.total_population()
            self_weight /= self._total_population
            other_weight /= self._total_population
                    
            # update center and risk using weights
            self._vert_center = self_weight * self._vert_center + other_weight * other_cluster.vert_center()
            self._horiz_center = self_weight * self._horiz_center + other_weight * other_cluster.horiz_center()
            self._averaged_risk = self_weight * self._averaged_risk + other_weight * other_cluster.averaged_risk()
            return self

    def cluster_error(self, data_table):
        """
        Input: data_table is the original table of cancer data used in creating the cluster.
        
        Output: The error as the sum of the square of the distance from each county
        in the cluster to the cluster center (weighted by its population)
        """
        # Build hash table to accelerate error computation
        fips_to_line = {}
        for line_idx in range(len(data_table)):
            line = data_table[line_idx]
            fips_to_line[line[0]] = line_idx
        
        # compute error as weighted squared distance from counties to cluster center
        total_error = 0
        counties = self.fips_codes()
        for county in counties:
            line = data_table[fips_to_line[county]]
            singleton_cluster = Cluster(set([line[0]]), line[1], line[2], line[3], line[4])
            singleton_distance = self.distance(singleton_cluster)
            total_error += (singleton_distance ** 2) * singleton_cluster.total_population()
        return total_error


## Helper function provided and five algorithms implemented in Project 3 from 
## pseudocode:

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters
    in a list.

    Input: cluster_list is list of clusters, idx1 and idx2 are integer 
    indices for two clusters.
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2].
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2),
            max(idx1, idx2))

def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the 
    clusters cluster_list[idx1] and cluster_list[idx2] have minimum distance 
    dist.       
    """
    dist, idx1, idx2 = float("inf"), -1, -1
    for idx_u in range(len(cluster_list)):
        for idx_v in range(len(cluster_list)):
            if idx_u != idx_v:
                dist_uv = pair_distance(cluster_list, idx_u, idx_v)
                dist, idx1, idx2 = min((dist, idx1, idx2), dist_uv)
    return (dist, idx1, idx2)

def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list.

    Input: cluster_list is list of clusters SORTED such that horizontal 
    positions of their centers are in ascending order.
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the 
    clusters cluster_list[idx1] and cluster_list[idx2] have minimum distance 
    dist.       
    """
    # Sort cluster_list in case it has not been done
    cluster_list.sort(key = lambda cluster: cluster.horiz_center())
    if len(cluster_list) <= 3:
        dist, idx1, idx2 = slow_closest_pair(cluster_list)
    else:
        half = len(cluster_list) / 2
        left = cluster_list[:half]
        right = cluster_list[half:]
        dist_l, idx_il, idx_jl = fast_closest_pair(left)
        dist_r, idx_ir, idx_jr = fast_closest_pair(right)
        dist, idx1, idx2 = min((dist_l, idx_il, idx_jl),
                               (dist_r, idx_ir + half, idx_jr + half))
        mid = (cluster_list[half - 1].horiz_center() + \
               cluster_list[half].horiz_center()) / 2
        dist, idx1, idx2 = min((dist, idx1, idx2),
                               closest_pair_strip(cluster_list, mid, dist))
    return (dist, idx1, idx2)

def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical 
    strip.
    
    Input: cluster_list is a list of clusters produced by fast_closest_pair.
    horiz_center is the horizontal position of the strip's vertical center. 
    line. 
    half_width is the half the width of the strip (i.e; the maximum 
    horizontal distance that a cluster can lie from the center line).

    Output: tuple of the form (dist, idx1, idx2) where the centers of the 
    clusters cluster_list[idx1] and cluster_list[idx2] lie in the strip and 
    have minimum distance dist.       
    """
    new_list = [cluster_list[idx].copy() for idx in range(len(cluster_list))]
    new_list.sort(key = lambda cluster: cluster.vert_center())
    indices = []
    for idx in range(len(new_list)):
        if abs(new_list[idx].horiz_center() - horiz_center) < half_width:
            indices.append(idx)
    dist, idx1, idx2 = float("inf"), -1, -1
    total_indices = len(indices)
    if total_indices > 0:
        for idx_u in range(total_indices - 1):
            for idx_v in range(idx_u + 1, min(idx_u + 4, total_indices)):
                dist, idx1, idx2 = min((dist, idx1, idx2), 
                                       pair_distance(new_list, indices[idx_u], 
                                                     indices[idx_v]))
        cluster1 = new_list[idx1]
        cluster2 = new_list[idx2]
        new_list.sort(key = lambda cluster: cluster.horiz_center())
        idx1 = min(new_list.index(cluster1), new_list.index(cluster2))
        idx2 = max(new_list.index(cluster1), new_list.index(cluster2))
    return (dist, idx1, idx2)
	
def hierarchical_clustering(cluster_list, num_clusters):
	"""
	Compute a hierarchical clustering of a set of clusters.
	Note: the function may mutate cluster_list.

	Input: List of clusters, integer number of clusters.
	Output: List of clusters whose length is num_clusters.
	"""
	while len(cluster_list) > num_clusters:
		cluster_list.sort(key = lambda cluster: cluster.horiz_center())
		dummy_dist, idx_i, idx_j = fast_closest_pair(cluster_list)
		cluster_list[idx_i].merge_clusters(cluster_list[idx_j])
		cluster_list.pop(idx_j)
	return cluster_list

def kmeans_clustering(cluster_list, num_clusters, num_iterations):
	"""
	Compute the k-means clustering of a set of clusters
	Note: the function may not mutate cluster_list

	Input: List of clusters, integers number of clusters and number of
	iterations.
	Output: List of clusters whose length is num_clusters.
	"""
	total_clusters = len(cluster_list)
	clusters = sorted(cluster_list, key = lambda cluster: \
					  cluster.total_population(), reverse = True)
	k_clusters = clusters[:num_clusters]
	for dummy_idx_i in range(num_iterations):
		k_empties = [Cluster(set([]), 0, 0, 0, 0) for \
					 dummy_idx in range(num_clusters)]
		for idx_j in range(total_clusters):
			dist = [cluster_list[idx_j].distance(k_clusters[idx_f]) for \
					idx_f in range(num_clusters)]
			idx_l = dist.index(min(dist))
			k_empties[idx_l].merge_clusters(cluster_list[idx_j])
		k_clusters = k_empties[:]
	return k_clusters

## Code from alg_project3_viz used for questions 2 onward:
## Note that sequential_clustering is not actually referenced in this application.

DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"
DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"

def load_data_table(data_url):
	"""
	Import a table of county-based cancer risk data
	from a csv format file
	"""
	data_file = urllib2.urlopen(data_url)
	data = data_file.read()
	data_lines = data.split('\n')
	print "Loaded", len(data_lines), "data points"
	data_tokens = [line.split(',') for line in data_lines]
	return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])]
			for tokens in data_tokens]
			
def sequential_clustering(singleton_list, num_clusters):
	"""
	Take a data table and create a list of clusters
	by partitioning the table into clusters based on its ordering

	Note that method may return num_clusters or num_clusters + 1 final clusters
	"""
	cluster_list = []
	cluster_idx = 0
	total_clusters = len(singleton_list)
	cluster_size = float(total_clusters)  / num_clusters

	for cluster_idx in range(len(singleton_list)):
		new_cluster = singleton_list[cluster_idx]
		if math.floor(cluster_idx / cluster_size) != \
		   math.floor((cluster_idx - 1) / cluster_size):
			cluster_list.append(new_cluster)
		else:
			cluster_list[-1] = cluster_list[-1].merge_clusters(new_cluster)

	return cluster_list

# New function based on code to generate a singleton_list
def singleton_list(data_table):
	"""
	Return a singleton list from a county data table.
	"""
	singleton_list = []
	for line in data_table:
		singleton_list.append(Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
		
	return singleton_list

## Provided code from alg_clusters_matplotlib.py module to plot clusters.
## Includes URLs for datasets, defind colors, and helper functions.

DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
MAP_URL = DIRECTORY + "data_clustering/USA_Counties.png"

COLORS = ['Aqua', 'Yellow', 'Blue', 'Fuchsia', 'Black', 'Green', 'Lime', 'Maroon', 'Navy', \
				  'Olive', 'Orange', 'Purple', 'Red', 'Brown', 'Teal']

def circle_area(pop):
	"""
	Compute area of circle proportional to population
	"""
	return math.pi * pop / (200.0 ** 2)

def plot_clusters(data_table, cluster_list, draw_centers = False):
	"""
	Create a plot of clusters of counties
	"""
	fips_to_line = {}
	for line_idx in range(len(data_table)):
		fips_to_line[data_table[line_idx][0]] = line_idx

	# Load map image
	map_file = urllib2.urlopen(MAP_URL)
	map_img = plt.imread(map_file)

	# Scale plot to get size similar to CodeSkulptor version
	ypixels, xpixels, bands = map_img.shape
	DPI = 60.0                  # adjust this constant to resize your plot
	xinch = xpixels / DPI
	yinch = ypixels / DPI
	plt.figure(figsize=(xinch,yinch))
	implot = plt.imshow(map_img)

	# draw the counties colored by cluster on the map
	if not draw_centers:
		for cluster_idx in range(len(cluster_list)):
			cluster = cluster_list[cluster_idx]
			cluster_color = COLORS[cluster_idx % len(COLORS)]
			for fips_code in cluster.fips_codes():
				line = data_table[fips_to_line[fips_code]]
				plt.scatter(x = [line[1]], y = [line[2]], s =  circle_area(line[3]), lw = 1,
							facecolors = cluster_color, edgecolors = cluster_color)

	# add cluster centers and lines from center to counties
	else:
		for cluster_idx in range(len(cluster_list)):
			cluster = cluster_list[cluster_idx]
			cluster_color = COLORS[cluster_idx % len(COLORS)]
			for fips_code in cluster.fips_codes():
				line = data_table[fips_to_line[fips_code]]
				plt.scatter(x = [line[1]], y = [line[2]], s =  circle_area(line[3]), lw = 1,
							facecolors = cluster_color, edgecolors = cluster_color, zorder = 1)
		for cluster_idx in range(len(cluster_list)):
			cluster = cluster_list[cluster_idx]
			cluster_color = COLORS[cluster_idx % len(COLORS)]
			cluster_center = (cluster.horiz_center(), cluster.vert_center())
			for fips_code in cluster.fips_codes():
				line = data_table[fips_to_line[fips_code]]
				plt.plot( [cluster_center[0], line[1]],[cluster_center[1], line[2]], cluster_color, lw=1, zorder = 2)
		for cluster_idx in range(len(cluster_list)):
			cluster = cluster_list[cluster_idx]
			cluster_color = COLORS[cluster_idx % len(COLORS)]
			cluster_center = (cluster.horiz_center(), cluster.vert_center())
			cluster_pop = cluster.total_population()
			plt.scatter(x = [cluster_center[0]], y = [cluster_center[1]], s =  circle_area(cluster_pop), lw = 2,
						facecolors = "none", edgecolors = "black", zorder = 3)

	plt.show()
	
## Write compute_distortion function as per 3-7, to be used in several questions.

def compute_distortion(cluster_list, data_table):
	"""
	Compute distortion for a list of cluster objects against a data table.
	"""
	distortion = 0
	for cluster in cluster_list:
		distortion += cluster.cluster_error(data_table)
	return distortion
#################################################

# Work for this question was split into Desktop Python and CodeSkulptor 
# Python. Here, it is combined and matplotlib is used to plot the results.

def app_301():
	'''
	QUESTION 1

	The next four questions will consider the efficiency of hierarchical clustering
	and k-means clustering. Note that successfully computing the 3108 county
	images for Questions 2 and 3 in desktop Python may require some fine
	tuning of your code for one or both methods.

	Write a function gen_random_clusters(num_clusters) that creates a list of
	clusters where each cluster in this list corresponds to one randomly
	generated point in the square with corners (+/-1, +/-1). Use this function
	and your favorite Python timing code to compute the running times of the
	functions slow_closest_pair and fast_closest_pair for lists of clusters of
	size 2 to 200. 

	Once you have computed the running times for both functions, plot the 
	result as two curves combined in a single plot. Use a line plot for each curve.
	The horizontal axis for your plot should be the number of initial clusters
	while the vertical axis should be the running time of the function (in seconds).
	Please include a legend in your plot that distinguishes the two curves.

	Once you are satisfied with your plot, upload your plot in the box below. It 
	will be assessed by: does it follow formatting guidelines, do the curves have
	the correct shapes. 
	'''
	
	# Write function to generate random clusters using Cluster class.
	
	def gen_random_clusters(num_clusters):
		"""
		Generate a list of clusters of size num_clusters where each cluster 
		corresponds to one randomly generated point in the square with
		corners (+/- 1, +/- 1).
		"""
		cluster_list = []
		lower_bound = -1
		upper_bound = 1
		range_width = upper_bound - lower_bound
		for idx in range(num_clusters):
			x_val = random.random() * range_width + lower_bound
			y_val = random.random() * range_width + lower_bound
			cluster_list.append(Cluster(set([]), x_val, y_val, 0, 0))
		return cluster_list	
		
	# Use this function and a timing code to compute running times of
	# SlowClosestPair and FastClosestPair for lists of clusters of size 
	# n = 2 to 200.
	
	scp_times = []
	fcp_times = []
	x_vals = range(2, 201)

	for num_clusters in x_vals:
		cluster_list = gen_random_clusters(num_clusters)
		start = time.time()
		scp = slow_closest_pair(cluster_list)
		end = time.time()
		runtime = end - start
		scp_times.append(runtime)

	for num_clusters in x_vals:
		cluster_list = gen_random_clusters(num_clusters)
		start = time.time()
		fcp = fast_closest_pair(cluster_list)
		end = time.time()
		runtime = end - start
		fcp_times.append(runtime)
		
	# Use matplotlib to generate a plot of running times for both algorithms.
	
	scp_line = plt.plot(x_vals, scp_times, color='b', label="SlowClosestPair")
	fcp_line = plt.plot(x_vals, fcp_times, color='r', label="FastClosestPair")
	plt.legend()
	plt.title("Desktop Python Running Times of Slow and Fast Closest Pair Algms")
	plt.xlabel("No. of Initial Clusters")
	plt.ylabel("Running Time in Seconds")
	plt.show()
	
## ANSWER
#app_301()
# See AlgThink_App3-1_Plot
#################################################

# Code from this question on was taken from the provided module
# alg_project3_viz. Annotated changes have been removed in this final 
# version. Referenced code placed above in shared class/module area.

def app_302():
	'''
	QUESTION 2

	Use alg_project3_viz (module) to create an image of the 15 clusters generated 
	by applying hierarchical clustering to the 3108 county cancer risk data set. You 
	may submit an image with the 3108 counties colored by clusters or an enhanced
	visualization with the original counties colored by cluster and linked to the center
	of their corresponding clusters by lines. You can generate such an enhanced plot
	using our alg_clusters_matplotlib code by modifying the last parameter of 
	plot_clusters to be True. Note that plotting only the resulting cluster centers is
	not acceptable.

	Once you are satisfied with your image, upload your image in the box below. 
	Your submitted image will be assessed based on whether it matches our 
	solution image. You do not need to include axes, axis labels, or a title for it.
	'''
	
	# Load data from 3108 data set and apply HierarchicalClustering algm to it
	# to generate 15 clusters. 
	
	data_table = load_data_table(DATA_3108_URL)
	data_list = singleton_list(data_table)
	
	cluster_list = hierarchical_clustering(data_list, 15)
	print "Displaying", len(cluster_list), "sequential clusters"
	
	# Plot clusters using provided code (placed above in shared area).
	plot_clusters(data_table, cluster_list, True)
	
## ANSWER
#app_302()
# See AlgThink_App3-2_Plot or AlgThink_App3-2_Plot_HiRes
#################################################

# Code for 3-3 mirrors 3-2 but uses KMeansClustering method.

def app_303():
	'''
	QUESTION 3
	
	Use alg_project3_viz to create an image of the 15 clusters generated by applying
	5 iterations of k-means clustering to the 3108 county cancer risk data set. You 
	may submit an image with the 3108 counties colored by clusters or an enhanced
	visualization with the original counties colored by cluster and linked to the center
	of their corresponding clusters by lines. As in Project 3, the initial clusters should
	correspond to the 15 counties with the largest populations.

	Once you are satisfied, upload your image. Your submitted image will be assessed
	based on whether it matches our solution image. You do not need to include axes,
	axis labels, or a title for this image.
	'''
	
	# Load data from 3108 data set and apply KMeansClustering algm to it
	# to generate 15 clusters for 5 iterations.
	
	data_table = load_data_table(DATA_3108_URL)
	data_list = singleton_list(data_table)
	
	cluster_list = kmeans_clustering(data_list, 15, 5)
	print "Displaying", len(cluster_list), "sequential clusters"
	
	# Plot clusters using provided code (placed above in shared area).
	plot_clusters(data_table, cluster_list, True)
	
## ANSWER
#app_303()
# See AlgThink_App3-3_Plot or AlgThink_App3-3_Plot_HiRes
#################################################

# 	Question 3-4 is text-only, and the answer will be a returned string.

def app_304():
	'''
	QUESTION 4

	Which clustering method is faster when the number of output clusters is either
	a small fixed number or a small fraction of the number of input clusters? Provide
	a short explanation in terms of the asymptotic running times of both methods. 
	You should assume that hierarchical_clustering uses fast_closest_pair and that
	k-means clustering always uses a small fixed number of iterations.
	'''
	
	answer = "See string in function."
	
	"""
	The running time of FastClosestPair dictates the speed of Hierarchical Clustering.
	The recurrence model that best fits the former is T(n) = 2T(n/2) + f(n), T(2) = d. In this case, 
	the f(n) is the running time of ClosestPairStrip, which is O(n log(n)). Using the Master 
	Theorem, the worst-case running time of FastClosestPair is O(n log(n)**2). This is
	pulled straight from the homework and verified as correct. Also from the homework is
	that the running time of HierarchicalClustering is O(n**2 + h(n) n) for some function
	h(n) that governs how fast line 4 of the pseudocode (the argmin computation) runs.
	Since line 4 in this case implements FastClosestPair, the total running time of the
	HierarchicalClustering algorithm, as implemented according to the pseudocode, is
	O(n**2 + (n * log(n)**2) * n) which can be simplified to O(n**2) with a large enough
	input size n. 

	The running time of KMeansClustering is O(qkn) where q = iterations, k = number of
	clusters, and n = input size. When this algorithm uses a small fixed number of
	iterations and a small number of output clusters (whether a fixed number or a small
	fraction of n)	, the running time is very close to some reasonable constant times n, or
	a running time of O(n).

	The running time of O(n) is much faster than that of O(n**2), and so the k-means
	clustering method is much faster than the hierarchical clustering method when executed
	in the described conditions. This difference in running time was evident when processing
	the code for questions 2 and 3.
	"""
	
	print answer
	
	
## ANSWER
#app_304()
#################################################

# Code mirrors 3-2 but with different parameters.

def app_305():
	'''
	QUESTION 5

	In the next five questions, we will compare the level of human supervision required for
	each method.

	Use alg_project3_viz to create an image of the 9 clusters generated by applying 
	hierarchical clustering to the 111 county cancer risk data set. You may submit an image
	with the 111 counties colored by clusters or an enhanced visualization with the original
	counties colored by cluster and linked to the center of their corresponding clusters by lines.

	Once you are satisfied with your image, upload it. It's assessed like those from 3-2 and 3-3.
	'''
	
	# Load data from 3108 data set and apply HierarchicalClustering algm to it
	# to generate 15 clusters. 
	
	data_table = load_data_table(DATA_111_URL)
	data_list = singleton_list(data_table)
	
	cluster_list = hierarchical_clustering(data_list, 9)
	print "Displaying", len(cluster_list), "sequential clusters"
	
	# Plot clusters using provided code (placed above in shared area).
	plot_clusters(data_table, cluster_list, True)
	
	# Return HierarchicalClustering cluster list for 3-7.
	return cluster_list
	
## ANSWER
#app_305()
# See AlgThink_App3-5_Plot or AlgThink_App3-5_Plot_HiRes
#################################################

# Code for 3-6 mirrors 3-5 but uses KMeansClustering method.

def app_306():
	'''
	QUESTION 6
	
	Use alg_project3_viz to create an image of the 9 clusters generated by applying 5
	iterations of k-means clustering to the 111 county cancer risk data set. Submit
	your image as previously described. Upload and be done.
	'''
	
	# Load data from 3108 data set and apply KMeansClustering algm to it
	# to generate 15 clusters for 5 iterations.
	
	data_table = load_data_table(DATA_111_URL)
	data_list = singleton_list(data_table)
	
	cluster_list = kmeans_clustering(data_list, 9, 5)
	print "Displaying", len(cluster_list), "sequential clusters"
	
	# Plot clusters using provided code (placed above in shared area).
	plot_clusters(data_table, cluster_list, True)
	
	# Return KMeansClustering cluster list for 3-7.
	return cluster_list
	
## ANSWER
#app_306()
# See AlgThink_App3-6_Plot or AlgThink_App3-6_Plot_HiRes
#################################################

# Required function compute_distortion() written and added to bottom of 
# shared classes/functions. Use this function to first calculate distortions for
# 290 county data set to check answers, then use on the clusters computed
# in 3-5 and 3-6. Run KMeansClustering first, as HierarchicalClustering will
# mutate the data_list passed to it.

def app_307():
	'''
	QUESTION 7

	The clusterings that you computed in 3-5 and 3-6 illustrate that not all clusterings are equal.
	In particular, some clusterings are better than others. One way to make this concept more
	precise is to formulate a mathematical measure of the error associated with a cluster. Given
	a cluster C, its error is the sum of the squares of the distances from each county in the cluster
	to the cluster's center, weighted by each county's population. If p_i is the position of the
	county and w_i is its population, the cluster's error is:

	error(C) = SIG (of all p_i in C) w_i (d_(p_i c))**2
	Or, the sum of population times distance squared between position and cluster center, for all
	positions in C.

	-where c is the center of the cluster C. The Cluster class includes a method cluster_error(data_table)
	that takes a Cluster object and the original data table associated with the counties in the cluster and 
	computes the error associated with a given cluster.

	Given a list of clusters L, the distortion of the clustering is the sum of the errors associated with
	its clusters.

	distortion(L) = SIG (of all C in L) error(C)
	Or, the sum of error of cluster C, for all clusters in list L.

	Write a function compute_distortion(cluster_list) that takes a list of clusters and uses
	cluster_error to compute its distortion. Now, use compute_distortion to compute the
	distortions of the two clusterings in 3-5 and 3-6. Enter the values for the distortions
	(with at least four sig digits) for these two clusterings in the box below. Clearly indicate
	the clusterings to which each value corresponds. 

	As a check on the correctness of your code, the distortions associated with the 16 output
	clusters produced by hierarchical clustering and k-means clustering (with 5 iterations)
	on the 290 county data set are approximately 2.575 x 10**11 and 2.323 x 10**11,
	respectively.
	'''
	
	# Test expected vs. actual values on 290 county data set.
	
	data_table = load_data_table(DATA_290_URL)
	data_list = singleton_list(data_table)
	kclust = kmeans_clustering(data_list, 16, 5)
	print "KMeansClustering"
	print "Expected: 2.323 x 10**11"
	print "Actual:", compute_distortion(kclust, data_table)
	hclust = hierarchical_clustering(data_list, 16)
	print "HierarchicalClustering"
	print "Expected: 2.575 x 10**11"
	print "Actual:", compute_distortion(hclust, data_table)
	
	# Compute and store answers to 3-5 and 3-6, then compute distortion of each.
	# The order is arbitrary as each function separately initializes the data_list that
	# is passed to the respective clustering function. Plots will still be generated.
	
	data_table = load_data_table(DATA_111_URL)
	hclust = app_305()
	hdistortion = compute_distortion(hclust, data_table)
	print "HierarchicalClustering Distortion:", hdistortion
	kclust = app_306()
	kdistortion = compute_distortion(kclust, data_table)
	print "KMeansClustering Distortion:", kdistortion
	
	answer = "See string in function."
	
	"""
	HierarchicalClustering Distortion: 1.752 x 10**11
	KMeansClustering Distortion: 2.713 x 10**11
	"""
	
	return answer
		
## ANSWER
#app_307()
#################################################

# 	Question 3-8 is text-only, and the answer will be a returned string.

def app_308():
	'''
	QUESTION 8

	Examine the clusterings generated in 3-5 and 3-6. In particular, focus your attention
	on the number and shape of the clusters located on the west coast of the USA.

	Describe the difference between the shapes of the clusters produced by these two 
	methods on the west coast of the USA. What caused one method to produce a
	clustering with a much higher distortion? To help you answer this question, you
	should consider how k-means clustering generates its initial clustering in this case.

	In explaining your answer, review the geography of the west coast of the USA:
	https://en.wikipedia.org/wiki/West_Coast_of_the_United_States
	'''
	
	answer = "See string in function."

	"""
	The HierarchicalClustering algorithm creates 3 clusters on the west coast roughly 
	centered in the Seattle/Portland area in the far north, the San Francisco Bay area in 
	the lower middle in Northern California, and the Los Angeles/San Diego area in the far 
	south in Southern California. 

	The KMeansClustering algorithm also creates 3 clusters, but with different centers. 
	The first is halfway between the Seattle/Portland and San Francisco areas,
	somewhere close to the northern border of California and Oregon; the second
	is positioned on top of Los Angeles; the third is nearby, positioned roughly where
	the southern-most cluster center was generated, around Los Angeles/San Diego. 

	The KMeansClustering algorithm created clusterings with higher distortion due to
	the way that this implementation of KMeansClustering generates its initial clustering.
	The initial clustering is based on the k most populated counties. Of the 9 most
	populated counties in the USA, the 3 that are in California are all in Southern
	California. As the KMeansClustering algorithm iterates up to q times (q = 5 in
	this case), these cluster centers are updated to reflect the very populous
	areas outside of Southern California, from San Francisco up to Seattle/Portland.
	As the centers are updated, 1 of the 3 in California is dragged northward, toward
	these other areas, while the other 2 linger around Los Angeles and San Diego.

	Since these cluster centers will not venture too far once they find a "harmonious"
	spot (increase q to 50 to see that not much changes even with 10 times the
	iterations), the distortion introduced by centering the initial clusters around the
	k most populated counties (and thus giving them preference over the others
	counties) persists. This distortion is not as great with HierarchicalClustering
	because that algorithm gives preference only to those clusters which are close
	in proximity initially. There is less distortion when the 3 areas with the greatest
	population density on the west coast of the USA (Seattle/Portland, San Francisco, 
	Los Angeles/San Diego) each have a unique cluster. With KMeansClustering, the 
	former 2 areas have to share one cluster, while the latter area is divided in half,
	with each half given its own unique cluster (wastefully).
	"""
	
	print answer
	
## ANSWER
#app_308()
#################################################

# 	Question 3-9 is text-only, and the answer will be a returned string.

def app_309():
	'''
	QUESTION 9

	Based on your answer to 3-8, which method requires less human supervision
	to produce clusterings with relatively low distortion?
	'''
	
	answer = "See string in function."
	
	"""
	While it may take longer to process, the HierarchicalClustering method seemed to
	produce clusterings with relatively low distortion all on its own. Someone using the
	KMeansClustering method would have to experiment with different parameters in
	order to optimize clusterings. The basis for initial cluster centers could be changed
	to something other than population, and the k and q values could be fine-tuned. 
	With HierarchicalClustering, it is a "set and forget" kind of computation.
	"""
	
	print answer
	
## ANSWER
#app_309()
#################################################

# Question 3-10 was the only answer originally written as a stand-alone function.

def app_310(data_set = 111, lower = 6, upper = 20, iterations = 5):
	'''
	QUESTION 10

	In the last two questions, you will analyze the quality of the clusterings produced
	by each method as measured by their distortion.

	Compute the distortion of the list of clusters produced by hierarchical clustering
	and k-means clustering (using 5 iterations) on 111, 290, and 896 county data sets,
	respectively, where the number of output clusters ranges from 6 to 20 (inclusive).
	Important note: To compute the distortion for all 15 output clusterings produced
	by hierarchical_clustering, you should remember that you can use the hierarchical
	cluster of size 20 to compute the hierarchical clustering of size 19 and so on. 
	Otherwise, you will introduce an unnecessary factor of 15 into the computation of 
	the 15 hierarchical clusterings.

	Once you have computed these distortions for both clustering methods, create
	3 separate plots (one for each data set) that compare the distortion of the 
	clusterings produced by both methods. Each plot should include two curves
	drawn as line plots. The horizontal axis for each plot should indicate the number
	of output clusters while the vertical axis should indicate the distortion associated
	with each output clustering. For each plot, include a title that indicates the data set
	used in creating the plots and a legend that distinguishes the two curves.

	Once you are satisfied, upload them in the box. They will be graded based on 
	guidelines and shape.
	'''
	
	if data_set == 111:
		data = DATA_111_URL
		title_id = "111"
	elif data_set == 290:
		data = DATA_290_URL
		title_id = "290"
	elif data_set == 896:
		data = DATA_896_URL
		title_id = "896"
		
	data_table = load_data_table(data)
	
	list_data = []
	for line in data_table:
		list_data.append(Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
		
	x_vals = range(lower, upper + 1)
	k_distortions = []
	h_distortions = []
	
	for output_clusters in x_vals:
		kclust = kmeans_clustering(list_data, output_clusters, iterations)
		k_distortions.append(compute_distortion(kclust, data_table))
		
	h_list_data = list_data
	for output_clusters in range(upper, lower - 1, -1):
		hclust = hierarchical_clustering(h_list_data, output_clusters)
		h_distortions.insert(0, compute_distortion(hclust, data_table))
		h_list_data = hclust
		
	k_line = plt.plot(x_vals, k_distortions, color='g', label="KMeansClustering")
	h_line = plt.plot(x_vals, h_distortions, color='r', label="HierarchicalClustering")
	plt.legend()
	plot_title = "Distortion of Clustering Methods on " + title_id + " County Data Set"
	plt.title(plot_title)
	plt.xlabel("Number of Output Clusters")
	plt.ylabel("Distortion")
	plt.show()

## ANSWER
# Uncomment out the line for the data set you want to print (default = 111)
#app_310()
#app_310(290)
#app_310(896)

# See AlgThink_App3-10_Plot_111_HiRes, AlgThink_App3-10_Plot_290_HiRes 
# and AlgThink_App3-10_Plot_896_HiRes
#################################################

# 	Question 3-11 is text-only, and the answer will be a returned string.

def app_311():
	'''
	QUESTION 11

	For each data set (111, 290, and 896 counties), does one clustering method
	consistently produce lower distortion clusterings when the number of output
	clusters is in the range 6 to 20? If so, indicate on which data set(s) one method
	is superior to the other.
	'''
	
	answer = "See string in function."
	
	"""
	For the 111 data set, HierarchicalClustering produced a slightly-to-much smaller
	distortion than KMeansClustering. For the 290 data set, HierarchicalClustering
	produced a slightly-smaller-to-equal distortion compared to KMeansClustering.
	For the 896 data set, the distortion was roughly the same for both methods.

	While HierarchicalClustering generated lower distortion at a smaller n, as
	the input size grew, its distortion was comparable to that generated by the
	KMeansClustering method, thus neither method CONSISTENTLY produced
	lower distortion clusterings. HierarchicalClustering appeared to be superior
	at smaller input sizes.
	"""
	
	print answer
	
## ANSWER
#app_311()
#################################################

# Question 3-12 (BONUS) is text-only, and the answer will be a returned string.

def app_312():
	'''
	BONUS QUESTION

	Which clustering method would you prefer when analyzing these data sets? 
	Provide a summary of each method's strengths and weaknesses on these
	data sets in the three areas considered in this application. Your summary should 
	be at least a paragraph in length (4 sentences minimum).
	'''
	
	answer = "See string in function."
	
	"""
	In this analysis, we looked at the efficiency (via running time), automation
	(via supervision required when using), and quality (via distortion) of the two
	clustering methods HierarchicalClustering and KMeansClustering. Below, I 
	will summarize the results for each method in each of those three areas.

	HierarchicalClustering took O(n**2) running time to process the data sets. 
	KMeansClustering took O(qkn) running time to process the data sets. By 
	keeping q (number of iterations) and k (number of output clusters) low,
	the running time appeared to be near O(n). As the number of inputs in a
	data set increases, the KMeansClustering method tends to be the better
	method to use with regard to efficiency.

	HierarchicalClustering generated clusters that appeared to be better centered
	on the map of USA counties than those generated by KMeansClustering. 
	The cluster centers were spread out more effectively such that each was
	centered on a clearly isolated population zone. KMeansClustering
	placed cluster centers in locations that caused very distant population
	zones to share a center point midway between them. The placement of these
	centers was dependent on specific components of KMeansClustering's 
	implementation (e.g. how are the initial cluster centers chosen). Additionally, 
	this method's parameters could be tweaked to improve results. 
	HierarchicalClustering did not require such in-depth reworking to optimize 
	results, so it performed better with regard to automation.

	Regarding the quality assessment, both methods produced similar results.
	At smaller input sizes, the distortion generated by HierarchicalClustering was
	lower than that generated by KMeansClustering. As the input size grew, the
	distortion of both methods was roughly equal. Neither was proven to
	consistently be of better quality than the other, unless input size was low.

	When analyzing these data sets, the best method to use is largely determined
	by time constraints and input size. If the input size is small and you do not
	have time to optimize the implementation and parameters of KMeansClustering,
	it is best to use HierarchicalClustering to very easily generate accurate
	results with little to no headache. If you will be working intimately with varying
	input sizes, and you have additional time to fine-tune and optimize your
	method, it is best to use KMeansClustering. Once optimized, KMeansClustering
	could work as efficiently on smaller input sizes as HierarchicalClustering, and
	you can feel comfortable knowing that you have a fast, effective method if you
	are ever required to analyze several, or all, clusters from the data set.
	"""
	
	print answer

## ANSWER
#app_312()
#################################################
#################################################