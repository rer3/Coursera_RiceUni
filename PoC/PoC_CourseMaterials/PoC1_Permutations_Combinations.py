"""
Function to generate permutatoins of outcomes
Repetition of outcomes not allowed
"""

def gen_permutations(outcomes, length):
    """
    Function to generate permutations.
    """
    ans = set([()])
    for index in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                if item not in seq:
                    new_seq = list(seq)
                    new_seq.append(item)
                    temp.add(tuple(new_seq))
        ans = temp
                
    return ans

def gen_combinations(outcomes, length):
    """
    Function to generate combinations.
    """
    all_perms = gen_permutations(outcomes, length)
    sorted_seq = [tuple(sorted(sequence)) for sequence in all_perms]
    return set(sorted_seq)

def run_example1():
    """
    Function to run examples of permutations.
    """
    
    # example for digits
    outcomes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #outcomes = ["Red", "Green", "Blue"]
    #outcomes = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    
    length = 4
    permutations = gen_permutations(outcomes, length)
    print "Computed", len(permutations), "permutations of", str(length), "outcomes"
    print "Permutations were", permutations

def run_example2():
    """
    Function to run examples of combinations.
    """
    # example for digits
    outcomes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #outcomes = ["Red", "Green", "Blue"]
    #outcomes = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    
    length = 4
    combos = gen_combinations(outcomes, length)
    print "Computed", len(combos), "combinations of", str(length), "outcomes"
    print "Combinations were", combos
    
run_example1()
run_example2()

# Perms for numbers of lengths 1-4
#10
#90
#720
#5040

# Combos for numbers of lengths 1-4
#10
#45
#120
#210
########################################
## Code to test factorial and optimize runtime of computations,
## also to test number of permutations and combinations using
## input 59 outcomes and length 6 (lottery example).
import time
import math

start = time.time()
print math.factorial(59) / math.factorial(59 - 6)
end = time.time()
print "That took", str(end - start), "seconds to compute"

num_perms = 1
for idx in range(59, 59 - 6, -1):
    num_perms *= idx
    
start = time.time()
print num_perms
end = time.time()
print "That took", str(end - start), "seconds to compute"

print "Combinations"
print num_perms / math.factorial(6)

print math.factorial(10) / math.factorial(10 - 4)