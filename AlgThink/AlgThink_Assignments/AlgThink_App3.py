"""
Coursera / Rice University
Algorithmic Thinking (Part 2)
Application 3
"""

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

#################################################
## Work will be done on desktop Python to optimize running time.
## Data will be generated on the desktop and transferred to CodeSkulptor
## for plotting of data points.
#################################################

# Pasting Cluster class (vs. importing) and necessary functions in this file.
# Writing functions to refer to class directly instead of alg_cluster.

"""
Desktop Python
AlgThink Part 2
App 3-1
"""

import math
import random
import time

random.seed(1)

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
    
    ## Sort cluster_list in case it has not been done
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
#################################################

# Write gen_random_clusters functions using the Cluster class

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
# SlowClosestPair and FastClosestPair for lists of clusters of size 2-200.

scp_times = []
fcp_times = []

for num_clusters in range(2, 201):
	cluster_list = gen_random_clusters(num_clusters)
	start = time.time()
	scp = slow_closest_pair(cluster_list)
	end = time.time()
	runtime = end - start
	scp_times.append((num_clusters, runtime))

print scp_times

for num_clusters in range(2, 201):
	cluster_list = gen_random_clusters(num_clusters)
	start = time.time()
	fcp = fast_closest_pair(cluster_list)
	end = time.time()
	runtime = end - start
	fcp_times.append((num_clusters, runtime))
	
print fcp_times

## Desktop (PyCharm) returned scp_times	
[(2, 0.0), (3, 0.0), (4, 0.0), (5, 0.0), (6, 0.0009999275207519531), (7, 0.0), (8, 0.0), (9, 0.0), (10, 0.0), (11, 0.0), (12, 0.0009999275207519531), (13, 0.0), (14, 0.0), (15, 0.0009999275207519531), (16, 0.0), (17, 0.0010001659393310547), (18, 0.0), (19, 0.0009999275207519531), (20, 0.0), (21, 0.0009999275207519531), (22, 0.0010001659393310547), (23, 0.0009999275207519531), (24, 0.0009999275207519531), (25, 0.0010001659393310547), (26, 0.0009999275207519531), (27, 0.0009999275207519531), (28, 0.002000093460083008), (29, 0.0009999275207519531), (30, 0.002000093460083008), (31, 0.0009999275207519531), (32, 0.002000093460083008), (33, 0.0019998550415039062), (34, 0.002000093460083008), (35, 0.0019998550415039062), (36, 0.002000093460083008), (37, 0.003000020980834961), (38, 0.002000093460083008), (39, 0.0029997825622558594), (40, 0.002000093460083008), (41, 0.003000020980834961), (42, 0.003000020980834961), (43, 0.003000020980834961), (44, 0.003999948501586914), (45, 0.003000020980834961), (46, 0.003999948501586914), (47, 0.003000020980834961), (48, 0.003999948501586914), (49, 0.003999948501586914), (50, 0.004000186920166016), (51, 0.003999948501586914), (52, 0.003999948501586914), (53, 0.005000114440917969), (54, 0.004999876022338867), (55, 0.005000114440917969), (56, 0.006000041961669922), (57, 0.004999876022338867), (58, 0.006000041961669922), (59, 0.006000041961669922), (60, 0.006000041961669922), (61, 0.006000041961669922), (62, 0.006999969482421875), (63, 0.006000041961669922), (64, 0.006999969482421875), (65, 0.006999969482421875), (66, 0.007999897003173828), (67, 0.006999969482421875), (68, 0.00800013542175293), (69, 0.007999897003173828), (70, 0.00800013542175293), (71, 0.008999824523925781), (72, 0.00800013542175293), (73, 0.009000062942504883), (74, 0.009000062942504883), (75, 0.008999824523925781), (76, 0.009999990463256836), (77, 0.009999990463256836), (78, 0.009999990463256836), (79, 0.01100015640258789), (80, 0.010999917984008789), (81, 0.01100015640258789), (82, 0.012999773025512695), (83, 0.015000104904174805), (84, 0.01399993896484375), (85, 0.018000125885009766), (86, 0.020999908447265625), (87, 0.02200007438659668), (88, 0.01699995994567871), (89, 0.013000011444091797), (90, 0.014000177383422852), (91, 0.01399993896484375), (92, 0.01399993896484375), (93, 0.015000104904174805), (94, 0.014999866485595703), (95, 0.015000104904174805), (96, 0.014999866485595703), (97, 0.014999866485595703), (98, 0.016000032424926758), (99, 0.016000032424926758), (100, 0.01699995994567871), (101, 0.019999980926513672), (102, 0.017000198364257812), (103, 0.017999887466430664), (104, 0.018000125885009766), (105, 0.018999814987182617), (106, 0.01900005340576172), (107, 0.01900005340576172), (108, 0.019999980926513672), (109, 0.019999980926513672), (110, 0.019999980926513672), (111, 0.020999908447265625), (112, 0.021000146865844727), (113, 0.020999908447265625), (114, 0.020999908447265625), (115, 0.023000001907348633), (116, 0.02200007438659668), (117, 0.023000001907348633), (118, 0.023999929428100586), (119, 0.023999929428100586), (120, 0.023999929428100586), (121, 0.026000022888183594), (122, 0.02500009536743164), (123, 0.02500009536743164), (124, 0.020999908447265625), (125, 0.03299999237060547), (126, 0.03399991989135742), (127, 0.0279998779296875), (128, 0.0280001163482666), (129, 0.026999950408935547), (130, 0.0280001163482666), (131, 0.029000043869018555), (132, 0.028999805450439453), (133, 0.029999971389770508), (134, 0.03000020980834961), (135, 0.03099989891052246), (136, 0.03099989891052246), (137, 0.037999868392944336), (138, 0.04200005531311035), (139, 0.04900002479553223), (140, 0.03299999237060547), (141, 0.025999784469604492), (142, 0.04700016975402832), (143, 0.03099989891052246), (144, 0.04900002479553223), (145, 0.03600001335144043), (146, 0.03600001335144043), (147, 0.03699994087219238), (148, 0.03699994087219238), (149, 0.03800010681152344), (150, 0.03800010681152344), (151, 0.037999868392944336), (152, 0.03900003433227539), (153, 0.03900003433227539), (154, 0.039999961853027344), (155, 0.0409998893737793), (156, 0.0410001277923584), (157, 0.0409998893737793), (158, 0.04200005531311035), (159, 0.042999982833862305), (160, 0.042999982833862305), (161, 0.042999982833862305), (162, 0.04400014877319336), (163, 0.04499983787536621), (164, 0.04500007629394531), (165, 0.046000003814697266), (166, 0.046000003814697266), (167, 0.046000003814697266), (168, 0.04700016975402832), (169, 0.04699993133544922), (170, 0.04799985885620117), (171, 0.04900002479553223), (172, 0.04900002479553223), (173, 0.04999995231628418), (174, 0.05000019073486328), (175, 0.05099987983703613), (176, 0.05200004577636719), (177, 0.05200004577636719), (178, 0.05200004577636719), (179, 0.05300021171569824), (180, 0.053999900817871094), (181, 0.054000139236450195), (182, 0.05500006675720215), (183, 0.0559999942779541), (184, 0.056999921798706055), (185, 0.056999921798706055), (186, 0.056999921798706055), (187, 0.05800008773803711), (188, 0.05900001525878906), (189, 0.05900001525878906), (190, 0.06000018119812012), (191, 0.06099987030029297), (192, 0.06200003623962402), (193, 0.06299996376037598), (194, 0.06299996376037598), (195, 0.06300020217895508), (196, 0.06399989128112793), (197, 0.06500005722045898), (198, 0.06500005722045898), (199, 0.06700015068054199), (200, 0.06699991226196289)]
## Desktop returned fcp_times
[(2, 0.0), (3, 0.0), (4, 0.0), (5, 0.0), (6, 0.0), (7, 0.0), (8, 0.0), (9, 0.0), (10, 0.0), (11, 0.0), (12, 0.0009999275207519531), (13, 0.0), (14, 0.0), (15, 0.0010001659393310547), (16, 0.0), (17, 0.0), (18, 0.0009999275207519531), (19, 0.0), (20, 0.0009999275207519531), (21, 0.0), (22, 0.0010001659393310547), (23, 0.0), (24, 0.0009999275207519531), (25, 0.0), (26, 0.0009999275207519531), (27, 0.0010001659393310547), (28, 0.0009999275207519531), (29, 0.0), (30, 0.0), (31, 0.0009999275207519531), (32, 0.0010001659393310547), (33, 0.0009999275207519531), (34, 0.0009999275207519531), (35, 0.0010001659393310547), (36, 0.0009999275207519531), (37, 0.0010001659393310547), (38, 0.0009999275207519531), (39, 0.0009999275207519531), (40, 0.0009999275207519531), (41, 0.0010001659393310547), (42, 0.0009999275207519531), (43, 0.002000093460083008), (44, 0.0009999275207519531), (45, 0.0009999275207519531), (46, 0.0010001659393310547), (47, 0.0019998550415039062), (48, 0.0010001659393310547), (49, 0.0009999275207519531), (50, 0.0019998550415039062), (51, 0.002000093460083008), (52, 0.0009999275207519531), (53, 0.002000093460083008), (54, 0.0009999275207519531), (55, 0.002000093460083008), (56, 0.0019998550415039062), (57, 0.002000093460083008), (58, 0.002000093460083008), (59, 0.0019998550415039062), (60, 0.002000093460083008), (61, 0.002000093460083008), (62, 0.0029997825622558594), (63, 0.002000093460083008), (64, 0.002000093460083008), (65, 0.0019998550415039062), (66, 0.0019998550415039062), (67, 0.003000020980834961), (68, 0.002000093460083008), (69, 0.003000020980834961), (70, 0.0019998550415039062), (71, 0.003000020980834961), (72, 0.003000020980834961), (73, 0.002000093460083008), (74, 0.003000020980834961), (75, 0.0029997825622558594), (76, 0.002000093460083008), (77, 0.003000020980834961), (78, 0.002000093460083008), (79, 0.002000093460083008), (80, 0.0029997825622558594), (81, 0.003000020980834961), (82, 0.003000020980834961), (83, 0.003000020980834961), (84, 0.003000020980834961), (85, 0.003000020980834961), (86, 0.003000020980834961), (87, 0.003000020980834961), (88, 0.003000020980834961), (89, 0.003000020980834961), (90, 0.003000020980834961), (91, 0.003000020980834961), (92, 0.003000020980834961), (93, 0.003999948501586914), (94, 0.003000020980834961), (95, 0.003999948501586914), (96, 0.003000020980834961), (97, 0.003000020980834961), (98, 0.003000020980834961), (99, 0.003000020980834961), (100, 0.003999948501586914), (101, 0.003000020980834961), (102, 0.003999948501586914), (103, 0.004000186920166016), (104, 0.0029997825622558594), (105, 0.004000186920166016), (106, 0.003999948501586914), (107, 0.003000020980834961), (108, 0.003999948501586914), (109, 0.004000186920166016), (110, 0.003999948501586914), (111, 0.004999876022338867), (112, 0.003999948501586914), (113, 0.005000114440917969), (114, 0.003000020980834961), (115, 0.003999948501586914), (116, 0.005000114440917969), (117, 0.004999876022338867), (118, 0.004000186920166016), (119, 0.003999948501586914), (120, 0.005000114440917969), (121, 0.004999876022338867), (122, 0.006000041961669922), (123, 0.005000114440917969), (124, 0.004999876022338867), (125, 0.005000114440917969), (126, 0.004999876022338867), (127, 0.005000114440917969), (128, 0.005000114440917969), (129, 0.006000041961669922), (130, 0.004999876022338867), (131, 0.005000114440917969), (132, 0.004999876022338867), (133, 0.004999876022338867), (134, 0.006000041961669922), (135, 0.006000041961669922), (136, 0.006000041961669922), (137, 0.004999876022338867), (138, 0.004999876022338867), (139, 0.005000114440917969), (140, 0.00599980354309082), (141, 0.006000041961669922), (142, 0.006000041961669922), (143, 0.006000041961669922), (144, 0.006000041961669922), (145, 0.004999876022338867), (146, 0.006000041961669922), (147, 0.006000041961669922), (148, 0.006000041961669922), (149, 0.006000041961669922), (150, 0.004999876022338867), (151, 0.006999969482421875), (152, 0.006999969482421875), (153, 0.006000041961669922), (154, 0.006000041961669922), (155, 0.006999969482421875), (156, 0.006000041961669922), (157, 0.006000041961669922), (158, 0.006000041961669922), (159, 0.006000041961669922), (160, 0.006999969482421875), (161, 0.0070002079010009766), (162, 0.00599980354309082), (163, 0.0070002079010009766), (164, 0.006000041961669922), (165, 0.00599980354309082), (166, 0.0070002079010009766), (167, 0.006999969482421875), (168, 0.006999969482421875), (169, 0.006000041961669922), (170, 0.006000041961669922), (171, 0.006999969482421875), (172, 0.006999969482421875), (173, 0.006999969482421875), (174, 0.006999969482421875), (175, 0.00800013542175293), (176, 0.006999969482421875), (177, 0.006999969482421875), (178, 0.006999969482421875), (179, 0.006999969482421875), (180, 0.006999969482421875), (181, 0.007999897003173828), (182, 0.0070002079010009766), (183, 0.006999969482421875), (184, 0.006999969482421875), (185, 0.006999969482421875), (186, 0.006999969482421875), (187, 0.007999897003173828), (188, 0.006999969482421875), (189, 0.00800013542175293), (190, 0.007999897003173828), (191, 0.009000062942504883), (192, 0.006999969482421875), (193, 0.00800013542175293), (194, 0.008999824523925781), (195, 0.0070002079010009766), (196, 0.006999969482421875), (197, 0.007999897003173828), (198, 0.006999969482421875), (199, 0.006999969482421875), (200, 0.009000062942504883)]
#################################################

# The above results were pasted in CodeSkulptor and plotted with the code below.

"""
CodeSkulptor Python
AlgThink Part 2
App 3-1
"""

import simpleplot

scp_times = [(2, 0.0), (3, 0.0), (4, 0.0), (5, 0.0), (6, 0.0009999275207519531), (7, 0.0), (8, 0.0), (9, 0.0), (10, 0.0), (11, 0.0), (12, 0.0009999275207519531), (13, 0.0), (14, 0.0), (15, 0.0009999275207519531), (16, 0.0), (17, 0.0010001659393310547), (18, 0.0), (19, 0.0009999275207519531), (20, 0.0), (21, 0.0009999275207519531), (22, 0.0010001659393310547), (23, 0.0009999275207519531), (24, 0.0009999275207519531), (25, 0.0010001659393310547), (26, 0.0009999275207519531), (27, 0.0009999275207519531), (28, 0.002000093460083008), (29, 0.0009999275207519531), (30, 0.002000093460083008), (31, 0.0009999275207519531), (32, 0.002000093460083008), (33, 0.0019998550415039062), (34, 0.002000093460083008), (35, 0.0019998550415039062), (36, 0.002000093460083008), (37, 0.003000020980834961), (38, 0.002000093460083008), (39, 0.0029997825622558594), (40, 0.002000093460083008), (41, 0.003000020980834961), (42, 0.003000020980834961), (43, 0.003000020980834961), (44, 0.003999948501586914), (45, 0.003000020980834961), (46, 0.003999948501586914), (47, 0.003000020980834961), (48, 0.003999948501586914), (49, 0.003999948501586914), (50, 0.004000186920166016), (51, 0.003999948501586914), (52, 0.003999948501586914), (53, 0.005000114440917969), (54, 0.004999876022338867), (55, 0.005000114440917969), (56, 0.006000041961669922), (57, 0.004999876022338867), (58, 0.006000041961669922), (59, 0.006000041961669922), (60, 0.006000041961669922), (61, 0.006000041961669922), (62, 0.006999969482421875), (63, 0.006000041961669922), (64, 0.006999969482421875), (65, 0.006999969482421875), (66, 0.007999897003173828), (67, 0.006999969482421875), (68, 0.00800013542175293), (69, 0.007999897003173828), (70, 0.00800013542175293), (71, 0.008999824523925781), (72, 0.00800013542175293), (73, 0.009000062942504883), (74, 0.009000062942504883), (75, 0.008999824523925781), (76, 0.009999990463256836), (77, 0.009999990463256836), (78, 0.009999990463256836), (79, 0.01100015640258789), (80, 0.010999917984008789), (81, 0.01100015640258789), (82, 0.012999773025512695), (83, 0.015000104904174805), (84, 0.01399993896484375), (85, 0.018000125885009766), (86, 0.020999908447265625), (87, 0.02200007438659668), (88, 0.01699995994567871), (89, 0.013000011444091797), (90, 0.014000177383422852), (91, 0.01399993896484375), (92, 0.01399993896484375), (93, 0.015000104904174805), (94, 0.014999866485595703), (95, 0.015000104904174805), (96, 0.014999866485595703), (97, 0.014999866485595703), (98, 0.016000032424926758), (99, 0.016000032424926758), (100, 0.01699995994567871), (101, 0.019999980926513672), (102, 0.017000198364257812), (103, 0.017999887466430664), (104, 0.018000125885009766), (105, 0.018999814987182617), (106, 0.01900005340576172), (107, 0.01900005340576172), (108, 0.019999980926513672), (109, 0.019999980926513672), (110, 0.019999980926513672), (111, 0.020999908447265625), (112, 0.021000146865844727), (113, 0.020999908447265625), (114, 0.020999908447265625), (115, 0.023000001907348633), (116, 0.02200007438659668), (117, 0.023000001907348633), (118, 0.023999929428100586), (119, 0.023999929428100586), (120, 0.023999929428100586), (121, 0.026000022888183594), (122, 0.02500009536743164), (123, 0.02500009536743164), (124, 0.020999908447265625), (125, 0.03299999237060547), (126, 0.03399991989135742), (127, 0.0279998779296875), (128, 0.0280001163482666), (129, 0.026999950408935547), (130, 0.0280001163482666), (131, 0.029000043869018555), (132, 0.028999805450439453), (133, 0.029999971389770508), (134, 0.03000020980834961), (135, 0.03099989891052246), (136, 0.03099989891052246), (137, 0.037999868392944336), (138, 0.04200005531311035), (139, 0.04900002479553223), (140, 0.03299999237060547), (141, 0.025999784469604492), (142, 0.04700016975402832), (143, 0.03099989891052246), (144, 0.04900002479553223), (145, 0.03600001335144043), (146, 0.03600001335144043), (147, 0.03699994087219238), (148, 0.03699994087219238), (149, 0.03800010681152344), (150, 0.03800010681152344), (151, 0.037999868392944336), (152, 0.03900003433227539), (153, 0.03900003433227539), (154, 0.039999961853027344), (155, 0.0409998893737793), (156, 0.0410001277923584), (157, 0.0409998893737793), (158, 0.04200005531311035), (159, 0.042999982833862305), (160, 0.042999982833862305), (161, 0.042999982833862305), (162, 0.04400014877319336), (163, 0.04499983787536621), (164, 0.04500007629394531), (165, 0.046000003814697266), (166, 0.046000003814697266), (167, 0.046000003814697266), (168, 0.04700016975402832), (169, 0.04699993133544922), (170, 0.04799985885620117), (171, 0.04900002479553223), (172, 0.04900002479553223), (173, 0.04999995231628418), (174, 0.05000019073486328), (175, 0.05099987983703613), (176, 0.05200004577636719), (177, 0.05200004577636719), (178, 0.05200004577636719), (179, 0.05300021171569824), (180, 0.053999900817871094), (181, 0.054000139236450195), (182, 0.05500006675720215), (183, 0.0559999942779541), (184, 0.056999921798706055), (185, 0.056999921798706055), (186, 0.056999921798706055), (187, 0.05800008773803711), (188, 0.05900001525878906), (189, 0.05900001525878906), (190, 0.06000018119812012), (191, 0.06099987030029297), (192, 0.06200003623962402), (193, 0.06299996376037598), (194, 0.06299996376037598), (195, 0.06300020217895508), (196, 0.06399989128112793), (197, 0.06500005722045898), (198, 0.06500005722045898), (199, 0.06700015068054199), (200, 0.06699991226196289)]
fcp_times = [(2, 0.0), (3, 0.0), (4, 0.0), (5, 0.0), (6, 0.0), (7, 0.0), (8, 0.0), (9, 0.0), (10, 0.0), (11, 0.0), (12, 0.0009999275207519531), (13, 0.0), (14, 0.0), (15, 0.0010001659393310547), (16, 0.0), (17, 0.0), (18, 0.0009999275207519531), (19, 0.0), (20, 0.0009999275207519531), (21, 0.0), (22, 0.0010001659393310547), (23, 0.0), (24, 0.0009999275207519531), (25, 0.0), (26, 0.0009999275207519531), (27, 0.0010001659393310547), (28, 0.0009999275207519531), (29, 0.0), (30, 0.0), (31, 0.0009999275207519531), (32, 0.0010001659393310547), (33, 0.0009999275207519531), (34, 0.0009999275207519531), (35, 0.0010001659393310547), (36, 0.0009999275207519531), (37, 0.0010001659393310547), (38, 0.0009999275207519531), (39, 0.0009999275207519531), (40, 0.0009999275207519531), (41, 0.0010001659393310547), (42, 0.0009999275207519531), (43, 0.002000093460083008), (44, 0.0009999275207519531), (45, 0.0009999275207519531), (46, 0.0010001659393310547), (47, 0.0019998550415039062), (48, 0.0010001659393310547), (49, 0.0009999275207519531), (50, 0.0019998550415039062), (51, 0.002000093460083008), (52, 0.0009999275207519531), (53, 0.002000093460083008), (54, 0.0009999275207519531), (55, 0.002000093460083008), (56, 0.0019998550415039062), (57, 0.002000093460083008), (58, 0.002000093460083008), (59, 0.0019998550415039062), (60, 0.002000093460083008), (61, 0.002000093460083008), (62, 0.0029997825622558594), (63, 0.002000093460083008), (64, 0.002000093460083008), (65, 0.0019998550415039062), (66, 0.0019998550415039062), (67, 0.003000020980834961), (68, 0.002000093460083008), (69, 0.003000020980834961), (70, 0.0019998550415039062), (71, 0.003000020980834961), (72, 0.003000020980834961), (73, 0.002000093460083008), (74, 0.003000020980834961), (75, 0.0029997825622558594), (76, 0.002000093460083008), (77, 0.003000020980834961), (78, 0.002000093460083008), (79, 0.002000093460083008), (80, 0.0029997825622558594), (81, 0.003000020980834961), (82, 0.003000020980834961), (83, 0.003000020980834961), (84, 0.003000020980834961), (85, 0.003000020980834961), (86, 0.003000020980834961), (87, 0.003000020980834961), (88, 0.003000020980834961), (89, 0.003000020980834961), (90, 0.003000020980834961), (91, 0.003000020980834961), (92, 0.003000020980834961), (93, 0.003999948501586914), (94, 0.003000020980834961), (95, 0.003999948501586914), (96, 0.003000020980834961), (97, 0.003000020980834961), (98, 0.003000020980834961), (99, 0.003000020980834961), (100, 0.003999948501586914), (101, 0.003000020980834961), (102, 0.003999948501586914), (103, 0.004000186920166016), (104, 0.0029997825622558594), (105, 0.004000186920166016), (106, 0.003999948501586914), (107, 0.003000020980834961), (108, 0.003999948501586914), (109, 0.004000186920166016), (110, 0.003999948501586914), (111, 0.004999876022338867), (112, 0.003999948501586914), (113, 0.005000114440917969), (114, 0.003000020980834961), (115, 0.003999948501586914), (116, 0.005000114440917969), (117, 0.004999876022338867), (118, 0.004000186920166016), (119, 0.003999948501586914), (120, 0.005000114440917969), (121, 0.004999876022338867), (122, 0.006000041961669922), (123, 0.005000114440917969), (124, 0.004999876022338867), (125, 0.005000114440917969), (126, 0.004999876022338867), (127, 0.005000114440917969), (128, 0.005000114440917969), (129, 0.006000041961669922), (130, 0.004999876022338867), (131, 0.005000114440917969), (132, 0.004999876022338867), (133, 0.004999876022338867), (134, 0.006000041961669922), (135, 0.006000041961669922), (136, 0.006000041961669922), (137, 0.004999876022338867), (138, 0.004999876022338867), (139, 0.005000114440917969), (140, 0.00599980354309082), (141, 0.006000041961669922), (142, 0.006000041961669922), (143, 0.006000041961669922), (144, 0.006000041961669922), (145, 0.004999876022338867), (146, 0.006000041961669922), (147, 0.006000041961669922), (148, 0.006000041961669922), (149, 0.006000041961669922), (150, 0.004999876022338867), (151, 0.006999969482421875), (152, 0.006999969482421875), (153, 0.006000041961669922), (154, 0.006000041961669922), (155, 0.006999969482421875), (156, 0.006000041961669922), (157, 0.006000041961669922), (158, 0.006000041961669922), (159, 0.006000041961669922), (160, 0.006999969482421875), (161, 0.0070002079010009766), (162, 0.00599980354309082), (163, 0.0070002079010009766), (164, 0.006000041961669922), (165, 0.00599980354309082), (166, 0.0070002079010009766), (167, 0.006999969482421875), (168, 0.006999969482421875), (169, 0.006000041961669922), (170, 0.006000041961669922), (171, 0.006999969482421875), (172, 0.006999969482421875), (173, 0.006999969482421875), (174, 0.006999969482421875), (175, 0.00800013542175293), (176, 0.006999969482421875), (177, 0.006999969482421875), (178, 0.006999969482421875), (179, 0.006999969482421875), (180, 0.006999969482421875), (181, 0.007999897003173828), (182, 0.0070002079010009766), (183, 0.006999969482421875), (184, 0.006999969482421875), (185, 0.006999969482421875), (186, 0.006999969482421875), (187, 0.007999897003173828), (188, 0.006999969482421875), (189, 0.00800013542175293), (190, 0.007999897003173828), (191, 0.009000062942504883), (192, 0.006999969482421875), (193, 0.00800013542175293), (194, 0.008999824523925781), (195, 0.0070002079010009766), (196, 0.006999969482421875), (197, 0.007999897003173828), (198, 0.006999969482421875), (199, 0.006999969482421875), (200, 0.009000062942504883)]

simpleplot.plot_lines("Desktop Python Running Times of Slow and Fast Closest Pair Algms",
								700, 600, "No. of Initial Clusters", "Running Time in Seconds",
								[scp_times, fcp_times], False, ["SlowClosestPair", "FastClosestPair"])
								
## ANSWER
# See AlgThink_App3-1_Plot for resulting plot

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

#################################################
## Work will be done in CodeSkulptor Python unless runtime issues occur.
## What do you know, runtime issues...will run on Desktop.
#################################################

# Pasting alg_project3_viz module. All changed lines will be annotated.
# References to modules will be removed as functions will be directly called.
# All (#*n: n > 2) lines from this module replaced with lines: (#!!!...).

"""
CodeSkulptor Python
AlgThink Part 2
App 3-2

---------------------------------------------
Example code for creating and visualizing
cluster of county-based cancer risk data

Note that you must download the file
http://www.codeskulptor.org/#alg_clusters_matplotlib.py
to use the matplotlib version of this code
"""

# Flavor of Python - desktop or CodeSkulptor
DESKTOP = True

import math
import random
import urllib2
## Removing for PyCharm.
##import alg_cluster

# conditional imports
if DESKTOP:
	## Commenting out as I will paste the contents directly into this file in PyCharm.
	## Adding print statement for cheekiness.
	#import alg_project3_solution      # desktop project solution
	#import alg_clusters_matplotlib
	print "Using Desktop, move along!"
else:
	#import userXX_XXXXXXXX as alg_project3_solution   # CodeSkulptor project solution
	import alg_clusters_simplegui
	import codeskulptor
	## Removing for PyCharm.
	##codeskulptor.set_timeout(60)


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Code to load data tables

# URLs for cancer risk data tables of various sizes
# Numbers indicate number of counties in data table

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


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Code to create sequential clustering
# Create alphabetical clusters for county data

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


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Code to load cancer data, compute a clustering and
# visualize the results


def run_example():
	"""
	Load a data table, compute a list of clusters and
	plot a list of clusters

	Set DESKTOP = True/False to use either matplotlib or simplegui
	"""
	## App3-2, 3-3
	## data_table = load_data_table(DATA_3108_URL)
	
	## App3-5, 3-6
	## data_table = load_data_table(DATA_111_URL)
	
	## App3-7 Correctness Check
	## data_table = load_data_table(DATA_290_URL)
	
	## App3-7 
	data_table = load_data_table(DATA_111_URL)

	singleton_list = []
	for line in data_table:
		## Removing alg_cluster reference below. Reminder to add Cluster class to PyCharm file.
		singleton_list.append(Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

	#cluster_list = sequential_clustering(singleton_list, 15)
	#print "Displaying", len(cluster_list), "sequential clusters"

	## App3-2 image generated by running this code chunk <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
	## cluster_list = hierarchical_clustering(singleton_list, 15)
	## print "Displaying", len(cluster_list), "hierarchical clusters"

	## App3-3 image generated by running this code chunk <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
	## cluster_list = kmeans_clustering(singleton_list, 15, 5)
	## print "Displaying", len(cluster_list), "k-means clusters"
	
	## App3-5 image generated by running this code chunk <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
	## cluster_list = hierarchical_clustering(singleton_list, 9)
	## print "Displaying", len(cluster_list), "hierarchical clusters"
	
	## App3-6 image generated by running this code chunk <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
	## cluster_list = kmeans_clustering(singleton_list, 9, 5)
	## print "Displaying", len(cluster_list), "k-means clusters"
	
	## App3-7 distortions computed using code below <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
	## Note that each must be run separately, as hierarchical_clustering mutates the input.
	## TEST ON 290 COUNTIES
	## hclust = hierarchical_clustering(singleton_list, 16)
	## print "HierarchicalClustering Distortion:", compute_distortion(hclust, data_table)
	## Confirmed 2.575 x 10**11
	## kclust = kmeans_clustering(singleton_list, 16, 5)
	## print "KMeansClustering Distortion:", compute_distortion(kclust, data_table)
	## Confirmed 2.323 x 10**11
	## ACTUAL CODE
	## hclust = hierarchical_clustering(singleton_list, 9)
	## print "Displaying", len(hclust), "hierarchical clusters"
	## print "HierarchicalClustering Distortion:", compute_distortion(hclust, data_table)
	## Returned: 1.75163886916e+11 or 1.752 x 10**11
	## kclust = kmeans_clustering(singleton_list, 9, 5)
	## print "Displaying", len(kclust), "k-means clusters"
	## print "KMeansClustering Distortion:", compute_distortion(kclust, data_table)
	## Returned: 2.71254226924e+11 or 2.713 x 10**11
	
	## Commenting out below code used for 3-2, 3-3, 3-5, 3-6
	## No plotting necessary from here on out
	## --------------------------------------------------------------
	# # draw the clusters using matplotlib or simplegui
	# if DESKTOP:
		# #plot_clusters(data_table, cluster_list, False)
		# ## Module removed from these lines.
		# ##alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, False)
		# plot_clusters(data_table, cluster_list, True)  #add cluster centers
	# else:
		# alg_clusters_simplegui.PlotClusters(data_table, cluster_list)   # use toggle in GUI to add cluster centers
	## --------------------------------------------------------------
		
## Removing run_example() for use at the very end.
##run_example()
#################################################

# Pasting pair distance and clustering functions.

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

	## Sorting just in case.
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
#################################################

# Pasting alg_clusters_matplotlib.py contents.

"""
Some provided code for plotting the clusters using matplotlib
"""

import math
import urllib2
import matplotlib.pyplot as plt


# URLS for various important datasets
DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
MAP_URL = DIRECTORY + "data_clustering/USA_Counties.png"

# Define colors for clusters.  Display a max of 16 clusters.
COLORS = ['Aqua', 'Yellow', 'Blue', 'Fuchsia', 'Black', 'Green', 'Lime', 'Maroon', 'Navy', 'Olive', 'Orange', 'Purple', 'Red', 'Brown', 'Teal']



# Helper functions

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
#################################################

# Cluster class for use in App3-2.

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
#################################################

# Run example in PyCharm to generate the image.

## run_example()
## print "FINISHED!"

## ANSWER
# See AlgThink_App3-2_Plot or AlgThink_App3-2_Plot_HiRes

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

#################################################
## I will use the above code with minor, annotated changes. I will comment 
## out the lines used for App3-2 and identify the lines used for 3-3 on.
## Look at the run_example() function for changes. 
#################################################

# Ran into issues with PyCharm running the kmeans_clustering() function.
# There was an issue with an indentation that caused an error with the
# idx_j and idx_f comparison ("index out of range") but a change to the
# indentation, I think using a catch-all indentation change fix built into PyCharm,
# fixed it. I pasted the fixed code from '''QUESTION 2... down to the answer
# to this question ...## ANSWER. 

## run_example()
## print "FINISHED!"

## ANSWER
# See AlgThink_App3-3_Plot or AlgThink_App3-3_Plot_HiRes

'''
QUESTION 4

Which clustering method is faster when the number of output clusters is either
a small fixed number or a small fraction of the number of input clusters? Provide
a short explanation in terms of the asymptotic running times of both methods. 
You should assume that hierarchical_clustering uses fast_closest_pair and that
k-means clustering always uses a small fixed number of iterations.
'''

## ANSWER

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

## run_example()
## print "FINISHED!"

## ANSWER
# See AlgThink_App3-5_Plot or AlgThink_App3-5_Plot_HiRes

'''
QUESTION 6

Use alg_project3_viz to create an image of the 9 clusters generated by applying 5
iterations of k-means clustering to the 111 county cancer risk data set. Submit
your image as previously described. Upload and be done.
'''

## run_example()
## print "FINISHED!"

## ANSWER
# See AlgThink_App3-6_Plot or AlgThink_App3-6_Plot_HiRes

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

#################################################
## I will use some code above as necessary. If it is used, it will be identified.
## The new function will be written below and appended to code used in PyCharm.
## Once again, everything will get copied from '''QUESTION 2... until ...## ANSWER.
#################################################

# Write function to compute distortion

def compute_distortion(cluster_list, data_table):
	"""
	Compute distortion for a list of cluster objects against a data table.
	"""
	distortion = 0
	for cluster in cluster_list:
		distortion += cluster.cluster_error(data_table)
	return distortion
	
## run_example()
## print "FINISHED!"

## ANSWER
"""
HierarchicalClustering Distortion: 1.752 x 10**11
KMeansClustering Distortion: 2.713 x 10**11
"""

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

## ANSWER

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

'''
QUESTION 9

Based on your answer to 3-8, which method requires less human supervision
to produce clusterings with relatively low distortion?
'''

## ANSWER

"""
While it may take longer to process, the HierarchicalClustering method seemed to
produce clusterings with relatively low distortion all on its own. Someone using the
KMeansClustering method would have to experiment with different parameters in
order to optimize clusterings. The basis for initial cluster centers could be changed
to something other than population, and the k and q values could be fine-tuned. 
With HierarchicalClustering, it is a "set and forget" kind of computation.
"""

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

#################################################
## Now is when I realized that I should be rewriting run_example() for each 
## question. This will greatly clarify things. I may just do this next time for all
## questions, but for now I will rewrite that for this question.
## I will also utilize matplotlib to produce my plots for this question.
#################################################

# Write run_question_310() function based on run_example()
# Pasting load_data_table() down here to quickly reference for modifications.

# DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
# DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
# DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"
# DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
# DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"

# def load_data_table(data_url):
	# """
	# Import a table of county-based cancer risk data
	# from a csv format file
	# """
	# data_file = urllib2.urlopen(data_url)
	# data = data_file.read()
	# data_lines = data.split('\n')
	# print "Loaded", len(data_lines), "data points"
	# data_tokens = [line.split(',') for line in data_lines]
	# return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])]
			# for tokens in data_tokens]

def run_question_310(data_set = 111, lower = 6, upper = 20, iterations = 5):
	"""
	Produce a list of clusters with output clusters from 6 to 20 (inclusive), q = 5.
	Compute the distortion of each list and add it with the k value to a list for plotting.
	Compute these values and plot based on data_set parameter.
	"""
	
	if data_set == 111:
		data_table_111 = load_data_table(DATA_111_URL)
		
		list_111 = []
		for line in data_table_111:
			list_111.append(Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
			
		x_vals = range(lower, upper + 1)
		k_distortions_111 = []
		h_distortions_111 = []
		
		for output_clusters in x_vals:
			kclust = kmeans_clustering(list_111, output_clusters, iterations)
			k_distortions_111.append(compute_distortion(kclust, data_table_111))
		
		h_list_111 = list_111
		for output_clusters in range(upper, lower - 1, -1):
			hclust = hierarchical_clustering(h_list_111, output_clusters)
			h_distortions_111.insert(0, compute_distortion(hclust, data_table_111))
			h_list_111 = hclust
		
		k_line = plt.plot(x_vals, k_distortions_111, color='g', label="KMeansClustering")
		h_line = plt.plot(x_vals, h_distortions_111, color='r', label="HierarchicalClustering")
		plt.legend()
		plt.title("Distortion Between Clustering Methods on 111 County Data Set")
		plt.xlabel("Number of Output Clusters")
		plt.ylabel("Distortion")
		plt.show()
		
	elif data_set == 290:
		data_table_290 = load_data_table(DATA_290_URL)
		
		list_290 = []
		for line in data_table_290:
			list_290.append(Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
			
		x_vals = range(lower, upper + 1)
		k_distortions_290 = []
		h_distortions_290 = []
		
		for output_clusters in x_vals:
			kclust = kmeans_clustering(list_290, output_clusters, iterations)
			k_distortions_290.append(compute_distortion(kclust, data_table_290))
		
		h_list_290 = list_290
		for output_clusters in range(upper, lower - 1, -1):
			hclust = hierarchical_clustering(h_list_290, output_clusters)
			h_distortions_290.insert(0, compute_distortion(hclust, data_table_290))
			h_list_290 = hclust
		
		k_line = plt.plot(x_vals, k_distortions_290, color='g', label="KMeansClustering")
		h_line = plt.plot(x_vals, h_distortions_290, color='r', label="HierarchicalClustering")
		plt.legend()
		plt.title("Distortion Between Clustering Methods on 290 County Data Set")
		plt.xlabel("Number of Output Clusters")
		plt.ylabel("Distortion")
		plt.show()
			
	elif data_set == 896:
		data_table_896 = load_data_table(DATA_896_URL)
		
		list_896 = []
		for line in data_table_896:
			list_896.append(Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
			
		x_vals = range(lower, upper + 1)
		k_distortions_896 = []
		h_distortions_896 = []
		
		for output_clusters in x_vals:
			kclust = kmeans_clustering(list_896, output_clusters, iterations)
			k_distortions_896.append(compute_distortion(kclust, data_table_896))
		
		h_list_896 = list_896
		for output_clusters in range(upper, lower - 1, -1):
			hclust = hierarchical_clustering(h_list_896, output_clusters)
			h_distortions_896.insert(0, compute_distortion(hclust, data_table_896))
			h_list_896 = hclust
		
		k_line = plt.plot(x_vals, k_distortions_896, color='g', label="KMeansClustering")
		h_line = plt.plot(x_vals, h_distortions_896, color='r', label="HierarchicalClustering")
		plt.legend()
		plt.title("Distortion Between Clustering Methods on 896 County Data Set")
		plt.xlabel("Number of Output Clusters")
		plt.ylabel("Distortion")
		plt.show()

## Uncomment out the line for the data set you want to print (default = 111)		
#run_question_310()
#run_question_310(290)
#run_question_310(896)

## ANSWER
# See AlgThink_App3-10_Plot_111_HiRes, AlgThink_App3-10_Plot_290_HiRes 
# and AlgThink_App3-10_Plot_896_HiRes

'''
QUESTION 11

For each data set (111, 290, and 896 counties), does one clustering method
consistently produce lower distortion clusterings when the number of output
clusters is in the range 6 to 20? If so, indicate on which data set(s) one method
is superior to the other.
'''

## ANSWER

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

'''
BONUS QUESTION

Which clustering method would you prefer when analyzing these data sets? 
Provide a summary of each method's strengths and weaknesses on these
data sets in the three areas considered in this application. Your summary should 
be at least a paragraph in length (4 sentences minimum).
'''

## ANSWER

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
this method's parameters could be tweaked to improve results. HierarchicalClustering 
did not require such in-depth reworking to optimize results, so it performed better 
with regard to automation.

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