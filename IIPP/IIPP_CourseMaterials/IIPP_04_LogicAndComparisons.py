# Python Test 4
# Logic and Comparisons

# Includes the NOT and OR arguments

a = True
b = False
c = True
d = False

print a, b
print not a
print a and b
print a or b
print (a and b) or (c and (not d))
print a and b or c and not d
# Order of ops: and > or > not

# Comparison operators: >, <, >=, <=, ==, !=

print"---"
a = 7 > 3
print a

x = 9
y = 5
b = x >= y
print b

c = "Hello" == "Hello"
print c

d = 20.6 <= 18.3
print d
print (a and b) or (c and (not d))

# 1 == True and 0 == False
print 1 == True
print 0 == False