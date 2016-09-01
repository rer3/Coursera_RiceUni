"""
Rice University / Coursera: Principles of Computing (Part 2)
Week 1: Class Notes
Generators
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

#-----------------------------------------------------------------
## Provided code.

# A list comprehension
print "max in list:", max([num * 2 - 3 for num in range(7)])

# Remove the square brackets to create a generator expression.
# A generator expression
print "max in gen:", max(num * 2 - 3 for num in range(7))

# A generator function
def genfunc(limit):
    num = 0
    while num < limit:
        yield num
        num = num + 1

print genfunc(7)
        
# Iteration using a generator function
print "Iterate over generator:"
for number in genfunc(7):
    print number
    
# Pass to functions expecting a sequence
print "max in gen func:", max(genfunc(4))

# Use return to end generator
def genfunc2(endfunc):
    num = 0
    while True:
        if endfunc(num):
            return
        yield num
        num = num + 1
        
def endfn(num):
    if num == 7:
        return True
    return False

print "Iterate over second generator:"
for number in genfunc2(endfn):
    print number

##=================================================================

# Testing Grounds

# Create an end function.
def endfn(x, y):
    """
    End a generator function.
    """
    if x == y:
        return True
    return False
    
# Create a generator function.
def genfunc(endfunc, a, b):
    """
    Yield numbers in a range.
    """
    while True:
        if endfunc(a, b):
            return
        yield a
        a += 1
        
# Use generator function to print from 2 to 15:
print "-"*40
for number in genfunc(endfn, 2, 16):
    print number

##=================================================================
##=================================================================