# Python Test 10
# Global Variables and Functions

# Let's look at global/local vars
n = 0
def increment():
    global n # We need to identify global vars
    n = n + 1
increment()
increment()
increment()
print n
print ""

n = 0
def assign(x):
    global n # This now works, but note that we weren't looking at the value of n before modifying it
    n = x
assign(2)
assign(15)
assign(7)
print n
print ""

n = 0
def decrement():
    global n
    n = n - 1
    return n # We must return this value or x = None
x = decrement()
print "x = ", x
print "n = ", n
print ""

# Example of print debugging
# Label everything

import simplegui

x = 0

def f(n):
    print "f: n,x = ", n, x # Add to print input
    result = n ** x
    print "f: result = ",result # Add to print result
    return result
    
def button_handler():
    global x
    print "bh : x = ", x # Global var acts like an input
    x += 1
    print "bh : new x = ", x # And it acts like an output

def input_handler(text):
    print "ih : text = ", text
    print f(float(text))
    
frame = simplegui.create_frame("Example", 200, 200)
frame.add_button("Increment", button_handler)
frame.add_input("Number:", input_handler, 100)

frame.start()

## Code style
# Consider this example

def w(g, h):
    """Returns True exactly when g is False and h is True."""
    if g == False and h == True:
        return True
    else:
        return False

print w(True, True)
print w(True, False)
print w(False, True)
print w(False, False)
print""

# This can be rewritten as:
def t(g, h):
    return not g and h

print t(True, True)
print t(True, False)
print t(False, True)
print t(False, False)
print ""

# These statements return boolean values, so additional boolean statements are unnecessary

