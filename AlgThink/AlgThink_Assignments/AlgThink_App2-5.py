"""
Rice University / Coursera: Algorithmic Thinking (Part 1)
Application 2-5
"""

'''
Now, consider removing a significant fraction of the nodes in each graph 
using targeted_order. Examine the shape of the three curves from your plot in 
Question 4. Which of the three graphs are resilient under targeted attacks as the 
first 20% of their nodes are removed? Again, note that there is no need to 
compare the three curves against each other in your answer to this question.
'''

## ANSWER
# See AlgThink_App2-4_Plot
'''
All 3 graphs have a total of 1239 nodes, so the first 20% of nodes to be removed 
are roughly nodes 0 through 247. Rounding that to node 250, we can see that the 
largest CC of each graph during the removal of node 250 is approximately: 
Network - 1, ER - 950, UPA - 20. When 250 nodes are removed from one of these 
graphs, about 990 nodes remain to be removed. Resilience, as defined above, is 
shown when the graph's largest CC is about the size (within 25%) of all remaining 
nodes, or in this case, the largest CC is anywhere from 740 to 990. The ER graph 
shows resilience under targeted attack order conditions, while the network and UPA 
graphs do not. 
'''