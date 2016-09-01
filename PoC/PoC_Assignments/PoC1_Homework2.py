"""
Rice University / Coursera: Principles of Computing (Part 1)
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

##=================================================================

DIRECTIONS = '''
The Importance of Math
----------
The main emphasis of the homework in this class is helping you learn the math
skills required to flourish in CompSci. You will find these skills indespensable
as you tackle more and more difficult topics in CompSci. Remember that the 
"Science" part of CompSci corresponds primarily to Mathematics. In this homework,
we will review some basic topics you should be familiar with from high school math.
'''

##=================================================================

def hw_201():
    """
    QUESTION 1: Functions
    
    The first four questions cover mathematical functions. We recommend that you
    review the material in the Practice Activity for week 1 on "Functions" before
    attempting them.
    
    Consider the following Python function:
        def root(a, b, c):
            discriminant = b ** 2 - 4 * a * c
            return (-b - discriminant ** 0.5) / (2 * a)
            
    Which mathematical function below computes the same value as this function?
    
    Option 1
    root(a,b,c) = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
    
    Option 2
    root(a,b,c) = (b - sqrt(b - 4 * a * c)) / (2 * a)
    
    Option 3
    root(a,b,c) = (b - b**2 - 4 * a * c) / (2 * a)
    
    Option 4
    root(a,b,c) = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
    """
    # In the problem, the four options are shown as formulas and not written out
    # like I have above (due to my constraints). My method of representing each
    # option actually makes it much easier to identify the correct answer. In the
    # function, the value returned is (-b - discriminant ** 0.5) / (2 * a), where
    # "** 0.5" is just taking the sqrt of an expression. Matching the discriminant
    # with what's in the options is simple.
    
    # Option 1 is out because the sqrt(discriminant) is added, not subtracted.
    # Options 2-3 are out because the first "b" term is positive, not negative.
    # Option 4 remains, and it appears to be correct.
    
    answer = "root(a,b,c) = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)"

    print "Question 201 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_201()

##=================================================================

def hw_202():
    """
    QUESTION 2
    
    Which of the mathematical functions displayed below are linear? (Choose all)
    
    Option 1
    g(y) = 2*y - 3
    
    Option 2
    a(x) = x**2 + 2*x + 1
    
    Option 3
    f(x) = x + 10
    
    Option 4
    h(z) = 3
    
    Option 5
    c(z) = sqrt(z)
    """
    # A linear function is one that changes in a linear fashion, where the slope 
    # remains unchanged as the input increases. Linear functions do not have
    # terms that are raised to a power of something (e.g. quadratic, cubic, 
    # square root). 
    
    # Option 2 is out because it is quadratic.
    # Option 5 is out because it is a square root.
    
    answer = "g(y) = 2*y - 3" + "\n"
    answer += "f(x) = x + 10" + "\n"
    answer += "h(z) = 3"
    
    print "Question 202 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_202()
    
##=================================================================

def hw_203():
    """
    QUESTION 3
    
    As part of this class, we will develop methods for estimating the running time
    of various important algms as functions of the size of their input. One simple
    function that we will use in these estimates is the logarithm function, which
    is defined and discussed in Math notes on "Functions".
    
    Review this part of the notes. Then compute the logarithm base 5 of
    (5**7)**0.5 which corresponds to the value of the mathematical expression
    log_5((5**7)**0.5). Enter the answer in the box below in decimal form.
    """
    # Remember that the relationship between log and exponents is:
    # log_2(2 **5) == 5. The logarithm of a number is the exponent to which
    # another fixed value, the base, must be raised to produce that number.
    # Log base 5 (log_5) of a number returns the exponent to which 5 much
    # be raised to produce that number. 
    
    # In the example, (5**7)**0.5 == 5 ** (7 * 0.5) == 5 ** (3.5). Therefore,
    # log_5(5**(3.5)) == 3.5, since raising the value of 5 ** 3.5 is equal to 
    # the number 5 ** 3.5. 
    
    answer = 3.5
    
    print "Question 203 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_203()
        
##=================================================================

def hw_204():
    """
    QUESTION 4
    
    Consider the mathematical function explode(x) = (2**x)**2. What is the result of
    evaluating explode(log_2(y)) if y > 0? Your answer should be reduce to a simple
    expression that does not involve logarithms or exponentials.
    
    Hint: review the math notes on "Functions" carefully and note the relationship
    between the exponential function and the logarithm function when computed
    using the same base. Enter the answer as a math expression below.
    """
    # To discover the answer, I must implement this function and then evaluate
    # it at increasing inputs (1 and greater) where the input is modified to be
    # log_2(input). The resulting sequence will be analyzed via print statement.
    
    def explode(x):
        return (2 ** x) ** 2
        
    for num in range(10):
        input = math.log(num, 2)
        print "Num:", num, "Output:", explode(input)
    print "-"*10
    
    # The num:output pairs were: 0:0, 1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49,
    # 8:64, 9:81. The relationship is clearly y**2.
    
    answer = "y ** 2"
    
    print "Question 204 Answer:"
    print answer
    print "-"*50
    print "\n"
        
hw_204()

##=================================================================

def hw_205():
    """
    QUESTION 5: Significant figures
    
    An important concept in working with numbers is that of sig figs. The sig figs
    of a number are those digits that carry meaning contributing to its precision.
    A digit is significant based on 3 rules:
    * All non-zero digits are considered significant.
    * Zeros appearing anywhere between two non-zero digits are significant.
    * Trailing zeros in a number containing a decimal point are significant.
    
    How many sig digits does the decimal number 0.00400100 have?
    """
    # It has 2 non-zero digits. There are 2 zeros between them. And, since this
    # is a decimal number, the 2 trailing zeros are counted. 
    
    answer = 6
    
    print "Question 205 Answer:"
    print answer
    print "-"*50
    print "\n"
        
hw_205()
    
##=================================================================

def hw_206():
    """
    QUESTION 6
    
    Scientific notation is a way of writing numbers that are too big or too small
    to be conveniently written in decimal form. For decimal numbers, scientific
    notation has the form a x 10**b where a = number in range 1 <= |a| < 10
    and b is an integer. The number a is the mantissa while the integer b is the
    exponent. The mantissa is usually expressed using the same number of significant
    digits as used in the original decimal form.
    
    What is the mantissa for 0.00400100 when expressed in scientific notation?
    
    Option 1
    a = 0.400100
    
    Option 2
    a = 4.001
    
    Option 3
    a = 4.00100
    
    Option 4
    a = 0.4001
    """
    # Remember that the mantissa is expressed using the same number of sig figs
    # as used in the original decimal form. The number in the problem is the same as
    # that in question 5, which had 6 sig figs, thus the answer here will have 6 digits.
    
    # Options 2 and 4 are out because they are 4 and 5 digits, respectively.
    # Option 1 is out because it is less than 1.
    
    answer = 4.00100
    
    print "Question 206 Answer:"
    print answer
    print "-"*50
    print "\n"
        
hw_206()
        
##=================================================================

def hw_207():
    """
    QUESTION 7
    
    In Python, floating point numbers are represented in a binary version of scientific
    notation where the base 10 is replaced by 2 and the mantissa is a binary number
    that lies in the range 1 <= |a| < 2 and has 53 significant bits. Floating point
    numbers are usually printed out with up to 12 sig figs (although with trailing
    zeros suppressed).
    
    In some homework problems, you will be asked to write code that computes an
    answer as a floating point number and then enter your answer as decimal number
    with a specified number of sig figs. In practice, Python computes more sig figs
    than are required so you should round your answer to the closest decimal number
    with the specified number of sig figs.
    
    For this question, look up (or compute) the decimal representation of the number
    pi and enter the value of pi with five sig figs of precision in the box below.
    Remember to round as described above.
    """
    # The constant pi = 3.14159265359.
    
    ##################################################
    ## INCORRECT: Almost. You truncated 3.14159 to five digits. You should round
    ## to the closest decimal number with five significant digits.
    ##
    ## answer = 3.1415
    ##################################################
    
    # I didn't round the final digit up to 6.
    
    answer = 3.1416
    
    print "Question 207 Answer:"
    print answer
    print "-"*50
    print "\n"
        
hw_207()    
    
##=================================================================

def hw_208():
    """
    QUESTION 8: Grids
    
    Consider the following code snippet:
        row = ...
        col = ...
        nested_list = [[0,1,2,3,4], [5,6,7,8,9], [10,11,12,13,14]]
        print nested_list[row][col]
        
    If running this code snippet prints 13 in the console, what are the non-
    negative values of row and col? Enter these two values below as numbers
    separated by a space.
    """
    # This question simply asks us to identify the row and col of the value 13.
    # The third list (i.e. row) in nested_list holds 13, so row = 2 (remember
    # to count from 0 up). Within that inner list, 13 is found at the 4th spot,
    # of the 3rd index, so col = 3.
    
    answer = "2 3"
    
    print "Question 208 Answer:"
    print answer
    print "-"*50
    print "\n"
        
hw_208()    
        
##=================================================================

def hw_209():
    """
    QUESTION 9
    
    Review the math notes on Grids. Given a grid of size 4x6, what are the row and
    column indices for the upper right cell in this grid? Enter the row and col
    indices below as numbers separated by a space.
    """
    # upper right is the first row and last column, or (0,5).
    
    answer = "0 5"
    
    print "Question 209 Answer:"
    print answer
    print "-"*50
    print "\n"
        
hw_209()    
            
##=================================================================

def hw_210():
    """
    QUESTION 10
    
    Review the function traverse_grid from the Grids video lecture. Given a 4x4
    grid, what values for start_cell and direction would cause traverse_grid to
    traverse the diagonal of grid connecting the lower right tile to the upper
    left tile?
    
    Option 1
    start_cell = (3,3)
    direction = (-1,-1)
    
    Option 2
    start_cell = (0,0)
    direction = (1,1)
    
    Option 3
    start_cell = (3,0)
    direction = (-1,0)
    
    Option 4
    start_cell = (3,0)
    direction = (0,1)
    """
    # First let's look at the traverse_grid function from the Grid video.
    
    def traverse_grid(start_cell, direction, num_steps):
        """
        Function that iterates through the cells in a grid
        in a linear direction
        
        Both start_cell is a tuple(row, col) denoting the
        starting cell
        
        direction is a tuple that contains difference between
        consecutive cells in the traversal
        """
        
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            print "Processing cell", (row, col), 
            print "with value", EXAMPLE_GRID[row][col] 
            
    # Note that the direction is a tuple that contains the difference between
    # consecutive cells. In the function traverse_grid, first a for loop begins
    # that iterates through every step in num_steps. At each step, row and
    # col variables are initialized, and both are incremented pathways from the
    # start_cell whose lengths are determined by the relevant value in the
    # direction tuple that is passed to the function. If the direction is (1,1),
    # then at each step, the row and col increase by 1 each. If the direction
    # is (-1, -1), the row and col decrease by -1 each with each step. The rest
    # of the function simply prints to the console the cell in the grid that is
    # currently being traversed and its value.
    
    # In this question, we have a grid like the one below and we wish to traverse
    # it in a diagonal direction starting from the lower right tile and ending at
    # the upper left tile. 
    # 4 0 0 0 
    # 0 3 0 0
    # 0 0 2 0
    # 0 0 0 1
    # The numbers correspond to the ith step in the traversal. The starting
    # cell is bottom right, which is (3,3). This moves to (2,2), then (1,1), and
    # finishes at (0,0). This is a change of -1 in both directions. Option 1 is the
    # only option that is remotely close.
    
    answer = "start_cell = (3,3)" + "\n"
    answer += "direction = (-1,-1)"
    
    print "Question 210 Answer:"
    print answer
    print "-"*50
    print "\n"
        
hw_210()    
            
##=================================================================
##=================================================================