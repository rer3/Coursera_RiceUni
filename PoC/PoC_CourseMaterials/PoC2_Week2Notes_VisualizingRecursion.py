"""
Rice University / Coursera: Principles of Computing (Part 2)
Week 2: Class Notes
Visualizing Recursion
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# All import statements needed.

import random

#-----------------------------------------------------------------
## Provided code.

def collatz(num, count):
    """
    Given n, repeatedly perform n = f(n) where
    f(n) = n / 2 if n is even
    f(n) = 3 * n + 1 is n is odd
    Return number of iterations of this redution
    """
    if num == 1:
        return count
    elif (num % 2) == 0:
        return collatz(num / 2, count + 1)
    else:
        return collatz(3 * num + 1, count + 1)
    
# Additional calls added to 'collatz(5, 0)' call in original example.
for num in range(1, 20):
    print "Number = " + str(num) + ", count: " + str(collatz(num, 0))
print

def quicksort(num_list):
    """
    Recursive O(n log(n)) sorting algorithm
    Takes a list of numbers
    Returns sorted list of same numbers
    """
    if num_list == []:
        return num_list
    else:
        pivot = num_list[0]
        lesser = [num for num in num_list if num < pivot]
        pivots = [num for num in num_list if num == pivot]
        greater = [num for num in num_list if num > pivot]
        return quicksort(lesser) + pivots + quicksort(greater)
    

print quicksort([4, 5, 3, 1])
print

##=================================================================

# Testing Grounds

#Create random lists of varying lengths and sort them using quicksort().
for trial in range(10):
    length = random.choice(range(4, 10))
    unordered = [random.choice(range(10)) for elem in range(length)]
    print "Unordered list:", unordered
    print "Ordered list:", quicksort(unordered)
    print
    
##=================================================================
##=================================================================