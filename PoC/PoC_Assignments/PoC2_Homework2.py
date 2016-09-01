"""
Rice University / Coursera: Principles of Computing (Part 2)
Week 2: Homework 2
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# All import statements needed.

import math
import random

#-----------------------------------------------------------------
## Provided code for question 1.

"""
Recursion according to the "Cat in the Hat"
"""

#--------------------------------------------------
# Initialize global counter
COUNT = 0
#--------------------------------------------------

def get_next_cat(current_cat):
    """
    Helper function to get next cat
    """
    if current_cat == "Cat in the Hat":
        return "Little Cat A"
    elif current_cat != "Little Cat Z":
        return "Little Cat " + chr(ord(current_cat[-1]) + 1)
    else:
        return "Voom"

def clean_up(helper_cat):
    """
    Recursive function that prints out story
    """
    #--------------------------------------------------
    # Increment global counter
    global COUNT
    COUNT += 1
    #--------------------------------------------------
    
    if helper_cat == "Voom":
        print helper_cat + ": I got this. Mess is all cleaned up!"
    else:
        next_cat = get_next_cat(helper_cat)
        print helper_cat + ": I'll have", next_cat, "clean up!"
        clean_up(next_cat)
        
def run_example():
    clean_up("Cat in the Hat")
    
    #--------------------------------------------------
    # Counter is printed to verify answer to question 1.
    print "COUNT:", COUNT
    #--------------------------------------------------

# Uncomment to run example.
#run_example()

#-----------------------------------------------------------------
## Provided code...

#-----------------------------------------------------------------
## Provided code...

#-----------------------------------------------------------------
## Provided code...

#-----------------------------------------------------------------
## Provided code...

#-----------------------------------------------------------------
## Provided code...

##=================================================================

def hw_201():
    """
    QUESTION 1
    
    Examine the behavior of the recursive program provided (above) that models
    the story of the "Cat in the Hat" by Dr. Seuss. 
    
    How many calls to the function clean_up are made by the program?
    """
    
    run_example()
    print "-"*10
    
    # Running the code will print out 28 lines, so it appears that the answer is
    # there are 28 calls to clean_up, since the conditional always prints one 
    # statement, which terminates if the conditional returns True (and one
    # last statement is printed). I added a counter to verify that this is correct.
    
    answer = 28
    
    print "Question 201 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_201()

##=================================================================

def hw_202():
    """
    QUESTION 2
    
    Consider the following Python function:
    def add_up(n):
        if n == 0:
            return 0
        else:
            return n + add_up(n - 1)
    
    If n is non-negative integer, enter a math expression in n for the value
    returned by add_up(n).
    """
    # First write out this function. Then run the function on a series of n values
    # and analyze the returned value for each n. Use print statements to
    # generate the data.
    
    def add_up(n):
        """
        Return sum of all integers from 0 to n.
        """
        if n == 0:
            return 0
        else:
            return n + add_up(n - 1)
            
    # Look at n = 0 to 9.
    for n in range(10):
        result = add_up(n)
        print "For n =", n, "result =", result
    print "-"*10
    
    # The function returns the sum of all integers from 0 to n. The following
    # n: result pairs were returned: 0: 0, 1: 1, 2: 3, 3: 6, 4: 10, 5: 15, etc.
    # This is an established sequenced (n * (n + 1)) / 2.
    
    answer = "n * (n + 1)) / 2"
    
    print "Question 202 Answer:"
    print answer
    print "-"*50
    print "\n"  
    
hw_202()    

##=================================================================

def hw_203():
    """
    QUESTION 3
    
    Consider the following Python function:
    def multiply_up(n):
        if n == 0:
            return 1
        else:
            return n * multiply_up(n - 1)
            
    If n is non-negative integer, enter a math expression in n for the values 
    returned by multiply_up(n).
    """
    # Write out the function and run on n = 0 to 9. Look at print statements to
    # analyze the sequence.
    
    def multiply_up(n):
        """
        Returns product of all integers from 1 to n.
        """
        if n == 0:
            return 1
        else:
            return n * multiply_up(n - 1)
            
    for n in range(10):
        result = multiply_up(n)
        print "For n =", n, "result =", result
    
    print "-"*10
    
    # The n: result pairs returned were: 0: 1, 1: 1, 2: 3, 3: 6, 4: 10, 5: 15, etc.
    # This too is an established sequence. This function is a recursive
    # implementation of factorial. Verify below.
    
    for n in range(10):
        result = math.factorial(n)
        print "For n =", n, "result =", result
    
    print "-----"
    
    answer = "n!"
    
    print "Question 203 Answer:"
    print answer
    print "-"*50
    print "\n"
        
hw_203()

##=================================================================

def hw_204():
    """
    QUESTION 4
    
    Consider this recursive Python function that computes the Fibonacci numbers:
    def fib(num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fib(num - 1) + fib(num - 2)
            
    Let f(n) be the total number of calls to the function fib that are computed
    during the recursive evaluation of fib(n). Which recurrence reflects the number
    of times that fib is called during this evaluation of fib(n)?
    
    You may want to add a global counter to the body of fib that records the
    number of calls for small values of n.
    
    Option 1
    f(0) = 1; f(1) = 1; f(n) = f(n-1) + f(n-2) + 1
    
    Option 2
    f(0) = 1; f(1) = 1; f(n) = 2f(n-1) + 1
    
    Option 3
    f(0) = 0; f(1) = 1; f(n) = f(n-1) + f(n-2)
    
    Option 4
    f(0) = 1; f(1) = 1; f(n) = f(n-1) + 1
    """
    # Options 2 and 4 are obviously wrong, as they do not fit the function fib(n).
    # Option 3 appears to be correct as it fits the recurrence model of the function.
    
    ##################################################
    ## INCORRECT: Note that f(0) should be 1.
    ##
    ## answer = "f(0) = 0; f(1) = 1; f(n) = f(n-1) + f(n-2)
    ##################################################
    
    # Option 3 seems correct since f(0) = 0 and the function returns 0 for n = 0,
    # but intuition is wrong here. The recurrence must reflect the number of times
    # that fib is called, not the sequence itself. The call fib(0) executes once.
    # Therefore, f(0) must equal 1. 
    
    # The explanation for the correct answer states that the number of calls to
    # fib(n) is one plus the number of recursive calls to fib(n-1) and fib(n-2).
    
    answer = "f(0) = 1" + "\n"
    answer += "f(1) = 1" + "\n"
    answer += "f(n) = f(n-1) + f(n-2) + 1"
    
    print "Question 204 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_204()

##=================================================================

# Initialize a global counter for this problem.
COUNT = 0

def hw_205():
    """
    QUESTION 5
    
    The number of recursive calls to fib in the previous problem grows quite 
    quickly. The issue is that fib fails to "remember" the values computed during
    previous recursive calls. One technique for avoiding the issue is memoization,
    a technique in which the values computed by calls to fib are stored in an aux
    dictionary for later use.
    
    The Python function below uses memoization to efficiently compute the
    Fibonacci numbers:
    def memoized_fib(num, memo_dict):
        if num in memo_dict:
            return memo_dict[num]
        else:
            sum1 = memoized_fib(num - 1, memo_dict)
            sum2 = memoized_fib(num - 2, memo_dict)
            memo_dict[num] = sum1 + sum2
            return sum1 + sum2
            
    If n > 0, how many calls to memoized_fib are computed during the evaluation
    of the expression memoized_fib(n, {0:0, 1:1})? Enter the answer as a math
    expression in n below. You may want to add a counter.
    """
    # A counter is added as a global variable to easily solve this problem. The
    # function is written below and makes use of it. This function will be called
    # on n = 1 to 9, and the change in COUNT will be printed.
    
    def memoized_fib(num, memo_dict):
        """
        Return nth Fibonacci number.
        """
        #--------------------------------------------------
        # Counter added.
        global COUNT
        #--------------------------------------------------
        
        COUNT += 1
        if num in memo_dict:
            return memo_dict[num]
        else:
            sum1 = memoized_fib(num - 1, memo_dict)
            sum2 = memoized_fib(num - 2, memo_dict)
            memo_dict[num] = sum1 + sum2
            return sum1 + sum2
            
    for num in range(1, 10):
        start = COUNT
        memoized_fib(num, {0:0, 1:1})
        end = COUNT
        total = end - start
        print "For num =", num, "COUNT increased by", total, "from", start, "to", end
    
    print "-"*10
    
    # The num: total pairs returned were: 1: 1, 2: 3, 3: 5, 4: 7, 5: 9, 6: 11, etc.
    # The change appears to be 2*n - 1. 
    
    answer = "(2 * n) - 1"
    
    print "Question 205 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_205()

##=================================================================

def hw_206():
    """
    QUESTION 6
    
    In a previous homework, we implemented an iterative method for generating
    permutations of a set of outcomes. Permutations can also be generated
    recursively.
    
    Given a list outcomes of length n, we can perform the following recursive 
    computation to generate the set of all permutations of length n:
    
    * Compute the set of perms rest_permutations for the list outcomes[1:] of
        length n - 1.
    * For each perm in rest_permutations, insert outcome[0] at each possible
        position of perm to create permutations of length n.
    * Collect all of these perms of length n in a set and return that set.
    
    If p(n) is the number of perms returned by this method, what recurrence below
    captures the behavior of p(n)?
    
    Option 1
    p(0) = 1; p(n) = n*p(n-1)
    
    Option 2
    p(0) = 1; p(n) = 2*p(n-1)
    
    Option 3
    p(0) = 0; p(n) = p(n-1) + n
    
    Option 4
    p(0) = 1; p(n) = 2p(n/2) + n
    """
    # First try to write the code described above. Then look at the number of
    # permutations vs. the length of the outcomes.
    
    def gen_perms(outcomes, length):
        """
        Generate all permutations of a specified length from a list of outcomes.
        
        Actually returns ALL permutations of all lengths 0 to length.
        """
        if length == 0:
            return set([()])
            
        permutations = set([()])
        drop = outcomes[0]
        rest_permutations = gen_perms(outcomes[1:], length - 1)
        for perm in rest_permutations:
            store = list(perm)
            store.append(drop)
            permutations.add(tuple(store))
        permutations.update(rest_permutations)
                
        return permutations
        
    # Test the gen_perms function on a list of outcomes of length = 0 to 5.
    # Print the results for analysis.
    
    # outcome_list = range(10)
    # for length in range(6):
        # outcomes = [random.choice(outcome_list) for dummy_idx in range(length)]
        # print "Outcomes:", outcomes
        # perms = gen_perms(outcomes, length)
        # print "Permutations returned:"
        # for item in perms:
            # print item
        # print "For length", length, "returned", len(perms), "permutations"
        # print "-----"
    
    # Since the outcomes run in this function randomly chose n digits from 0-9,
    # there were repeated elements in the outcomes list. The number of perms
    # appeared to almost increase by a factor of 2**n when computing perms of
    # a list of outcomes of size n + 1 (0: 1, 1: 2, 2: 4, 3: 8, etc.). 
    # I will run this again with unique elements and comment out the above code.
    
    outcome_list = range(10)
    for length in range(6):
        outcomes = [outcome_list[idx] for idx in range(length)]
        perms = gen_perms(outcomes, length)
        print "For length", length, "returned", len(perms), "permutations"
        print "-----"
        
    # As expected, the number of permutations doubled (following a power of two
    # sequence) while the lengths increased by 1. I will use this knowledge to 
    # evaluate the 4 options.
    
    # Option 4 is out because I am not halving the length with each recursive call.
    # Option 2 appears to be incorrect, as this function does not simply double
    # the number of permutations each time. 
    # Option 3 appears to be correct as the previous permutation function we
    # implemented returns an empty string when the list of outcomes has len = 0.
    
    ##################################################
    ## INCORRECT: Incorrect. Try Again.
    ##
    ## answer = "p(0) = 0" + "\n" + "p(n) = p(n-1) + n"
    ##################################################
    
    # Option 3, I now see, can be disregarded, as p(0) = 1, not 0. Even when there
    # are no outcomes, there is one permutations: the null set. I think.
    # Option 1 seems to be correct simply by the process of elimination, though
    # there does seem to be a dependency on n in the gen_perms() function that
    # may not be entirely clear to me. Plugging in increasing values of n returns
    # 0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120. This is a factorial sequence. It is now
    # clear that my implementation returns ALL permutations, which is what the
    # question is asking you to do.
    
    # Another look at the description clearly shows that for a given n, you will
    # return n * p(n-1) permutations. 
    
    answer = "p(0) = 1" + "\n" + "p(n) = n*p(n-1)"
    
    print "Question 206 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_206()

##=================================================================

def hw_207():
    """
    QUESTION 7
    
    Using the math notes (https://class.coursera.org/principlescomputing2-004/
    wiki/view?page=recurrences) for recurrences, look up the solution to the
    recurrence from problem #6. Enter the solution to this recurrence as a math
    expression in n below.
    """
    # The solution to the recurrence in question #6 is n*(n+1) / 2.
    
    ##################################################
    ## INCORRECT: Match failed.
    ##
    ## answer = "n*(n+1) / 2"
    ##################################################
    
    # The solution to the recurrence in question #6 is n factorial.
    
    answer = "n!"
    
    print "Question 207 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_207()

##=================================================================

def hw_208():
    """
    QUESTION 8
    
    As part of this week's mini-project, you will implement a function
    merge(list1, list2) that takes two ordered lists and merges the lists into a
    single ordered list that contains all of the elements in either list1 or list2.
    
    The body of merge consists of a while loop that iterates until one of the lists
    list1 and list2 is empty. Each iteration of the loop compares the first elem
    in each list, pops the smaller elem from its containing list and appends this
    elem to the answer. Once one list is exhausted, the entries in the remaining
    list are appended to the answer.
    
    If list1 and list2 are both of length n, which expression below grows at the
    same rate as the running time (i.e. the number of Python statements executed)
    of merge?
    
    Option 1
    n
    
    Option 2
    n*log(n)
    
    Option 3
    n**2
    
    Option 4
    log(n)
    """
    # First let's look at the merge function from Project 2.
    
    def merge(list1, list2):
        """
        Merge two sorted lists.

        Returns a new sorted list containing all of the elements 
        that are in either list1 and list2.

        This function can be iterative.
        """
        merged = []
        copy1, copy2 = list(list1), list(list2)
        while len(copy1) > 0 and len(copy2) > 0:
            if copy1[0] <= copy2[0]:
                merged.append(copy1.pop(0))
            else:
                merged.append(copy2.pop(0))
        if len(copy1) == 0:
            merged.extend(copy2)
        else:
            merged.extend(copy1)
        return merged
        
    # Each iteration of the while loop removes one element from one of the lists.
    # Therefore, the while loop iterates at most 2*n times, where n = length of
    # each list.
    
    answer = "n"
    
    print "Question 208 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_208()

##=================================================================

def hw_209():
    """
    QUESTION 9
    
    Another part of this week's mini-project will be implementing a recursive sorting
    algm known as merge_sort. The basic idea behind it is to split the unordered 
    input list of size n into two unordered sub-lists of approximately size n/2,
    recursively call merge_sort to sort each of these sublists and, finally, use
    merge to merge these two sorted sublists.
    
    If t(n) corresponds to the running time of merge_sort as a function of the input
    list size n, which recurrence captures the behavior of t(n) most accurately?
    
    Option 1
    t(1) = 1; t(n) = t(n/2) + 1
    
    Option 2
    t(1) = 1; t(n) = 2*t(n/2) + 1
    
    Option 3
    t(1) = 1; t(n) = 2*t(n/2) + n
    
    Option 4
    t(1) = 1; t(n) = t(n/2) + n
    """
    # First let's look at the merge_sort function from Project 2.
    
    def merge_sort(list1):
        """
        Sort the elements of list1.

        Return a new sorted list with the same elements as list1.

        This function should be recursive.
        """
        if len(list1) < 2:
            return list1
        left = merge_sort(list1[:len(list1)/2])
        right = merge_sort(list1[len(list1)/2:])
        return merge(left, right)
    
    # Without even looking at this function, the description alone says that the
    # list is divided in half and merge_sort is called on each half. 
    # Options 1 and 4 can be disregarded because of this fact.
    
    # The running time of merge, as shown in question #8, is n. This would be
    # added to the running time of each recursive call.
    # Option 2 is out because there is a +1 after the recursive calls.
    # Option 3 is correct as it fulfills the aforementioned conditions.
    
    answer = "t(1) = 1" + "\n" + "t(n) = 2*t(n/2) + n"
    
    print "Question 209 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_209()

##=================================================================

def hw_210():
    """
    QUESTION 10
    
    Using the math notes (https://class.coursera.org/principlescomputing2-004/
    wiki/view?page=recurrences) for recurrences, look up the solution to the
    recurrence from problem #9. Enter the solution to this recurrence as a math
    expression in n below.
    """
    # The solution to the recurrence in question #9 is n*log(n).
    
    answer = "n*log(n)"
    
    print "Question 210 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_210()

##=================================================================
##=================================================================