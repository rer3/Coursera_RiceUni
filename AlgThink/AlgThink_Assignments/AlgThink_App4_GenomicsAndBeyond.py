"""
Rice University / Coursera: Algorithmic Thinking (Part 2)
Module 4: Application 4
Applications to Genomics and Beyond
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run on the desktop using PyCharm.
#=================================================================

# All import statements needed.

import math
import matplotlib.pyplot as plt
import random
import urllib2
random.seed(1)

# Below is the link to the description of this assignment.

COURSE = "https://class.coursera.org/algorithmicthink2-003/"
DESCRIPTION = COURSE + "human_grading/view/courses/975650/assessments/34/submissions"

#-----------------------------------------------------------------
## Provided code for App 4 to read scoring matrix and read words.

# URLs for data files
PAM50_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt"
HUMAN_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt"
FRUITFLY_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt"
CONSENSUS_PAX_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt"
WORD_LIST_URL = "http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt"

# provided code

def read_scoring_matrix(filename):
    """
    Read a scoring matrix from the file named filename.  

    Argument:
    filename -- name of file containing a scoring matrix

    Returns:
    A dictionary of dictionaries mapping X and Y characters to scores
    """
    scoring_dict = {}
    scoring_file = urllib2.urlopen(filename)
    ykeys = scoring_file.readline()
    ykeychars = ykeys.split()
    for line in scoring_file.readlines():
        vals = line.split()
        xkey = vals.pop(0)
        scoring_dict[xkey] = {}
        for ykey, val in zip(ykeychars, vals):
            scoring_dict[xkey][ykey] = int(val)
    return scoring_dict

def read_protein(filename):
    """
    Read a protein sequence from the file named filename.

    Arguments:
    filename -- name of file containing a protein sequence

    Returns:
    A string representing the protein
    """
    protein_file = urllib2.urlopen(filename)
    protein_seq = protein_file.read()
    protein_seq = protein_seq.rstrip()
    return protein_seq

def read_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    # load assets
    word_file = urllib2.urlopen(filename)
    
    # read in files as string
    words = word_file.read()
    
    # template lines and solution lines list of line string
    word_list = words.split('\n')
    print "Loaded a dictionary with", len(word_list), "words"
    return word_list

#-----------------------------------------------------------------
## Helper function from Project 4 which builds a matrix.

def make_matrix(height, width, fill_value):
    """
    Make a matrix of specified dimensions and fill it with the default fill_value.
    """
    return [[fill_value for dummy_col in range(width)] for 
                    dummy_row in range(height)]

#-----------------------------------------------------------------
## Four functions from Project 4 for building a scoring matrix, computing an
## alignment matrix, and computing global and local alignments.

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

#-----------------------------------------------------------------
## Helper functions for normalizing an un-normalized distribution dictionary
## taken from Application 1.

def normalize_list(a_list):
    """
    Function that normalizes a list of data.
    """
    if len(a_list) <1:
        return float('nan')
    divisor = float(sum(a_list))
    return [item / divisor for item in a_list]

def dict_to_normalized_lists(a_dict):
    """
    Function that converts a dictionary to a list of [sorted key, 
    normal_value] lists.
    """
    normal_list = []
    keys = sorted(a_dict.keys())
    normvals = normalize_list([a_dict[key] for key in keys])
    for index in range(len(keys)):
        normal_list.append([keys[index], normvals[index]])
    return normal_list

##=================================================================

DIRECTIONS = '''
Overview
----------
In Project 4, you implemented dynamic programming algorithms for determining
both global and local alignments of pairs of sequences. In this Application, we will
demonstrate the utility of these algms in two domains. In the first part of the App,
we examine an interesting problem from genomics. This is based on "Introduction
to Computational Genomics" by Nello Cristianini and Matthew W. Hahn. We will
compare two sequences that have diverged from a common ancestor sequence
due to mutation. Mutation here include base-pair substitution, which changes the
sequence content, and insertion/deletion, which change the sequence lengths. 
In the second part of the App, we consider words that have spelling mistakes.

For the genomics part of the App, you will load several protein sequences and an
appropriate scoring matrix. For the spelling correction part of the App, you will
load a provided word list. To simplify these tasks, you are welcome to use the
provided code (above).

Important: Use Coursera's "Attach a file" button to attach your plots/images
as required. You can attach more than one image and include text and math
(LaTeX) in the same answer box. Do not submit links to 3rd party sites.
'''

##=================================================================

def app_401():
    """
    QUESTION 1: Comparing two proteins
    
    In 1994, Walter Gehring and colleagues at the  University of Basel carried out
    an "interesting" experiment: they were able to turn on a gene called eyeless
    in various places on the body of the fruit fly, Drosophila melanogaster. The
    result was astonishing - fruit flies developed that had whole eyes sprouting
    up all over their bodies. It turned out that the eyeless is a master regulatory
    gene - it controls a cascade that contains more than 2000 other genes. 
    Turning it on anywhere in the body activates the cascade and produces a fully
    formed, but non-functioning, eye. Humans, as well as many other animals,
    have a slightly different version of the eyeless gene (that is, a similar, yet
    not identifical sequence of the same gene).
    
    This observation suggests that about 600 million years ago (the estimated
    divergence between humans and fruit flies) there was an ancestral organism
    that itself used some version of eyeless, and that throughout the evolution
    of humans and fruit flies this gene continued to be maintained, albeit while
    accumulating mutations that did not greatly affect its function. In particular,
    a substring of the eyeless protein of about 130 amino acids, known as the
    PAX domain, whose function is to bind specific sequences of DNA, is virtually
    identifical between the human and fruit fly versions of eyeless.
    
    In following questions, we compute the similarity between the human and
    fruit fly versions of the eyeless protein and see if we can identify the PAX
    domain.
    ------
    
    First, load the files HumanEyelessProtein:
    http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt
    and FruitflyEyelessProtein:
    http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt
    using the provided code. These files contain the amino acid sequences that
    form the eyeless proteins in the human and fruit fly genomes, respectively.
    Then load the scoring matrix PAM50:
    http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt
    for sequences of amino acids. This scoring matrix is defined over the alphabet
    {A,R,N,D,C,Q,E,G,H,I,L,K,M,F,P,S,T,W,Y,V,B,Z,X,-} which represents all possible
    amino acids and gaps (the "dashes" in the alignment).
    
    Next, compute the local alignments of the sequences of HumanEyelessProtein
    and FruitflyEyelessProtein using the PAM50 scoring matrix and enter the score
    and local alignments for these two sequences below. Be sure to clearly
    distinguish which alignment is which and include any dashes ('-') that might
    appear in the local alignment. This problem will be assessed according to the
    following two items:
    * Is the score of the local alignment correct? Hint: The sum of the decimal
        digits in the score is 20.
    * Are the two sequences in the local alignments (with dashes included if
        inserted by the algm) clearly distinguished and correct?
    """
    # First, I will paste the four functions from Project 4 above in the shared
    # area. Two of these will be used to compute an alignment matrix and local 
    # alignments of the two sequences.
    
    # Next, I must use the provided code to read the scoring matrix and the seqs.
    # Variable names will defy Pylint guidelines and mirror variable names used in
    # the pseudocode for the algorithms implemented in Project 4.
    
    X = read_protein(HUMAN_EYELESS_URL)
    Y = read_protein(FRUITFLY_EYELESS_URL)
    M = read_scoring_matrix(PAM50_URL)
    
    # Note that the alphabet does not need to be initialized here, since the scoring
    # matrix is already built, and the function to build it that was implemented in
    # Project 4 is the only function to take the alphabet as an input.
    
    # Now I am tasked with computing the local alignments of the sequences of
    # HumanEyelessProtein and FruitflyEyelessProtein using PAM50 scoring matrix.
    # First I must compute the alignment matrix, S.
    
    S = compute_alignment_matrix(X, Y, M, global_flag = False)
    
    local_alignments = compute_local_alignment(X, Y, M, S)
    score = local_alignments[0]
    align_human = local_alignments[1]
    align_fly = local_alignments[2]
    
    answer = "Score: " + str(score) + "\n"
    answer += "Human Local Alignment: " + align_human + "\n"
    answer += "Fruitfly Local Alignment: " + align_fly
    
    print "Question 401 Answer:"
    print answer
    print "-"*50
    print "\n"
    
app_401()

##=================================================================

def app_402():
    """
    QUESTION 2
    
    To continue our investigation, we next consider the similarity of the two
    sequences in the local alignment computed in question 1 to a third seq. The
    file ConsensusPAXDomain:
    http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt
    contains a "consensus" seq of the PAX domain; that is, the seq of amino acids
    in the PAX domain in any organism. In this problem, we will compare each of
    the two seqs of the local alignment computed in question 1 to this consensus
    sequence to determine whether they correspond to the PAX domain.
    
    Load the file ConsensusPAXDomain. For each of the two seqs of the local
    alignment computed in question 1, do the following:
    * Delete any dashes '-' present in the sequence
    * Compute the global alignment of this dash-less seq with the
        ConsensusPAXDomain seq. 
    * Compare corresponding elements of these two globally-aligned seqs (local
        vs. consensus) and compute the percentage of elements in these two seqs
        that agree.
        
    To reiterate, you will compute the global alignments of local human vs.
    consensus PAX domain as well as local fruitfly vs. consensus PAX domain.
    Your answer should be two percentages: one for each global alignment. Enter
    each percentage below. Be sure to label each answer clearly and include 3
    significant digits of precision.
    """
    # First I will run through the procedure in 401 to compute the local
    # alignment sequences.  
    X = read_protein(HUMAN_EYELESS_URL)
    Y = read_protein(FRUITFLY_EYELESS_URL)
    M = read_scoring_matrix(PAM50_URL)
    S = compute_alignment_matrix(X, Y, M, global_flag = False)
    local_alignments = compute_local_alignment(X, Y, M, S)
    # The score is unnecessary, but the local alignments will be referenced.
    local_align_human = local_alignments[1]
    local_align_fly = local_alignments[2]
    
    # Load the ConsensusPAXDomain sequence.
    PAX = read_protein(CONSENSUS_PAX_URL)
    
    # Remove dashes from local alignment sequences.
    nodash_hum = local_align_human.replace("-", "")
    nodash_fly = local_align_fly.replace("-", "")
    
    # Compute the global alignment of each dashless seq with PAX.
    S_humpax = compute_alignment_matrix(nodash_hum, PAX, M, global_flag = True)
    global_aligns_humpax = compute_global_alignment(nodash_hum, PAX, M, S_humpax)
    global_align_human = global_aligns_humpax[1]
    global_align_pax_human = global_aligns_humpax[2]
    
    S_flypax = compute_alignment_matrix(nodash_fly, PAX, M, global_flag = True)
    global_aligns_flypax = compute_global_alignment(nodash_fly, PAX, M, S_flypax)
    global_align_fly = global_aligns_flypax[1]
    global_align_pax_fly = global_aligns_flypax[2]
    
    # Compare corresponding elements of these two globally-aligned sequences
    # (local vs. consensus) and compute the percentage of elements in these two
    # sequences that agree.
    
    # Initialize a variable in which to increment when a match is made while iterating
    # over the two sequences (local vs. consensus) and comparing the two lined up
    # elements. Then compute (num matches) / (total elements) * 100 to get %.
    matches_humpax = 0
    for idx in range(len(global_align_human)):
        if global_align_human[idx] == global_align_pax_human[idx]:
            matches_humpax += 1
    percent_humpax = float(matches_humpax) / len(global_align_human) * 100
    print "Global alignments of human and PAX"
    print global_align_human
    print global_align_pax_human
    print "-"*5
    # Agreement percentage: 72.9323308271%.
    
    matches_flypax = 0
    for idx in range(len(global_align_fly)):
        if global_align_fly[idx] == global_align_pax_fly[idx]:
            matches_flypax += 1
    percent_flypax = float(matches_flypax) / len(global_align_fly) * 100
    print "Global alignments of fly and PAX"
    print global_align_fly
    print global_align_pax_fly
    print "-"*5
    # Agreement percentage: 70.1492537313%.
    
    answer = "Agreement between globally-aligned local-human and "
    answer += "consensus sequences:" + "\n"
    answer += str(percent_humpax) + "%" + "\n"
    answer += "Agreement between globally-aligned local-fly and "
    answer += "consensus sequences:" + "\n"
    answer += str(percent_flypax) + "%"
    
    print "Question 402 Answer:"
    print answer
    print "-"*50
    print "\n"
    
app_402()   

##=================================================================

def app_403():
    """
    QUESTION 3
    
    Examine your answers to questions 1-2. Is it likely that the level of similarity
    exhibited by the answers could have been due to chance? In particular, if you
    were comparing two random sequences of amino acids of length similar to
    that of HumanEyelessProtein and FruitflyEyelessProtein, would the level of
    agreement in these answers be likely? To help you in your analysis, there are
    23 amino acids with symbols in the string ("ACBEDGFIHKMLNQPSRTWVYXZ").
    Include a short justification for your answer.
    """
    # Prove the case when comparing two random sequences of amino acids of
    # length similar to that of HumanEyelessProtein and FruitflyEyelessProtein
    # (422 and 857, respectively) does not result in the same level of agreement
    # as exhibited in question 2's results. 
    
    # First create two randomly-filled sequences of amino acids with lengths
    # similar to those of HumanEyelessProtein and FruitflyEyelessProtein. Set
    # random.seed equal to 1 so that results can be replicated.
    
    HUMLEN = 422
    FLYLEN = 857
    amino_acids = "ACBEDGFIHKMLNQPSRTWVYXZ"
    PAX = read_protein(CONSENSUS_PAX_URL)
    
    X = ""
    for idx in range(HUMLEN):
        X += random.choice(amino_acids)
        
    Y = ""
    for idx in range(FLYLEN):
        Y += random.choice(amino_acids)
        
    # Run the same procedure on X and Y as done on hum and fly in question 2.
    # Compute local alignments.
    M = read_scoring_matrix(PAM50_URL)
    S = compute_alignment_matrix(X, Y, M, global_flag = False)
    locals = compute_local_alignment(X, Y, M, S)
    locals_x = locals[1]
    locals_y = locals[2]
    print "Score of local alignment between X and Y: " + str(locals[0])
    print "X: " + X
    print "Y: " + Y
    
    # Remove dashes and compute global alignments with PAX.
    nodash_x = locals_x.replace("-", "")
    S_xpax = compute_alignment_matrix(nodash_x, PAX, M, global_flag = True)
    globals_xpax = compute_global_alignment(nodash_x, PAX, M, S_xpax)
    globals_x = globals_xpax[1]
    globals_pax_x = globals_xpax[2]
    
    nodash_y = locals_y.replace("-", "")
    S_ypax = compute_alignment_matrix(nodash_y, PAX, M, global_flag = True)
    globals_ypax = compute_global_alignment(nodash_y, PAX, M, S_ypax)
    globals_y = globals_ypax[1]
    globals_pax_y = globals_ypax[2]
    
    # Compute percentages and print the results.
    matches_xpax = 0
    for idx in range(len(globals_x)):
        if globals_x[idx] == globals_pax_x[idx]:
            matches_xpax += 1
    percent_xpax = float(matches_xpax) / len(globals_x) * 100
    
    matches_ypax = 0
    for idx in range(len(globals_y)):
        if globals_y[idx] == globals_pax_y[idx]:
            matches_ypax += 1
    percent_ypax = float(matches_ypax) / len(globals_y)
    
    print "Global alignments of local X and PAX"
    print globals_x
    print globals_pax_x
    print "Agreement: " + str(percent_xpax) + "%" 
    print "-"*5
    # Agreement percentage: 8.0%.
    
    print "Global alignments of local Y and PAX"
    print globals_y
    print globals_pax_y
    print "Agreement: " + str(percent_ypax) + "%"
    print "-"*5
    # Agreement percentage: 0.08%.
    
    answer = '''
The level of similarity exhibited by the answers in questions 1-2 does not surprise
me. Humans and fruit flies share a common ancestor that carried the eyeless
gene, and it is even stated in question 1 that emperical observations have suggested
that this gene is largely maintained in both human and fruit fly DNA. The PAX domain
is defined as a substring of the eyeless protein which is virtualy identical between
the human and fruit fly versions of eyeless.

In question 1, we simply computed the local alignments of the human and fruit fly
eyeless proteins, which were stated as being very similar. A quick glance at the
two computed local alignments shows this to be the case. Question 1 verified
this similarity using our implementation of the local alignment algorithm.

In question 2, we computed global alignment of the local human sequence and
the consensus PAX domain sequence, as well as global alignment of the local
fruit fly sequence and the consensus PAX domain sequence. Since the two local
sequences were very alike, we expected their global alignments with PAX to be
roughly the same, and this was the case, verified through our computations
(agreement percentages of 72.9% and 70.1% are very close). That high degree
of similarity between either local alignment, human or fly, and PAX was expected, 
as it was stated at the beginning that the eyeless sequence was largely maintained 
in both species' DNA, and the PAX domain was described as being virtually identical 
between the human and fruit fly versions of eyeless. 

Essentially, we proved that two DNA sequences were alike when a local alignment
was computed between them, and that each was, globally, very similar to the
PAX domain, with around 70% agreement between elements in localized human/fly 
eyeless protein sequences and the PAX sequence. I would not expect this level of
similarity if I were to compare two random sequences of amino acids of length
similar to that of HumanEyelessProtein and FruitflyEyelessProtein. In fact, I set
the random seed to 1 so that my results could be replicated, and I generated
two random amino acid sequences of lengths 422 and 857, respectively (X and Y).
I ran X and Y through the same procedure as the human and fly sequences
and computed agreement percentages of 8.0% and 0.08%. Randomly-generated
amino acid sequences do not necessarily share a common ancestor, but humans
and fruit flies do, so in the case of the random sequences, there is no guaranty
that ANY degree of similarity will arise.
'''
    
    print "Question 403 Answer:"
    print answer
    print "-"*50
    print "\n"

app_403()

##=================================================================

def app_404():
    """
    QUESTION 4: Hypothesis testing
    
    One weakness of our approach in question 3 was that we assumed that the
    probability of any particular amino acid appearing at a particular location in a
    protein was equal. In the next two questions, we will consider a more
    mathematical approach to answer question 3 that avoids this assumption. In
    particular, we will take an approach known as statistical hypothesis testing
    (https://en.wikipedia.org/wiki/Statistical_hypothesis_testing) to determine
    whether the local alignments computed in question 1 are statistically significant
    (that is, that th eprobability that they could have arisen by chance is small).
    
    Write a function generate_null_distribution(seq_x, seq_y, scoring_matrix,
    num_trials) that takes as input two sequences, a scoring matrix, and a number
    of trials. This function should return a dictionary scoring_distribution that
    represents an un-normalized distribution generated by performing the following
    process num_trials times:
    * Generate a random permutation rand_y of the sequence seq_y using
        random.shuffle().
    * Compute the maximum value score for the local alignment of seq_x and
        rand_y using the score matrix scoring_matrix.
    * Increment the entry score in the dictionary scoring_distribution by one.
    
    Use the function generate_null_distribution to create a distribution with
    1000 trials using the protein sequences HumanEyelessProtein and 
    FruitflyEyelessProtein (using the PAM50 scoring matrix). Important: Use
    HumanEyelessProtein as the first parameter seq_x (which stays fixed)
    and FruitflyEyelessProtein as the second parameter seq_y (which is randomly
    shuffled) when calling generate_null_distribution. Switching the order of these
    two parameters will lead to a slightly different answer for question 5 that
    may lie outside the accepted ranges for correct answers.
    
    Next, create a bar plot of the normalized version of this distribution using
    plt.bar in matplotlib (CodeSkulptor is too slow to do the required number of
    trials). The horizontal axis should be the scores and the vertical axis should
    be the fraction of total trials corresponding to each score. As usual, choose
    reasonable labels for the axes and title. You may wish to save the distribution
    that you compute in this question for later use in question 5 [I will return it].
    
    Once you have created your bar plot, upload your plot in the box below.
    Make sure that it follows the formatting guidelines for plots. 
    """
    # First implement the generate_null_distribution (GND) function.
    
    def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
        """
        Returns an un-normalized distribution of scores generated by computing
        the local alignment of seq_x and a random permutation of seq_y 
        num_trials times.
        """
        # Initialize score distribution dictionary.
        scoring_distribution = {}
        
        for trial in range(num_trials):
            # Generate random permutation of seq_y
            rand_y = list(seq_y)
            random.shuffle(rand_y)
            rand_y = "".join(rand_y)
            
            # Compute local alignment score of seq_x and rand_y
            alignment_matrix = compute_alignment_matrix(seq_x, rand_y, \
                                                        scoring_matrix, False)
            local_alignment = compute_local_alignment(seq_x, rand_y, scoring_matrix, \
                                                    alignment_matrix)
            score = local_alignment[0]
            
            # Update scoring distribution dictionary
            if score in scoring_distribution:
                scoring_distribution[score] += 1
            else:
                scoring_distribution[score] = 1
        
        return scoring_distribution
        
    # Use the function GND to create a null dist with 1000 trials using the human and
    # fruit fly eyeless protein sequences (and PAM50 scoring matrix). The random
    # seed was set to 1 so that this could be reproduced. Since the computation for
    # GND takes several minutes to complete, the returned dictionary will be
    # stored here in a variable for future reference.
    
    X = read_protein(HUMAN_EYELESS_URL)
    Y = read_protein(FRUITFLY_EYELESS_URL)
    M = read_scoring_matrix(PAM50_URL)
    NUM_TRIALS = 1000
    
    # Uncomment to re-run GND function.
    #local_humfly_dist = generate_null_distribution(X, Y, M, NUM_TRIALS)
    
    local_humfly_dist = {37: 1, 38: 1, 39: 2, 40: 5, 41: 14, 42: 22, 43: 30, 44: 42, 
                        45: 60, 46: 59, 47: 68, 48: 67, 49: 61, 50: 64, 51: 57, 
                        52: 55, 53: 56, 54: 45, 55: 55, 56: 46, 57: 36, 58: 30, 
                        59: 22, 60: 19, 61: 15, 62: 16, 63: 9, 64: 7, 65: 4, 66: 4, 
                        67: 5, 68: 4, 69: 3, 70: 2, 71: 1, 72: 1, 73: 3, 74: 3, 
                        75: 3, 77: 1, 78: 2}

    
    # Create a bar plot of the normalized version of the dist. I will shamelesly
    # steal the helper functions normalize_list and dict_to_normalized_lists
    # from Application 1 (in the shared area above).
            
    normdist = dict_to_normalized_lists(local_humfly_dist)
    x_vals = [key for key, normval in normdist]
    y_vals = [normval * 100 for key, normval in normdist]

    bar = plt.bar(x_vals, y_vals, color = "r")
    plt.title("Normalized Null Distribution:" + "\n" + "Local Alignment of Human and Fruit Fly Eyeless Protein")
    plt.xlabel("Local Alignment Score")
    plt.ylabel("Percent of Total Trials")
    plt.show()
    
    answer = "See image file: AlgThink_App404_Plot_NullDistLocalHumFly.png"
    
    print "Question 404 Answer:"
    print answer
    print "-"*50
    print "\n"
    
app_404()

##=================================================================

def app_405():
    """
    QUESTION 5
    
    Given the distribution computed in question 4, we can do some very basic
    statistical analysis of this distribution to help us understand how likely the 
    local alignment score from question 1 is. To this end, we first compute the
    mean mu and the standard deviation sig of this distribution via:
    
    mu = (1/n) * SIG_i (s_i)
    sig = sqrt((1/n) * SIG_i (s_i - mu)**2
    
    where the values s_i are the scores returned by the n trials. If s is the score
    of the local alignment for the human eyeless protein and the fruitfly eyeless
    protein, the z-score (https://en.wikipedia.org/wiki/Standard_score) z for this 
    alignment is
    
    z = (s - mu) / sig
    
    The z-score helps quantify the likelihood of the score s being a produce of
    chance. Small z-scores indicate a greater likelihood that the local alignment
    score was due to chance while higher scores indicate a lower likelihood that
    the local alignment score was due to chance.
    * What are the mean and standard deviation (mu and sig) that you computed
        in question 4?
    * What is the z-score for the local alignment for the human eyeless protein
    vs. the fruitfly eyeless protein based on these values?
    """
    # The local human and fruit fly distribution data from question 404 is below.
    local_humfly_dist = {37: 1, 38: 1, 39: 2, 40: 5, 41: 14, 42: 22, 43: 30, 44: 42, 
                    45: 60, 46: 59, 47: 68, 48: 67, 49: 61, 50: 64, 51: 57, 
                    52: 55, 53: 56, 54: 45, 55: 55, 56: 46, 57: 36, 58: 30, 
                    59: 22, 60: 19, 61: 15, 62: 16, 63: 9, 64: 7, 65: 4, 66: 4, 
                    67: 5, 68: 4, 69: 3, 70: 2, 71: 1, 72: 1, 73: 3, 74: 3, 
                    75: 3, 77: 1, 78: 2}
    # Convert into a list of all 1000 scores.
    dist_scores_divided = [[key] * value for key, value in local_humfly_dist.items()]
    dist_score_list = []
    for item in dist_scores_divided:
        dist_score_list.extend(item)
    
    # Implement custom functions to compute mean, standard deviation, and the
    # z score of an element.
    
    def compute_mean(score_list):
        """
        Returns mean score from a list of scores.
        """
        mu = sum(score_list) / float(len(score_list))
        return mu
        
    def compute_stdev(score_list):
        """
        Returns standard deviation from a list of scores.
        """
        mu = sum(score_list) / float(len(score_list))
        squared_deviations = [(score - mu)**2 for score in score_list]
        sig = math.sqrt(sum(squared_deviations) / float(len(score_list)))
        return sig
        
    def compute_zscore(score, mean, stdev):
        """
        Returns z score of a score based on mean and stdev.
        """
        zscore = (score - mean) / float(stdev)
        return zscore
    
    # Calculate mean and standard deviation for the distribution from question 404.
    dist_mean = compute_mean(dist_score_list)
    dist_stdev = compute_stdev(dist_score_list)
    
    # Calculate z-score for local alignment for the human eyeless protein vs. fruitfly
    # eyeless protein based on the mean and stdev above.
    
    SCORE_LOCAL_HUMFLY = 875
    zscore_local_humfly = compute_zscore(SCORE_LOCAL_HUMFLY, dist_mean, dist_stdev)
    
    answer = "For the null distribution computed in question 4 for local alignments "
    answer += "of HumanEyelessProtein and permutations of FruitflyEyelessProtein:"
    answer += "\n"
    answer += "Mean: " + str(dist_mean) + "\n"
    answer += "StDev: " + str(dist_stdev) + "\n"*2
    answer += "The z-score for the local alignment (score = 875) for HumanEyelessProtein "
    answer += "vs. FruitflyEyelessProtein based on those values was:" + "\n"
    answer += "z-score: " + str(zscore_local_humfly)

    print "Question 405 Answer:"
    print answer
    print "-"*50
    print "\n"
    
app_405()

##=================================================================

def app_406():
    """
    QUESTION 6
    
    For bell-shaped distributions such as the normal distribution
    (https://en.wikipedia.org/wiki/Normal_distribution), the likelihood that an
    observation will fall within three multiples of the standard deviation for such
    distributions is very high (https://en.wikipedia.org/wiki/Standard_deviation
    #Rules_for_normally_distributed_data). 
    
    Based on your answers to question 4 and 5, is the score resulting from the
    local alignment of the HumanEyelessProtein and the FruitflyEyelessProtein due
    to chance? As a concrete question, which is more likely: the similarity between
    the human eyeless protein and the fruitfly eyeless protein being due to chance
    or winning the jackpot in an extremely large lottery 
    (https://en.wikipedia.org/wiki/Lottery_jackpot_records)? Provide a short
    explanation for your answers.
    """
    # Note that the z-score represents the distance between the raw score and
    # the population mean in units of the stdev. A positive z is above the mean.
    # The likelihood that an observation should be between -3*stdev and 3 * stdev
    # is very high. The probability P that an experimental result with a z value
    # less than or equal to that observed is due to chance. Q = 1 - P, where Q is
    # the probability that the observed z score is due to chance. 
    
    # At the website for Fourmilab Switzerland, there is a Q calculator for inputs
    # of z-scores. Passing z = 127.450586766 to the calculate returns Q = 1/INF.
    # Link: http://www.fourmilab.ch/rpkp/experiments/analysis/zCalc.html. 
    
    answer = '''
The chance of such a high z-score is extremely low. On the Fourmilab Switzerland
website (http://www.fourmilab.ch/rpkp/experiments/analysis/zCalc.html) there is a
very handy Q calculator that takes as input a z-score. Q is the proability that the
z-score observed is due to chance. A low Q value for the z-score of the local 
alignment of HumanEyelessProtein and FruitflyEyelessProtein means that the score
resulting from the previous computations (score = 875, z-score = 127.5) did 
not result due to chance.

Entering a z-score of 127.5 into the calculator returns a Q value of 0, or about one
in infinity chance of the resulting alignment score being due to chance. Compare that
to the odds of winning an extremely large lottery. The website for the Powerball lottery
(http://www.powerball.com/powerball/pb_prizes.asp) states that the odds of winning
their Grand Prize are 1 in 292,201,338.

Play around with the Q calculator at the Fourmilab site to see that any z-score entered
that is greater than 6 will result in a Q of 0. At z-score = 6, the returned Q is
9.855 x 10**-10, a one in 1,014,713,328 (1 billion) chance that the observed z-score
of just SIX is due to chance. Refer to the Wikipedia link in this question and look at 
the reference table for z * standard deviations, in the column for "Fraction 
outside CI". At 7 std devs (when z-score = 7), the fraction of values outside CI is 1 in
390,682,215,445 (390 billion). 

Compare that to the z-score of 127.5 computed in question 6, and you see that it is 
extremely unlikely that the similarity between the human eyeless protein and the 
fruit fly eyeless protein is due to chance. There is a far greater likelihood that a
person could win the lottery multiple times than there is that the similarity between
the two proteins is due to chance.
'''
    
    print "Question 406 Answer:"
    print answer
    print "-"*50
    print "\n"
    
app_406()

##=================================================================

def app_407():
    """
    QUESTION 7: Spelling correction
    
    Up to now, we have measured the similarity of two strings. In other applications,
    measuring the dissimilarity of two sequences is also useful. Given two strings,
    the edit distance (https://en.wikipedia.org/wiki/Edit_distance) corresponds to
    the minimum number of single character insertions, deletions, and substitutions
    that are needed to transform one string into another. In particular, if x and y
    are strings and a and b are characters, these edit operations have the form:
    * Insert - Replace the string x + y by the string x + a + y.
    * Delete - Replace the string x + a + y by the string x + y.
    * Substitute - Replace the string x + a + y by the string x + b + y.
    
    Not surprisingly, similarity between pairs of sequences and edit distances
    between pairs of strings are related. In particular, the edit distance for two
    strings x and y can be expressed in terms of the lengths of the two strings
    and their corresponding similarity score as follows:
    
    |x| + |y| - score(x, y)
    
    where score(x, y) is the score returned by the global alignment of these two
    strings using a very simple scoring matrix that can be computed using
    build_scoring_matrix.
    
    Determine the values for diag_score, off_diag_score, and dash_score such that
    the score from the resulting global alignment yields the edit distance when
    substituted into the formula above. Be sure to indicate which values correspond
    to which parameters. Finally, as a side note, note that there are alternative
    formulations of edit distance as a DP problem using different scoring matrices.
    For this problem, please restrict your consideration to the formulation above.
    """
    # First look at the edit distance equestion '|x| + |y| - score(x,y)' that defines
    # the relationship between the lengths of the strings and the corresponding
    # similarity score, which is the score returned by global alignment of the two
    # strings using a scoring matrix built in the same manner (using the same function)
    # as the DNA sequences we've been evaluating.
    
    # Two strings "abcd" and "abcd", exactly like, should evaluate to an edit dist
    # of zero, since no changes need to be made; score("abcd", "abcd") = 8 in
    # this case since the length of each string is 4, and edit distance = 4 + 4 - 8,
    # which is zero. This means that the global alignment of the two strings must
    # return a score of 8 given the scoring matrix. The best global alignment is
    # simple "abcd" and "abcd", so each matching pair should add +2 to the
    # computed score. DIAG_SCORE = 2 works for this case.
    
    # Look at "abc" and "abd", which require only one substitution. The edit dist
    # equation should look like: 3 + 3 - score(x,y) = 1, so score(x,y) must return
    # 5. Since the first two elements are alike, the score up to element 3 is +2 + 2,
    # or 4. The score for two dissimilar, non-dash (which here correspond to
    # a needed deletion) elements should be +1. OFF_DIAG_SCORE = 1, then.
    
    # Look at "abc" and "abcd", which require one deletion (or insertion, really).
    # The edit dist = 3 + 4 - score(x,y) = 1, so score(x,y) must return 6. Since
    # the first three elements accumulate a score of 6, the final -:d comparison
    # must add nothing to the score. Therefore, DASH_SCORE = 0.
    
    # Look at "acee" and "abcdef". Using the aforementioned scores, this alignment
    # should return a score of +2 (a:a) + 0 (-:b) + 2 (c:c) + 1 (e:d) + 2 (e:e) +
    # 0 (-:f), which equals 7. The edit dist then is 4 + 6 - 7 = 3. This corresponds
    # to modifying the first string by inserting a "b", replacing the first "e" with a
    # "d", and then inserting an "f" at the end. The scores seem to be accurate.
    
    answer = "diag_score = 2" + "\n"
    answer += "off_diag_score = 1" + "\n"
    answer += "dash_score = 0"
    
    print "Question 407 Answer:"
    print answer
    print "-"*50
    print "\n"
    
app_407()

##=================================================================

def app_408():
    """
    QUESTION 8
    
    In practice, edit distance is a useful tool in applications such as spelling
    correction and plagiarism detection when determining whether two strings are
    similar/dissimilar is important. For this final question, we will implement a 
    simple spelling correction function that uses edit distance to determine whether
    a given string is the misspelling of a word.
    
    To begin, load this list 
    (http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt)
    of 79339 words. Then, write a function check_spelling(checked_word, dist, word_list)
    that iterates through word_list and returns the set of all words that are within edit
    distance dist of the string checked_word.
    
    Use your function check_spelling to compute the set of words within an edit
    distance of one from the string "humble" and the set of words within an edit
    distance of two from the string "firefly". Note this is not "fruitfly". Enter these
    two sets of words in the box below. As a quick check, both sets should include
    eleven words.
    """
    # Load the list of 79339 words.
    WORDS = read_words(WORD_LIST_URL)
    
    # Write the check_spelling function. Remember that edit dist = len(x) + len(y) -
    # global alignment of x and y. Each call to global alignment requires a scoring
    # matrix, which is the same each time (for the same alphabet), and an alignment
    # matrix. First the function must build the scoring matrix. Then it must iterate
    # through the word list to find matches. Words that fit the edit dist equation
    # with their returned global alignment score will be added to a words_found
    # list, which is then returned.
    
    def check_spelling(checked_word, dist, word_list):
        """
        Returns all words in word_list that are evalute to edit distance
        dist from checked_word.
        """
        # Initialize alphabet, scores, and build scoring matrix.
        alphabet = set([chr(ord("a") + idx) for idx in range(26)])
        diag_score, off_diag_score, dash_score = 2, 1, 0
        score_matrix = build_scoring_matrix(alphabet, diag_score, off_diag_score, \
                                            dash_score)
        
        # Initialize returned list of words and length variable for checked_word.
        words_found = []
        len_x = len(checked_word)
        
        # Iterate through each word in word_list to find all that match.
        for word in word_list:
            len_y = len(word)
            align_matrix = compute_alignment_matrix(checked_word, word, score_matrix, \
                                                    True)
            score = compute_global_alignment(checked_word, word, score_matrix, \
                                            align_matrix)[0]
            # "Within" edit distance means less than or equal to. I made an error here
            # in the first attempt (== instead of <=).
            if len_x + len_y - score <= dist:
                words_found.append(word)
                
        return words_found
        
    # Use check_spelling to compute the set of words within an edit dist of one
    # from the string "humble" and the set of words within edit dist of two from
    # the string "firefly".
    
    humble_words = check_spelling("humble", 1, WORDS)
    firefly_words = check_spelling("firefly", 2, WORDS)
    
    answer = "Words an edit distance of one from 'humble' in provided words list:"
    answer += "\n" + str(humble_words) + "\n"
    answer += "Words an edit distance of two from 'firefly' in provided words list:"
    answer += "\n" + str(firefly_words)
    
    print "Question 408 Answer:"
    print answer
    print "-"*50
    print "\n"
    
app_408()   

##=================================================================

def app_409():
    """
    QUESTION 9: Extra credit
    
    As you may have noted in question 8, your spelling correction function is not
    particularly responsive. In particular, the function may require several seconds
    to compute a set of possible corrections. This slow performance is due to the
    need to iterate through the entire list of provided words.
    
    Reconsider the formulation of question 8 from a more general point of view
    and design a spelling correction tool that would provide real-time (almost
    instantaneous) correction of spelling errors within an edit distance of two.
    To guide you in the correct direction, we will provide two hints. First, you
    should convert your list of provided words to a set of words to enable a fast
    check for whether a string is a valid word. Second, you do not need to use
    DP to solve this problem. However, you will need to focus on the structure of
    the three editing operations described in question 7.
    
    Please provide an English description of your approach to this problem. You may
    also include pseudocode if you so desire. You do not need to implement your
    algorithm in Python.
    """
    
    answer = '''
I will assume that the provided words have been converted from a list to a set 
(no word is listed more than once). This would be part of the pre-work vs. the
meat of the check_spelling function.

First, check_spelling should check the word list for the existence of checked_word.
This would run at O(n) time, as it is just a linear search. If checked_word is
found, then the function can assume that the typed word is correct and return.

Second, since this implementation of check_spelling is to only consider words within
an edit distance of two, any words in the word list longer than checked_word + 2
can be disregarded. At an edit distance of 2, at most 2 operations can be done
on checked_word, between insert, delete, and substitute. The insert operation
adds one letter, so two operations adds a total of two letters at most. The same
approach could be regarded with the deletion operation, so from the words list,
all words of length less than checked_word - 2 can also be ignored. This allows
a tighter input into the next operations. Though these checks require O(n) time,
as the entire words list must be searched to identify only those within the range
checked_word - 2 <= word <= checked_word + 2, the next operations require
quadratic running time (so a smaller input will greatly save on overall time).

Finally, the alignment matrix and global alignment computations should execute
on the input list from the second part. There are likely much better ways to
increase the speed of this function, but this is one such way to improve it with
just a small modification.
'''
    
    print "Question 409 Answer:"
    print answer
    print "-"*50
    print "\n"
    
app_409()

##=================================================================
##=================================================================