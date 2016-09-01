"""
Rice University / Coursera: Algorithmic Thinking (Part 1)
Application 2-2
"""

'''
Consider removing a significant fraction of the nodes in each graph 
using random_order. We will say that a graph is resilient under this 
type of attack if the size of its largest connected component is roughly 
(within ~25%) equal to the number of nodes remaining, after the 
removal of each node during the attack.

Examine the shape of the three curves from your plot in Question 1. 
Which of the three graphs are resilient under random attacks as the first 
20% of their nodes are removed? Note that there is no need to compare 
the three curves against each other in your answer to this question.
'''

## ANSWER
# See AlgThink_App2-1_Plot
'''
All 3 graphs have a total of 1239 nodes, so the first 20% of nodes to be 
removed are roughly nodes 0 through 247. Rounding that to node 250, 
we can see that the largest CC of each graph during the removal of node 
250 is approximately: Network - 800, ER - 950, UPA - 950. When 250 
nodes are removed from one of these graphs, about 990 nodes remain to 
be removed. The ER and UPA graphs demonstrate strong resilience, as defined 
by having largest CCs roughly equal to nodes remaining (within 25%, which 
means the CC has at least 742 nodes, or 25% of 990). Each has about 950 
nodes in the largest CC when node 250 is removed, or about 96% of the total 
nodes remaining. The network graph, however, shows weak resilience with its 
largest CC at the removal of node 250 only including about 81% of the remaining 
nodes. It barely makes the within-25% cut off, but it is technically resilient 
according to that definition. 
'''