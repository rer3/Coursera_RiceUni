"""
Rice University / Coursera: Principles of Computing (Part 1)
Week 1: Project 1
Merge Function for 2048 Game
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# Below is the link to the description of this assignment.

COURSE = "https://class.coursera.org/principlescomputing1-004/"
DESCRIPTION = COURSE + "wiki/view?page=2048_(Merge)"

##=================================================================

DIRECTIONS = '''
Overview
----------
2048 is a simple grid-based numbers game. The rules of the game are described here:
https://class.coursera.org/principlescomputing1-004/wiki/2048_Game.

In the first two assignments, we will implement a version of the 2048 game. Although
the original game is played on a 4x4 grid, your version should be able to have
an arbitrary height and width. In this first assignment, we will focus on only one
aspect of the game: merging tiles. The template is provided (very basic). The signature
(name and parameters) of the functions in this file must remain unchanged, but
you may add additional functions or other code that you need to.

Coding Style
----------
In this class, you will be asked to strictly follow a set of coding style guidelines.
Good programmers not only get their code to work, but they also write it in a way
that enables others to easily read and understand their code. Please read the style
guidelines carefully and get into the habit of following them from the start: 
https://class.coursera.org/principlescomputing1-004/wiki/view?page=style_guidelines.

Testing Your Code
----------
As always, testing is a critical part of the process of building your mini-project.
Remember you should be testing your code as you write it. Don't try to implement
everything and then test. You will have lots of errors that all interact in strange
ways that make your program very hard to debug.

Throughout this course, you will be using a machine grader (OwlTest) to help you
assess your code. The OwlTest page has a pale yellow background and does not submit
your code to Coursera. OwlTest is just meant to allow you to test your mini-project
automatically. Note that trying to debug your mini-project using the tests in OwlTest
can be very tedious since they are slow and give limited feedback. Instead, first test
your program using your own tests.

Remember that OwlTest uses Pylint to check that you have followed style guidelines
for this class. Deviation will result in deductions from your final score. Please read
the feedback from Pylint closely. Submit final code to the CourseraTest page, which
has a white background and DOES submit your grade to Coursera.

Merge
----------
For this assignment, you will implement a function merge(line) that models the
process of merging all of the tile values in a single row or column. This function
takes a list "line" as a parameter and returns a new list with the tile values from
line slid towards the front of the list and merged. Do not modify the input. 

In this function, you are always sliding the values in the list towards the front
of the list (the list position with index 0). You will make sure you order the entries
in "line" appropriately when you call this function later in the next assignment.
Empty grid squares with no displayed value will be assigned a value of zero in
our representation.

For example, if a row of the board started as follows:
2 _ 2 2
And you slid the tiles left, the row would become:
4 2 _ _
Note that the two leftmost tiles merged to become a 4 and the third 2 just slides
over next to the 4. A given tile can only merge once on any given turn, although
many pairs of tiles could merge on a single turn.

For the above example, the input to the merge function would be the list [2,0,2,2].
The function should produce the output [4,2,0,0]. We suggest you begin to implement
the function as follows:
1.) Start with a result that contains the same number of 0's as the length of the
    line argument.
2.) Iterate over the line input looking for non-zero entries. For each one, put the 
    value into the next available entry of the result list (starting at position 0).
    
Notice if you only follow this process, you would end up with the result [2,2,2,0].

Now you should think through what you should add to your function in order to merge
tiles. Keep in mind, however, that any tile should only be merged once and that these
merges should happen in order from lowest index to highest index. For instance, on the
input [2,0,2,4], the result should be [4,4,0,0], not [8,0,0,0]. 

Note that there are many ways to implement the merge function. The objective of this
project is for you to use what you've learned in our previous classes to implement a
complex function. You have already learned all of the Python required to implement
merge, so the challenge is to think carefully about what the function does and how
to best accomplish that.

Here is one basic strategy to implement the merge function:
1.) Iterate over the input and create an output list that has all of the non-zero 
    tiles slid over to the beginning of the list with the appropriate number of zeroes
    at the end of the list.
2.) Iterate over the list created in the previous step and create another new list
    in which pairs of tiles in the first list are replaced with a tile of twice the
    value and a zero tile.
3.) Repeat step one using the list created in step two to slide the tiles to the
    beginning of the list again.
    
This is NOT the most efficient way of implementing merge. While it is fine to
implement it this way, we challenge you to think of other ways of doing it that do
not require creating so many lists. Ultimately, how you approach the problem is
up to you. As you work on it, here are some simple tests you should try:
* [2,0,2,4] should return [4,4,0,0]
* [0,0,2,2] should return [4,0,0,0]
* [2,2,0,0] should return [4,0,0,0]
* [2,2,2,2,2] should return [4,4,2,0,0]
* [8,16,16,8] should return [8,32,8,0]

These tests are by no means exhaustive and are just meanto to get you started.
'''

##=================================================================

# For my first attempt at what sounds simple yet challenging, I will follow the
# recommended "easier" method of sliding numbers, combining, and sliding again.

def merge(line):
    """
    Function that merges a single row or column in 2048.
    A left-merged list with trailing zeros is returned.
    """
    # Iterate over input and create output with non-zeros slid to the left.
    slid = []
    for num in line:
        if num == 0:
            continue
        else:
            slid.append(num)
    for dummy_slot in range(len(line) - len(slid)):
        slid.append(0)

    # Iterate over slid_left and create output with tile pairs replaced with
    # a tile of twice the value and a zero tile.
    paired = []
    idx = 0
    while idx < len(slid):
        if idx == len(slid) - 1:
            paired.append(slid[idx])
            idx += 1
        elif slid[idx] == slid[idx + 1]:
            paired.append(slid[idx] * 2)
            paired.append(0)
            idx += 2
        else:
            paired.append(slid[idx])
            idx += 1
    
    # Slide the tiles in paired.
    merged = []
    for num in paired:
        if num == 0:
            continue
        else:
            merged.append(num)
    for dummy_slot in range(len(line) - len(merged)):
        merged.append(0)
        
    return merged

# This implementation works. It passes both OwlTest and the suggested simple tests
# with the 5 lines. This is indeed a long, unruly implementation that could stand to
# be trimmed down. The first thought that comes to mind is the use of list
# comprehensions to form a list of all non-zero numbers in the originally passed
# "line", something like: new_list = [num for num in line if num != 0]. The zeros
# could be appended like so: new_list + [0]*(len(line) - len(new_list)).

# Since the nonzero numbers in slid are all found in the front, with trailing
# zeros padding the length, there does not seem to be any reason to include
# these zeros before combining. Zeros are added again in the "merged" list, and
# the number of zeros added there is based on the length of the input line anyway
# (done so here just to be safe in these initial attempts). 

def merge(line):
    """
    Function that merges a single row or column in 2048. 
    A left-merged list with trailing zeros is returned.
    """
    # Slide nonzeros to the left.
    slid = [num for num in line if num != 0]
    
    # Combine like pairs.
    paired = []
    idx = 0
    while idx < len(slid):
        if idx == len(slid) - 1:
            paired.append(slid[idx])
            idx += 1
        elif slid[idx] == slid[idx + 1]:
            paired.append(slid[idx] * 2)
            paired.append(0)
            idx += 2
        else:
            paired.append(slid[idx])
            idx += 1
    
    # Slide the paired nonzeros, add trailing zeros.
    merged = [num for num in paired if num != 0]
    return merged + [0] * (len(line) - len(merged))
    
# This method works as well. It's cleaner, for certain, but is it implemented
# in the cleanest possible way? The combination step looks sloppy, and it
# could just modify the "slid" list since that would not fail the condition of
# not modifying the original list passed to the function ("line"). Now, a
# for loop can be used instead of a while loop that increments an index
# variable. Three conditionals can be cut down to a single conditional.

def merge(line):
    """
    Function that merges a single row or column in 2048. 
    A left-merged list with trailing zeros is returned.
    """
    # Slide nonzeros to the left.
    slid = [num for num in line if num != 0]
    
    # Combine like pairs.
    for idx in range(len(slid) - 1):
        if slid[idx] == slid[idx+1] and slid[idx] != 0:
            slid[idx] *= 2
            slid[idx+1] = 0
    
    merged = [num for num in slid if num != 0]
    return merged + [0] * (len(line) - len(merged))
    
# The combine step will be implemented as an inner function within merge. 
# That inner function can be called on the list comprehension in one single
# statement (instead of initializing slid and modifying it in separate statements).
# This actually adds a few additional lines of code, but it may facilitate and/or
# increase extensibility of this code. Regardless, I will use the previous
# implementation in my 2048 game code.

def merge(line):
    """
    Function that merges a single row or column in 2048. 
    A left-merged list with trailing zeros is returned.
    """
    def combine_alike(line):
        """
        Inner function that combines adjacent, equal numbers
        once and replaces the second number with a zero.
        """
        for idx in range(len(line)-1):
            if line[idx] == line[idx+1] and line[idx] != 0:
                line[idx] *= 2
                line[idx+1] = 0
        return line
    
    merged = combine_alike([num for num in line if num!= 0])
    result = [num for num in merged if num!= 0]
    return result + [0]*(len(line)-len(result))
    
# Testing Grounds

# I'll begin with the 5 simple tests mentioned in the directions. 

line1 = [2,0,2,4]
line2 = [0,0,2,2]
line3 = [2,2,0,0]
line4 = [2,2,2,2,2]
line5 = [8,16,16,8]

print merge(line1)
print merge(line2)
print merge(line3)
print merge(line4)
print merge(line5)

# All tests returns the correct results using all implementations above.

##=================================================================
##=================================================================