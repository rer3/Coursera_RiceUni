"""
Rice University / Coursera: Principles of Computing (Part 1)
Week 4: Project 4
Yahtzee
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# All import statements needed.

import codeskulptor
codeskulptor.set_timeout(20)

# Below is the link to the description of this assignment.

COURSE = "https://class.coursera.org/principlescomputing1-004/"
DESCRIPTION = COURSE + "wiki/view?page=yahtzee"

#-----------------------------------------------------------------
## Provided template for Yahtzee planner (poc_yahtzee_template). All stubs
## are commented out but the gen_all_sequences function that is needed
## as well as the run_example function used for testing.

# """
# Planner for Yahtzee
# Simplifications:  only allow discard and roll, only score against upper level
# """

# # Used to increase the timeout, if necessary
# import codeskulptor
# codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

# def score(hand):
    # """
    # Compute the maximal score for a Yahtzee hand according to the
    # upper section of the Yahtzee score card.

    # hand: full yahtzee hand

    # Returns an integer score 
    # """
    # return 0

# def expected_value(held_dice, num_die_sides, num_free_dice):
    # """
    # Compute the expected value based on held_dice given that there
    # are num_free_dice to be rolled, each with num_die_sides.

    # held_dice: dice that you will hold
    # num_die_sides: number of sides on each die
    # num_free_dice: number of dice to be rolled

    # Returns a floating point expected value
    # """
    # return 0.0

# def gen_all_holds(hand):
    # """
    # Generate all possible choices of dice from hand to hold.

    # hand: full yahtzee hand

    # Returns a set of tuples, where each tuple is dice to hold
    # """
    # return set([()])

# def strategy(hand, num_die_sides):
    # """
    # Compute the hold that maximizes the expected value when the
    # discarded dice are rolled.

    # hand: full yahtzee hand
    # num_die_sides: number of sides on each die

    # Returns a tuple where the first element is the expected score and
    # the second element is a tuple of the dice to hold
    # """
    # return (0.0, ())

def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
# run_example()

# #import poc_holds_testsuite
# #poc_holds_testsuite.run_suite(gen_all_holds)

#-----------------------------------------------------------------
## Provided test suite (poc_holds_testsuite) for Yahtzee planner.

"""
Test suite for gen_all_holds in "Yahtzee"
"""

#import poc_simpletest

def run_suite(gen_all_holds):
    """
    Some informal testing code for gen_all_holds
    """
    # create a TestSuite object
    suite = TestSuite()
    
    # test gen_all_holds on various inputs
    hand = tuple([])
    suite.run_test(gen_all_holds(hand), set([()]), "Test #1:")

    hand = tuple([2, 4])
    suite.run_test(gen_all_holds(hand), set([(), (2,), (4,), (2, 4)]), "Test #2:")
    
    hand = tuple((3, 3, 3))
    suite.run_test(gen_all_holds(hand), set([(), (3,), (3, 3), (3, 3, 3)]), "Test #4:")

    hand = tuple((1, 2, 2))
    suite.run_test(gen_all_holds(hand), set([(), (1,), (2,), (1, 2), (2, 2), (1, 2, 2)]), "Test #3:")

    hand = tuple([2, 3, 6])
    suite.run_test(gen_all_holds(hand),set([(), (2,), (3,), (6,), (2, 3), (2, 6), (3, 6), (2, 3, 6)]), "Test #5:")

    suite.report_results()

#-----------------------------------------------------------------
## Provided TestSuite class (poc_simpletest).

"""
Lightweight testing class inspired by unittest from Pyunit
https://docs.python.org/2/library/unittest.html
Note that code is designed to be much simpler than unittest
and does NOT replicate unittest functionality
"""

class TestSuite:
    """
    Create a suite of tests similar to unittest
    """
    def __init__(self):
        """
        Creates a test suite object
        """
        self.total_tests = 0
        self.failures = 0
    
    def run_test(self, computed, expected, message = ""):
        """
        Compare computed and expected
        If not equal, print message, computed, expected
        """
        self.total_tests += 1
        if computed != expected:
            msg = message + " Computed: " + str(computed)
            msg += " Expected: " + str(expected)
            print msg
            self.failures += 1
    
    def report_results(self):
        """
        Report back summary of successes and failures
        from run_test()
        """
        msg = "Ran " + str(self.total_tests) + " tests. "
        msg += str(self.failures) + " failures."
        print msg

##=================================================================

DIRECTIONS = '''
Overview
----------
Yahtzee is a dice game with 5 dice where you try to score the most points by matching
certain combinations. You can play the game here (http://www.yahtzee-game.com/). 
In Yahtzee, you get to roll the dice 3 times on each turn. Yadda yadda yadda (I know
the rules). For this project, you will implement a strategy function designed to help 
you choose which dice to hold after your second roll during the first t urn of a game
of Yahtzee. This function will consider all possible choices of dice to hold and
recommend the choice that maximizes the expected value of your score after the
final roll.

To simplify the project, we will consider scores corresponding to the "upper" section
of the scorebard. Boxes in the upper section correspond to numbers on the dice. 
After each turn, you may choose one empty box and enter the sum of the dice you
have with the corresponding number. For example, if you rolled (2,3,3,3,4), you could
score 2 in the Twos box, 9 in the Threes box, or 4 in the Fours box. 

Testing
----------
The provided template includes the function gen_all_sequences from lecture (which
you should not modify) as well as a run_example function that you may modify as you
see fit while developing, debugging, and testing your strategy function. The template
includes the stubs for the four functions that you will need to implement for this
project. Remember to test each function as you write it. We suggest that you build your
own collection of tests using the poc_simpletest module. If you test your code with
five dice, it will be more difficult to understand what is going on. Instead, we
recommend that you should test first with two dice. In particular, you may want to 
work out some examples by hand with two dice and create a small test suite that
checks these examples. 

Submit your code to this OwlTest page: http://codeskulptor.appspot.com/owltest?
urlTests=poc.poc_yahtzee_tests.py&urlPylintConfig=poc.pylint_config.py. Comment
out the call to run_example before submitting. Remember to follow style guidelines.
Submit your final code to the CourseraTest page.

Implementation
----------
Your task is to implement the following four functions which do the following:
* score(hand): This function takes as input a tuple "hand" that represents the
    die values in the given yahtzee hand. Since ordering of the die valuesw in
    Yahtzee hands is unimportant, tuples corresponding to Yahtzee hands will always
    be stored in sorted order to guarantee that each tuple correponds to a unique
    hand. The function score(hand) computes a score for hand as the maximum of
    the possible values for each choice of box in the upper section of the Yahtzee
    scorecard.
* expected_value(held_dice, num_die_sides, num_free_dice): This function computes
    the expected value of the scores for the possible Yahtzee hands that result from
    holding some dice and rolling the remaining free dice. The dice being held are 
    specified by the sorted tuple held_dice. The number of sides and the number of
    dice that are free to be rolled are specified by num_die_sides and num_free_dice,
    respectively. You should use gen_all_sequences to compute all possible rolls for
    the dice being rolled. As an example, in a standard Yahtzee game using 5 dice,
    the length of held_dice plus num_free_dice should always be 5.
* gen_all_holds(hand): This function takes a sorted tuple hand and returns the
    set of all possible sorted tuples formed by discarding a subset of the entries
    in hand. The entries in each of these tuples correspond to the dice that will
    be held. If the tuple hand has the entries (h_0, h_1, ..., h_m-1), the returned
    tuples should have the form (h_i0, h_i1, ...h_ik-1) where 0<= k <= m and the
    integer indices satisfy 0 <= i_0 < i_1 < ... < i_k-1 < m. In the case where
    values in the tuple hand happen to be distinct, the set of tuples returned by
    gen_all_holds will correspond to all possible subsets of hand.
* strategy(hand, num_die_sides): This function takes a sorted tuple hand and computes
    which dice to hold to maximize the expected value of the score of the possible
    hands that result from rolling the remaining free dice (with the specified number
    of sides). The function should return a tuple consisting of this maximal value
    and the choice of dice (specified as a sorted tuple) that should be held to 
    achieve this value. If there are several holds that generate the maximal expected
    value, you may return any of these holds.
    
As you implement these functions, make sure you think about the best order to
write and test them. You may add extra helper functions if so desired, however, the
signature of the functions must match the provided descriptions.

Coding gen_all_holds
----------
Implementing gen_all_holds is one of the main challenges of this project. While its
implementation is short, the actual code requires thought. Since tuples are 
immutable, your algm for computing the required set of tuples cannot directly
delete from the tuple hand. Instead, gen_all_holds should compute the set of all
possible holds in a manner very similar to that of gen_all_sequences. In particular,
your implementation should iterate over the entries of hand and compute all
possible holds for the first k entries in hand using all possible holds for the first
k-1 entries of hand. Use the test suite provided.

Once you have working code, you may wish to extend the score function to
include scores from the lower section of the Yahtzee scorecard (optional). With
this extension, the strategy function gives quite accurate recommendations.
'''

##=================================================================

# First, let's take a look at gen_all_sequences again:

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set
    
# Let's pass it a few simple examples and see what comes out the other end.

# Uncomment to run.
# print "Testing gen_all_sequences(outcomes, length)"
# outcomes = [1, 2, 3, 4, 5]
# length = 3
# print gen_all_sequences(outcomes, length)
# set([(1, 1, 2), (1, 1, 3), (1, 1, 1), (1, 1, 4), (1, 1, 5), (2, 1, 5), (2, 1, 4), 
# (2, 1, 3), (2, 1, 2), (2, 1, 1), (5, 4, 3), (5, 4, 2), (5, 4, 1), (5, 4, 5), 
# (5, 4, 4), (3, 5, 4), (3, 5, 5), (3, 5, 1), (3, 5, 2), (3, 5, 3), (2, 2, 4), 
# (2, 2, 5), (2, 2, 1), (2, 2, 2), (2, 2, 3), (4, 2, 4), (4, 2, 5), (4, 2, 2), 
# (4, 2, 3), (4, 2, 1), (1, 4, 5), (1, 4, 4), (1, 4, 3), (1, 4, 2), (1, 4, 1), 
# (4, 4, 1), (4, 4, 2), (4, 4, 3), (4, 4, 4), (4, 4, 5), (5, 2, 5), (5, 2, 4), 
# (5, 2, 1), (5, 2, 3), (5, 2, 2), (1, 2, 1), (1, 2, 3), (1, 2, 2), (1, 2, 5), 
# (1, 2, 4), (5, 5, 2), (5, 5, 3), (5, 5, 1), (5, 5, 4), (5, 5, 5), (3, 2, 3), 
# (3, 2, 2), (3, 2, 1), (3, 2, 5), (3, 2, 4), (2, 5, 3), (2, 5, 2), (2, 5, 1), 
# (2, 5, 5), (2, 5, 4), (3, 1, 1), (3, 1, 2), (3, 1, 3), (3, 1, 4), (3, 1, 5), 
# (1, 3, 1), (1, 3, 2), (1, 3, 3), (1, 3, 4), (1, 3, 5), (1, 5, 1), (1, 5, 2), 
# (1, 5, 3), (1, 5, 4), (1, 5, 5), (2, 3, 1), (2, 3, 2), (2, 3, 3), (2, 3, 4), 
# (2, 3, 5), (2, 4, 1), (2, 4, 2), (2, 4, 3), (2, 4, 4), (2, 4, 5), (3, 3, 1), 
# (3, 3, 2), (3, 3, 3), (3, 3, 4), (3, 3, 5), (3, 4, 1), (3, 4, 2), (3, 4, 3), 
# (3, 4, 4), (3, 4, 5), (4, 1, 1), (4, 1, 2), (4, 1, 3), (4, 1, 4), (4, 1, 5), 
# (4, 3, 1), (4, 3, 2), (4, 3, 3), (4, 3, 4), (4, 3, 5), (4, 5, 1), (4, 5, 2), 
# (4, 5, 3), (4, 5, 4), (4, 5, 5), (5, 1, 1), (5, 1, 2), (5, 1, 3), (5, 1, 4), 
# (5, 1, 5), (5, 3, 1), (5, 3, 2), (5, 3, 3), (5, 3, 4), (5, 3, 5)])

# A set is returned of all 125 sequences that can be made by choosing (repeating)
# elements from outcomes with a total sequence length of length (3, above). 
# The function works by initializing an empty set to be returned. Then it uses
# 3 nested loops to append elements to that set. The first iterates from 0 to
# length - 1. Here, a temp_set is initialized. The second loop iterates over the
# elements in answer_set, which is initially filled with an empty tuple. The third
# loop iterates over each item in outcomes and executes 3 statements: initializes
# new_sequence as a list filled with the partial sequence (at first the empty tuple),
# appends the outcome item to this list, then converts that list with the appended
# item to a tuple and adds it to the temp_set. After the two inner loops have
# iterated over all of the partials in answer_set and all of the items in outcomes,
# respectively, the answer_set is assigned to the temp_set. The next iteration
# in the outermost loop begins. At the very end, the answer_set is returned, which
# should now have all of the possible sequences (unsorted). Note that (1,1,4) and
# (4,1,1) are both returned.

# The first function to implement is score(hand). It takes a tuple with die values 
# in a hand (e.g. (2,2,3,4,5)) and computes the maximum of the possible values for
# each choice of box in the upper section of a Yahtzee scorecard, which is just the
# sum of all matching die, from 1 to 6. This function should score the example hand
# as the max of 2+2=4, 3, 4, and 5. The score 5 should be returned.

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    return max(num * hand.count(num) for num in hand)

# Uncomment to run.
# print "Testing score(hand)"
# hands = [(2, 2, 2, 4, 5), (1, 2, 3, 4, 5), (3, 3, 4, 4, 4), (1, 1, 1, 1, 4), 
         # (1, 1, 1, 1, 5), (5, 5, 6, 6, 6)]
# for hand in hands:
    # print score(hand)

# The score function appeared to be successful, provided I understood its aim.

# Next, I will implement expected_value. This function computes expected value of
# the scores for the possible Yahtzee hands resulting from holding some dice
# and rolling the remaining free dice. This function makes use of the
# gen_all_sequences function to compute all possible rolls for the dice
# being rolled. The outcomes and length of that function correspond to the
# num_die_sides and num_free_dices params passed to the expected_value call.

# To calculate expected value, now is a good time to review the practice activity
# on analysis of a dice game. In that example, the gen_all_sequences function
# is used as a baseline on which to build helper functions that compute expected
# value. The template poc_dice_game_template was provided with stubs for the
# helpers. 

# The first helper method is max_repeats(seq) that computes the maximum number
# of times that an outcome is repeated in a sequence. The implementation provided
# by the Rice University team is similar to my score(hand) function:

def max_repeats(seq):
    """
    Compute the maximum number of times that an outcome is
    repeated in a sequence.
    """
    item_count = [seq.count(item) for item in seq]
    return max(item_count)
    
# Instead of a list comprehension, I used a generator expression in my call to max.
# Where I returned the max score of a hand by multiplying the number of occurrences
# by the number itself, the max_repeats function simply returns the number of
# occurrences without factoring in the value of the repeated numbers.
# Using that max_repeats function, the Rice team implemented their own function
# to compute expected value:

def compute_expected_value():
    """
    Function to compute expected value of simple dice game
    """
    all_rolls = gen_all_sequences([1, 2, 3, 4, 5, 6], 3)
    results = [max_repeats(roll) for roll in all_rolls]
    
    expected_value = 0
    for result in results:
        if result == 2:
            expected_value += 10 / 216.0
        elif result == 3:
            result == 3
            expected_value += 200 / 216.0
    return expected_value
    
# Note that all sequences of length 3 were generated for a 6-sided die in that
# implementation. A results var was initialized using a list comprehension exprsn
# that returned for each sequence generated the max_repeats that occurred in it,
# essentially showing how many singles, pairs, and above were generated for all
# generated sequences in that list. The 216.0 number corresponds to the number
# of total sequences generated (or len(all_rolls) if parameters were used in this
# function). The expected_value was initialized to 0 and then a for loop was used
# to iterate over the list of results. If the result == 2 (i.e. that seq had a pair),
# then expected value was incremented by 10 / 216.0, which is taken from the
# word problem (you're paid $10 for every pair and $200 for every triple, but
# keeps your initial bet of $10 if you roll neither). 

# In this project, the expected value corresponds to the score of each roll divided
# by the total number of rolls. Note that the outcomes in the gen_all_sequences
# function is not just the num_die_sides, but the range of 1 to num_die_sides + 1.

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcomes = range(1, num_die_sides + 1)
    rolls = gen_all_sequences(outcomes, num_free_dice)
    return sum([score(held_dice + roll) for roll in rolls]) / float(len(rolls))
    
# print "Testing expected_value"
# all_held_dice = [(1,1), (1,2), (1,1,1), (1,1,2), (2,3,4), (2,3,4,5), (1,1,3,3)]
# for held_dice in all_held_dice:
    # print expected_value(held_dice, 6, (5 - len(held_dice)))
    
# It's difficult to clearly see the expected values and know if they are accurate
# or not, but let's take a look. For (1,1), expected value was 6. I can assume
# that this corresponds to a roll of a 6 and holding onto that. In fact, 6 is the 
# EXPVAL for the next, (1,2). The next two are 5, the (2,3,4) is 6.8, the next
# one is 6.7, and then (1,1,3,3) is 6.5. Let's look at some easier examples.

# print "Testing expected_value"
# all_held_dice = [(1,1,1,1), (2,2,2,2), (3,3,3,3), (4,4,4,4), (5,5,5,5), (6,6,6,6), 
                 # (1,2,3,4,5)]
# for held_dice in all_held_dice:
    # print expected_value(held_dice, 6, (5 - len(held_dice)))
    
# The EXPVALs were 4.7, 8.3, 12.5, 16.7, 20.8, 25, and 5, respectively. If I were
# to keep the four of a kind, that should be 4, 8, 12, 16, 20, and 24. That's close.
# That last hand where I don't have free dice should return the score of the hand,
# which it did. This looks successful.

# Next I will implement gen_all_holds, which takes a full Yahtzee hand and generates
# all possible holds from it, from 0 free dice to 5, and returns a set of tuples
# where each shows which dice to hold. The restrictions denoted by the tuple hand
# having entries h_0...h_m-1, returned tuples having the form h_i0...h_ik-1, 
# 0 <= k <= m, and integer indices 0 <= i_0 <- i_1 < i_k-1 simply mean, respectively,
# that the hand entries of a hand of length m are indexed from 0 to m-1 (typical
# Python syntax), and that the returned tuple can have a subset size equal to any
# number from 0 to the length of the hand, and the elements in the tuple retain the
# order that they were in while in the hand passed to the function. So, the hand
# (1,1,3,4,5) passed to this function can return anything from () to (1,3,5) to
# (1,1,3,4,5).

# Note that the directions identify gen_all_holds as needing to be implemented
# in a similar manner to gen_all_sequences. In particular, the implementation
# should iterate over the entries of hand and compute all possible holds for the
# first k entries in hand using all possible holds for the first k-1 entries of hand.
# Let's look at gen_all_sequences again:

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set
    
# Again, that iterates over all elems of an answer_set for all possible
# lengths from 0 to length-1, each time appending an item from the outcomes
# to the partial sequence. For gen_all_holds, the outcomes are simply the remaining
# elements of the hand that are not yet a part of the specific sequence being
# generated at a given time. 

# First, I need to initialize a list with only the null set. Then I will iterate
# over each die in the hand, and then at each iteration I will iterate over each
# subset in the list of subsets (which is initialized with the null set). At this
# innermost loop, I will reassign the list of subsets to the current list of subsets
# plus the current subset plus the die. This will in effect add the die to each
# subset, each time increasing the list of subsets so that the next die can be
# added to each of THOSE subsets.

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    subsets = [()]
    for die in hand:
        for subset in subsets:
            subsets = subsets + [tuple(subset) + (die, )]
           
    return set(subsets)
            
# Running gen_all_holds on a hand of (1,2,3,4,4) generated all possible subsets.
# Running the test suite also resulted in zero failures of the 5 tests.

# Uncomment to run
#run_suite(gen_all_holds)

# Finally, I will implement the strategy function. This takes a sorted tuple hand
# and computes which dice to hold to maximize the expected value of the score of
# the possible hands resulting from rolling the remaining free dice. The function
# should return a tuple consisting of the maximal expected value and the choice
# of dice (as a sorted tuple).

# I will first generated all holds and initialize max_val and best_hold
# vars. Then I will iterate over the holds, calculate the expected value of
# each, and update the max value and best hold as appropriate.

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    holds = gen_all_holds(hand)
    max_val = 0
    best_hold = ()
    for hold in holds:
        val = expected_value(hold, num_die_sides, len(hand)-len(hold))
        if max_val < val:
            max_val = val
            best_hold = hold
            
    return (max_val, best_hold)
    
# I will test all functions by running the example.

# Uncomment to run
#run_example()

# The example ran perfectly. Below is an example posted by Ivan in the forum that uses
# list comprehensions.

##=================================================================

## Ivan's implementation:

def gen_all_sequences(outcomes, length):
    ans = set([()])
    for _ in range(length):
        ans = set([seq + tuple([item]) for item in outcomes for seq in ans])
    return ans

def score(hand):
    return max([hand.count(die) * die for die in set(hand)])

def expected_value(held_dice, num_die_sides, num_free_dice):
    roll_enum = gen_all_sequences(range(1, num_die_sides + 1), num_free_dice)
    return sum(score(held_dice + roll) for roll in roll_enum) / float(len(roll_enum))

def gen_all_holds(hand):
    return set(map(tuple, reduce(lambda r, d: r + [l + [d] for l in r], hand, [[]])))

def strategy(hand, num_die_sides):
    return max([(expected_value(hold, num_die_sides, len(hand) - len(hold)), hold) for \
    hold in gen_all_holds(hand)])
    
## Compared to mine:

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def score(hand, section):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.
    """
    return max(num * hand.count(num) for num in hand)
    
def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.
    """
    outcomes = range(1, num_die_sides + 1)
    rolls = gen_all_sequences(outcomes, num_free_dice)
    return sum([score(held_dice + roll) for roll in rolls]) / float(len(rolls))
    
def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.
    """
    subsets = [()]
    for die in hand:
        for subset in subsets:
            subsets = subsets + [tuple(subset) + (die, )]
           
    return set(subsets)
    
def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.
    """
    holds = gen_all_holds(hand)
    max_val = 0
    best_hold = ()
    for hold in holds:
        val = expected_value(hold, num_die_sides, len(hand)-len(hold))
        if max_val < val:
            max_val = val
            best_hold = hold
            
    return (max_val, best_hold)

##=================================================================
##=================================================================