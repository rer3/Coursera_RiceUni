"""
Rice University / Coursera: Intro to Interactive Programming in Python (Part 2)
Week 2: Homework 6b
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

##=================================================================

def hw_601():
    """
    QUESTION 1
    
    What is the pos of the center of the top-left card (Ace of clubs) in the tiled
    image (http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png)
    discussed in the "Tiled Images" video? Remember that each card in this tiled
    image has size 73 x 98 pixels. 
    
    Option 1
    (0,0)
    
    Option 2
    (73, 98)
    
    Option 3
    (5 * 73 + 36.5, 1 * 98 + 49)
    
    Option 4
    (36.5, 49)
    """
    
    answer = (36.5, 49)
    
    print "Question 601 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_601()

##=================================================================

def hw_602():
    """
    QUESTION 2
    
    What is the pos of the center of the bottom right card (King of Diamonds) in
    the same image? Enter the two numbers, separated by a space.
    """
    
    answer = (36.5 + 12 * 73, 49 + 3 * 98)
    
    print "Question 602 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_602()

##=================================================================

def hw_603():
    """
    QUESTION 3
    
    When using Dropbox to store images for use with CodeSkulptor, what should the
    www portion of the DropBox URL be replaced by?
    
    Options: dl, www, gif, html, jpg.
    """
    
    answer = "dl"
    
    print "Question 603 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_603()

##=================================================================

def hw_604():
    """
    QUESTION 4
    
    Within the __init__ method, the new object should be returned with what code?
    
    Option 1
    No return statement is needed in __init__.
    
    Option 2
    return whatever_the_object_is_named (Use the appropriate variable name)
    
    Option 3
    return self
    
    Option 4
    return
    """
    
    answer = "No return statement is needed in __init__."
    
    print "Question 604 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_604()

##=================================================================

def hw_605():
    """
    QUESTION 5
    
    One way of understanding code is to think about other code that accomplishes
    the same thing, i.e. given the same starting values, it returns and/or mutates the
    same values. This following defines one way to concat multiple lists. For example,
    list_extend_many([[1,2], [3], [4,5,6], [7]]) returns [1,2,3,4,5,6,7] and doesn't
    mutate anything.
    
    def list_extend_many(lists):
        '''
        Returns a list that is the concatenation of all the lists in the given list
        of lists.
        '''
        result = []
        for l in lists:
            results.extend(l)
        return result
        
    Which of the following definitions are equivalent? (Choose all).
    
    Option 1
    def list_extend_many(lists):
        result = []
        i = 0
        while i < len(lists): 
            result += lists[i]
            i += 1
        return result
        
    Option 2
    def list_extend_many(lists):
        result = []
        i = 0
        while i <= len(lists): 
            result.extend(lists[i])
            i += 1
        return result
    
    Option 3
    def list_extend_many(lists):
        result = []
        i = 0
        while i < len(lists): 
            i += 1
            result.extend(lists[i])
        return result
        
    Option 4
    def list_extend_many(lists):
        result = []
        for i in range(len(lists)):
            result.extend(lists[i])
        return result
    """
    
    answer = '''
def list_extend_many(lists):
    result = []
    i = 0
    while i < len(lists): 
        result += lists[i]
        i += 1
    return result
    
def list_extend_many(lists):
    result = []
    for i in range(len(lists)):
        result.extend(lists[i])
    return result
'''
    
    print "Question 605 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_605()

##=================================================================

def hw_606():
    """
    QUESTION 6
    
    Which of the following programs would never end if it weren't for CodeSkulptor's
    timeout? Assume no break or return statement is used in the elided loop bodies.
    You might want to add a print statement to each loop to better understand the
    behavior.
    
    Option 1
    n = 1000
    while n > 0:
        ... # Assume this doesn't modify n
        n -= 1
    
    Option 2
    n = 1
    while n > 0:
        ... # Assume this doesn't modify n
        n += 1
    
    Option 3
    n = 127834876
    while n >= 0:
        ... # Assume this doesn't modify n
        n //= 2
    
    Option 4
    my_list = ...
    for x in my_list:
        ... # Assume this doesn't mutate my_list
    """

    answer = '''
n = 1
while n > 0:
    ... # Assume this doesn't modify n
    n += 1  
    
n = 127834876
while n >= 0:
    ... # Assume this doesn't modify n
    n //= 2
'''
    
    print "Question 606 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_606()

##=================================================================

def hw_607():
    """
    QUESTION 7
    
    Convert the following English description into code.
    
    1.) Initialize n to be 1000. Initialize numbers to be a list of numbers from
        2 to n, but not including n.
    2.) With results starting as the empty list, repeat the following as long as
        numbers contains any numbers.
        * Add the first number in numbers to the end of results.
        * Remove every number in numbers that is evenly divisible by (has no remainder
            when divided by) the number that you had just added to results.
            
    How long is results? To test your code, when n is instead 100, the length
    of results is 25. Enter your answer below.
    """
    # Build this code.
    
    n = 1000
    numbers = range(2, n)
    results = []
    while len(numbers) > 0:
        hold = numbers[0]
        results.append(hold)
        for number in numbers:
            if number % hold == 0:
                numbers.remove(number)
    
    answer = len(results)
    # Looks like the prime numbers result from this code.
    
    print "Question 607 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_607()

##=================================================================

def hw_608():
    """
    QUESTION 8
    
    We can use loops to simulate natural processes over time. Write a program that 
    calculates the populations of two kinds of wumpuses over time. At the beginning 
    of year 1, there are 1000 slow wumpuses and 1 fast wumpus. This one fast wumpus 
    is a new mutation. Not surprisingly, being fast gives it an advantage, as it can 
    better escape from predators. Each year, each wumpus has one offspring. (We'll 
    ignore the more realistic niceties of sexual reproduction, like distinguishing 
    males and females.). There are no further mutations, so slow wumpuses beget 
    slow wumpuses, and fast wumpuses beget fast wumpuses. Also, each year 40% 
    of all slow wumpuses die each year, while only 30% of the fast wumpuses do.

    So, at the beginning of year one there are 1000 slow wumpuses. Another 1000 slow 
    wumpuses are born. But, 40% of these 2000 slow wumpuses die, leaving a total of 
    1200 at the end of year one. Meanwhile, in the same year, we begin with 1 fast 
    wumpus, 1 more is born, and 30% of these die, leaving 1.4. (We'll also allow 
    fractional populations, for simplicity.)
    
    Beginning of Year       Slow Wumpuses          Fast Wumpuses
    1                               1000                          1
    2                               1200                           1.4
    3                               1440                          1.96
    
    Enter the first year in which the fast wumpuses outnumber the slow wumpuses.
    Remember that the table above shows the populations at the start of the year.
    (So I assume that means when wumpus population shifts from one to the other,
    that means the previous year is the one in which that shift occurred).
    """
    # First I'll write a function to simulate one year of wumpus life cycles. 
    
    def wumpus_year(num_slow, num_fast):
        """
        Simulate one year of wumpus reproduction and death. Returns a tuple with
        slow and fast population by the end of the year. Every wumpus has one child.
        40% of the slow wumpuses die, and 30% of the fast wumpuses die.
        """
        total_slow = (2 * num_slow) * 0.6
        total_fast = (2 * num_fast) * 0.7
        return (total_slow, total_fast)
        
    # Now let me test this using the provided starting data, simulating 1 and 2 years
    # (which are the starting populations for years 2 and 3).
    
    init_slow = 1000
    init_fast = 1
    
    slow, fast = wumpus_year(init_slow, init_fast)
    print "Beginning of Year 2"
    print "Slow:", slow, "Fast:", fast
    slow, fast = wumpus_year(slow, fast)
    print "Beginning of Year 3"
    print "Slow:", slow, "Fast:", fast
    print "-"*10
    
    # Now I will repeat that function until the population ratio shifts. I'll save
    # the years and populations in a list of lists to double-check since this
    # could get confusing (i.e. the year that the shift occurs could be the one
    # that I land on or the previous one if I'm not careful).
    
    year = 1
    slow = init_slow
    fast = init_fast
    data = []
    while slow > fast:
        data.append([year, slow, fast])
        slow, fast = wumpus_year(slow, fast)
        year += 1
    for sublist in data:
        print sublist
    print "-"*10
    
    # The data list shows the population at the beginning of each year. The last
    # list in that list is [45, 3047718.32334, 2689264.81522]. Using those
    # numbers to double check that the next year will have more fast wumpuses
    # than slow wumpuses:
    
    slow = 3047718.32334
    fast = 2689264.81522
    slow, fast = wumpus_year(slow, fast)
    print "Slow:", slow, "Fast:", fast
    print "-"*10
    
    # At the beginning of year 46, there are more fast than slow wumpuses, so that
    # shift occurs within the previous year, 45.
    
    answer = 45
    
    print "Question 608 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_608()

##=================================================================
##=================================================================