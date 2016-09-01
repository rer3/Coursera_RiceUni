"""
Rice University / Coursera: Principles of Computing (Part 2)
Week 2: Class Notes
Recursion
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

#-----------------------------------------------------------------
## Provided code.

def sum_up_to(n):
    if n == 1:
        # base case
        return 1
    else:
        # recursive case
        return n + sum_up_to(n - 1)

print sum_up_to(1)
print sum_up_to(2)
print sum_up_to(10)
print sum_up_to(55)
# Check previous line of code
print sum(range(56))
print "\n"

def is_palindrome(word):
    if len(word) < 2:
        # base case
        return True
    else:
        # recursive case
        if word[0] != word[-1]:
            return False
        else:
            return is_palindrome(word[1:-1])

print is_palindrome("a")
print is_palindrome("aa")
print is_palindrome("is")
print is_palindrome("madamimadam")
print is_palindrome("abcdefdcba")
print "\n"

##=================================================================

# Testing Grounds

# Write a factorial function.
print "Regular old factorial function using the recurrence model."
def factorial(n):
    """
    Return the factorial of a number n.
    """
    if n < 2:
        return 1
    else:
        answer = n * factorial(n - 1)
        return answer
        
for n in range(10):
    print "Factorial with n = " + str(n) + ": " + str(factorial(n))
print "\n"

# Write a fibonacci function.
print "Regular old Fibonacci function using the recurrence model."
def fibonacci(n):
    """
    Return the nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n < 3:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
for n in range(10):
    print "Fibonacci number at n = " + str(n) + ": " + str(fibonacci(n))
print "\n"  

# A faster, iterative solution exists for computing fibonacci numbers.
print "Faster Fibonacci function using iteration rather than recursion."
def fibi(n):
    """
    Return the nth Fibonacci number.
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
    
for n in range(10):
    print "Fibonacci number at n = " + str(n) + ": " + str(fibi(n))
print "\n"  

# A "memory" can be implemented for the recursive version to save time.
print "Optimizing running time with the recusive function and a 'memory'"
memo = {0:0, 1:1}
def fibm(n):
    """
    Return the nth Fibonacci number.
    """
    if not n in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]
    
for n in range(10):
    print "Fibonacci number at n = " + str(n) + ": " + str(fibm(n))
print "\n"  

# Exercises taken from www.python-course.eu/recursive_functions.php

## 1. Think of a recursive version of the function f(n) = 3 * n (multiples of 3).
## 2. Write a recursive Python function that returns the sum of the first n integers.
## 3. Write a function which implements the Pascal's triangle.

print "Question 1: Recursive Function That Returns Multiples of 3"
print "Base case: f(0) = 0, f(1) = 3"
print "Recurrence: f(n) = f(n-1) + 3"

def multiples_of_three(n):
    """
    Returns the nth multiple of 3.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 3
    else:
        return 3 + multiples_of_three(n-1)
        
for n in range(10):
    print "For n = " + str(n) + " the answer is: " + str(multiples_of_three(n))
print "Note: replace the + operator with a * operator to get exponents of 3."
print "\n"

print "Question 2: Recursive Function That Returns Sum of First n Integers"
print "See 'sum_up_to' function above."
print "\n"

print "Question 3: Function Which Implements the Pascal's Triangle"
print "This is the implementation from the website:"

def pascal(n):
    """
    Returns the nth line from Pascal's triangle.
    """
    if n == 1:
        return [1]
    else:
        previous_line = pascal(n-1)
        line = [previous_line[i] + previous_line[i+1] for i in range(len(previous_line)-1)]
        line.insert(0, 1)
        line.append(1)
    return line

for n in range(1, 11):
    print pascal(n)

"""
This implementation looks at the previous line, then sums up adjacent elements.
This creates len(previous line) - 1 elements for the new line.
print "Then a 1 is inserted into the first position and appended to the last to complete it.
"""
print "\n"

# From that source, the Fibonacci numbers can be found using Pascal's triangle like so:

def fib_pascal(n, fib_pos):
    if n == 1:
        line = [1]
        fib_sum = 1 if fib_pos == 0 else 0
    else:
        line = [1]
        (previous_line, fib_sum) = fib_pascal(n-1, fib_pos+1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
        if fib_pos < len(line):
            fib_sum += line[fib_pos]
    return (line, fib_sum)

def fib(n):
    return fib_pascal(n, 0)[1]

# and now printing out the first ten Fibonacci numbers:
for i in range(1,10):
    print(fib(i))

##=================================================================
##=================================================================