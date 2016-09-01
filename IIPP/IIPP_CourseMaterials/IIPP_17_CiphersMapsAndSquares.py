# Python Test 17
# Ciphers, Maps, and Squares

## Ciphers

import simplegui

CIPHER = {'a': 'x', 'b': 'c', 'c': 'r', 'd': 'm', 'e': 'l'}

message = ""

# Encode button
def encode():
    emsg = ""
    for ch in message:
        emsg += CIPHER[ch]
    print message, "encodes to", emsg

# Decode button
def decode():
    dmsg = ""
    for ch in message:
        for key, value in CIPHER.items():
            if ch == value:
                dmsg += key
    print message, "decodes to", dmsg

# Update message input
def newmsg(msg):
    global message
    message = msg
    label.set_text(msg)
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Cipher", 2, 200, 200)
frame.add_input("Message:", newmsg, 200)
label = frame.add_label("", 200)
frame.add_button("Encode", encode)
frame.add_button("Decode", decode)

# Start the frame animation
frame.start()

## Demonstration of a magnifier on a map

import simplegui

# 1521x1818 pixel map of native American language
# source - Gutenberg project

image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")

# Image dimensions
MAP_WIDTH = 1521
MAP_HEIGHT = 1818

# Scaling factor
SCALE = 3

# Canvas size
CAN_WIDTH = MAP_WIDTH // SCALE
CAN_HEIGHT = MAP_HEIGHT // SCALE

# Size of magnifier pane and initial center
MAG_SIZE = 120
mag_pos = [CAN_WIDTH // 2, CAN_HEIGHT // 2]


# Event handlers
# Move magnifier to clicked position
def click(pos):
    global mag_pos
    mag_pos = list(pos)

# Draw map and magnified region
def draw(canvas):
    # Draw map
    canvas.draw_image(image, 
            [MAP_WIDTH // 2, MAP_HEIGHT // 2], [MAP_WIDTH, MAP_HEIGHT], 
            [CAN_WIDTH // 2, CAN_HEIGHT // 2], [CAN_WIDTH, CAN_HEIGHT])

    # Draw magnifier    
    map_center = [SCALE * mag_pos[0], SCALE * mag_pos[1]]
    map_rectangle = [MAG_SIZE, MAG_SIZE]
    mag_center = mag_pos
    mag_rectangle = [MAG_SIZE, MAG_SIZE]
    canvas.draw_image(image, map_center, map_rectangle, mag_center, mag_rectangle)
    
# Create frame for scaled map
frame = simplegui.create_frame("Map magnifier", CAN_WIDTH, CAN_HEIGHT)

# register even handlers
frame.set_mouseclick_handler(click)    
frame.set_draw_handler(draw)

# Start frame
frame.start()

## Calculating squares and distance

def square_list1(numbers):
    """Returns a list of the squares of the numbers in the input."""
    result = []
    for n in numbers:
        result.append(n ** 2)
    return result

def square_list2(numbers):
    """Returns a list of the squares of the numbers in the input."""
    return [n ** 2 for n in numbers]

print square_list1([4, 5, -2])
print square_list2([4, 5, -2])

def is_in_range(ball):
    """Returns whether the ball is in the desired range.  """
    return ball[0] >= 0 and ball[0] <= 100 and ball[1] >= 0 and ball[1] <= 100

def balls_in_range1(balls):
    """Returns a list of those input balls that are within the desired range."""
    result = []
    for ball in balls:
        if is_in_range(ball):
            result.append(ball)
    return result

def balls_in_range2(balls):
    return [ball for ball in balls if is_in_range(ball)]

print balls_in_range1([[-5,40], [30,20], [70,140], [60,50]])
print balls_in_range2([[-5,40], [30,20], [70,140], [60,50]])
