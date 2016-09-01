# Python Test 11
# Canvas, Strings, and Units

import simplegui

#Define draw handler
def draw(canvas):
    canvas.draw_text("Hello!", [100,100], 24, "red")
    canvas.draw_circle([100,100], 2, 2, "white")

#Create frame
frame = simplegui.create_frame("Test", 300, 200)

#Register draw handler
frame.set_draw_handler(draw)

#Start frame
frame.start()

#String processing

#String literals
s1 = "Bobby's string"
s2 = "Another string"
s3 = " And another one"
print s1, s2
print s3

#Combine strings (concatenate)
s4 = s1 + s2
print s4

#Find pieces of strings
print s1[0]
print s4[5]
print s1[-1] #Find last character of string
print len(s1) #Print length of string
print s1[0:7] #Print out a slice of a string
#Slices do not include the last char indexed
print s1[0:6] + s2[6:]
#Leaving the second index blank references rest of string from first index on
print s1[:8]
#This works in reverse

#Converting strings
s5 = str(375)
print s5[1:]
int1 = int(s5[1:])
print int1 + 36

#Convert xx.yy to xx dollars and yy cents
def convert(val):
    dollars = int(val)
    cents = int(100 * (val - dollars))
    return str(dollars) + " dollars and " + str(cents) + " cents"

print convert(11.23)
print convert(11.20)
print convert(1.12)
print convert(12.01)
print convert(1.01)
print convert(0.01)
print convert(1.00)
print convert(0)
print convert(-1.40)
print convert(12.55555)


def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result
        
# convert xx.yy to xx dollars and yy cents
def convert2(val):
    # Split into dollars and cents
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))

    # Convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string

print
print convert2(11.23)
print convert2(11.20) 
print convert2(1.12)
print convert2(12.01)
print convert2(1.01)
print convert2(0.01)
print convert2(1.00)
print convert2(0)