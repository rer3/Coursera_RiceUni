"""
Rice University / Coursera: Principles of Computing (Part 2)
Week 4: Class Notes
Assertions
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# All import statements needed.

import math

#-----------------------------------------------------------------
## Code provided during lecture on assertions. Use assertions if you have a
## complicated piece of code where it's relatively easy to check if the result of
## that is valid.

def hypotenuse(sidea, sideb):
    """
    Calculate the length of the hypotenuse of a right
    triangle with sides of length sidea and sideb.
    """
    # Compute hypotenuse (original line)
    #hyp = math.sqrt(sidea2 + sideb)
    # First fix - cube the sides.
    #hyp = math.sqrt(sidea**3 + sideb**3)
    # Second fix - square the sides.
    hyp = math.sqrt(sidea**2 + sideb**2)
    
    # Make sure value is reasonable
    assert hyp > sidea and hyp > sideb, "hypotenuse too short"
    assert hyp < (sidea + sideb), "hypotenuse too long"
    
    return hyp

#  Throws "hypotenuse too short" error
#print hypotenuse(3, 4)

# Make first fix and try again. Note that this will
# throw "hypotenuse too long" error.
#print hypotenuse(3,4)

# Make second fix and try again. Success!
print hypotenuse(3,4)
# This does not guaranty that we calculated the right thing.

def odd_fraction(lst):
    """
    Return the fraction of odd elements in lst
    """
    odds = 0
    total = 0
    
    # Count odd numbers
    for item in lst:
        if item % 2:
            odds += 1
        # Fix 1 - increment total
        total += 1
            
    # Make sure we don't divide by 0
    assert total != 0, "no elements"
    # Fix 1 - add another check
    #assert odds < total, "too long"
    # Fix 2 - change comparison check
    assert odds <= total, "too long"
    
    fraction = float(odds) / total
    return fraction

numbers = [2, 8, 1, 4, 3, 7, 9]

# Throws "no elements" error.
#print odd_fraction(numbers)

# Make first fix and try again. Success! Or is it?
print odd_fraction(numbers)
# It wasn't discussed here, but should the odds not be
# less than OR EQUAL to total? Think of a list with all odds.
numbers = [3, 5, 7, 9]
#print odd_fraction(numbers)

# Make second fix and try again. Success! There was an issue
# here after all.
print odd_fraction(numbers)

##=================================================================
##=================================================================