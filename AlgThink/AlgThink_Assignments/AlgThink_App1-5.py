"""
Rice University / Coursera: Algorithmic Thinking (Part 1)
Application 1-5
"""
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

## ANSWER
'''
1.) The plot of the in-degree distribution for the DPA graph is indeed similar to that 
of the citation graph. Both plots begin with the first in-degree number at the maximum 
distribution and then gradually decrease in distribution as the in-degree number increases. 
At very high in-degree numbers, the plot becomes "dirtier" and the somewhat continuous 
best fit line splits into multiple lines.

2.) The "rich gets richer" phenomenon mimics the DPA process. The DPA graph begins as 
a complete digraph with m  nodes. With each node addition up to n nodes, the algorithm 
chooses m random nodes from the existing set of nodes to which the new node is linked. 
The probability of choosing a node via this process is directly related to the number of 
in-degrees that each existing node has, since the numerator of the probability function is 
the number of in-degrees that an existing node (j) has, plus 1. As the number of in-degrees 
of a particular node increases, so does the probability of that node being chosen in the next 
node addition. This effect is compounded with each addition. 

3.) This "rich gets richer" phenomenon could explain the structure of the physics citation graph 
very easily. Scientific research has always been built on the foundation of all research that has 
come before it. Certain underlying principles in a particular field (like physics theory) will be 
discovered when repeated study is applied to the data that stem from their existence. Subsequent 
research studies will refer to these principles as a basis for their new approaches and experiments. 
Slowly over time, as evidence builds toward newer theories, more principles are revealed, and 
hese new principles become popular, more modern points of reference--although often they do 
not entirely supplant the originally-discovered, "fundamental" principles. An example in the field of 
Physics is Newton's laws of motion, laying the foundation for classical mechanics. These principles 
lead to the understanding of projectile motion, which eventually leads to the understanding of rocket 
ships and ultimately space travel and beyond. 
'''