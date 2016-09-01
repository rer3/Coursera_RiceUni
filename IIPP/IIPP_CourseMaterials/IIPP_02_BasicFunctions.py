# Python Test 2
# Basic Functions

# Compute the area of a triangle

def triangle_area(base, height):
    area = (1.0 / 2) * base * height
    return area

# def is "define", 'triangle_area' is the name
# base and height are the parameters
# Name your parameters to make them obvious
# The colon means you're about to start a new code block
# The body is indented automatically, depending on IDE

a1 = triangle_area(3,8)
print a1
a2 = triangle_area(14,2)
print a2
print

# Let's play

def multiply(x, y):
    a = x * y
    return a

a3 = multiply(5,9)
print a3

# Convert F to C

def f2c(fahrenheit):
    celsius = (5.0/9) * (fahrenheit - 32)
    return celsius
c1 = f2c(32)
c2 = f2c(212)
print c1, c2
print

# It worked, of course
# Convert F to K

def f2k(fahrenheit):
    kelvin = f2c(fahrenheit) + 273.15
    return kelvin
k1 = f2k(32)
k2 = f2k(212)
print k1, k2
print

# Convert C to F

def c2f(celsius):
    fahrenheit = 1.8 * celsius + 32
    return fahrenheit
f1 = c2f(20)
f2 = c2f(100)
print f1, f2
print

# This fn prints hello world

def hello():
    print "Hello, world!"
hello()
print

# What happens when you do this?

h = hello()
print 'this returns a value when it is assigned to "h"'
print h
print '"None" is returned'

# "None" is returned, meaning there's nothing there



