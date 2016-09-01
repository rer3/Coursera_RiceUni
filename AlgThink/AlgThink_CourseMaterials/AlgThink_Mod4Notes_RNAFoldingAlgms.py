"""
Rice University / Coursera: CLASSNAME
Module 4: Class Notes
RNA Folding Algorithms: Dynamic Programming vs. Recursive Implementations
"""
##################################################
##################################################
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in PyCharm to optimize running times.
##################################################

## All import statements needed.

import math
import matplotlib.pyplot as plt
import random
import time

##################################################

# Testing Grounds

# From the notes, the basic structure of the DP (dynamic programming) 
# implementation of an RNA secondary structure / folding algorithm is:
# 1.  Initialize OPT(i,j) <- 0 when i >= j - 4
# 2.  For k <- 5 to n-1:
# 3.      For i <- 1 to n-k:
# 4.          j <- i + k
# 5.          OPT(i,j) = max{OPT(i,j-1), max-over-t(1 + OPT(i,t+1) + OPT(t+1,j-1))}
# 6.  Return OPT(1, n)
# Note that t = i to j-1 where (t,j) is a link (hence the +1 in the statement).

# First I will write a function to make a matrix and fill it with whatever default
# value I specify. This is the first utility function.

def make_matrix(height, width, fill_value):
    """
    Make a matrix of specified dimensions and fill it with the default value.
    """
    return [[fill_value for dummy_col in range(width)] for 
					dummy_row in range(height)]
    ## Note that the below syntax will lead to changes made to EVERY row
    ## when a [row][col] index is referenced and an assignment made.
    ## return [[fill_value] * width] * height
    
# Next, a function is needed that checks for complementary nucleotides.
# The A-T pair is added for use of this function with DNA strands. 

def is_complement(a, b):
    """
    Return True if nucleotide a is complementary to nucleotide b.
    """
    if len(a) == len(b) == 1:
        return (a.upper(), b.upper()) in [
            ("A", "T"), ("T", "A"),
            ("C", "G"), ("G", "C"),
            ("A", "U"), ("U", "A")]
            
# A function to print the matrix with the RNA/DNA strand across the top
# and down the left side would be helpful.

def print_matrix(sequence, matrix):
    """
    Prints the matrix of a given DNA/RNA sequence.
    """
    seq = sequence
    mat = matrix
    length = len(seq)
    maxlen = 0
    for row in range(length):
        for col in range(length):
            score = mat[row][col]
            if len(str(score)) > maxlen:
                maxlen = len(str(score))
    
    result = "   "
    for nuc in seq:
        result += str(nuc) + " "*(maxlen)
    result += "\n"
    
    for row in range(length):
        result += seq[row] + "  "
        for col in range(length):
            scorelen = len(str(mat[row][col]))
            result += str(mat[row][col]) + " "*(1+maxlen-scorelen)
        result += "\n"
    print result
    
# The DP RNA folding function will be implemented first, followed by a recursive
# version. Then the running times will be compared in PyCharm using matplotlib.

def rnafold(seq):
    """
    Dynamic programming function to traverse an RNA sequence
    and return the maximum number of linkages and associated
    pairs.
    """
    n = len(seq)
    OPT = make_matrix(n, n, 0)
    
    for i in range(n):
        for j in range(n):
            if i >= j - 4:
                OPT[i][j] = 0
               
    for k in range(5, n):
        for i in range(n-k):
            j = i + k
            
            # Start with j not being paired
            best_t = OPT[i][j-1]
            
            # Find max over t for substring
            for t in range(i, j-4):
                if is_complement(seq[t], seq[j]):
                    if t > i:
                        t_val = 1 + OPT[i][t-1] + OPT[t+1][j-1]
                    # When t <= i, the first term is omitted
                    # No pairs beyond this diagonal are permitted
                    else:
                        t_val = 1 + OPT[t+1][j-1]
                    if t_val > best_t:
                        best_t = t_val
            OPT[i][j] = best_t
         
    return OPT

def rnafold_recur(seq):
    """
    Recursive function to traverse an RNA sequence and return
    the maximum number of linkages and associated pairs.
    """
    if len(seq) < 6:
        return 0
    
    best_t = 0
    for k in range(5, len(seq)):
        for i in range(len(seq) - k):
            j = i + k
            best_t = rnafold_recur(seq[:-1])
            for t in range(i, j-4):
                if is_complement(seq[t], seq[j]):
                    if t > i:
                        t_val = 1 + rnafold_recur(seq[i:t]) + \
                        rnafold_recur(seq[t+1:j])
                    else:
                        t_val = 1 + rnafold_recur(seq[t+1:j])
                    if t_val > best_t:
                        best_t = t_val
                        
    return best_t
    
# Next I will create random strands of varying length (6 to 12 units) from the
# {A, U, C, G} set. 

rna_nucleobases = ["A", "U", "C", "G"]
sequences = []
for length in range(6, 13):
    seq = ""
    for nuc in range(length):
        seq += random.choice(rna_nucleobases)
    sequences.append(seq)
print "Sequences are:"
for item in sequences:
    print item
print "-"*20

# Now compute running times for DP and recursive functions.

dp_times = []
recur_times = []

for seq in sequences:
	# DP function
	start = time.time()
	opt = rnafold(seq)
	end = time.time()
	dp_times.append(end-start)
	# Recursive function
	start = time.time()
	opt = rnafold_recur(seq)
	end = time.time()
	recur_times.append(end-start)
	
# Plot the two sets of values.

x_vals = range(6, 13)
dp_line = plt.plot(x_vals, dp_times, color='g', label="DP")
recur_line = plt.plot(x_vals, recur_times, color='r', label="Recursion")
plt.legend()
plt.title("DP vs. Recursive RNA Folding Scoring Computation")
plt.xlabel("Length of Sequence")
plt.ylabel("Running Time (seconds)")
plt.show()

# Now I will build a loglog plot of these values. 

log_x = [math.log(val)  if val > 0 else 0 for val in x_vals]
log_dp = [math.log(val) if val > 0 else 0 for val in dp_times]
log_recur = [math.log(val) if val > 0 else 0 for val in recur_times]

dp_logline = plt.plot(log_x, log_dp, color='g', label="DP")
recur_logline = plt.plot(log_x, log_recur, color='r', label="Recursion")
plt.legend()
plt.title("DP vs. Recursive RNA Folding Scoring Computation (loglog)")
plt.xlabel("Length of Sequence (log)")
plt.ylabel("Running Time (log(seconds))")
plt.show()

# The T(n) for the recursive implementation appears to be n**3. 

# The next part of this overall problem is to implement a backtrace function that
# is passed a matrix to be analyzed backwards from the end point and returns
# a list of pairs of indices of nucleobases which are matched up when the optimum
# score is returned by the DP rna folding function.

def rnafold_backtrace(matrix):
	"""
	Returns a list of tuples which correspond to indices of a sequence
	that are paired up at the highest optimality score.
	"""
	pass

##################################################
##################################################