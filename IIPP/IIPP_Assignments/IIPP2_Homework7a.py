"""
Rice University / Coursera: Intro to Interactive Programming in Python (Part 2)
Week 3: Homework 7a
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
    
    Let's define a class for 2D points:
        class Point 2D:
            def __init__(self, x=0, y=0):
                self.x = x
                self.y = y
            
            def translate(self, deltax=0, deltay=0):
                '''Translate the point in the x direction by deltax
                    and in the y direction by deltay.'''
                self.x += deltax
                self.y += deltay
                
            ...
    Which of the following code snippets are valid usages of the Point2D initializer
    and its translate method? For your first attempt at this problem, we suggest
    that you try to answer without using CodeSkuklptor. (Choose all).
    
    Option 1
    point = Point2D(3,9)
    translate(point, 5, -2)
    
    Option 2
    point = Point2D(3,9)
    point.translate(5,-2)
    
    Option 3
    point = Point2D([3,9])
    point.translate(5, -2)
    
    Option 4
    point1 = Point2D(3,9)
    point2 = Point2D()
    point2.translate(20,4)
    """
    # Option 1 is out because it does not reference the Point instance point 
    # correctly. 
    # Option 3 is out because a list is passed to the initializer instead
    # of two separate arguments.
    
    answer = "point = Point2D(3, 9)" + "\n"
    answer += "point.translate(5, -2)" + "\n" + "\n"
    answer += "point1 = Point2D(3, 9)" + "\n"
    answer += "point2 = Point2D()" + "\n"
    answer += "point2.translate(20, 4)"
    
    print "Question 701 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_701()

##=================================================================

def hw_702():
    """
    QUESTION 2
    
    Let's continue to use the same class for 2D points (see above). Which of the 
    following code snippets are valid usages of the Point2D initializer and its
    translate method? For your first attempt, try not to use CodeSkulptor. 
    (Choose all).
    
    Option 1
    point0 = Point2D(2, 5)
    point1 = Point2D(8, 3)
    point2 = Point2D(0, 2)
    points = [point0, point1, point2]
    for point in points:
        point.translate(-1, -1)
        
    Option 2
    points = [(2, 5), (8, 3), (0, 2)]
    for point in points:
        point.translate(-1, -1)
    
    Option 3
    point0 = Point2D(2, 5)
    point1 = Point2D(8, 3)
    point2 = Point2D(0, 2)
    points = [point0, point1, point2]
    points.translate(-1, -1)
    """
    # Option 2 is out because the list of points are not Point object instances.
    # Option 3 is out because the list points does not have a translate method.
    
    answer = "point0 = Point2D(2, 5)" + "\n"
    answer += "point1 = Point2D(8, 3)" + "\n"
    answer += "point2 = Point2D(0, 2)" + "\n"
    answer += "points = [point0, point1, point2]" + "\n"
    answer += "for point in points:" + "\n"
    answer += "    point.translate(-1, -1)" + "\n"
    
    print "Question 702 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_702()

##=================================================================

def hw_703():
    """
    QUESTION 3
    
    Let's keep it going. Which of the following code snippets (choose all) are
    valid usages of the Point2D initializer and its translate method? 
    
    Option 1
    point = Point2D(3,6)
    s = str(point)
    
    Option 2
    point = Point2D(3,6)
    tup = tuple(point)
    
    Option 3
    point = Point2D(3,6)
    s = str(point)
    newpoint = Point(s)
    
    Option 4
    point = Point2D(3,6)
    lst = list(point)
    x = lst[0]
    """
    # Option 2 is out because Point2D object is not iterable.
    # Option 3 is out because passing a string instead of an int/float for
    # x may in fact work, but I wouldn't consider it to be a "valid" use.
    # Option 4 is out because Point2D object is not iterable.
    
    answer = "point = Point2D(3, 6)" + "\n"
    answer += "s = str(point)"

    print "Question 703 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_703()

##=================================================================

def hw_704():
    """
    QUESTION 4
    
    In SimpleGUI, the func draw_image takes an optional sixth parameter that
    determines the angle of rotation of the dest rect around its center. Do pos
    values for the angle rotate the image clockwise or counterclockwise? Is the
    angle specified in degrees or radians?
    """
    
    answer = "clockwise, radians"
    
    print "Question 704 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_704()

##=================================================================

def hw_705():
    """
    QUESTION 5
    
    One interesting extension of Rice Rocks would be to have two ships, with each
    controlled by a separate player, instead of one single ship. Using the provided
    class definitions, what is the best way to represent the two ships in this
    new variant?
    
    Option 1
    In the Ship class def, duplicate every method. For ex, Ship.draw1(...) would
    be used to draw the first ship, while Ship.draw2(...) would be used to draw
    the second ship.
    
    Option 2
    Copy the Ship class code, e.g.,
        class Another_Ship:
            def __init__(self, pos, vel, angle):
                ...
            ...
    Then create two ship objects, one of each class, assigning each to a global
    variable.
        ship1 = Ship(...)
        ship2 = Another_Ship(...)
        
    Option 3
    Add another call to the Ship constructor, assigning the result to another
    global variable.
    ship1 = Ship(...)
    ship2 = Ship(...)
    
    Option 4
    In the Ship class def, change the variables pos, vel, angle to be lists of
    two values each. Then change each method to take an additional number
    argument that indicates which ship should be used. Thus, when we call the
    constructor now, we are creating both ships.
        ships = Ship(...)
    """
    
    answer = "Add another call to the Ship constructor, assigning the result to"
    answer += " another global variable." + "\n"
    answer += "    ship1 = Ship(...)" + "\n"
    answer += "    ship2 = Ship(...)"
    
    print "Question 705 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_705()

##=================================================================

def hw_706():
    """
    QUESTION 6
    
    Which of the following (choose all) fully support MP3 audio files?
    """
    
    answer = "Safari, Chrome"
    
    print "Question 706 Answer"
    print answer
    print "-"*50
    print "\n"
    
hw_706()

##=================================================================

def hw_707():
    """
    QUESTION 7
    
    Consider a spaceship where the ship's thrusters can accelerate the ship by
    10 pixels per second for each second that the thrust key is held down. If
    the friction induces a deceleration that is 10% of the ship's velocity per
    second, what is the maximal velocity of the ship? If you are having trouble,
    consider writing a short program to help you understand.
    
    Option 1
    The ship has no maximal velocity. It can reach any velocity the player desires
    if you hold the thrust key down long enough.
    
    Option 2
    Around 10 pixels per second
    
    Option 3
    Around 100 pixels per second
    
    Option 4
    Around 1000 pixels per second
    """
    # Let's think about this without having rewatched the video and without
    # writing a program. Your ship's thrusters accelerate the ship by 10 pps.
    # Okay, I'm rewatching the video now.
    
    # So from the equation vel = (1-c) * vel + thrust, the vel increases like
    # so: vel = (1-.1) * 0 + 10 = 10, vel = (1-.1) * 10 + 10 = 19, etc.
    # At vel = 100, the acceleration levels out. This is because vel = 90 + 10
    # at vel = 100 (or 90% of vel plus thrust). 
    
    answer = "Around 100 pixels per second"
    
    print "Question 707 Answer"
    print answer
    print "-"*50
    print "\n"
    
hw_707()

##=================================================================
##=================================================================