"""
Rice University / Coursera: Principles of Computing (Part 2)
Week 3: Class Notes
Lambda Functions (Anonymous Functions)
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

#-----------------------------------------------------------------
## Provided code, with variables renamed for clarity

def double(val):
    return 2 * val

def square(val):
    return val ** 2

data = [1, 3, 6, 9, 18]

newdata_1a = map(square, data)
print newdata_1a

newdata_1b = map(lambda x: x ** 2, data)
print newdata_1b

def even(val):
    if val % 2:
        return False
    else:
        return True
    
newdata_2a = filter(even, data)
print newdata_2a

newdata_2b = filter(lambda val: val % 2 == 0, data)
print newdata_2b

# Testing alternative expression to return same results as newdata_2b:
newdata_2c = filter(lambda val: not val % 2, data)
print newdata_2c

# Write keyword lambda then all arguments referenced, followed
# by a colon and then the expression that uses the arguments.

##=================================================================

# Testing Grounds

ints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
points = [(1,3), (2,2), (4,4), (5,7), (8,9)]
a = [14, 33, 56, 12, 48]
b = [88, 13, 7, 55, 99]

# Sum of exponential products of elems in two lists
test1 = map(lambda x,y: x**2 + y**3, ints, primes)
print test1

# Find max in a pair of points (in a single tuple)
test2 = map(lambda xy: max(xy), points)
print test2

# Multiply two elems in a tuple
test3 = map(lambda xy: xy[0] * xy[1], points)
print test3

# Find min in a pair of points (between two lists)
test4 = map(lambda xy: min(xy), zip(a, b))
print test4

##=================================================================
##=================================================================