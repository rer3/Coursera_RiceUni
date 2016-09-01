"""
Rice University / Coursera: Algorithmic Thinking (Part 2)
Module 4: Project
Computing Alignments of Sequences
"""
##################################################
##################################################
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
##################################################

## Below is the link to the description of this assignment.

COURSE = "https://class.coursera.org/algorithmicthink2-003/"
DESCRIPTION = COURSE + "wiki/project_4"

#########################
## Implementation from AlgThink_Mod4Notes_RNAFoldingAlgms.py.

def make_matrix(height, width, fill_value):
	"""
	Make a matrix of specified dimensions and fill it with the default fill_value.
	"""
	return [[fill_value for dummy_col in range(width)] for 
					dummy_row in range(height)]

##################################################

DIRECTIONS = """
Overview
----------
In Homework 4, we explored the use of dynamic programming in measuring the
similarity between two sequences of characters. Given an alphabet SIG and a 
scoring matrix M defined over SIG U {'-'}, the dynamic programming method
computed a score that measured the similarity of two sequences X and Y based
on the values of this scoring matrix. In particular, this method involved computing
an alignment matrix S between X and Y whose entry S_ij scored the similarity of
substrings X[0...i-1] and Y[0...j-1]. These notes (https://d396qusza40orc.
cloudfront.net/algorithmicthink/handouts/SequenceAlignment.pdf) provide an 
overview of the process.

In Project 4, we will implement four functions. The first pair will return matrices
that we will use in computing the alignment of two sequences. The second pair
will return global and local alignments of two input sequences based on a provided
alignment matrix. You will then use these functions in Application 4 to analyze two
problems involving comparison of similar sequences.

Modeling Matrices
----------
For Project 4, you will work with two types of matrices: alignment matrices and
scoring matrices. Alignment matrices will follow the same indexing scheme that
we used for grids (https://class.coursera.org/algorithmicthink2-003/wiki/grids)
in Principles of Computing. Entries in the alignment matrix will be indexed by
their row and column with these integer indices starting at zero. We will model
these matrices as lists of lists in Python and can access a particular entry via an
expression of the form alignment_matrix[row][col].

For scoring matrices, we take a different approach since the rows and cols of
the matrix are indexed by characters in SIG U {'-'} (specified alphabet plus 
dash). In particular, we will represent a scoring matrix in Python as a dictionary
of dictionaries. Given two characters row_char and col_char, we can access the
matrix entry corresponding to this pair of characters via:
scoring_matrix[row_char][col_char].

Matrix Functions
----------
The first two functions that you will implement compute a common class of
scoring matrices and compute the alignment matrix for two provided sequences,
respectively. The first function builds a scoring matrix as a dictionary of
dictionaries.
* build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score): - 
	Takes as input a set of characters alphabet and 3 scores diag_score, 
	off_diag_score, and dash_score. The function returns a dict of dicts whose
	entries are indexed by pairs of characters in alphabet plus '-'. The score for
	any entry indexed by one or more dashes is dash_score. The score for the
	remaining diagonal entries is diag_score. Finally, the score for the remaining
	off-diagonal entries is off_diag_score.
One final note for this function is that, although an alignment with two matching
dashes is not allowed, the scoring matrix should still include an entry for two
dashes (which will never be used). 

The second function computes an alignment matrix using the method
ComputeGlobalAlignmentScores (CGAS) described in Homework 4. The function
computes either a global alignment matrix or a local alignment matrix depending
on the value of global_flag.
* compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag): - Takes
	as input two sequences seq_x and seq_y whose elements share a common 
	alphabet with the scoring matrix scoring_matrix. The function computes and
	returns the alignment matrix for seq_x and seq_y as described in the Homework.
	If global_flag is True, each entry of the alignment matrix is computed using the
	method described in Question 8 of the Homework. If global_flag is False, each
	entry is computed using the method described in Question 12 of the Homework.

Alignment Functions
----------
For the second part of Project 4, you will use the alignment matrix returned by
compute_alignment_matrix to compute global and local alignments of two sequences
seq_x and seq_y. The first function will implement the method ComputeAlignment
discussed in Question 9 of the Homework.
* compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix): -
	Takes as input two sequences seq_x and seq_y whose elements share a common
	alphabet with scoring_matrix. This function computes a global alignment of the
	sequences using global alignment matrix alignment_matrix.
The function returns a tuple of the form (score, align_x, align_y) where score is
the score of the global alignment align_x and align_y. Note that align_x and align_y
should have the same length and may include a padding character '-'.

This second function will compute an optimal local alignment starting at the max
entry of the local alignment matrix and working backwards to zero as described
in Question 13 of the Homework. 
* compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix): -
	Takes as input two sequences whose elems share a common alphabet with
	scoring_matrix. This func computes a local alignment of the sequences using
	local alignment matrix alignment_matrix.
The function returns a tuple of the form (score, align_x, align_y) where score is
the score of the optimal local alignment align_x and align_y. Note that the two
alignments should be of the same length and may include the padding char '-'.

Grading and Coding Standards
----------
As you implement each matrix function, test it thoroughly. Use the function
build_scoring_matrix to generate scoring matrices for alphabets such as "ACTG"
and "abcd[...]z". Realistic choices for the scoring matrix should have large scores
on the diagonal to reward matching the same character and low scores off the
diagonal to penalize the mismatches. Use the scoring matrices to test
compute_alignment_matrix for simple examples you can verify by hand. Once you
are confident that your implementation of these two functions is correct, submit
your code to this Owltest page (http://codeskulptor.appspot.com/owltest?urlTests=
alg.module4_tests.py&urlPylintConfig=alg.pylint_config.py&) for testing.

Next, implement your alignment functions. Use the alignment matrices to generate
global and local alignments for simple test examples. Verifying that the global
alignments are correct is relatively easy. Generating interesting local alignments
and verifying that they are correct is harder. In general, the off-diagonal and 
dash scores in your scoring matrix should be negative for local alignments. One
interesting test for your local alignment function is to choose a scoring matrix
that mimics the computation of the longest common subsequence of seq_x and
seq_y (https://en.wikipedia.org/wiki/Longest_common_subsequence_problem).
Once you are confident that your implementation of these two functions is correct,
submit your code to Owltest.

Coding style guidelines: https://class.coursera.org/algorithmicthink2-003/
wiki/view?page=style_guidelines.
Pylint errors (Owltest): https://class.coursera.org/algorithmicthink2-003/
wiki/view?page=pylint_errors.
"""

##################################################

# Implement a function that builds a scoring matrix as a dict of dicts.

def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
	"""
	Returns a dictionary of dictionaries whose entries are indexed by pairs of
	characters in alphabet plus '-', whose scores are determined by the three
	scoring parameters.
	"""
	# First, determine what the dict of dicts will look like. For alphabet AB plus
	# '-', it may be: {'-':{'-':val, 'A':val, 'B':val}, 'A':{'-':val, 'A':val, 'B':val},
	# 'B':{'-':val, 'A':val, 'B':val}} that is indexed by [row_char][col_char], so
	# the first set of keys corresponds to row values, and the second to col
	# values. Then it fills the values with diag_score, off_diag_score, and 
	# dash_score depending on whether or not the keys match, don't match,
	# or contain dashes, respectively. For scores = 10, 2, -5, the matrix written
	# out would look like:
	#      -   A    B
	# -  -5  -5  -5   (corresponds to '-':{'-':-5, 'A':-5, 'B':-5})
	# A -5  10   2   (corresponds to 'A':{'-':-5, 'A':10, 'B':2})
	# B -5   2   10  (corresponds to 'B':{'-':-5, 'A':2, 'B':10})
	# So let's build this dict of dicts.
	
	scoring_matrix = {}
	# Copy alphabet and add a dash to it.
	alpha_dash = set(alphabet)
	alpha_dash.add('-')
	# Iterate through alphabet and assign scores.
	for char_i in alpha_dash:
		scoring_matrix[char_i] = {}
		for char_j in alpha_dash:
			if char_i == '-' or char_j == '-':
				scoring_matrix[char_i][char_j] = dash_score
			elif char_i == char_j:
				scoring_matrix[char_i][char_j] = diag_score
			else:
				scoring_matrix[char_i][char_j] = off_diag_score
				
	return scoring_matrix

# Testing Grounds

# I will create scoring matrices for two simple alphabets: ACTG and a-z. 
# Each will have two versions, a set of elements and a string of characters,
# each of which will be passed to the function to verify that the type check works.

def test_build_scoring_matrix():
	"""
	Run build_scoring_matrix on several alphabets and print the results.
	Use constants for diagonal, off_diagonal, and dash scores. 
	"""
	print "="*30
	print "Test build_scoring_matrix function"
	print "="*30
	
	alphabet1a = set(['A','C','T','G'])
	alphabet1b = "ACTG"
	alphabet1c = ['A', 'C', 'T', 'G']
	alphabet2a = set([chr(ord("a") + idx) for idx in range(26)])
	alphabet2b = "".join(chr(ord("a") + idx) for idx in range(26))
	alphabet2c = [chr(ord("a") + idx) for idx in range(26)]

	DIAG = 10
	OFF_DIAG = 3
	DASH = -5

	alphabets = [alphabet1a, alphabet1b, alphabet1c, alphabet2a, alphabet2b, alphabet2c]
	scoring_matrices = []
	for alphabet in alphabets:
		scoring_matrices.append(build_scoring_matrix(alphabet, DIAG, OFF_DIAG, DASH))
	for matrix in scoring_matrices:
		print "Alphabet:", alphabets[scoring_matrices.index(matrix)]
		for key, value in matrix.items():
			print key, value
		print "-"*10
	# Success! All 3 alphabet data types were passed and returned the same results.
		
# Uncomment the function call to run test procedures.
#test_build_scoring_matrix()

##################################################

# Implement a function that computes an alignment matrix using the CGAS method
# from Homework 4. 

def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
	"""
	Return an alignment matrix for two sequences seq_x and seq_y using the data
	in scoring_matrix. If global_flag = False, negative values to be assigned to the
	alignment matrix entries are changed to zeros. 
	"""
	# First, I will use the helper function make_matrix from my Module 4 Class
	# Notes on RNA Folding Algorithms, found above in the shared area, to create
	# an empty matrix after initializing dimension variables.
	height = len(seq_x) + 1
	width = len(seq_y) + 1
	alignment_matrix = make_matrix(height, width, float('-inf'))
	alignment_matrix[0][0] = 0
	
	# Case where negative values are allowed.
	if global_flag:
		# Assign sig:- and -:sig entries to cumulative negative scores.
		for idx_i in range(1, height):
			alignment_matrix[idx_i][0] = alignment_matrix[idx_i-1][0] + \
														scoring_matrix[seq_x[idx_i-1]]['-']
														
		for idx_j in range(1, width):
			alignment_matrix[0][idx_j] = alignment_matrix[0][idx_j-1] + \
														scoring_matrix['-'][seq_y[idx_j-1]]
		# Traverse alignment matrix and assign scores based on best step
		# from diagonal, above, or left entries. 
		for idx_i in range(1, height):
			for idx_j in range(1, width):
				diag = alignment_matrix[idx_i-1][idx_j-1] + \
							scoring_matrix[seq_x[idx_i-1]][seq_y[idx_j-1]]
				vert = alignment_matrix[idx_i-1][idx_j] + scoring_matrix[seq_x[idx_i-1]]['-']
				horiz = alignment_matrix[idx_i][idx_j-1] + scoring_matrix['-'][seq_y[idx_j-1]]
				alignment_matrix[idx_i][idx_j] = max(diag, vert, horiz)
	else:
		# Case where negative values are not allowed.
		for idx_i in range(1, height):
			alignment_matrix[idx_i][0] = 0
		
		for idx_j in range(1, width):
			alignment_matrix[0][idx_j] = 0
		
		for idx_i in range(1, height):
			for idx_j in range(1, width):
				diag = max(0, alignment_matrix[idx_i-1][idx_j-1] + \
									scoring_matrix[seq_x[idx_i-1]][seq_y[idx_j-1]])
				vert = max(0, alignment_matrix[idx_i-1][idx_j] + \
									scoring_matrix[seq_x[idx_i-1]]['-'])
				horiz = max(0, alignment_matrix[idx_i][idx_j-1] + \
									scoring_matrix['-'][seq_y[idx_j-1]])
				alignment_matrix[idx_i][idx_j] = max(diag, vert, horiz)
				
	return alignment_matrix
	
# Testing Grounds

# I will test out the scoring and alignment matrix functions on examples
# from Homework 4 since that work has already been done. That work will
# verify the accuracy of the two functions.

def test_compute_alignment_matrix():
	"""
	Pass Homework 4 examples to the scoring and alignment matrix-building
	functions and verify the accuracy of the answers via print statements.
	"""
	print "="*30
	print "Test compute_alignment_matrix function"
	print "="*30
	
	# Homework 4, Question 12 example (using global_flag = False).
	#       -     T    A     A     T
	#  -    0   0     0     0     0
	#  A   0    4    10   10    4
	#  A   0    4    14   20   14
	alphabet = "ACTG"
	X = "AA"
	Y = "TAAT"
	DIAG = 10
	OFF_DIAG = 4
	DASH = -6
	
	M = build_scoring_matrix(alphabet, DIAG, OFF_DIAG, DASH)
	S = compute_alignment_matrix(X, Y, M, False)
	
	for item in S:
		print item
	print "-"*5
	# Success! The alignment matrix looked exactly like that built in H4Q12.
	
	# Unfortunately, there are no Homework 4 examples where global_flag = True
	# so I will use the same X, Y, and M and build the scoring matrix here.
	#           -      T     A     A     T
	#  -       0    -6  -12  -18  -24
	#  A     -6     4     4    -2    -8
	#  A   -12    -2   14    14    8
	#     S[1,1] = max{0+4, -6-6, -6-6} = 4
	#     S[1,2] = max{-6+10, -12-6, 4-6} = 4
	#     S[1,3] = max{-12+10, -18-6, 4-6} = -2
	#     S[1,4] = max{-18+4, -24-6, -2-6} = -8
	#     S[2,1] = max{-6+4, 4-6, -12-6} = -2
	#     S[2,2] = max{4+10, 4-6, -2-6} = 14
	#     S[2,3] = max{4+10, -2-6, 14-6} = 14
	#     S[2,4] = max{-2+4, -8-6, 14-6} = 8
	
	S = compute_alignment_matrix(X, Y, M, True)
	
	for item in S:
		print item
	# Success! The alignment matrix was accurate to the comment above.
	
# Uncomment the function call to run test procedures.
#test_compute_alignment_matrix()

##################################################

# Implement a function that uses the alignment matrix returned by the previous
# function to compute a global alignment of two sequences. This will implement
# the method ComputeAlignment discussed in Homework 4 Question 9.

def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
	"""
	Returns a global alignment of two sequences seq_x and seq_y using a
	scoring matrix and an alignment matrix.
	"""
	# Initialize variables for indices, score, and global pairwise alignments.
	# Note that the global alignment score is the bottom-right value in the
	# alignment matrix.
	idx_i = len(seq_x)
	idx_j = len(seq_y)
	align_x = ""
	align_y = ""
	score = alignment_matrix[idx_i][idx_j]
	
	# Traverse alignment_matrix from bottom-right to find the global alignment.
	while idx_i != 0 and idx_j != 0:
		# Check for diagonal step.
		if alignment_matrix[idx_i][idx_j] == alignment_matrix[idx_i-1][idx_j-1] + \
										scoring_matrix[seq_x[idx_i-1]][seq_y[idx_j-1]]:
			align_x = seq_x[idx_i-1] + align_x
			align_y = seq_y[idx_j-1] + align_y
			idx_i -= 1
			idx_j -= 1
		else:
			# Check for downward step.
			if alignment_matrix[idx_i][idx_j] == alignment_matrix[idx_i-1][idx_j] + \
										scoring_matrix[seq_x[idx_i-1]]['-']:
				align_x = seq_x[idx_i-1] + align_x
				align_y = "-" + align_y
				idx_i -= 1
			else:
				# Assume rightward step.
				align_x = "-" + align_x
				align_y = seq_y[idx_j-1] + align_y
				idx_j -= 1
	# Run through rest of steps where seq_y is expended.
	while idx_i != 0:
		align_x = seq_x[idx_i-1] + align_x
		align_y = "-" + align_y
		idx_i -= 1
	# Run through rest of steps where seq_x is expended.
	while idx_j != 0:
		align_x = "-" + align_x
		align_y = seq_y[idx_j-1] + align_y
		idx_j -= 1
	
	return (score, align_x, align_y)
				
# Testing Grounds

# I will run test the global alignment function on X = AA and Y = TAAT with
# expected outcome: (8, "-AA-", "TAAT").

def test_compute_global_alignment():
	"""
	Pass X = AA and Y = TAAT to the scoring and alignment matrix functions,
	then pass the sequences and those matrices to the global alignment function.
	"""
	print "="*30
	print "Test compute_global_alignment function"
	print "="*30
	
	# Define sequences, pass them to the build/create matrix functions using the
	# same scoring constants and alphabet as the previous test function to verify 
	# the score. Be sure to set global_flag = True so that neg scores are assigned.
	alphabet = "ACTG"
	X = "AA"
	Y = "TAAT"
	DIAG = 10
	OFF_DIAG = 4
	DASH = -6
	M = build_scoring_matrix(alphabet, DIAG, OFF_DIAG, DASH)
	S = compute_alignment_matrix(X, Y, M, True)
	
	print compute_global_alignment(X, Y, M, S)
	# Success! Returns (8, '-AA-', 'TAAT'), which is expected.
		
# Uncomment the function call to run test procedures.
#test_compute_global_alignment()

##################################################

# Implement a function that uses the alignment matrix returned by the alignment
# function to compute a local alignment of two sequences. This will implement
# the modified function described in Homework 4 Question 13. Note that the
# modifications require global_flag = False in the compute_alignment_matrix
# function. This function to compute local alignment begins at the maximum
# entry of the local alignment matrix (the highest score).

def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
	"""
	Returns a local alignment of two sequences seq_x and seq_y using a
	scoring matrix and an alignment matrix.
	"""
	# Initialize variables for indices, score, and global pairwise alignments.
	# Note that the indices i and j and the score are set to 0, 0, and -inf, 
	# respectively, as placeholders.
	idx_i = 0
	idx_j = 0
	align_x = ""
	align_y = ""
	score = float("-inf")
	
	# Find highest score in the local alignment matrix.
	height = len(alignment_matrix)
	width = len(alignment_matrix[0])
	for row in range(height):
		for col in range(width):
			if alignment_matrix[row][col] > score:
				score = alignment_matrix[row][col]
				idx_i = row
				idx_j = col
	
	# Traverse alignment_matrix from highest score until a zero value is found.
	while alignment_matrix[idx_i][idx_j] != 0:
		# Check for diagonal step.
		if alignment_matrix[idx_i][idx_j] == alignment_matrix[idx_i-1][idx_j-1] + \
										scoring_matrix[seq_x[idx_i-1]][seq_y[idx_j-1]]:
			align_x = seq_x[idx_i-1] + align_x
			align_y = seq_y[idx_j-1] + align_y
			idx_i -= 1
			idx_j -= 1
		else:
			# Check for downward step.
			if alignment_matrix[idx_i][idx_j] == alignment_matrix[idx_i-1][idx_j] + \
										scoring_matrix[seq_x[idx_i-1]]['-']:
				align_x = seq_x[idx_i-1] + align_x
				align_y = "-" + align_y
				idx_i -= 1
			else:
				# Assume rightward step.
				align_x = "-" + align_x
				align_y = seq_y[idx_j-1] + align_y
				idx_j -= 1

	return (score, align_x, align_y)
	
# Testing Grounds

# I will run test the global alignment function on X = AA and Y = TAAT with
# expected outcome: (20, "AA", "AA").

def test_compute_local_alignment():
	"""
	Pass X = AA and Y = TAAT to the scoring and alignment matrix functions,
	then pass the sequences and those matrices to the local alignment function.
	"""
	print "="*30
	print "Test compute_local_alignment function"
	print "="*30
	
	# Define sequences, pass them to the build/create matrix functions using the
	# same scoring constants and alphabet as the previous test function to verify 
	# the score. Be sure to set global_flag = False to replace all negative scores
	# with zeros.
	alphabet = "ACTG"
	X = "AA"
	Y = "TAAT"
	DIAG = 10
	OFF_DIAG = 4
	DASH = -6
	M = build_scoring_matrix(alphabet, DIAG, OFF_DIAG, DASH)
	S = compute_alignment_matrix(X, Y, M, False)
	
	print compute_local_alignment(X, Y, M, S)
	# Success! Returns (8, '-AA-', 'TAAT'), which is expected.
	
	##########
	## OWLTEST FAILURE!
	## [-5.0 pts] compute_local_alignment(X,Y,M,S) score of returned alignments
	## does not match returned score, score of returned alignments was 16 but
	## returned score was 19. 
	##########
	
	# The X, Y, M, and S inputs from the Owltest failure are shown below. Note
	# that M = scoring_matrix and S = alignment_matrix.
	
	X = 'happypedestrianwalker'
	Y = 'sadpedesxtriandriver'
	
	M = {'-': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 
			'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 
			'y': -1, 'x': -1, 'z': -1}, 'a': {'-': -1, 'a': 2, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 
			'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 
			'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'c': {'-': -1, 'a': -1, 'c': 2, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 
			'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 
			'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'b': {'-': -1, 'a': -1, 'c': -1, 'b': 2, 'e': -1, 
			'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 
			's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'e': {'-': -1, 'a': -1, 'c': -1, 
			'b': -1, 'e': 2, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 
			'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'd': {'-': -1, 
			'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': 2, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 
			'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 
			'g': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': 2, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 
			'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 
			'x': -1, 'z': -1}, 'f': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': 2, 'i': -1, 'h': -1, 
			'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 
			'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'i': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 
			'i': 2, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 
			't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'h': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 
			'g': -1, 'f': -1, 'i': -1, 'h': 2, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 
			'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'k': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 
			'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': 2, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 
			'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'j': {'-': -1, 'a': -1, 
			'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': 2, 'm': -1, 'l': -1, 'o': -1, 
			'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 
			'm': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 
			'm': 2, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 
			'x': -1, 'z': -1}, 'l': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 
			'k': -1, 'j': -1, 'm': -1, 'l': 2, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 
			'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'o': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1,
			'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': 2, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 
			't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'n': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 
			'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': 2, 'q': -1, 'p': -1, 's': -1, 
			'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'q': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 
			'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': 2, 
			'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'p': {'-': -1, 'a': -1, 
			'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 
			'n': -1, 'q': -1, 'p': 2, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 
			's': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 
			'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': 2, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 
			'x': -1, 'z': -1}, 'r': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 
			'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': 2, 'u': -1, 't': -1, 'w': -1, 
			'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'u': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 
			'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': 2, 
			't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 't': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1,
			'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 
			'r': -1, 'u': -1, 't': 2, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'w': {'-': -1, 'a': -1, 'c': -1, 'b': -1,
			'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 
			'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': 2, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'v': {'-': -1, 'a': -1, 
			'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 
			'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': 2, 'y': -1, 'x': -1, 'z': -1}, 
			'y': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 
			'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': 2, 
			'x': -1, 'z': -1}, 'x': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1,
			'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 
			'v': -1, 'y': -1, 'x': 2, 'z': -1}, 'z': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 
			'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 
			't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': 2}}
	
	S = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0], 
		[0, 0, 1, 1, 3, 2, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 1, 4, 3, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
		[0, 0, 0, 2, 1, 3, 6, 5, 4, 3, 2, 1, 0, 0, 0, 2, 1, 0, 0, 1, 1], 
		[0, 0, 0, 1, 1, 3, 5, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 0, 0, 2, 1], 
		[0, 2, 1, 0, 0, 2, 4, 7, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 1], 
		[0, 1, 1, 0, 0, 1, 3, 6, 9, 9, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 
		[0, 0, 0, 0, 0, 0, 2, 5, 8, 8, 10, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4], 
		[0, 0, 0, 0, 0, 0, 1, 4, 7, 7, 9, 12, 15, 14, 13, 12, 11, 10, 9, 8, 7],
		[0, 0, 2, 1, 0, 0, 0, 3, 6, 6, 8, 11, 14, 17, 16, 15, 14, 13, 12, 11, 10],
		[0, 0, 1, 1, 0, 0, 0, 2, 5, 5, 7, 10, 13, 16, 19, 18, 17, 16, 15, 14, 13],
		[0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 6, 9, 12, 15, 18, 18, 17, 16, 15, 14, 13],
		[0, 0, 2, 1, 0, 0, 0, 0, 3, 3, 5, 8, 11, 14, 17, 17, 17, 16, 15, 14, 13],
		[0, 0, 1, 1, 0, 0, 0, 0, 2, 2, 4, 7, 10, 13, 16, 16, 16, 16, 15, 14, 13], 
		[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 3, 6, 9, 12, 15, 15, 15, 15, 15, 14, 13], 
		[0, 0, 0, 0, 0, 2, 1, 2, 1, 0, 2, 5, 8, 11, 14, 14, 14, 14, 14, 17, 16], 
		[0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 4, 7, 10, 13, 13, 16, 15, 14, 16, 19]]
		
	# Passing above variables to compute_local_alignment returns: 
	# (19, '---pedes-trian', 'sadpedesxtrian')
	# Comparing the two with the scoring matrix, this alignment does in fact have
	# a score of 16 (-1-1-1+2+2+2+2+2-1+2+2+2+2+2). The score of 19 does
	# in fact correspond to at least local alignment: 'pedes-trian', 'pedesxtrian',
	# which is the alignment that should have been returned using the score 19.
	#	
	# What appears to set this apart from other examples is that OFF_DIAG and DASH
	# scores are both equal to -1. There is no discrimination between the two in
	# the scoring matrix M. 
	#
	# Also, and maybe more importantly, the local alignment function hits a 0 before
	# the upper and left boundaries where there is only one leading dash in seq, and
	# also where one of the indices equals zero. The relevant while statement here
	# checks: idx_i != 0 and idx_j != 0. If a 0 is embedded in the matrix beyond
	# these boundaries, neither index would equal zero. 
	#
	# I must change this condition to: alignment_matrix[idx_i][idx_j] != 0. This
	# fixes it so that if a 0 is found in the middle of the alignment matrix, the
	# loop terminates. This was the only change made to the local alignment func.
	
	print compute_local_alignment(X, Y, M, S)
	# Success! This returned (19, 'pedes-trian', 'pedesxtrian'), as expected.
	
# Uncomment the function call to run test procedures.
#test_compute_local_alignment()
	
##################################################
##################################################