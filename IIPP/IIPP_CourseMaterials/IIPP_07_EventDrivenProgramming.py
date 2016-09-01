# Python Test 7
# Event-driven Programming Model

# It looks like this: START -> INITIALIZE -> WAIT -> HANDLER -> "QUIT"
# The WAIT -> HANDLER steps can occur many, many times
# Events in this class: input, keyboard, mouse, and timer
# Subcategories exist within each event (input: button, text box,...)

# Import simplegui that was built for this IDE
import simplegui

# Define an event handler
def tick():
    print "tick!"

# Register handler
timer = simplegui.create_timer(1000, tick)

# Start your timer running
timer.start()

# There is an event queue that is handled internally by the system
# Each event piles up on a list and the handler goes through each 1 by 1



## Global vs Local Variables
# Examples

a = 1
print a
print

def fun():
    a = 3
    b = a + 1
    print b

fun()

# Trying to print b in the global env throws an error
# That's a local var, while a is a global var
# This fn uses local vars

def fahren_to_kelvin(fahren):
    celsius = 5.0 / 9 * (fahren - 32)
    zero_celsius_in_kelvin = 273.15
    return celsius + zero_celsius_in_kelvin

print fahren_to_kelvin(212)

# Use the "global" keyword to reference a global var

num = 4

def fun1():
    global num
    num = 5
    
def fun2():
    global num
    num = 6
    
print num
fun1()
print num
fun2()
print num

# Note that the global var 'num' was changed
