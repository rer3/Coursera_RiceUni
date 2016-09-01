# Python Test 3
# Remainder - modular arithmetic

num = 49
tens = num // 10
ones = num % 10
print tens, ones
print 10 * tens + ones

# Modular arithmetic is good for computing time using the military clock

hour = 20
shift = 8
print (hour + shift) % 24

# Parentheses are needed because % calculates first

# Have a 2D game, and you have to deal with screen wraparound
# Spaceship from week 7

width = 800
position = 797
move = 5
position = (position + move) % width
print position

# Data conversion operations
# Convert an integer into string - str
# Convert an hour into 24-h format

hour = 3
ones = hour % 10
tens = hour // 10
print tens, ones, ":00"

# That doesn't look very good...
# Try str function

print str(tens), str(ones), ":00"

# Same, but now they're strings...

print str(tens) + str(ones) + ":00"

# Concatenated strings look nicer here

# Let's look at math functions

import simplegui # Access drawing operations
import math # Access std math fns
import random # Access fns to generate random numbers

print math.pi

# Convert a string into numbers using int and float