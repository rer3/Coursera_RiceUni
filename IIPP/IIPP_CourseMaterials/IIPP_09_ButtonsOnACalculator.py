# Python Test 9
# Buttons on a Calculator

# Building a calculator
# Calculator logic:
#	Data
##		Store
##		Operand
#	Operations
##		Print
##		Swap
##		Add
##		Subtract
##		Multiply
##		Divide
# Basic calculator computation
# Store = store operation operand

# Starting point for calculator
import simplegui
# Initialize globals
store = 0 # changed from 12
operand = 0 # changed from 3
# Define functions that manipulate store and operand
def output():
    """Prints output"""
    print "Store = ", store
    print "Operand = ", operand
    print ""
def swap():
    """Swaps store and operand"""
    global store, operand
    store, operand = operand, store
    output()
def add():
    """Adds operand to store"""
    global store
    store = store + operand
    output()
def sub():
    """Subtracts operand from store"""
    global store
    store = store - operand
    output()
def mult():
    """Multiplies store by operand"""
    global store
    store = store * operand
    output()
def div():
    """Divides store by operand"""
    global store
    if (operand == 0): # I added this to avoid an error
        print "You can't divide by zero"
    else:
        store = store / operand
        output()
def enter(inp):
    global operand
    operand = float(inp)
    output()
# Create a frame
frame = simplegui.create_frame("Calculator", 300, 300)
# Register event handlers
frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Sub", sub, 100)
frame.add_button("Mult", mult, 100)
frame.add_button("Div", div, 100)
frame.add_input("Enter operand", enter, 100)
# Start the frame
frame.start()

# Now we can create an input field to enter numbers
# We'll have a bare bones version of a modern calculator
# We want a number input, but let's see what we can do w/ text
# The input handler is called with a single parameter, what the user entered
# We have to have this parameter in the function