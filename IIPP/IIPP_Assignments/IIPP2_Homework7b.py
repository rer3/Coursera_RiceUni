"""
Rice University / Coursera: Intro to Interactive Programming in Python (Part 2)
Week 3: Homework 7b
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

##=================================================================

def hw_701():
    """
    QUESTION 1
    
    The class code provided for this week's mini-project supporst an ImageInfo
    class to organize the data associated with the image. Consider an ImageInfo
    object of the form:
        ImageInfo([45,45], [90,90], 35)
    What is the radius of the shape associated with this object?
    """
    
    answer = 35
    
    print "Question 701 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_701()

##=================================================================

def hw_702():
    """
    QUESTION 2
    
    Consider the provided ImageInfo and Sprite class code. Assume we want 
    ten asteroids on the screen, each looking exactly alike and using the same
    image file. How many ImageInfo objects and how many Sprite objects should
    we create?
    
    Option 1
    one ImageInfo object, one Sprite object
    
    Option 2
    ten ImageInfo objects, one Sprite object
    
    Option 3
    one ImageInfo object, ten Sprite objects
    
    Option 4
    ten ImageInfo objects, ten Sprite objects
    """
    
    answer = "one ImageInfo object, ten Sprite objects"
    
    print "Question 702 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_702()

##=================================================================

def hw_703():
    """
    QUESTION 3
    
    The version of Rice Rocks that we will implement uses only a single asteroid
    image and spawns multiple instances of the provided Sprite class using this
    image. In the original Asteroids, a large asteroid split into two medium
    asteroids which themselves split into two small asteroids.
    
    If we only had one image and wanted to implement asteroids of varying
    sizes in our version, how should we do this?
    
    Option 1
    Add a size attribute in the Sprite class and a size parameter to Sprite.__init__.
    Use the size attribute when drawing the sprite.
    
    Option 2
    Store a list of sizes for each asteroid in a global variable. Use the corresponding
    size when drawing a sprite.
    
    Option 3
    Store the size in a global variable. Use this variable when drawing a sprite.
    
    Option 4
    Add a size attribute in the ImageInfo class and a size parameter to 
    ImageInfo.__init__. Use this attribute when drawing the sprite.
    """
    
    answer = "Add a size attribute in the Sprite class and a size parameter to Sprite.__init__." + "\n"
    answer += "Use the size attribute when drawing the sprite."

    print "Question 703 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_703()

##=================================================================

def hw_704():
    """
    QUESTION 4
    
    What is the supported range of sound volumes in set_volume?
    """
    
    answer = "0 to 1"
    
    print "Question 704 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_704()

##=================================================================

def hw_705():
    """
    QUESTION 5
    
    Assume you have code that loads and plays a sound. Unfortunately, you don't hear
    anything. Which of the following (choose all) could be a reason?
    """
    
    answer = "No file is found with the given URL." + "\n"
    answer += "The given URL exists, but is inaccessible due to network problems." + "\n"
    answer += "Your browser is loading a big sound file. Wait longer." + "\n"
    answer += "You have set the volume level to 0." + "\n"
    answer += "A file found with the given URL isn't a sound file recognized by your browser."
    
    print "Question 705 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_705()

##=================================================================

def hw_706():
    """
    QUESTION 6
    
    Which of the following are valid HTML representations of the color blue (choose all)?
    """
    
    answer = "rgb(0,0,255), #0000FF, Blue"
    
    print "Question 706 Answer"
    print answer
    print "-"*50
    print "\n"
    
hw_706()

##=================================================================

def hw_707():
    """
    QUESTION 7
    
    Imagine we are writing code for something like Rice Rocks, where things are
    moving in 2D toroidal space, i.e., the wrap around all four sides of the screen.
    How can we eliminate the duplicated code in the following function?
        def move(position, vector):
            '''Moves the pos by the given vec in 2D toroidal space.'''
            position[0] = (position[0] + vector[0]) % SCREEN_SIZE[0]
            position[1] = (position[1] + vector[1]) % SCREEN_SIZE[1]
    """

    answer = "NUM_DIMENSIONS = 2" + "\n"
    answer += "def move(position, vector):" + "\n"
    answer += "    for d in range(NUM_DIMENSIONS):" + "\n"
    answer += "        position[d] = (position[d] + vector[d]) % SCREEN_SIZE[d]" + "\n"
    answer += "\n"
    answer += "def move_dimension(dimension, position, vector):" + "\n"
    answer += "    position[dimension] = (position[dimension] + vector[dimension]) % SCREEN_SIZE[dimension]" + "\n"
    answer += "def move(position, vector):" + "\n"
    answer += "    move_dimension(0, position, vector)" + "\n"
    answer += "    move_dimension(1, position, vector)" + "\n"

    print "Question 707 Answer"
    print answer
    print "-"*50
    print "\n"
    
hw_707()

##=================================================================

def hw_708():
    """
    QUESTION 8
    
    What is the primary reason for not duplicating code? 
    """
    
    answer = "You only need to get the code correct once."
    
    print "Question 708 Answer"
    print answer
    print "-"*50
    print "\n"
    
hw_708()
    
##=================================================================

def hw_709():
    """
    QUESTION 9
    
    What is Mike Massimino's greatest accomplishment?
    """
    
    answer = "Appearing on An Introduction to Interactive Programming in Python."
    
    print "Question 709 Answer"
    print answer
    print "-"*50
    print "\n"
    
hw_709()
    
##=================================================================
##=================================================================