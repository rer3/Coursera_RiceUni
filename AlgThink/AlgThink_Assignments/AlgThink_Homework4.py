"""
Rice University / Coursera: Algorithmic Thinking (Part 2)
Module 4: Homework
"""
##################################################
##################################################
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
##################################################

## All necessary import statements are below.

import math

## Below is the link to the notes on sequence alignment provided by Luay Nakhleh.

COURSE = "https://class.coursera.org/algorithmicthink2-003/"
DESCRIPTION = COURSE + "quiz/attempt?quiz_id=263"

##################################################

def hw_401():
	"""
	QUESTION 1
	
	Questions 1-3 will test your understanding of the feasibility conditions of
	global pairwise sequence alignment. Let X = AC and Y = CA be two DNA
	sequences. Which of the following are global alignments of X and Y?
	
	Option 1
	X' = AC and Y' = CA
	
	Option 2
	X' = AC-- and Y' = --CA
	
	Option 3
	X' = AC and Y' = --CA
	
	Option 4
	X' = CA and Y' = CA

	Option 5
	X' = CA- and Y' = -AC
	"""
	# From the link provided at the top of the page, the following criteria
	# are given for feasible global alignment: an alignment of X and Y is two
	# sequences X' and Y' over the alphabet SIG U {-} where X' is formed from
	# X by adding only dashes to it (and Y' analogously from Y) such that
	# 1.) |X'| = |Y'| (they are the same length)
	# 2.) there does not exist an i such that X'[i] = Y'[i] = - (no same spot dash)
	# 3.) and X is a subsequence of X' (and Y of Y') (elements in same order).
	# I will use these rules to evaluate the 5 options.
	
	# Option 3 is out because X' and Y' violate rule 1.
	# Option 4 is out because X' violates rule 3.
	# Option 5 is out because both violate rule 3.
	
	answer = "X' = AC and Y' = CA" + "\n"
	answer += "X' = AC-- and Y' = --CA"
	
	print "Question 401 Answer:"
	print answer
	print "-"*50
	print "\n"
	
hw_401()
	
##################################################

def hw_402():
	"""
	QUESTION 2
	
	How many possible global alignments are there for two sequences X and Y if
	|X| = |Y| = 1? How many possible global alignments are there for two seqs
	X and Y if |X| = |Y| = 2? Give your answer as two numbers separated by a
	space.
	"""
	# For length = 1, you can either have the original nucleobase or a dash (by
	# removing the initial nucleobase and replacing it with one). You can do this
	# to both, but not at the same time or rule 2 will be violated. Therefore,
	# you have 3 options: one with both initial bases, one where X is a dash and 
	# Y is the base, and one where X is the base and Y is a dash: A:C, A:-, -:C.
	# I almost forgot that you can also add dashes to the existing bases to get:
	# A-:-C, -A:C-. Now we have 5 possible alignments.
	
	# For length = 2, I must use an example. Let's say X = AC and Y = CA like in
	# question 1. Starting by changing Y and then changing X so not to violate the
	# second rule, we get X':Y' pairs: AC:CA, AC:-A, AC:C-A, AC:--, -C:CA, -C:C-,
	# A-:CA, A-:-A, --:CA. It appears that there are 9 possible global alignments.
	# It almost passed me that bases can be removed and dashes can be added
	# even when the length is two. This leaves many more alignments, such as:
	# A:C, A:A, A:-, C:C, C:A, -:A, as well as -AC:C-A, -AC:CA-, A-C:-CA,
	# A-C:CA-, AC-:-CA, AC-:C-A, --A:CA-, --C:CA-, -A-:C-A, -C-:C-A, 
	# -AC-:C--A, A--C:-CA-, A-C-:-C-A, -A-C:C-A-. This leaves 29 alignments,
	# but how do I know if I missed any? I actually got 51 when I did it on paper.

	##==========
	## INCORRECT: Try working out the number of possible global alignments for
	## each length of the alignment.
	##
	## answer = "5 51"
	##==========
	
	# Neither answer was marked as correct during the first review. A quick lookup
	# of this later: http://pages.cs.wisc.edu/~bsettles/ibs08/lectures/02-alignment.pdf
	# was found which presented this equation for finding all possible alignments for 2
	# sequences of length n:
	# Num of Alignments = (2n choose n) = ((2n)! / (n!)**2) which is roughly equivalent
	# to 2**(2*n) / sqrt(pi * n).
	# An implementation of that expression is:
	
	def num_alignments(n):
		"""
		Returns the number of possible global alignments for 2 sequences of
		length n.
		"""
		return math.factorial(2*n) / (math.factorial(n)**2)
		
	# Another source: http://www.primate.or.kr/bioinformatics/Course/Boston/04.pdf
	# presents two equations f(m,n) and g(m,n) for finding the total num of possible
	# alignments between a of length m and b of length n and total num of possible
	# NON-REDUNDANT alignments between a and b, respectively. L = length of an
	# alignment (with padded gaps).
	#
	# When n = m = 1, a = A, b = B:
	# L = 1: A:B. L = 2: -A:B-, A-:-B.
	# f(1,1) = 3 and g(1,1) = 2.
	# The value of g(1,1) for non-redundant alignments corresponds to the value
	# returned by the formula found in the source referenced above.
	# Note that -:B and A:-, interestingly, were not included here.
	#
	#When n = m = 2, a = AB, b = CD:
	# L = 2: AB:CD, L = 3: -AB:C-D, A-B:-CD, A-B:CD-, AB-:C-D, AB-:-CD, -AB:CD-, 
	# L = 4: A--B:-CD-, -A-B:C-D-, A-B-:-C-D, AB--:--CD, -AB-:C--D, --AB:CD--.
	# f(2,2) = 13 and g(2,2) = 6. Again, g() corresponds to the num_alignments
	# function.
	
	# One more source: http://www.cs.otago.ac.nz/cosc348/alignments/
	# Lecture05_GlobalAlignment.pdf gives the following equation for possible
	# global alignments between 2 sequences of length L (and it is similar to
	# an equivalent expression given in the first source): Total Alignments = 
	# 2**(2*n) / (pi * n)**(1/2).
	
	def total_alignments(n):
		"""
		Returns the number of possible global alignments for 2 sequences of
		length n.
		"""
		return 2**(2*n) / math.sqrt((math.pi * n))
	
	## Look to the linked source in the provided area. A global alignment is defined
	## as one where X' is formed from X by adding only dashes to it (so no elems
	## are removed, which I was doing). That makes sense within the context of
	## GLOBAL alignment vs. local alignment. This doesn't explain what is redundant
	## and what is NOT redundant within this context.	
	## ????????????????????????????????????????????????????????????????????????

	ans1 = num_alignments(1) # 2
	ans2 = num_alignments(2) # 6
	
	ans3 = total_alignments(1) # 2.25675833419
	ans4 = total_alignments(2) # 6.38307648642
	
	# The answers are very close, so I will stick with 2 and 6.
	
	##==========
	## INCORRECT: Try working out the number of possible global alignments for
	## each length of the alignment.
	##
	## answer = str(ans1) + " " + str(ans2)
	##==========
	
	answer = "INCORRECT"
	
	print "Question 402 Answer:"
	print answer
	print "-"*50
	print "\n"
	
hw_402()

##################################################

def hw_403():
	"""
	QUESTION 3
	
	Recall from the feasibility conditions of a sequence alignment that for X' and
	Y' to be an alignment of two sequences X and Y, X' and Y' must satisfy this
	condition: there does not exist an i such that X'_i = Y'_i = "-". 
	What happens if we remove this condition, that is allow both to equal "-"
	for some values of i?
	"""
	# If dashes can line up, then you can add an INIFINITE number of dashes,
	# anywhere, and all would be fine. There were several options, but this was
	# one of them.
	
	answer = "The number of possible alignments of a pair of sequences becomes infinite"
	
	print "Question 403 Answer:"
	print answer
	print "-"*50
	print "\n"
	
hw_403()

##################################################

def hw_404():
	"""
	QUESTION 4
	
	Questions 4-5 will test your understanding of optimality of global pairwise
	sequence alignment (that is, what the score of an alignment is and what makes
	an alignment optimal). Consider the scoring matrix M for alphabet SIG = {A,C,T,G}
	with the following entries (sig = lowercase sigma, SIG = uppercase sigma, and 
	E = "is an element of":
	* M_sig,sig = 5 for every sig E SIG
	* M_sig,sig' = 2 for every sig, sig' E SIG and sig !- sig'
	* M_sig,- = -2 for every sig E SIG
	* M_-,sig = -4 for every sig E SIG
	What is the score of the following alignment:
	X' = AC--CT
	Y' = TACGGT
	Enter your answer below as a single number.
	"""
	# From the notes linked above, the score of the alignment is: 
	# SIG(i=1 to k) of M_X'i, Y'i, or the sum of all scores from i=1 to k where
	# the score is given by the matrix value corresponding to X'_i and Y'_i.
	# The example given is a scoring scheme respective to the 4 conditions above
	# that assigns values of: 5, 2, -2, and -4, just like in this problem. The seqs
	# are X' = -AC-CT and Y' = TACGGT, very similar. The expression given is:
	# M_-,T + M_A,A + M_C,C + M_-,G + M_C,G + M_T,T, which evalutes to
	# - 4 (-,sig) + 5 + 5 (sig,sig pairs) - 4 (-,sig) + 2 (sig,sig') + 5 (sig,sig) = 9.
	
	# In this problem, the expression to evaluate looks like:
	# M_A,T + M_C,A + M_-,C + M_-,G + M_C,G + M_T,T, which evalutes to:
	
	answer = 2 + 2 - 4 - 4 + 2 + 5
	
	print "Question 404 Answer:"
	print answer
	print "-"*50
	print "\n"
	
hw_404()
	
##################################################

def hw_405():
	"""
	QUESTION 5
	
	Let X = AC and Y = GG be two DNA sequences (SIG = {A, C, T, G}), and
	consider the scoring matrix M given by:
	* M_sig,sig = 6 for every sig E SIG
	* M_sig,sig' = 2 for every sig,sig' E SIG where sig != sig'
	* M_sig,- = M_-,sig = -4 for every sig E SIG
	Under this scoring matrix, which pair of sequences below is the optimal global
	alignment of X and Y?
	
	Option 1
	X' = A-C- and Y' = -G-G
	
	Option 2
	X' = AC- and Y' = -GG
	
	Option 3
	X' = -AC- and Y'= -GG-
	
	Option 4
	X' = AC and Y' = GG
	
	Option 5
	X' = AC-- and Y' = --GG
	"""
	# First check to make sure that feasibility criteria are met. The pairs of
	# sequences are of the same length. The bases are in the proper order
	# related to the original sequences' elements. 
	
	# Option 3 is out because the dashes line up, violating that rule.
	# The rest must be scored using the scoring matrix provided in the problem.
	# Option 1:
	# Score = M_A,- + M_-,G + M_C,- + M_-,G = - 4 - 4 - 4 - 4 = -16
	# Option 2:
	# Score = M_A,- + M_C,G + M_-,G = - 4 + 2 - 4 = -6
	# Option 4
	# Score = M_A,G + M_C,G = 2 + 2 = 4
	# Option 5
	# Score  = ...clearly all four elems are dash-base pairs, so 4 * (-4) = -16
	
	answer = "X' = AC and Y' = GG"
	
	print "Question 405 Answer:"
	print answer
	print "-"*50
	print "\n"
	
hw_405()

##################################################

def hw_406():
	"""
	QUESTION 6
	
	Let B(m,n) denote the number of global alignments of two sequences X and Y
	of lengths m and n, respectively. A recursive formula for B(m,n) is:
	
	Option 1
	B(m,n) = m * B(m-1, n)
	
	Option 2
	B(m,n) = m * B(m-1,n) + n * B(m, n-1)
	
	Option 3
	B(m,n) = n * B(m, n-1)
	
	Option 4
	B(m,n) = B(m-1, n) + B(m-1, n-1) + B(m, n-1)
	
	Option 5
	B(m,n) = B(m-1, n) + B(m, n-1)
	"""
	# Since I tried to tackle this above and failed miserably, this should be fun.
	# Let's try to reason through this first. 
	# Options 1 and 3 seem wrong because both m and n should affect the recursive
	# functions and outcome. Looking at examples of X = AB and Y = CD, and 
	# X = AB and Y = C will yield much different results (50 and 13, respectively,
	# provided my scratch work is correct).
	# Without base cases, I can't plug those numbers into the remaining options
	# as far as I can tell. 
	
	# Option 2 reminds me of a problem that we've encountered before. In my
	# Principles of Computing (Part 2) assignment Homework 2, Question 6, there
	# is a description of a recursive function that computes permutations. The
	# base case is p(0) = 1, and the recurrence is p(n) = n * p(n-1). In the 
	# problem here, it certainly appears that permutations of each sequences
	# are being computed, which very much appeared to be the case when
	# jotting down all of the alignments for X = AB and Y = CD on paper. 
	
	# I'm going to guess here that the base case is B(1,1) where there are 5
	# alignments (A:B, A:-, -:B, A-:-B, -A:B-). If B(1,1) = 5, I will plug in
	# m = 2, n = 2 and m = 2, n = 1 to see what I get, using option 2. I will
	# also assume that base case B(0,0) = 0, while B(1,0) and B(0,1) = 1
	# since X = A can be paired with Y' = -. Using option 2:
	# B(1,1) = 1*B(0,1) + 1*B(1,0) = 1 + 1 = 2...Incorrect.
	# Using Option 4: B(1,1) = B(0,1) + B(0,0) + B(1,0) = 1 + 0 + 1 = 2...hmm.
	# Using Option 5: B(1,1) = B(0,1) + B(1,0) = 1 + 1 = 2.
	# So they all return 2. My base case must be off.
	
	# Let's try m = 2, n = 1 in these and assume B(1,1) = 5.
	# Option 2: B(2,1) = 2*B(1,1) + 1*B(2,0) = 2*5 + 1*3 = 13.
	# I'm assuming B(2,0) = 3 because X = AB and Y = nada can pair like so:
	# AB:--, A:-, B:-. So Option 2 still looks correct to me.
	# Option 4: B(2,1) = B(1,1) + B(1,0) + B(2,0) = 5 + 1 + 3 = 9...wrong?
	# Option 5: B(2,1) = B(1,1) + B(2,0) = 5 + 3 = 9...wrong too?
	
	## This is a sloppier-than-I'd-prefer method of solving, but I'm going to
	## use the answer from here. If correct, I will come back and reason through
	## the base case of B(0,0). 
	
	##==========
	## INCORRECT: This recurrence doesn't account for the recursive case when
	## we have two seqs of length m-1 and n-1. Consider how adding one element
	## to the end of one or both seqs increases the number of possible global
	## alignments.
	##
	## answer = "B(m,n) = m * B(m-1, n) + n * B(m, n-1)"
	##==========
	
	# From a source in a previous question (http://www.primate.or.kr/bioinformatics/
	# Course/Boston/04.pdf), the recurrence function for number of total possible
	# alignments (non-redundant) g(m,n) of two sequences X and Y with lengths m
	# and n, respectively is:
	# g(m,n) = g(n-1, m) + g(n, m-1), base: f(0,0) = f(m,0) = f(0,n) = 1.
	# This corresponds to option 5.	
	
	##==========
	## INCORRECT: This recurrence doesn't account for the recursive case when
	## we have two seqs of length m-1 and n-1. Consider how adding one element
	## to the end of one or both seqs increases the number of possible global
	## alignments.
	##
	## answer = "B(m,n) = B(m-1, n) + B(m, n-1)"
	##==========
	
	answer = "INCORRECT"

	print "Question 406 Answer:"
	print answer
	print "-"*50
	print "\n"
	
hw_406()
	
##################################################

def hw_407():
	"""
	QUESTION 7
	
	Questions 7-10 develop a dynamic programming (DP) algm for solving the
	Global Pairwise Alignment Problem. Algorithm GlobalAlignment below call two
	helper algms to compute a global alignment:
	-----
	Algorithm 1: GlobalAlignment
	Input: Sequences X and Y and scoring matrix M.
	Output: Optimal global pairwise alignment X' and Y' of seqs X and Y.
	1.  S <- ComputeGlobalAlignmentScores(X,Y,M);
	2.  (X',Y') <- ComputeAlignment(X,Y,M,S);
	3.  return (X',Y')
	-----
	These two helper functions do the following:
	* ComputeGlobalAlignmentScores computes a global alignment matrix S whose
		entries S[i,j] are the maximum scores over all possible global alignments for
		the pair of sequences X[0...i-1] and Y[0...j-1].
	* ComputeAlignment takes this alignment matrix and traces backwards from the
		entry S[m,n] to the entry S[0,0] to compute the actual optimal global
		alignment of X and Y.
	If you find it easier to refer to, open the figure here: https://d396qusza40orc.
	cloudfront.net/algorithmicthink/AT-Homework4/GlobalAlignmentFig.jpg.
	
	Since the entries S[i,j] of the global alignment matrix are the maximum scores
	for all possible global alignments for the pair of sequences X[0...i-1] and
	Y[0...j-1], which values of S will this DP method use in computing S[i,j] when
	i > 0 and j > 0?
	
	Option 1
	S[i-1, j-1], S[i-1, j], S[i, j-1]
	
	Option 2
	S[i-1, j-1]
	
	Option 3
	S[i-1, j], S[i, j-1]
	
	Option 4
	S[i-1, j-1], S[i-1, j], S[i, j-1], and S[i,j]
	"""
	# Once question 8 is solved, you can see in the next to last line that the
	# ComputeGlobalAlignmentScores algorithm assigns S[i,j] by looking at
	# the values of S[i-1, j-1], S[i-1, j], and S[i, j-1]. These correspond to the
	# S positions diagonal, above, and to the left of S[i,j] used to find the
	# optimal alignment.
	
	answer = "S[i-1, j-1], S[i-1, j], and S[i, j-1]"
	
	print "Question 407 Answer:"
	print answer
	print "-"*50
	print "\n"
	
hw_407()
		
##################################################

def hw_408():
	"""
	QUESTION 8
	
	In this question, we will complete the partial pseudo-code for the algorithm
	ComputeGlobalAlignmentScores that computes the global alignment matrix S.
	In particular, the entry S[i,j] of this matrix should contain the maximum score
	over every possible global alignment of the pair of sequences X[0...i-1] and
	Y[0...j-1].
	-----
	Algorithm 2: ComputeGlobalAlignmentScores
	Input: Sequences X and Y and scoring matrix M.
	Output: The DP table S.
	1.  m <- |X|; n <- |Y|;
	2.  S[0,0] <- 0;
	3.  for i <- 1 to m do
	4.      S[i,0] <- (...);
	5.  for j <- 1 to n do
	6.      S[0,j] <- (...);
	7.  for i <- 1 to m do
	8.      for j <- 1 to n do
	9.          S[i,j] <- (...);
	10.return S;
	-----
	If you find it easier, refer to the link: https://d396qusza40orc.cloudfront.net/
	algorithmicthink/AT-Homework4/ComputeGlobalAlignmentScoresFig.jpg to
	see the figure. The pseudocode is missing details on lines 4, 6, and 9. Which of
	the following options completes the algm so that it correctly computes the 
	global alignment matrix S? Note: in the question, these are labeled 1, 2 and 3.
	
	Option 1
	Line 4: M_Xi-1,-
	Line 6: M_-,Yj-1
	Line 9: max{S[i-1, j-1] + M_Xi-1,Yj-1, S[i-1, j], S[i, j-1]}
	
	Option 2
	Line 4: S[i-1, 0]
	Line 6: S[0, j-1]
	Line 9: max{S[i-1, j-1] + M_Xi-1,Yj-1, S[i-1, j], S[i, j-1]}
	
	Option 3
	Line 4: S[i-1, 0] + M_Xi-1,-
	Line 6: S[0, j-1] + M_-,Yj-1
	Line 9: max{S[i-1, j-1], S[i-1, j], S[i, j-1]}
	
	Option 4
	Line 4: S[i-1, 0]
	Line 6: S[0, j-1]
	Line 9: max{S[i-1, j-1] + M_Xi-1,Yj-1, S[i-1, j] + M_Xi-1,-, S[i, j-1] + M_-,Yj-1}
	
	Option 5
	Line 4: M_Xi-1,-
	Line 6: M_-,Yj-1
	Line 9: max{S[i-1, j-1] + M_Xi-1,Yj-1, S[i-1, j] + M_Xi-1,-, S[i, j-1] + M_-,Yj-1}
	
	Option 6
	Line 4: S[i-1, 0] + M_Xi-1,-
	Line 6: S[0, j-1] + M_-,Yj-1
	Line 9: max{S[i-1, j-1] + M_Xi-1,Yj-1, S[i-1, j] + M_Xi-1,-, S[i, j-1] + M_-,Yj-1}
	"""
	# The best approach is to break down what ComputeGlobalAlignmentScores is doing.
	# Line 1:  Initializing vars m and n to the lengths of X and Y, respectively.
	# Line 2:  Initializing S[0,0] to zero (I believe for illegal -:- matches?).
	# Line 3:  For loop iterating with index i across the range of length m (|X|).
	# Line 4:      Assigning S[i,0] to something.
	# Line 5:  For loop iterating with index j across the range of length n (|Y|).
	# Line 6:      Assigning S[0,j] to something.
	# Line 7:  For loop iterating with index i across the range of length m.
	# Line 8:      For loop iterating with index j across the range of length n.
	# Line 9:          Assigning S[i,j] to something.
	# Line 10: Returning DP table S.
	
	# The question is how is scoring matrix M referenced, as it is passed to this
	# algorithm but not included in the provided pseudocode. From the link above,
	# an example where X = AC and Y = TAG and scoring matrix M given by:
	# M_sig,sig = 5, M_sig,sig' = 2, M_sig,- = -2, and M_-,sig = -4 yields a 
	# DP table (without AC and TAG on the table in the example):
	#              T    A     G
	#       0   -4   -8  -12
	#  A  -2    2     1   -3
	#  C  -4    0     4     3
	
	# Using the ComputeGlobalAlignmentScores on these X and Y sequences would
	# compute m = 2 and n = 3. The first for loop appeared to compute for i = 1
	# to m (2): -2 then -4, which is S[i,0] = S[i-1,0] + M_sig,-. The second loop
	# did the same from 1 to n (3) but with S[0,j] = S[0,j-1] + M_-,sig. 
	## Options 1-2, and 4-5 are out because lines 4 and 6 in these do not follow
	# that format, leaving options 3 and 6.
	
	# I will plug values from the DP table S in the linked example into the line 9s
	# from options 3 and 6:
	# S[1,1] = 2, S[2,1] = 0, S[2,1] = 1, S[2,2] = 4, S[1,3] = -3, S[2,3] = 3. 
	#
	# Option 3: Line 9: max{S[i-1, j-1], S[i-1, j], S[i, j-1]}.
	# S[1,1] = max{0, -4, -2}...already this is wrong, as the answer is 2.
	# S[2,2] = max{2, 1, 0} = 2...this should be 4.
	## Option 3 is out.
	#
	# Option 6: Line 9: max{S[i-1, j-1] + M_Xi-1,Yj-1, S[i-1, j] + M_Xi-1,-, 
	# S[i, j-1] + M_-,Yj-1}
	# S[1,1] = max{0+2, -4-2, -2-4} = 2...looks okay so far, although the
	# score of X_i-1,Y_j-1 at S[0,0] being 2 is not obvious to me. Obviously,
	# this comparison is scored by M_sig,sig' + S[0,0].
	# S[1,2] = max{-4+5, -8-2, 2-4} = 1...correct.
	# S[2,2] = max{2+2, 1-2, 0-4} = 4...correct.
	# S[2,3] = max{1+2, -3-2, 4-4} = 3...correct.
	# Option 6 is also better than option 3 simply becaues it assigns a previous
	# entry's score plus some change to vs. just assigning one of the previous
	# entry's score plus no change. All of the scores would be 0, as that is the
	# max value in the matrix at the start.
	
	# Reflecting back on this problem, it is easy to see how DP table S is built.
	# With X = AC and Y = TAG, you have the following alignments being compared:
	# S[1,1]: X' = A, Y' = T. M_sig,sig' = 2, so value = 2.
	# S[1,2]: X' = -A, Y' = TA. M_-,sig + M_sig,sig = -4 + 5 = 1.
	# S[1,3]: X' = -A-, Y' = TAG. -4 + 5 - 4 = -3. Note that the best config of -A-
	# is determined by the max{} evaluation on the 3 components, where the max
	# is S[i,j-1] + M_-,Yj-1 or 1 - 4 = -3. 
	# S[2,1]: X' = AC, Y' = T. Either with T- or -T, you get 2 - 2 = 0.
	# S[2,2]: X' = AC, Y' = TA. 2 + 2 = 4.
	# S[2,3]: X' = AC, Y' = TAG. The best config must be the max of either 
	# diagonal: 1 + 2 = 3, above: -3 - 2 = -5, left: 4 - 4 = 0. This corresponds
	# to the global alignments X = -AC and Y = TAG where all components of each
	# sequence are used to evaluate.
	# The highest score returned in 4, which is AC and TA, where no dashes detract
	# from the score and you have two sig:sig' pairs equal to 2 + 2 = 4, per M.
	#
	# Also it is important to point out what the 3 terms are that get passed to
	# the max function in line 9. The first is a diagonal step, the second is a step
	# downward, and the third a step rightward. Since steps accumulate the score
	# of an alignment, for a given entry S[i,j] you need to look at the diagonal
	# score S[i-1,j-1] and add to it the score for the alignments where each has
	# had one more element added. This corresponds to M_Xi-1,Yj-1, and while it
	# may look like it should be M_Xi,Yj due to the indices of the scoring matrix,
	# this -1 in i-1 and j-1 take into account that there is no leading dash in the 
	# actual sequence, while there is one in the scoring matrix. So, unlike other
	# pseudocode that may have had a range 1 to n that in code was really 0 to
	# n-1, here an index of 0,0 is used (for the -:- pair) in the pseudocode.
	#
	# And so if you have alignments T and A and make a diagonal step, you first
	# look at the score for T:A, and then add to it the score for TA:AC (assuming
	# those are the next two elements) which here is for a sig:sig' pair. A downward
	# step is made when X' increases by an element but Y' does not, as X corresponds
	# to the rows and Y to the cols. You find the score above, for -T:AC, then add
	# the score for -TA:AC- which here is comparing A to -, a sig:- pair, hence why
	# M_Xi-1,- is referenced. Remember that Xi-1 is really just the current element
	# that lines up with i in the S matrix (A in this example). Similarly, a rightward
	# step corresponds to Y' adding an element while X' does not. If you move
	# from TA:AC to the right, one col space further, and one Y element further,
	# you get TA-:ACT (assuming that's the next Y elem). In this case, you'd add
	# the score of S[j-1,i], corresponding to TA:AC to the score of TA-:ACT, which
	# is M_-,Y_j-1, a -:sig pair represented by -:T. 
	#
	# The maximum value is found from all 3 steps because this algm is choosing
	# the optimal score, so lower scores are disregarded.
	
	answer = 	"Line 4: S[i-1, 0] + M_Xi-1,-" + "\n"
	answer += "Line 6: S[0, j-1] + M_-,Yj-1" + "\n"
	answer += "Line 9: max{S[i-1, j-1] + M_Xi-1,Yj-1, S[i-1, j]"
	answer += " + M_Xi-1,-, S[i, j-1] + M_-,Yj-1}"

	print "Question 408 Answer:"
	print answer
	print "-"*50
	print "\n"
	
hw_408()	

##################################################

def hw_409():
	"""
	QUESTION 9
	
	Here is the pseudocode of an incomplete ComputeAlignment algorithm:
	-----
	Algorithm 3: ComputeAlignment
	Input: Sequences X and Y, scoring matrix M, and a DP table S.
	Output: A global pairwise alignment of X and Y using DP table S and matrix M.
	1.  i <- |X|; j <- |Y|;
	2.  X' <- E; Y' <- E; (where E is an empty string
	3.  while i != 0 and j != 0 do
	4.      if S[i, j] = S[i-1, j-1] + M_Xi-1,Yj-1 then
	5.          X' <- (...);
	6.          Y' <- (...);
	7.          i <- i - 1; j <- j - 1;
	8.      else
	9.          if S[i, j] = S[i-1, j] + M_Xi-1,- then
	10.            X' <- (...);
	11.            Y' <- (...);
	12.            i <- i - 1;
	13.        else
	14.            X' <- (...);
	15.            Y' <- (...);
	16.            j <- j - 1;
	17.while i != 0 do
	18.    X' <- X_i-1 + X'; Y' <- "-" + Y';
	19.    i <- i -1;
	20.while j != 0 do
	21.    X' <- "-" + X'; Y' <- Y_j-1 + Y'
	22.    j <- j - 1;
	23.return (X', Y')
	Refer to this figure if necessary: https://d396qusza40orc.cloudfront.net/
	algorithmicthink/AT-Homework4/TracebackFig.jpg. The pseudocode is missing
	details on lines 5-6, 10-11, and 14-15. Which of the following options completes
	the algorithm so that it correctly computes an optimal global alignment using
	the global alignment matrix S that was computed using the previous algorithm
	ComputeGlobalAlignmentScores? In the problem, these are labeled lines 1-6.
	
	Option 1
	Line 5: X_i-1 + X'
	Line 6: Y_j-1 + Y'
	Line 10: "-" + X'
	Line 11: "-" + Y'
	Line 14: "-" + X'
	Line 15: "-" + Y'
	
	Option 2
	Line 5: X' + X_i-1
	Line 6: Y' + Y_j-1
	Line 10: X' + X_i-1
	Line 11: Y' + "-"
	Line 14: X' + "-"
	Line 15: Y' + Y_j-1
	
	Option 3
	Line 5: X_i-1 + X'
	Line 6: Y' + Y_j-1 + Y'
	Line 10: X_i-1 + X'
	Line 11: E + Y'
	Line 14: E + X'
	Line 15: Y_j-1 + Y'
	
	Option 4
	Line 5: X_i-1 + X'
	Line 6: Y_j-1 + Y'
	Line 10: X_i-1 + X'
	Line 11: "-" + Y'
	Line 14: "-" + X'
	Line 15: Y_j-1 + Y'
	
	Option 5
	Line 5: E + X'
	Line 6: E + Y'
	Line 10: X_i-1 + X'
	Line 11: "-" + Y'
	Line 14: "-" + X'
	Line 15: Y_j-1 + Y'
	
	Option 6
	Line 5: E + X'
	Line 6: E + Y'
	Line 10: X_i-1 + X'
	Line 11: E + Y'
	Line 14: E + X'
	Line 15: Y_j-1 + Y'
	"""
	# Again, look at what this algorithm does.
	# Line 1:  Initializes i and j to the lengths of X and Y, respectively.
	# Line 2:  Initializes X' and Y' to empty strings.
	# Line 3:  While loop that checks for i and j both being greater than zero.
	# Line 4:      Conditional check (starting at bottom-left cell of S table) for 
	#                 equivalence between S[i, j] and S[i-1,j-1] + M_Xi-1,Yj-1.
	# Line 5:          Assign X' to something.
	# Line 6:          Assign Y' to something.
	# Line 7:          Decrease i and j both by 1. 
	# Line 8:      else
	# Line 9:          Conditional check S[i,j] = S[i-1,j] + M_xi-1,-.
	# Line 10:            Assign X' to something.
	# Line 11:            Assign Y' to something.
	# Line 12:            Decrease i by 1.
	# Line 13:        else
	# Line 14:            Assign X' to something.
	# Line 15:            Assign Y' to something.
	# Line 16:            Decrease j by 1.
	# Line 17:While loop that checks for i != 0.
	# Line 18:    Assign X' to X_i-1 + X' and assign Y' to "-" + Y'.
	# Line 19:    Decrease i by 1.
	# Line 20:While loop that checks for j != 0.
	# Line 21:    Assign X' to "-" + X' and assign Y' to Y_j-1 + Y'.
	# Line 22:    Decrease j by 1.
	# Line 23:Return (X', Y'), the global pairwise alignment of X and Y.
	
	# Lines 3-16 appear to do the heavy lifting, while 17-22 do the cleanup.
	# The first while loop works as long as there are components of both seqs
	# being compared to one another. The second and third handle the two
	# scenarios when i or j is expended during the first loop. If i > 0 (there are
	# components of X still relevant), X' is assigned to X_i-1 + X', so if X is
	# TAG, and X' = AG, this would assign X' to TAG, since T is X_i-1. Y' is
	# then assigned to -Y', adding that preceding dash for as long as there are
	# X components left to compare. The reverse situation inserts dashes in
	# front of X' while it inserts Y_j-1 values in front of Y'.
	
	# Let's think about this for X = AC and Y = TAG. This creates a 3x4 DP table.
	# The first while loop's 1st conditional on its 1st run compares S[i,j], or AC:TAG,
	# or actually the DP table's score of AC:TAG, to S[i-1,j-1] + M_Xi-1,Yj-1, which
	# is A:TA, or the score of A:TA from table S, plus the score that A:A receives
	# from the scoring matrix (M_sig,sig). Using the example S table from the
	# linked source, S[2,3] = 3 and M_sig,sig = 5, and S[1,2] = 1.
	# Check if 3 == 1 + 5: nope. Then check if S[i,j] = S[i-1,j] + M_Xi-1,-.
	# S[1,3] = -3 and M_Xi-1,- = -2. Check if 3 = -3 - 2: nope. This means
	# that to get to S[2,3], the path must have been from S[i,j-1], which is
	# S[2,2] = 4. M_-,Yj-1 = -4. Check if 3 == 4 - 4: nope. 
	
	## I investigated further and now understand my misreading of the values
	## of M_Xi-1,Yj-1. See the latter two comment blocks in 408 for details.
	## My mistake was painfully obvious once I began to implement these functions
	## in Project 4.
	
	# So assuming the first check returns True, it appears to signify that a
	# diagonal step was taken from i-1,j-1 to i,j. As X' and Y' are being built
	# from right to left, the assignments in lines 5-6 likely append old X' to the end
	# of the new alignment X'. 
	## Options 2-3 are out because in lines 5-6 and line 6, respectively, this would
	## not occur.
	## Options 5-6 are out because you do not want to constantly append X' and Y' 
	## to empty strings, as this will accomplish nothing (lines 1-2 in both).
	# Clearly, then, you are appending X' and Y' to X_i-1 and Y_j-1, respectively,
	# as you build your global alignments (in this case, where it steps diagonally).
	
	# If there is no diagonal step, the else statement's conditional checks for an
	# equivalence of S[i,j] to S[i-1,j] + M_Xi1,-. If True, then there was a step
	# from above. This means that X' would be concatenated to current X elem
	# X_i-1 (remember we're moving backwards) and Y' did not change, so it 
	# would get a dash inserted in front of it as X_i-1 was paired with a dash at
	# this entry. The else for this second conditional assumes then that the step
	# was from the left, where Y' increased by one elem (in the front) and X' did
	# not (hence the leading dash). 
	## Option 1 is out because in it lines 10-11 and 14-15 are inserting dashes in
	## front of the alignment in all 4 cases.
	
	answer = 	"Line 5: X_i-1 + X'" + "\n"
	answer += "Line 6: Y_j-1 + Y'" + "\n"
	answer += "Line 10: X_i-1 + X'" + "\n"
	answer += "Line 11: '-' + Y'" + "\n"
	answer += "Line 14: '-' + X'" + "\n"
	answer += "Line 15: Y_j-1 + Y'"
	
	print "Question 409 Answer:"
	print answer
	print "-"*50
	print "\n"
	
hw_409()	

##################################################

def hw_410():
	"""
	QUESTION 10
	
	Given two strings X and Y of lengths m and n, respectively, which of the
	following gives the tightest worst-case running time of GlobalAlignment as
	given by the pseudocode in question 7?
	
	Option 1
	O(2**(m+n))
	
	Option 2
	O(m*n)
	
	Option 3
	O(m**2 * n**2)
	
	Option 4
	O(m+n)
	"""
	# GlobalAlignment is determined by the running time of its subprocedures 
	# ComputeGlobalAlignmentScores and ComputeAlignment.
	# The first appears to have a running time of m + n + m*n, or O(m*n).
	# The second appears to have a running time of m + n or O(m + n).
	# Running time of GlobalAlignment = O(m*n) + O(m+n), which can be
	# reduced to the component with the most effect: O(m*n).
	
	answer = "O(m*n)"
	
	print "Question 410 Answer:"
	print answer
	print "-"*50
	print "\n"
	
hw_410()	

##################################################

def hw_411():
	"""
	QUESTION 11
	
	Recall that given a string x, the string v is a substring of x if there exist
	strings u and w such that x = u + v + w. Given a string x of length n, how
	many substrings v of x are there? You may assume that each character
	of x is distinct if necessary to clarify the problem. Enter your answer below
	as a mathematical expression in n.
	"""
	# Note that the empty string E (epsilon) can be a substring of any string, so
	# u and w could equal empty strings and x = v. A substring is just any segment
	# of x, from an empty string all the way to x, that is plucked from it with
	# no changes to its internal members, so if x = ABCD, a substring is BC but
	# not ACD because A and CD are separated by a B within x, which violates the
	# rule that v not itself be split up, only that more segments from x can come
	# before and/or after it to form x.
	
	# Let's look at a few examples before writing simple code to compute this.
	# x = "". Subs = "". Num = 1. This may be the base case.
	# x = "A". Subs = "", "A". Num = 2.
	# x = "AB". Subs = "", "A", "B", "AB". Num = 4.
	# x = "ABC". Subs = "", "A", "B", "C", "AB", "BC", "ABC". Num = 7. 
	# x = "ABCD". Subs = "", "A", "B", "C", "D", "AB", "BC", "CD", "ABC", "BCD",
	# "ABCD". Num = 11. 
	# "ABCDE". Subs = "", 5*components, "AB", "BC", "CD", "DE", "ABC", "BCD",
	# "CDE", "ABCD", "BCDE", "ABCDE". Num = 16. 
	# A lookup of sequence 1, 2, 4, 7, 11, 16 returns the 'Lazy caterer's sequence'
	# which is the maximal number of pieces formed when slicing a pancake with
	# n cuts. The formula p = (n**2 + n + 2) / 2 when n >= 0 is given. A quick
	# test for correctness of n:p pairs: 0:1, 1:2, 2:4, 3:7, 4:11, 5:16. Looks good.
	# No code necessary to solve.
	
	# Not incidentally, the recurrence relation is given as f(n) = n + f(n-1) with a
	# base case of f(0) = 1. This can be written as f(n) = 1 + (1 + 2 + 3 + ... + n).
	# That can be simplified using the formula for the sum of an arithmetic progression:
	# f(n) = 1 + ((n*(n+1))/2) = (n**2 + n + 2)/2.
	
	answer = "(n**2 + n + 2)/2"
	
	print "Question 411 Answer:"
	print answer
	print "-"*50
	print "\n"
	
hw_411()	
	
##################################################

def hw_412():
	"""
	QUESTION 12
	
	In questions 12-15, we will make simple mods to ComputeGlobalAlignment-
	Scores and ComputeAlignment that yield an efficient algm for the Local
	Pairwise Alignment Problem.
	
	In this question, we will focus on modifying ComputeGlobalAlignmentScores to
	compute a matrix of local alignment scores. Our modification is as follows:
	Whenever that algm computes a value to assign to S[i,j], if the computed
	value is negative, the algm instead assigns 0 to S[i,j]. The result of this
	computation is the local alignment matrix for the two sequences. No other
	modification is done.
	
	As an example, consider X = AA and Y = TAAT over alphabet SIG = {A,C,T,G}
	and the scoring matrix M given by (in = is an element of, not using E as it has
	been used above to refer to epsilon, instead of here to refer to that set operator).
	* M_sig,sig = 10 for every sig in SIG
	* M_sig,sig' = 4 for every sig,sig' in SIG where sig != sig'
	* M_sig,- = M_-,sig = -6 for every sig in SIG
	
	Given the two sequences X and Y and scoring matrix M, what values would the
	modified algm assign to the entries S[0,2], S[2,0] and S[2,2] of the local
	alignment matrix S? Enter your answer below as 3 numbers separated by spaces.
	"""
	# The very first thing to do here is to build that DP matrix S from scratch.
	# m = 2, Y = 4, S[0,0] = 0, and the rest of the spaces will be set to 'Z' as
	# a placeholder. The table will look like this:
	#       -     T    A     A     T
	#  -    0   Z     Z    Z     Z
	#  A   Z    Z     Z    Z     Z
	#  A   Z    Z     Z     Z    Z
	#
	# Now I will step through the CGAS algm assigning scores to S, but with the
	# modification where S[i,j] = 0 if S[i,j] <= 0. 
	# For i = 1 to 2, S[i,0] = S[i-1,0] + M_Xi-1,- (cases of X':- pairs).
	#     S[1,0] = 0 - 6 = -6 or 0.
	#     S[1,2] = 0 - 6 = -6 or 0.
	# For j = 1 to 4, S[0,j] = S[0,j-1] + M_-,Yj-1 (cases of -:Y' pairs).
	#     S[0,1] = 0 - 6 = -6 or 0 (across for j = 1 to 3, all 3 values).
	#       -     T    A     A     T
	#  -    0   0     0     0     0
	#  A   0    Z     Z    Z     Z
	#  A   0    Z     Z     Z    Z
	# 
	# For i = 1 to 2: For j = 1 to 4: S[i,j] = max{S[i-1, j-1] + M_Xi-1,Yj-1, 
	# S[i-1, j] + M_Xi-1,-, S[i, j-1] + M_-,Yj-1} (all other cases).
	#     S[1,1] = max{0+4, 0-6, 0-6} = 4
	#     S[1,2] = max{0+10, 0-6, 4-6} = 10
	#     S[1,3] = max{0+10, 0-6, 10-6} = 10
	#     S[1,4] = max{0+4, 0-6, 10-6} = 4
	#     S[2,1] = max{0+4, 4-6, 0-6} = 4
	#     S[2,2] = max{4+10, 10-6, 4-6} = 14
	#     S[2,3] = max{10+10, 10-6, 14-6} = 20
	#     S[2,4] = max{10+4, 4-6, 20-6} = 14
	#       -     T    A     A     T
	#  -    0   0     0     0     0
	#  A   0    4    10   10    4
	#  A   0    4    14   20   14
	# 
	# We are tasked with finding S[0,2], S[2,0], and S[2,2].
	
	answer = "0 0 14"
	
	print "Question 412 Answer:"
	print answer
	print "-"*50
	print "\n"
	
hw_412()	
	
##################################################

def hw_413():
	"""
	QUESTION 13
	
	During the computation of a global alignment, the traceback in the global 
	alignment matrix S starts at the bottom right corner of the matrix (S[m,n])
	and traces to the upper left corner (S[0,0]). Given the local alignment matrix
	S computed in question 12, algorithm ComputeAlignment can be modified
	to generate a local alignment of 2 sequences as follows:
	
	Start the traceback from the entry in S that has the maximum value over the
	entire matrix and trace backwards using exactly the same technique as in
	ComputeAlignment. Stop the traceback when the first entry with value 0 is
	encountered. If the local alignment matrix has more than one entry that has
	the maximum value, any entry with max value may be used as the starting
	entry.
	
	As a concrete example of this process, what is the maximum value in an entry
	in the local alignment matrix S that you computed in Question 12? Enter your
	answer below as a single number.
	"""
	# The highest score on the DP matrix S is 20. This corresponds to the optimal
	# alignments X' = AA and Y' = AA, where both A's line up with other A's in each
	# and the score is 10 + 10 = 20.
	
	answer = 20
	
	print "Question 413 Answer:"
	print answer
	print "-"*50
	print "\n"
	
hw_413()	
	
##################################################

def hw_414():
	"""
	QUESTION 14
	
	At what entry does the modified ComputeAlignment from question 13 start the
	traceback and at what entry does it end the traceback?
	
	If the traceback starts at entry S[i,j] and ends at entry S[k,l], what are the
	values for the starting entry (i,j) and ending entry (k,l)? Enter your answer
	below as four individual numbers i, j, k, l, separated by spaces. For example,
	if the traceback starts at S[15,20] and ends at S[2,4], enter 15 20 2 4 below.
	"""
	# Recall that the DP alignment matrix S computed in question 12, referenced
	# in question 13, was:
	#       -     T    A     A     T
	#  -    0   0     0     0     0
	#  A   0    4    10   10    4
	#  A   0    4    14   20   14
	#
	# The traceback would start at the highest entry, which is 20, located at
	# entry S[2,3]. If the same traceback procedure is followed, you can trace the 
	# following steps through each of the statements:
	# Find indices i,j where S[i,j] = maximum score in matrix S.
	# While S[i,j] > 0:
	#     Check conditionals.
	#     Decrement i and/or j accordingly.
	# While S[i,j] > 0:
	#     Check: S[2,3] > 0.
	#     Check: S[2,3] = S[i-1,j-1] + M_Xi-1,Yj-1
	#     Result: 20 = 10 + 10 returns True. X' = A + "", Y' = A + "", i and j -= 1.
	#     Check: S[1,2] > 0.
	#     Check: S[1,2] = S[i-1,j-1] + M_Xi-1,Yj-1.
	#     Result: 10 = 0 + 10 returns True. X' = A + A, Y' = A + A, i and j -= 1.
	#     Check: S[0,1] > 0.
	# STOP traceback at S[0,1] since it equals zero.
	
	# A diagonal path was carved that ended with alignments X' = AA and Y' = AA.
	# A quick scribble of possible permutations of X = AA and Y = TAAT shows that
	# being the optimal alignment, scoring 20. The algorithm starts with A:A, then 
	# steps diagonally to AA:AA, then terminates. 
	
	answer = "2 3 0 1"
	
	print "Question 414 Answer:"
	print answer
	print "-"*50
	print "\n"
	
hw_414()	
		
##################################################

def hw_415():
	"""
	QUESTION 15
	
	Using the modded CGAS and CA algorithms in questions 12 and 13, what is the
	local alignment they compute on the sequences X and Y using the scoring matrix
	in question 12?
	
	Option 1
	X' = AA- and Y' = AAT
	
	Option 2
	X' = AA and Y' = AA
	
	Option 3
	X' = A and Y' = A
	
	Option 4
	X' = -AA and Y' = TAA
	
	Option 5
	X' = -AA- and Y' = TAAT
	"""
	# My notes clearly show that X' = AA and Y' = AA, so option 2 is correct. All
	# other outcomes either do not line up all As in both sequences, or dashes
	# are added which detract from the score.
	
	answer = "X' = AA and Y' = AA"
	
	print "Question 415 Answer:"
	print answer
	print "-"*50
	print "\n"
	
hw_415()	
			
##################################################

def hw_416():
	"""
	QUESTION 16
	
	Given two strings X and Y of lengths m and n, respectively, which of the
	following gives the tightest worst-case running time of computing a local
	alignment of the two strings using the modified algms in questions 12 and 13?
	
	Option 1
	O(m**2 * n**2)
	
	Option 2
	O(m*n)
	
	Option 3
	O(m+n)
	
	Option 4
	O(2**(m+n))
	"""
	# The original version of the algorithm GlobalAlignment appeared to have a
	# running time of O(m*n) + O(m+n) = O(m*n). 
	# The modification in the first subprocedure does not preclude it from having
	# to compute scores for m*n positions in matrix S. The modification to the
	# second subprocedure does appear to improve its running time, but the total
	# running time is most affected by the first subprocedure. The running time
	# does not appear to be better.
	
	answer = "O(m*n)"
	
	print "Question 416 Answer:"
	print answer
	print "-"*50
	print "\n"
	
hw_416()	
				
##################################################

def hw_417():
	"""
	QUESTION 17
	
	Is this statement true or false?
	
	If all entries in a scoring matrix M are non-negative, then the score of an 
	optimal local alignment and an optimal global alignment of two sequences
	X and Y using M are identifical.
	"""
	# This is a brain teaser. I need to identify a case where the score of an
	# optimal local alignment and an optimal global alignment of 2 sequences
	# are not identifical, but where all entries in a scoring matrix M are >= 0.
	
	# The material in the provided link note the problem with two sequences of
	# very different length where the smaller strongly corresponds to a small
	# local region in the longer can lead to a problem where negative values
	# mask the high similarity found if the two regions were removed and compared
	# without the rest of each sequence. If the values are NOT negative, it seems
	# that this problem might not persist, at last not to the point where local
	# alignments need to be computed. I will guess that the answer is true.
	
	answer = "true"
	
	print "Question 417 Answer:"
	print answer
	print "-"*50
	print "\n"	

hw_417()

##################################################

## Print out number of total incorrect answers and which they are.

incorrect = [402, 406]
print "The following questions were answered incorrectly and need to be solved:"
for problem in incorrect:
	print "Question #" + str(problem)
	
##################################################
##################################################