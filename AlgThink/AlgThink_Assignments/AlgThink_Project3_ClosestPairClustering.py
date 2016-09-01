"""
Coursera / Rice University
Algorithmic Thinking (Part 2)
Project 3: Implementing Closest Pair and Clustering Algms
"""
######################################################
## alg_cluster class
######################################################
"""
Cluster class for Module 3
"""

import math

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
######################################################
######################################################
"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""
import math
import alg_cluster

######################################################
# Code for closest pairs of clusters

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
    
    ## List should already be sorted, commenting out next line
    #cluster_list.sort(key = lambda cluster: cluster.horiz_center())
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
        ## Not used due to 17/15 variables in function (OwlTest restriction)
        ##cluster1_idx = new_list.index(cluster1)
        ##cluster2_idx = new_list.index(cluster2)
        ##idx1 = min(cluster1_idx, cluster2_idx)
        ##idx2 = max(cluster1_idx, cluster2_idx)
    return (dist, idx1, idx2)


######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters.
    Note: the function may mutate cluster_list.
    
    Input: List of clusters, integer number of clusters.
    Output: List of clusters whose length is num_clusters.
    """
    while len(cluster_list) > num_clusters:
		# Sort cluster_list in prep for use of FastClosestPair algm
        cluster_list.sort(key = lambda cluster: cluster.horiz_center())
		# Find the closest pair of clusters, union and difference steps
        dummy_dist, idx_i, idx_j = fast_closest_pair(cluster_list)
        cluster_list[idx_i].merge_clusters(cluster_list[idx_j])
        cluster_list.pop(idx_j)
    return cluster_list


######################################################################
# Code for k-means clustering (heavily annotated)

    
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of 
    iterations.
    Output: List of clusters whose length is num_clusters.
    """
    total_clusters = len(cluster_list)
    # position initial clusters at the location of clusters with 
    # largest populations (instructions).
    clusters = sorted(cluster_list, key = lambda cluster: \
                      cluster.total_population(), reverse = True)
    k_clusters = clusters[:num_clusters]
    # Run loop num_iterations (q) times
    for dummy_idx_i in range(num_iterations):
        # Initialize k empty cluster centers (here, empty Cluster objects)
        k_empties = [alg_cluster.Cluster(set([]), 0, 0, 0, 0) for \
                     dummy_idx in range(num_clusters)]
        # For each cluster in cluster_list, do the following:
        for idx_j in range(total_clusters):
            # Find all distances between the cluster and all initial (k) clusters
            dist = [cluster_list[idx_j].distance(k_clusters[idx_f]) for \
                    idx_f in range(num_clusters)]
            # Return the index of the closest initial (k) cluster
            ## Original used below line, another effective method, but less clear
            ##idx_l = min(range(len(dist)), key = dist.__getitem__)
            idx_l = dist.index(min(dist))
            # Merge the empty cluster at that index with the cluster_list cluster
            # to build a weighted cluster based on proximity of each cluster to
            # each initial cluster, minimizing distance each time.
            k_empties[idx_l].merge_clusters(cluster_list[idx_j])
        # Replace the initial cluster list with the new k centers based on
        # distance computation from initial centers to cluster_list clusters.
        k_clusters = k_empties[:]
    return k_clusters

###########
# TESTING #
###########

#a = alg_cluster.Cluster([1234, 2345, 3456, 4567], 11, 5, 5000, 2.5)
#b = alg_cluster.Cluster([888, 555, 333, 222], 15, 4, 2000, 1.2)
#c = alg_cluster.Cluster([12, 13, 14, 15], 5, 17, 1200, 0.9)
#d = alg_cluster.Cluster([2, 4, 6, 8], 2, 2, 750, 0.5)
#clusters = [a,b,c,d]
#for item in clusters:
#    print item
#print "\n"
#
#scp = slow_closest_pair(clusters)
#print "SlowClosestPair:", scp
#print "A distance of", scp[0], "between:"
#print clusters[scp[1]]
#print "and"
#print clusters[scp[2]]
#print "\n"
#
#clusters.sort(key = lambda cluster: cluster.horiz_center())
#print "Sorted SlowClosestPair:"
#print slow_closest_pair(clusters)
#print "Sorted FastClosestPair:"
#fcp = fast_closest_pair(clusters)
#print fcp
#print "\n"


#print "*"*30
#print "Figuring out errors in OwlTest"
#
#print "First problem"
##
##[-7.0 pts] closest_pair_strip(([alg_cluster.Cluster(set([]), 
##0.1, 0.42, 1, 0), alg_cluster.Cluster(set([]), 0.21, 0.51, 1, 0), 
##alg_cluster.Cluster(set([]), 0.33, 0.39, 1, 0), alg_cluster.Cluster
##(set([]), 0.7, 0.24, 1, 0)], 0.27000000000000002, 0.142127)) expected 
##one of the tuples in set([(0.16970562748477142, 1, 2)]) but received 
##(0.16970562748477142, 1, 3)
##
#a = alg_cluster.Cluster(set([]), 0.1, 0.42, 1, 0)
#b = alg_cluster.Cluster(set([]), 0.21, 0.51, 1, 0)
#c = alg_cluster.Cluster(set([]), 0.33, 0.39, 1, 0)
#d = alg_cluster.Cluster(set([]), 0.7, 0.24, 1, 0)
#clusters = [a, b, c, d]
#cps = closest_pair_strip(clusters, 0.27000000000000002, 0.142127)
#print "Expected: one of the tuples in set([(0.16970562748477142, 1, 2)])"
#print "But received:", cps
#print
#
#print "Second problem"
##
##[-1.5 pts] closest_pair_strip(([alg_cluster.Cluster(set([]), -1.0, 0.0, 1, 0), 
##alg_cluster.Cluster(set([]), -0.99, -10.0, 1, 0), alg_cluster.Cluster
##(set([]), -0.98, -20.0, 1, 0), alg_cluster.Cluster(set([]), 0.98, 20.0, 1, 0), 
##alg_cluster.Cluster(set([]), 0.99, 10.0, 1, 0), alg_cluster.Cluster(set([]), 
##1.0, 0.0, 1, 0)], 0.0, 10.000005)) expected one of the tuples in 
##set([(2.0, 0, 5)]) but received (10.000004999998751, 0, 1)
##
#a = alg_cluster.Cluster(set([]), -1.0, 0.0, 1, 0)
#b = alg_cluster.Cluster(set([]), -0.99, -10.0, 1, 0)
#c = alg_cluster.Cluster(set([]), -0.98, -20.0, 1, 0)
#d = alg_cluster.Cluster(set([]), 0.98, 20.0, 1, 0)
#e = alg_cluster.Cluster(set([]), 0.99, 10.0, 1, 0)
#f = alg_cluster.Cluster(set([]), 1.0, 0.0, 1, 0)
#clusters = [a, b, c, d, e, f]
#cps = closest_pair_strip(clusters, 0.0, 10.000005)
#print "Expected: one of the tuples in set([(2.0, 0, 5)])"
#print "Received:", cps
#print
#
#print "Third problem"
##
##[-5.0 pts] closest_pair_strip(([alg_cluster.Cluster(set([]), 0.32, 0.16, 1, 0), 
##alg_cluster.Cluster(set([]), 0.39, 0.4, 1, 0), alg_cluster.Cluster(set([]), 
##0.54, 0.8, 1, 0), alg_cluster.Cluster(set([]), 0.61, 0.8, 1, 0), 
##alg_cluster.Cluster(set([]), 0.76, 0.94, 1, 0)], 0.46500000000000002, 
##0.070000000000000007)) expected one of the tuples in set([(inf, -1, -1)]) but 
##received (inf, 4, 4)
##
#a = alg_cluster.Cluster(set([]), 0.32, 0.16, 1, 0)
#b = alg_cluster.Cluster(set([]), 0.39, 0.4, 1, 0)
#c = alg_cluster.Cluster(set([]), 0.54, 0.8, 1, 0)
#d = alg_cluster.Cluster(set([]), 0.61, 0.8, 1, 0)
#e = alg_cluster.Cluster(set([]), 0.76, 0.94, 1, 0)
#clusters = [a, b, c, d, e]
#cps = closest_pair_strip(clusters, 0.46500000000000002, 0.070000000000000007)
#print "Expected: one of the tuples in set([(inf, -1, -1)])"
#print "Received:", cps
#print