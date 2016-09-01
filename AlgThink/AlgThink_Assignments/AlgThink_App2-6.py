"""
Rice University / Coursera: Algorithmic Thinking (Part 1)
Application 2-6 (Bonus)
"""

'''
An increasing number of people with malevolent intent are 
interested in disrupting computer networks. If you found one 
of the two random graphs to be more resilient under targeted 
attacks than the computer network, do you think network 
designers should always ensure that networks' topologies 
follow that random model? Think about the considerations that 
one might have to take into account when designing networks 
and provide a short explanation for your answer.
'''

## ANSWER
'''
The ER graph model has many disadvantages as a network topology, 
even if it is resilient against targeted attacks. First, the ER model can form 
many redundant loops between nodes, likely a reason behind its resilience 
against a targeted attack. This will increase the cost of this network, similar 
to a network with mesh topology. This high level of complexity may want 
to be avoided in most instances, as not only would it be costly, but also 
difficult to manage.
'''