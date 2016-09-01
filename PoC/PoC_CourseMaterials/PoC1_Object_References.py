"""
Rice University / Coursera: Principles of Computing (Part 1)
Week 3 Lecture
We show how functions refer to objects and change
the referenced objects. 
"""

print "Function 1"
def func(alist):
    alist[2] = 100
    return alist

mylist = ["a", "b", "c"]
yourlist = func(mylist)

print mylist
print yourlist
print

print "Function 2"
def func2(alist):
    temp = alist
    temp[2] = 300
    return temp

ourlist = func2(mylist)

print mylist
print yourlist
print ourlist
print

print "Function 3"
# The temp variable finally refers to a new object
# as a new list is created with the list() method
def func3(alist):
    temp = list(alist)
    temp[2] = 777
    return temp

theirlist = func3(mylist)

print mylist
print yourlist
print ourlist
print theirlist
print

print "Function 4"
# The temp variable again refers to a new object
# as a new list is created using list comprehension
def func4(alist):
    temp = [item for item in alist]
    temp[2] = 9000
    return temp

lastlist = func4(mylist)

print mylist
print yourlist
print ourlist
print theirlist
print lastlist
print