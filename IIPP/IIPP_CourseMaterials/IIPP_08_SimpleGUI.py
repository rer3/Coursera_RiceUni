# Python Test 8
# Learning the SimpleGUI custom module and its components

#These commands create frames and modify them.

# Create a new frame for interactive programs
# A frame has a control panel on the left and a canvas on the right
# Syntax: simplegui.create_frame("TITLE", canvas_width, canvas_height, control_width
# The first 3 arguments are required, and all are automatic pixel values
# The canvas_height also affects control panel height
import simplegui
#frame = simplegui.create_frame("MyFF", 100, 100)
myframe = simplegui.create_frame("MySF", 300, 300, 200)

# Change the background color of the frame's canvas (default=black)
# Syntax: FRAME.set_canvas_background("COLOR")
myframe.set_canvas_background("Lime")
# The colors that are supported by this command have odd names given to them
# The color names are capitalized and note that the color is written in quotes

# Begin the frame's interactivity
# Syntax: FRAME.start()
myframe.start()
# Note that the canvas isn't drawn until this line is run (even if the frame appears)
# All frame event handlers are started with this command, including controls

# A useful command is given for computing the width of the text in pixels
# Syntax: FRAME.get_canvas_textwidth("TEXT", font_size, "FONT FACE")
print myframe.get_canvas_textwidth("Hello", 12, "sans-serif")
# This returns "29", meaning that text in that font and size is 29 pixels wide
# "serif" (default), "sans-serif", and "monospace" are supported font faces
# This is useful in computing the position to draw text when you want to center/right-justify it


"""These commands create and modify control objects."""

# Add a text label to a frame control panel
# Syntax: FRAME.add_label("TEXT", width)
label1 = myframe.add_label("My First Label")
label2 = myframe.add_label("My Second Label", 200)
label3 = myframe.add_label("My Third Label", 200)
# Note that the width can be omitted (defaults to fit width of given text)
# The text can overflow the label if provided width < text width

# Add a button to the frame control panel
# Syntax: FRAME.add_button("TEXT", button_handler, width)
def buttonhand1():
    print "You pressed Button 1!"
def buttonhand2():
    print "You pressed Button 2!"
button1 = myframe.add_button("Button 1", buttonhand1)
button2 = myframe.add_button("Button 2", buttonhand2, 50)
# Note that the text was printed to this IDE's output instead of canvas
# If width of the button is not specified, it defaults to fit the given text
# The handler should be defined with no parameters

# Add text input box to frame control panel
# Syntax: FRAME.add_input("TEXT", input_handler, width)
def inputhand1(text):
    print "You've typed: " + text
input1 = myframe.add_input("Input 1", inputhand1, 75)
# The handler should be defined with one parameter, which is the text string
# When the user hits enter, the handler is run 

# Get the text of control object
# Syntax: CONTROL.get_text()
print label1.get_text()
print button1.get_text()
print input1.get_text()
# This command returns the text in a label, the text label of a button, or the text in the input field
# For an input field, this is useful to look at the contents before the user presses Enter

# Set the text of control object
# Syntax: CONTROL.set_text("TEXT")
label1.set_text("Label 1B")
button1.set_text("Button 1B")
input1.set_text("Default Contents")
print input1.get_text()
# A button created with no particular width is resized to fit the new text
# This is useful for default text box text 
# Note that I reran get_text() on input1 to show that it does indeed print the contents

# Set the keyboard input handler
# Syntax: FRAME.set_keydown_handler(key_handler)
# Syntax: FRAME.set_keyup_handler(key_handler)
def key1(key):
    print "Key Down!"
def key2(key):
    print "Key Up!"
myframe.set_keydown_handler(key1)
myframe.set_keyup_handler(key2)
# When any key is pressed, the keydown handler is called once
# When any key is released, the keyup handler is called once
# The handler for each should be designed with one parameter
# This parameter will receive an integer representing a keyboard char

# Set the mouse input handler
# Syntax: FRAME.set_mouseclick_handler(mouse_handler)
# Syntax: FRAME.set_mousedrag_handler(mouse_handler)
def mouse1(position):
    print position
def mouse2(position):
    print position
myframe.set_mouseclick_handler(mouse1)
myframe.set_mousedrag_handler(mouse2)
# These add keyboard event handlers waiting for mouseclick and mousedrag events
# When a mouse button is clicked, the mouseclick handler is called once
# When a mouse is dragged with the mouse button down, the mousedrag handler is called for each new position
# The handler for each should be defind with one parameter
# The parameter will receive a pair of screen coordinates (a tuple of two non-negative integers)

"""These commands draw on the canvas."""

# Set the draw handler on canvas
# Syntax: FRAME.set_draw_handler(draw_handler)
#def draw1(canvas):
    #CODE
#myframe.set_draw_handler(draw1)
# The handler should be defined with one parameter
# This parameter will receive a canvas object

# Draw text on canvas
# Syntax: CANVAS.draw_text("TEXT", point, font_size, "FONT_COLOR", "FONT_FACE")
def draw2(canvas):
    canvas.draw_text("A", (20, 20), 12, "Red")
    canvas.draw_text("B", (30, 50), 20, "Blue")
    canvas.draw_text("C", (80, 50), 12, "Gray", "serif")
myframe.set_draw_handler(draw2)
# The point is a 2-element tuple or list of screen coords representing the lower-lefthand corner of where to write text
# In order to position where the text should go, you may want to determine its width

# Draw line segment on canvas
# Syntax: CANVAS.draw_line(point1, point2, line_width, "LINE_COLOR")
def draw3(canvas):
    canvas.draw_line((50,100), (100, 150), 12, "Red")
    canvas.draw_line((10, 20), (200, 200), 20, "Blue")
myframe.set_draw_handler(draw3)
# Note that the draw2 letters are gone, overwritten with the two lines
# The line's width must be positive

# Draw connected line segments on canvas
# Syntax: CANVAS.draw_polyline(point_list, line_width, "LINE_COLOR")
def draw4(canvas2):
    canvas2.draw_polyline([(10, 20), (30, 20), (90, 70)], 12, "Green")
    canvas2.draw_polyline([(40, 20), (80, 40), (30, 90)], 20, "Gray")
myframe.set_draw_handler(draw4)
# Again, the canvas from before is overwritten
# The list of points cannot be empty
# Each point is a 2-element tuple or list of screen coords
# The line's width must be positive

# Draw polygon on canvas
# Syntax: CANVAS.draw_polygon(point_list, line_width, "LINE_COLOR", "FILL_COLOR")
def draw5(canvas):
    canvas.draw_polygon([(10, 20), (20, 30), (30, 10)], 5, "Green")
    canvas.draw_polygon([[130, 120], [140, 140], [150, 120], [110, 110]], 2, "Red")
    canvas.draw_polygon([(50, 70), (80, 40), (30, 90)], 5, "Blue", "White")
    canvas.draw_polygon([[190, 170], [180, 140], [170, 190], [170, 170]], 2, "Yellow", "Orange")
myframe.set_draw_handler(draw5)
# A line segment is added between first and last points
# Fill color defaults to "None"

# Draw circle on canvas
# Syntax: CANVAS.draw_circle(center_point, radius, line_width, "LINE_COLOR", "FILL_COLOR")
def draw6(canvas):
    canvas.draw_circle((10, 10), 20, 12, "Green")
    canvas.draw_circle([20, 30], 30, 12, "Red")
    canvas.draw_circle((50, 50), 20, 5, "Blue", "White")
    canvas.draw_circle([70, 80], 30, 10, "Yellow", "Orange")
myframe.set_draw_handler(draw6)
# Same background info as the above commands

# Draw point on canvas
# Syntax: CANVAS.draw_point(point, "COLOR")
def draw7(canvas):
    canvas.draw_point((10, 10), "Green")
    canvas.draw_point([40, 50], "Red")
myframe.set_draw_handler(draw7)

# Draw image on canvas
# Syntax: CANVAS.draw_image(image, center_source, width_height_source, center_dest, width_height_dest, rotation)
def draw8(canvas):
    canvas.draw_image(image, (1521 / 2, 1818 / 2), (1521, 1818), (100, 100), (100, 100))
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")
myframe2 = simplegui.create_frame("My Second Frame", 300, 300)
myframe2.set_draw_handler(draw8)
myframe2.start()
# Note that the new frame is the only one that pops up with these properties
# The image must be loaded in order to draw it on the canvas
# center_source is a pair of coords giving pos of the center of the image
# center_dest is coords specifying where the center of the image should be drawn on the canvas
# width_height_source is a pair of integers giving original image size
# width_height_dest is a pair of ints giving size of how the images should be drawn
# The image can be rotated clockwise by rotation radians (optional)
def draw8(canvas):
    canvas.draw_image(image, (1521 / 2, 1818 / 2), (1521, 1818), (150, 150), (300, 300), 2)
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")
myframe2.set_draw_handler(draw8)
# You can draw the whole image or just part of it
# The source info (center_source and width_height_source) specify which pixels to display
# If it attempts to use any pixels outside of the actual file size, no image will be drawn
# Specifying a different width or height in the destination than in the source will rescale the image

"""These commands load images and return sizes"""

# Load image
# Syntax: simplegui.load_image("URL")
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")
# The image can be in any format supported by the browser
# No error is raised if the file isn't found or is of an unsupported format

# Get image's width
# Syntax: IMAGE.get_width()
w = image.get_width()
print w
# Returns the width of the image in pixels
# While the image is still loading, it returns zero

# Get image's height
# Syntax: IMAGE.get_height()
h = image.get_height()
print h

