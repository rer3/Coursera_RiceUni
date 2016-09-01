"""
Rice University / Coursera: Principles of Computing (Part 1)
Week 4: Homework 4
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# All import statements needed.

import codeskulptor
import math
codeskulptor.set_timeout(60)

#-----------------------------------------------------------------
## Provided code poc_enumeration with functions to generate all sequences
## where repetition of outcomes is allowed. Calls to run example functions
## removed.

"""
Functions to enumerate sequences of outcomes
Repetition of outcomes is allowed
"""

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans

def run_example1():
    """
    Example of all sequences
    """
    outcomes = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    #outcomes = set(["Red", "Green", "Blue"])
    #outcomes = set(["Sunday", "Mondy", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
    
    length = 2
    seq_outcomes = gen_all_sequences(outcomes, length)
    print "Computed", len(seq_outcomes), "sequences of", str(length), "outcomes"
    print "Sequences were", seq_outcomes

def gen_sorted_sequences(outcomes, length):
    """
    Function that creates all sorted sequences via gen_all_sequences
    """    
    all_sequences = gen_all_sequences(outcomes, length)
    sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    return set(sorted_sequences)

def run_example2():
    """
    Examples of sorted sequences of outcomes
    """
    # example for digits
    outcomes = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    #outcomes = set(["Red", "Green", "Blue"])
    #outcomes = set(["Sunday", "Mondy", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
   
    length = 2
    seq_outcomes = gen_sorted_sequences(outcomes, length)
    print "Computed", len(seq_outcomes), "sorted sequences of", str(length) ,"outcomes"
    print "Sequences were", seq_outcomes

##=================================================================

DIRECTIONS = '''
Combinatorics
----------
In this week's material, we will create enumerations, permutations, and combinations
of items from a set of outcomes. We will then consider sequences of repeated trials
that are modeled by these objects. These problems will form our preparation for this
week's mini-project on Yahtzee.
'''

##=================================================================

def hw_401():
    """
    QUESTION 1: Enumeration
    
    Given the set of outcomes corresponding to a coin flip, {Heads,Tails}, how
    many sequences of outcomes of length five (repetition allowed) are possible?
    Enter your answer in the box below.
    """
    # Recall that, when repetition is allowed, the number of sequences of a set
    # of outcomes for a given length = num_outcomes ** length_sequence. 
    # Back in Intro to Logic, I learned this as contributions ** slots. 
    
    answer = 2**5
    # 32
    
    print "Question 401 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_401()

##=================================================================

def hw_402():
    """
    QUESTION 2
    
    How many sequences of length four can be formed by choosing the first two
    elements in the sequences from a set of outcomes of size x and the last two
    elements in the sequences from a set of outcomes of size y? In this case,
    repeated outcomes are allowed. Enter a math expression in x and y for the
    number of possible sequences of outcomes.
    """
    # Remember, contributions ** slots = num possible seqs when repetition is allowed.
    # For both x and y length outcome sets, two elements are being chosen, with the
    # num of sequences equal to x**2 and y**2, respectively. For each sequence
    # of x pairs, you can match it up with all of the y pair sequences--so you
    # must multiply the two expressions in order to final total number of possible
    # sequences of outcomes.
    
    answer = "x**2 * y**2"
    
    print "Question 402 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_402()

##=================================================================

def hw_403():
    """
    QUESTION 3: Probability for sequences of trials
    
    Consider a sequence of trials in which a fair four-sided die (with faces numbered
    1-4) is rolled twice. What is the expected value of the product of the two die
    rolls? Enter the answer as a floating point number below.
    """
    # Remember that there are 16 possible pairs of die values: 4 faces x 4 faces.
    # Calculate EV by multiplying 1/16 by each product that can be multiplied:
    # 1, 2, 3, 4, 2, 4, 6, 8, 3, 6, 9, 12, 4, 8, 12, 16.
    
    ratio_1 = float(1) / 16
    ratio_2 = float(2) / 16
    ratio_3 = float(3) / 16
    
    answer = ratio_1*1 + ratio_2*2 + ratio_2*3 + ratio_3*4 + ratio_2*6 + ratio_2*8 + \
             ratio_1*9 + ratio_2*12 + ratio_1*16
    # 6.25
             
    print "Question 403 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_403()

##=================================================================

def hw_404():
    """
    QUESTION 4
    
    Given a trial in which a decimal digit is selected from the list ["0", "1", "2",
    "3", "4", "5", "6", "7", "8", "9"] with equal probability 0.1, consider a 
    five-digit string created by a sequence of such trials (leading zeros and 
    repeated digits are allowed). What is the probability that this five-digit
    string consists of five consecutive digits in either ascending or descending
    order (e.g. "34567" or "43210")? Enter your answer as a floating point
    number with at least four significant digits of precision.
    """
    # The total number of permutations = 10 ** 5 = 100000 possible sequences of
    # outcomes. The number of outcomes with consecutive digits are: 0-4, 1-5, 2-6,
    # 3-7, 4-8, 5-9, and the same 6 sequences but in reverse order. So, out of 1000
    # permutations, 6 are possible that meet the consecutive-sequence criteria.
    
    # This can also be computed by first determining the probability of each possible
    # sequence. The probabilities are multiplied by one another, so a sequence of
    # length 5 - .1 * .1 * .1 * .1 * .1 = 0.00001. Since there are 12 sequences
    # with consecutive digits, the probability of one of those occurring is just
    # 0.00001 * 12 = 0.0001200. 
    
    #answer = float(12) / 100000
    
    # Note that the answer computed here disregards trailing zeros, and the question
    # asks for four sig figs. The answer must be returned as string so that the 
    # trailing zeros are included.
    
    answer = "0.0001200"
    
    print "Question 404 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_404()

##=================================================================

def hw_405():
    """
    QUESTION 5: Permutations
    
    Consider a trial in which five digit strings are formed as permutations of the
    digits ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]. (In this case, 
    repetition of digits is not allowed). If the probability of each permutation is
    the same, what is the probability that this five digit string consists of
    consecutive digits in either ascending or descending order? Enter your answer
    as a floating point number with at least four sig figs.
    """
    # Recall that since permutations do not repeat contributions, the expression
    # for evaluating the number of permutations is m! / (m-n)! where m = size
    # of outcomes and n = length of a permutation to be returned. 
    
    # Here, m = 10 and n = 5. Total permutations = 10! / (10 - 5)!. Again, there
    # are 12 possible permutations out of the total number of permutations where
    # digits are in consecutive order.
    
    answer = float(12) / (math.factorial(10) / math.factorial(10 - 5))
    # 0.000396825396825
    
    print "Question 405 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_405()

##=================================================================

def hw_406():
    """
    QUESTION 6
    
    In this week's lecture, we discussed an iterative approach to generating all 
    sequences of outcomes where repeated outcomes were allowed (above in shared
    area). Starting from this template (below, in the code), implement a function
    gen_permutations(outcomes, num_trials) that takes a list of outcomes and a number
    of trials and returns a list of all possible permutations of length num_trials from
    this set of outcomes. 
    
    Hint: gen_permutations can be built from gen_all_sequences by adding a single 
    if statement that prevents repeated outcomes. When you believe that your code
    works correctly, select the answer printed at the bottom of the console.
    
    Option 1:
    ['e', 'b', 'd', 'c']
    
    Option 2
    ['b', 'e', 'c', 'd']
    
    Option 3
    ['f', 'a', 'b', 'c']
    
    Option 4
    ['a', 'f', 'b', 'e']
    """
    # The provided template is below (poc_permutations_template).
    
    def gen_permutations(outcomes, num_trials):
        """
        Iterative function that generates set of permutations of
        outcomes of length num_trials
        No repeated outcomes allowed
        """
        ans = set([()])
        for dummy_idx in range(num_trials):
            temp = set()
            for seq in ans:
                for item in outcomes:
                    if item not in seq:
                        new_seq = list(seq)
                        new_seq.append(item)
                        temp.add(tuple(new_seq))
            ans = temp
        return ans
    
    # Much of the template has been trimmed (most of it, actually, several parts).
    # This question requires me to implement gen_permutations. I just cut and
    # pasted gen_all_sequences and added a conditional to the innermost for loop
    # at the top that checks the item in outcomes against the sequence being
    # iterated over in the set of sequences "ans" and if it does not exist yet,
    # it is appended to the temp list new_seq, which is then ultimately added to
    # the set "ans". 
    
    # I will run my own tests below.
    
    outcomes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    length = 3
    perms = gen_permutations(outcomes, length)
    print "Num permutations:", len(perms)
    print "The expected number is:", math.factorial(10) / math.factorial(10 - 3)
    print "-"*10
    
    # The function generated the correct number of permutations. Now I will paste the
    # tests corresponding to this homework question from the provided template.
    
    outcome = set(["a", "b", "c", "d", "e", "f"])
    permutations = gen_permutations(outcome, 4)
    permutation_list = list(permutations)
    permutation_list.sort()
    print
    print "Answer is", permutation_list[100]
    # ('b', 'e', 'c', 'd')
    print "-"*10
    
    answer = permutation_list[100]
    
    print "Question 406 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_406()

##=================================================================

def hw_407():
    """
    QUESTION 7: Subsets
    
    A set S is a subset of another set T (mathematically denoted as S -is_sub- T) if
    every element x in S (mathematically denoted as x -is_elem- S) is also a member
    of T. Which of the following sets are subsets of the set {1,2}? (Choose all).
    
    Option 1
    {2}
    
    Option 2
    {1,2}
    
    Option 3
    {}
    
    Option 4
    {1,2,3,4}
    
    Option 5
    {3,4}
    """
    # Option 4 is out because it includes elements 3 and 4 which are not in {1,2}.
    # Option 5 is out because neither element is a member of {1,2}.
    # Options 1-3 are correct. Note that 3 is correct because the null set is a subset
    # of every set.
    
    answer = "{2}" + "\n"
    answer += "{1,2}" + "\n"
    answer += "{}"
    
    print "Question 407 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_407()

##=================================================================

def hw_408():
    """
    QUESTION 8
    
    If the set T has n members, how many distinct sets S are subsets of T? You may
    want to figure out the answer for a few specific values of n first. Enter the
    answer below as a math expression in n.
    """
    # I can manually walk through this with ease. At n = 0 members, there is only
    # 1 distinct set, the null set. At n = 1, there are 2 sets, null and the identity
    # (the set itself). At n = 2, there are 4 distinct subsets: {}, {elem1}, {elem2},
    # and {elem1, elem2}. At n = 3, there are subsets: {}, {e1}, {e2}, {e3}, 
    # {e1, e2}, {e1, e3}, {e2, e3}, {e1, e2, e3}, so 8 total subsets. To summarize,
    # the n:num_subsets pairs are 0:1, 1:2, 2:4, 3:8. It appears that the number of
    # subsets is dependent on n by the expression 2**n. 
    
    answer = "2**n"
    
    print "Question 408 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_408()

##=================================================================

def hw_409():
    """
    QUESTION 9: Combinations
    
    Given a standard 52 card deck of playing cards, what is the probability of being
    dealt a five card hand where all five cards are of the same suit?
    
    Hint: Use the formula for combinations to compute the number of possible five
    card hands when the choice of cards is restricted to a single suit vs. when the
    choice of cards is unrestricted. 
    
    Compute your answer in Python using math.factorial and enter the answer below
    as a floating point number with at least four sig figs.
    """
    # The formula for combinations is below. It uses the gen_permutations
    # function, sorts each sequence in the returned set of perms, and returns
    # a set of that set to remove all repeated tuples (now that the sequences
    # of each are sorted, there will be many duplciates).
    
    # def gen_permutations(outcomes, num_trials):
        # """
        # Iterative function that generates set of permutations of
        # outcomes of length num_trials
        # No repeated outcomes allowed
        # """
        # ans = set([()])
        # for dummy_idx in range(num_trials):
            # temp = set()
            # for seq in ans:
                # for item in outcomes:
                    # if item not in seq:
                        # new_seq = list(seq)
                        # new_seq.append(item)
                        # temp.add(tuple(new_seq))
            # ans = temp
        # return ans

    # def gen_combinations(outcomes, length):
        # """
        # Function to generate combinations.
        # """
        # all_perms = gen_permutations(outcomes, length)
        # sorted_seq = [tuple(sorted(sequence)) for sequence in all_perms]
        # return set(sorted_seq)
        
    # First compute all combinations possible for a 5-card hand from the deck.
    # Verify the length of these combinations using the formula from the math notes
    # for permutations and combinations. Recall that the number of possible combos
    # of length n from an outcome list of length m = m! / ((m - n)! * n!).
    
    # print "Expected length:", math.factorial(52) / (math.factorial(52 - 5) * \
                              # math.factorial(5))
    
    # Build a deck of cards (this could probably be done without building an actual
    # deck, but I want to try this out). Ranks will be 1-13 with no faces.
    
    # SUITS = ["S", "C", "H", "D"]
    # RANKS = [num for num in range(1,14)]
    # deck = []
    # for suit in SUITS:
        # for rank in RANKS:
            # deck.append(suit + str(rank))
            
    # card_combos = gen_combinations(deck, 5)
    # print "Length of card combinations:", len(card_combos)
    
    ## The gen_combinations function times out! 
    
    # Since the function takes a very long time to compute in CodeSkulptor, I will
    # instead use the factorial expression to compute the number of combinations
    # of 5 cards of the same suit and divide that by the number of total combinations.
    
    suit_combos = math.factorial(13) / (math.factorial(13 - 5) * math.factorial(5))
    all_combos = math.factorial(52) / (math.factorial(52 - 5) * math.factorial(5))

    ##################################################
    ## INCORRECT: Remember to account for the fact that there are four
    ## possible suits.
    ##
    ## answer = float(suit_combos) / all_combos
    ## # 0.000495198079232
    ##################################################

    # My answer only computed the probability for a single suit of 13 cards. This
    # computation assumed that 13 cards are one suit, and the other 39 cards
    # do not count toward such a hand (a flush). Since there are four suits, I
    # can just multiply my previous answer by 4 to get the correct answer.
    
    answer = 4 * float(suit_combos) / all_combos
    # 0.00198079231693
    
    print "Question 409 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_409()

##=================================================================

def hw_410():
    """
    QUESTION 10
    
    Pascal's triangle (https://en.wikipedia.org/wiki/Pascal%27s_triangle) is a 
    triangular array of numbers in which the entry on one row of the triangle
    corresponds to the sum of the two entries directly above the entry. This
    program (provided, below) prints out the first few rows of Pascal's triangle.
    
    Enter a math expression in m and n using factorial that represents the value
    of the nth entry of the mth row of Pascal's triangle (both te row numbers and
    entry numbers are indexed starting at zero).
    """
    # The provided code is below. Some snippets have been removed.
    
    TRIANGLE_HEIGHT = 5

    def next_line(current_line):
        """
        Given a line in Pascal's triangle, generate the following line
        """
        ans = [1]
        
        for idx in range(len(current_line) - 1):
            ans.append(current_line[idx] + current_line[idx + 1])
        
        ans.append(1)
        
        return ans

    def run_example():
        # code to print out Pascal's triangle
        pascal_line = [1]   # row zero
        print pascal_line
        
        for dummy_idx in range(TRIANGLE_HEIGHT - 1):
            pascal_line = next_line(pascal_line)
            print pascal_line
            
    run_example()
    print "-"*10
    
    # The example above prints to the console the following:
    # [1]
    # [1, 1]
    # [1, 2, 1]
    # [1, 3, 3, 1]
    # [1, 4, 6, 4, 1]
    
    # Note how the function clever creates each row of the triangle. run_example()
    # initializes the first line to be [1] (row 0). Then it executes a for loop
    # height - 1 times, each time updating the pascal_line by passing the previous
    # line to the next_line() function, then the line is printed.
    
    # The next_line(current_line) function takes a line, initializes the answer
    # to be [1] (which is always the first element of a row in the triangle),
    # and then executes a for loop that runs len(current_line) - 1 times (to fill
    # in the meat of the line), then appends another 1 to the answer (as each
    # row ends with a 1 as well). The for loop appends to the initialized answer
    # (without the final 1) a series of numbers that are computed by adding
    # pairs from the current_line: line[0] + line[1], line[1] + line[2], etc. 
    # Looking at the triangle, you can see how each row adds elements together
    # to create the elements in the subsequent row. 
    
    # Remember that m = height/num rows, and n = width/num cols. Let's look at
    # a few values from the triangle to see if any patterns emerge (keeping in mind
    # that the directions for question 10 recommend using the factorial operation). 
    # At m=0/n=0:val=1. 
    # At m=1/n=0:val=1, m=1/n=1:val=1.
    # At m=2/n=0:val=1, m=2/n=1:val=2, m=2/n=2:val=1. 
    # At m=3/n=0:val=1, m=3/n=1:val=3, m=3/n=2:val=3, m=3/n=3:val=1.
    # At m=4/n=0:val=1, m=4/n=1:val=4, m=4/n=2:val=6, m=4/n=3:val=4, m=4/n=4:val=1.
    
    # I admit, I looked this up. I started to run through arbitrary forms, but it
    # became very difficult and tedious. The answer is m! / (n! * (m-n)!). 
    # The homework notes "Correct. The nth entry of the mth row is the number of
    # combinations of m items chosen n at a time." But what does this mean?
    # Recall that the number of possible combos of length n from an outcome list of 
    # length m = m! / ((m - n)! * n!).
    
    # This translates for [4][2] = 6, where m=4/n=2, that 6 is the number of 
    # combinations of 4 items chosen 2 at a time. At [4][1] = 4, this is the number
    # of combinations of 4 items chosen 1 at a time. At [4][3] = 4, this is the
    # number of combos of 4 items chosen 3 at a time. Note that when m=4, 
    # the number of combos is the same when n=1 or n=3. Is this true?
    
    # m=4/n=1: 4! / (1! * 3!) = 24 / 6 = 4.
    # m=4/n=3: 4! / (3! * 1!) = 24 / 6 = 4.
    # Eureka! The terms swap at col 3, so the number of combos is the same.
    # For outcomes = [1,2,3,4], at n = 1, you have [1], [2], [3], and [4].
    # For same outcomes, at n = 3, you have [1,2,3], [2,3,4], [1,2,4], and [1,3,4].
    
    # This all works out, but how does this relate to the mechanism behind Pascal's 
    # triangle? Is this as simple as identifying the sequences of numbers stemming
    # from the tip of the triangle, realizing that it's the pattern corresponding to
    # computing the number of combinations, and seeing how those numbers are
    # ordered within the triangle, specifically at which row and col? Or do I need
    # to learn more about what Pascal's triangle represents? Probably all of the above.
    
    answer = "m! / (n! * (m - n)!)"
    
    print "Question 410 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_410()

##=================================================================
##=================================================================