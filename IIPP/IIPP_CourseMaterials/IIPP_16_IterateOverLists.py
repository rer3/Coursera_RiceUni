# Python Test 16
# Iterate Over Lists

# Count the number of odds in the list

def count_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 1:
            count += 1
    return count
    
# Check if the list contains any odd numbers

def check_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            return True
    return False
    
# Remove odds in list of numbers
'''First example will cause an error as it removes elems of a list that is 
currently being iterated over'''

def remove_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            numbers.remove(num)

'''Second example attempts to remedy this by storing the indices of odd
numbers in the list in a separate list, then iterating over the original list
and removing elems at those indices...however this causes the exact same
error to occur, as it pops from the list as it iterates.'''

def remove_odd2(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(numbers.index(num))
            
    for idx in remove:
        numbers.pop(idx)
        
'''Third example uses the remove() method inherent to Python lists, however
this creates yet again the same error as before.'''
        
def remove_odd3(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(num)
            
    for num in remove:
        numbers.remove(num)
        
'''The solution in the fourth attempt is to store the even nums in a separate
list and then return that.'''
        
def remove_odd4(numbers):
    newnums = []
    for num in numbers:
        if num % 2 == 0:
            newnums.append(num)
    return newnums
    
'''The example below encounters a different problem: the last odd is not
removed, but instead the first odd is removed. Though the correct number
is stored in the last_odd var, the first time that element is encountered in the
passed list, that one is removed. The solution is to iterate through the list
backwards to remove the first occurrence from the right.'''

def remove_last_odd(numbers):
    has_odd = False
    last_odd = 0
    for num in numbers:
        if num % 2 == 1:
            has_odd = True
            last_odd = num
            
    if has_odd:
        numbers.remove(last_odd)
        
'''The solved function returns the new list without the last odd.'''
        
def remove_last_odd2(numbers):
    has_odd = False
    last_odd = 0
    for num in numbers:
        if num % 2 == 1:
            has_odd = True
            last_odd = num
            
    if has_odd:
        copy = list(numbers)
        copy.reverse()
        copy.remove(last_odd)
        copy.reverse()
    return copy

def run():
    numbers = [1, 7, 2, 34, 8, 7, 2, 5, 14, 22, 93, 48, 76, 15, 7]
    print numbers
    remove_last_odd(numbers)
    print numbers
    
run()