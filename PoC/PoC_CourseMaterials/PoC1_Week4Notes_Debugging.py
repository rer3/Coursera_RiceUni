"""
Rice University / Coursera: Principles of Computing (Part 1)
Week 4: Class Notes
Debugging
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# All import statements needed.

import random

#-----------------------------------------------------------------
## Provided debugging examples (examples_math_dice_errors).

"""
Math dice game.

Roll two 12-sided dice and multiply them to get the target number.

Roll three 6-sided dice.  Combine them into a mathematical equation to
get the closest to the target as possible.

All equations are evaluated from left to right: (a op b) op c
"""

#import random

### Math operators

def add(num1, num2):
    """
    Addition
    """
    return num1 + num2

def sub(num1, num2):
    """
    Subtraction
    """
    return num1 - num2

def mul(num1, num2):
    """
    Multiplication
    """
    return num1 * num2

def div(num1, num2):
    """
    Division
    """
    return float(num1) / num2

def power(num1, num2):
    """
    Exponentiation
    """
    return num1 ** num2

### Permutations and Sequences

def gen_permutations(elems):
    """
    Compute all permuations of elems.
    """
    stack = list(elems)
    results = [[stack.pop()]]
    while len(stack) != 0:
        item = stack.pop()
        new_results = []
        for perm in results:
            for i in range(len(perm)+1):
                new_results.append(perm[:i] + [item] + perm[i:])
        results = new_results
    return results

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """    
    ans = set([()])
    for dummy_idx in range(length + 1):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans

### Dice operations

def roll(ndice, nsides):
    """
    Roll ndice with nsides.  Return a list of values.
    """
    return [random.randrange(1, nsides + 1) 
            for dummy in range(ndice)]

def product(dice):
    """
    Multiply all dice together.
    """
    result = 1
    for die in dice:
        result *= die
    return result

### Equation operations

def make_equations(ops, dice):
    """
    Make all equations
    """
    dice_orders = gen_permutations(dice)
    ops_orders = gen_all_sequences(ops.keys(), len(dice) - 1)
    results = []
    for dice_order in dice_orders:
        for ops_order in ops_orders:
            eqn = []
            for idx in range(len(ops_order)):
                eqn.append(dice_order[idx])
                eqn.append(ops_order[idx])
            eqn.append(dice_order[-1])
            val = evaluate(ops, eqn)
            eqn.append('=')
            eqn.append(val)     
            results.append(eqn)
    return results

def evaluate(ops, eqn):
    """
    Evaluate string equation of the form:

    [num, op, num, op, num]

    List can be of any length, but "num" elements must be numbers and
    "op" elements must be keys in ops dictionary.
    """
    val = eqn[0]
    idx = 1
    while idx < len(eqn):
        operation = eqn[idx]
        idx += 1
        num = eqn[idx]
        idx += 1
        val = ops[operation](val, num)
    return val

def find_closest(target, eqns):
    """
    Find equation that is closest to target value.
    """
    closest = [float('inf')]
    for eqn in eqns:
        if abs(target - eqn[-1]) < abs(closest[-1]):
            closest = eqn
    return closest

def string_equation(eqn):
    """
    Turn equation into human readable string.
    """
    streqn = "(" + str(eqn[0]) + " " + str(eqn[1])
    streqn += " " + str(eqn[2]) + ") " + str(eqn[3])
    streqn += " " + str(eqn[4]) + " " + str(eqn[5])
    streqn += " " + str(eqn[6])
    return streqn

### Game

def play():
    """
    Play round of Math Dice.
    """
    ops = {'+': add,
           '-': sub,
           '*': mul,
           '/': div,
           '**': power}

    targetdice = roll(2, 12)
    targetval = product(targetdice)
    dice = roll(3, 6)

    print "Target:", targetval, targetdice
    print "Dice:", dice

    eqns = make_equations(ops, dice)
    eqn = find_closest(targetval, eqns)

    print "Closest Equation:", string_equation(eqn)

# Uncomment to run.
#play()

##=================================================================

# Above code, with changes:

"""
Math dice game.

Roll two 12-sided dice and multiply them to get the target number.

Roll three 6-sided dice.  Combine them into a mathematical equation to
get the closest to the target as possible.

All equations are evaluated from left to right: (a op b) op c
"""

#import random

### Math operators

def add(num1, num2):
    """
    Addition
    """
    return num1 + num2

def sub(num1, num2):
    """
    Subtraction
    """
    return num1 - num2

def mul(num1, num2):
    """
    Multiplication
    """
    return num1 * num2

def div(num1, num2):
    """
    Division
    """
    return float(num1) / num2

def power(num1, num2):
    """
    Exponentiation
    """
    return num1 ** num2

### Permutations and Sequences

def gen_permutations(elems):
    """
    Compute all permuations of elems.
    """
    stack = list(elems)
    results = [[stack.pop()]]
    while len(stack) != 0:
        item = stack.pop()
        new_results = []
        for perm in results:
            for i in range(len(perm)+1):
                new_results.append(perm[:i] + [item] + perm[i:])
        results = new_results
    return results

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """    
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans

### Dice operations

def roll(ndice, nsides):
    """
    Roll ndice with nsides.  Return a list of values.
    """
    return [random.randrange(1, nsides + 1) 
            for dummy in range(ndice)]

def product(dice):
    """
    Multiply all dice together.
    """
    result = 1
    for die in dice:
        result *= die
    return result

### Equation operations

def make_equations(ops, dice):
    """
    Make all equations
    """
    dice_orders = gen_permutations(dice)
    ops_orders = gen_all_sequences(ops.keys(), len(dice) - 1)
    results = []
    for dice_order in dice_orders:
        for ops_order in ops_orders:
            eqn = []
            for idx in range(len(ops_order)):
                eqn.append(dice_order[idx])
                eqn.append(ops_order[idx])
            eqn.append(dice_order[-1])
            val = evaluate(ops, eqn)
            eqn.append('=')
            eqn.append(val)     
            results.append(eqn)
    return results

def evaluate(ops, eqn):
    """
    Evaluate string equation of the form:

    [num, op, num, op, num]

    List can be of any length, but "num" elements must be numbers and
    "op" elements must be keys in ops dictionary.
    """
    val = eqn[0]
    idx = 1
    while idx < len(eqn):
        operation = eqn[idx]
        idx += 1
        num = eqn[idx]
        idx += 1
        val = ops[operation](val, num)
    return val

def find_closest(target, eqns):
    """
    Find equation that is closest to target value.
    """
    closest = [float('inf')]
    for eqn in eqns:
        if abs(target - eqn[-1]) < abs(target - closest[-1]):
            closest = eqn
    return closest

def string_equation(eqn):
    """
    Turn equation into human readable string.
    """
    streqn = "(" + str(eqn[0]) + " " + str(eqn[1])
    streqn += " " + str(eqn[2]) + ") " + str(eqn[3])
    streqn += " " + str(eqn[4]) + " " + str(eqn[5])
    streqn += " " + str(eqn[6])
    return streqn

### Game

def play():
    """
    Play round of Math Dice.
    """
    ops = {'+': add,
           '-': sub,
           '*': mul,
           '/': div,
           '**': power}
    
    targetdice = roll(2, 12)    
    targetval = product(targetdice)
    dice = roll(3, 6)

    print "Target:", targetval, targetdice
    print "Dice:", dice

    eqns = make_equations(ops, dice)
    eqn = find_closest(targetval, eqns)

    print "Closest Equation:", string_equation(eqn)

play()

# Understand how gen_permutations works:

def gen_permutations(elems):
    """
    Compute all permuations of elems.
    """
    # Convert your elements into a list to work with
    stack = list(elems)
    # Pop off that first item
    results = [[stack.pop()]]
    print " start with results =", results
    print "~"*100
    ## Loop 1 runs out the rest of the stack, if only one item it terminates immediately
    while len(stack) != 0:
        # Pop off the next item
        item = stack.pop()
        print "LAYER ONE: while loop, stack.pop item =", item
        # Initialize en empty list for holding new permutations
        new_results = []
        ## Loop 2 runs through every permutation thus far created in results
        for perm in results:
            print "LAYER TWO: for perm:", perm, "in results:", results
            ## Loop 3 generates every sequence with the perm and new item
            for i in range(len(perm)+1):
                print "LAYER THREE: i =", i, "of", range(len(perm)+1)
                print "Append below to new results"
                print "perm[:i]=", perm[:i], "+ [item]=", item, "+ perm[i:]=", perm[i:]
                # This line, with each iteration, inserts the next item into every spot in the perm
                new_results.append(perm[:i] + [item] + perm[i:])
                print "END 3, new results =", new_results
            print "END 2", ">"*100
        # Replace results with new list of permutations
        results = new_results
        print "END LAYER ONE: results = ", results
        print "END 1", "~"*50
    # Return the list of all permutations
    return results

# Uncomment to run.
# for item in gen_permutations([1,2,2,3,5]):
    # print item
    
##=================================================================
##=================================================================