"""
Rice University / Coursera: Intro to Interactive Programming in Python (Part 2)
Week 1: Homework 5a
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

##=================================================================

def hw_501():
    """
    QUESTION 1
    
    What is the type of parameter for a mouseclick handler (in CodeSkulptor)?
    """
    # A tuple of coordinates is passed to it.
    
    answer = "tuple"
    
    print "Question 501 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_501()

##=================================================================

def hw_502():
    """
    QUESTION 2
    
    Which of the following (choose all) expressions mutate my_list?
    
    Option 1
    my_list + [10,20]
    
    Option 2
    my_list.reverse()
    
    Option 3
    my_list.extend([10,20])
    
    Option 4
    my_list.append(10)
    
    Option 5
    another_list.extend(my_list)
    """
    # Option 1 is out because it mutates nothing.
    # Option 5 is out because it mutates another_list, not my_list.
    
    answer = "my_list.reverse()" + "\n"
    answer += "my_list.extend([10,20])" + "\n"
    answer += "my_list.append(10)"
    
    print "Question 502Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_502()

##=================================================================

def hw_503():
    """
    QUESTION 3
    
    We want to remove the element at the front of a list. For example, we want
    the following code to print "apple" and ["pear", "blueberry"], respectively.
    What function or method call should replace the question marks?
    
        fruits = ["apple", "pear", "blueberry"]
        fruit = ???
        print fruit, fruits
        
    Option 1
    fruits.pop()
    
    Option2
    fruits.pop(0)
    
    Option 3
    fruits.remove(0)
    
    Option 4
    fruits.remove("apple")
    
    Option 5
    fruits[1:]
    
    Option 6
    fruits[0]
    """
    # Option 1 is out because it pops and returns the last item in fruits.
    # Option 3 is out because it returns an error, as 0 is not in the list.
    # Option 4 is out because while it removes "apple", it returns None to fruit.
    # Options 5-6 are out because they do not mutate fruits.
    
    answer = "fruits.pop(0)"
    
    print "Question 503 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_503()

##=================================================================

def hw_504():
    """
    QUESTION 4
    
    Which of the following uses of range() will generate the list [2,5,8,11,14]?
    
    Option 1
    range(14, 1, -3)
    
    Option 2
    range(2, 15) * 3
    
    Option 3
    range(2, 15, 3)
    """
    # Option 1 is out because it generates the list in reverse order.
    # Option 2 is out because it generates a list where 2-14 are repeated 3 times.
    
    answer = "range(2, 15, 3)"
    
    print "Question 504 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_504()

##=================================================================

def hw_505():
    """
    QUESTION 5
    
    To correctly compute the product of a list of numbers, what statement should
    replace the question marks?
    
        numbers = ...
        ???
        for n in numbers:
            product *= n
            
    Option 1
    product = 1
    
    Option 2 
    product = 0
    
    Option 3
    product = numbers[0]
    
    Option 4
    product = []
    
    Option 5
    product = numbers[1]
    """
    # The var "product" is going to be updated continually by multiplying its
    # current value by the next iterated value in the list "numbers". Its initial
    # state must allow the first number iterated over to return itself as a value.
    # Thus, option 1 is the only correct option, as the others will, respectively,
    # return 0, an incorrect result, an error, and an incorrect result.
    
    answer = "product = 1"
    
    print "Question 505 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_505()

##=================================================================

def hw_506():
    """
    QUESTION 6
    
    We can loop over strings, too!

    The following incomplete function is a simple, but inefficient, way to reverse a 
    string. What line of code needs to replace the questions marks for the code to 
    work correctly?
    
        def reverse_string(s):
            '''
            Returns the reversal of the given string.
            '''
            ???
            for char in s:
                result = char + result
            return result

        print reverse_string("hello")
    
    Option 1
    result = ""
    
    Option 2
    result = []
    
    Option 3
    result = " "
    
    Option 4
    result = 0
    """
    # The function works by iterating over a string, adding a char to the
    # "result" string in reverse order, and returning result. The initial state of
    # result must allow the state of result after the first addition to simply
    # be the first char iterated over. Only option 1 (a blank string) allows this,
    # as the other options would return, respectively, a concatenation error,
    # a string with an extra blank space in it, and a concatenation error.
    
    answer = "result = ''"
    
    print "Question 506 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_506()

##=================================================================

def hw_507():
    """
    QUESTION 7
    
    Imagine a game on a map. At the beginning, we might want to randomly assign
    each player a starting point. Which of the following expressions may we use in 
    place of the question marks to correctly implement this functionality?
    
        import random

        def random_point():
            '''
            Returns a random point on a 100x100 grid.
            '''
            return (random.randrange(100), random.randrange(100))

        def starting_points(players):
            '''
            Returns a list of random points, one for each player.
            '''
            points = []
            for player in players:
                point = random_point()
                ???
            return points
            
    Option 1
    points.append(point)
    
    Option 2
    points.extend(point)
    
    Option 3
    point.append(points)
    
    Option 4
    point.extend(points)
    
    Option 5
    points + point
    
    Option 6
    points += point
    """
    # The random_point function returns a tuple of coordinates, which must be
    # added to the list of points so that they can be iterated over.
    # Option 2 is out because it will convert the tuple to a list and add the individual
    # vals to points such that it appends to the list with no separation of points.
    # Options 3-4 are out because tuples do not have append/extend methods, and
    # the relationship is reversed (adding a list of points to a point).
    # Option 5 is out because it doesn't mutate points.
    # Option 6 is out because, like option 2, it converts the tuple to a list before
    # appending the values to it with no separation of points.
    
    answer = "points.append(point)"
    
    print "Question 507 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_507()

##=================================================================

def hw_508():
    """
    QUESTION 8
    
    The following function is supposed to check whether the given list of nubmers
    is in ascending order. For example, we want is_ascending([2,6,9,12,400]) to
    return True, while is_ascending([4,8,2,13]) should return False.
    
        def is_ascending(numbers):
            '''
            Returns whether the given list of numbers is in ascending order.
            '''
            for i in range(len(numbers)): *******THIS LINE*******
                if numbers[i+1] < numbers[i]:
                    return False
            return True
            
    However the function doesn't work. Try it to verify this. The easiest fix
    is to make a small change to the highlighted code (here, the identified
    line). What should it be replaced with?
    
    Option 1
    range(1, len(numbers))
    
    Option 2
    range(len(numbers)) - 1
    
    Option 3
    range(len(numbers - 1))
    
    Option 4
    range(len(numbers) - 1)
    """
    # The function iterates over the list comparing the element at index i to that
    # at index i+1. The error arises from the range including the final element, which
    # has no element at i+1 to which it can be compared; the range must stop at
    # the element just before the last, which corresponds to len(numbers) - 1.
    
    # Option 1 is out because it is the same as in the function.
    # Option 2 is out because it attempts to subtract an int from a list.
    # Option 3 is out because it attempts to subtract an int from a list.
    
    answer = "range(len(numbers) - 1)"
    
    print "Question 508 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_508()

##=================================================================

def hw_509():
    """
    QUESTION 9
    
    Turn the following description into code:
    1.) Create a list with two numbers, 0 and 1, respectively.
    2.) For 40 times, add to the end of the list the sum of the last two numbers.
    
    What is the last number in the list? To test your code, if you repeat 10 times
    rather than 40, your answer should be 89.
    """
    # This code merely computes the Fibonacci numbers, which are contained in
    # a sequence created by adding the last two numbers in it and adding that 
    # sum to the end of the sequence (and repeating this ad infinitum).
    # The code as described here is very simple.
    
    def fib(num_trials):
        """
        Returns last number in Fibonacci sequence generated by adding
        num_trials Fibonacci numbers to the initial list [0,1].
        """
        seq = [0, 1]
        for trial in range(num_trials):
            new_num = seq[-1] + seq[-2]
            seq.append(new_num)
        return seq[-1]
        
    # Now let's test that on num_trials = 10 to see if 89 is returned.
    
    print fib(10)
    # 89 returned
    print "-"*10
    
    answer = fib(40)
    
    print "Question 509 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_509()

##=================================================================
##=================================================================