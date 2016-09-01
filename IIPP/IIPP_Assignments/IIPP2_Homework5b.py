"""
Rice University / Coursera: Intro to Interactive Programming in Python (Part 2)
Week 1: Homework 5b
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# All import statements needed.

import simplegui

##=================================================================

def hw_501():
    """
    QUESTION 1
    
    Which of the following expressions corresponds to a dictionary with no elements?
    
    Options: dict(), (), [], {}.
    """
    
    answer = "dict()" + "\n" + "{}"
    
    print "Question 501 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_501()

##=================================================================

def hw_502():
    """
    QUESTION 2
    
    Given an existing dictionary favorites, what Python statement adds the key
    "fruit" to this dict with the value "blackberry"?
    
    Option 1
    favorites["fruit": "blackberry"]
    
    Option 2
    favorites["fruit" = "blackberry"]
    
    Option 3
    favorites["fruit"] = "blackberry"
    
    Option 4
    favorites{"fruit": "blackberry"}
    """
    # Options 1-2 and 3 are syntactically incorrect.
    
    answer = "favorites['fruit'] = 'blackberry'"
    
    print "Question 502 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_502()

##=================================================================

def hw_503():
    """
    QUESTION 3
    
    Keys in a dict can have which of the following types? (Choose all).
    
    Options: lists, booleans, numbers, dictionaries, strings.
    """
    # Keys must be of immutable types.
    
    answer = "Booleans" + "\n" + "Numbers" + "\n" + "Strings"
    
    print "Question 503 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_503()

##=================================================================

def hw_504():
    """
    QUESTION 4
    
    Values in a dict can have which of the following types? (Choose all).
    
    Options: strings, booleans, numbers, tuples.
    """
    # Values can be mutable or immutable.
    
    answer = "Strings" + "\n" + "Booleans" + "\n" + "Numbers" + "\n" + "Tuples"
    
    print "Question 504 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_504()

##=================================================================

def hw_505():
    """
    QUESTION 5
    
    We often want to loop over all the key/value pairs in a dictionary. Assume the 
    variable my_dict stores a dictionary. One way of looping is as follows:
        for key in my_dict:
            value = my_dict[key]
            ...
    Howevger, there is a better way. We can instead write the following:
        for key, value in ???:
            ...
            
    What code should replace the ??? so that the two forms are equivalent?
    
    Option 1
    list(my_dict)
    
    Option 2
    my_dict.keys_values()
    
    Option 3
    my_dict.values()
    
    Option 4
    items(my_dict)
    
    Option 5
    my_dict.keys()
    
    Option 6
    my_dict.items()
    """
    # Option 1 is out because it creates a list of the keys in my_dict.
    # Options 2 and 4 are syntactically incorrect.
    # Option 3 is out because it only returns the values and no keys.
    # Option 5 is out because it only returns the keys and no values.
    
    answer = "my_dict.items()"
    
    print "Question 505 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_505()

##=================================================================

def hw_506():
    """
    QUESTION 6
    
    Conceptually, the purpose of a dictionary is to represent a relationship between
    two collections of data--each key is related to one value. Which of the following
    situations are instances of such a relationship?
    
    Do not include situations where you have to introduce additional information
    in order to fit them into such a relationship. (Choose all).
    
    Option 1
    Storing students' IDs and grades for a particular assignment.
    
    Option 2
    Computing averages
    
    Option 3
    Storing x and y coordinates of an arbitrary collection of 2D points.
    
    Option 4
    Storing where each person lives
    """
    # The focus of this question is on the relationship between data, specifically,
    # that between two corresponding data points. 
    # Option 2 is out because it relates to computation vs. storing data.
    # Option 3 is out because it only makes sense if the points were for a function,
    # so that each x coordinate occurred at most once.
    
    answer = "Storing students' IDs and grades." + "\n"
    answer += "Storing where each person lives."
    
    print "Question 506 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_506()
    
##=================================================================

def hw_507():
    """
    QUESTION 7
    
    Assume we have the definition:
        def is_even(number):
            '''
            Returns whether the number is even.
            '''
            return number % 2 == 0
            
    Which of the following will compute a list of all of the even elements of 
    list my_list?
    
    Option 1
    [is_even(number) for number in my_list]
    
    Option 2
    [n for n in my_list if is_even(n)]
    
    Option 3
    [if is_even(number): number for number in my_list]
    
    Option 4
    [number for number in my_list if is_even(number)]
    """
    # I will attempt these in CodeSkulptor.
    
    def is_even(number):
        return number % 2 == 0
        
    my_list = [1,2,3,4,5,6,7,8,9]
        
    print [is_even(number) for number in my_list]
    print "-"*10
    # Option 1 is out; this returns True/False values.
    # Printed: [False, True, False, True, False, True, False, True, False]
    
    print [n for n in my_list if is_even(n)]
    print "-"*10

    #print [if is_even(number): number for number in my_list]
    #print "-"*10
    # Option 3 is out; this is syntactically incorrect.
    
    print [number for number in my_list if is_even(number)]
    print "-"*10
    
    # The is_even function returns a True or False value based on whether or not
    # number % 2 == 0 (i.e. the number is even). Option 1 adds this direct
    # result to the printed list. Option 3 is syntactically incorrect because it
    # begins with an if statement. Both options 2 and 4 perform the same function
    # using different variable names (n vs. number): a for loop iterates over
    # the numbers in my_list and executes is_even on each; if True is returned,
    # the number is added to the printed list. Remember, True = even number.

    answer = "[n for n in my_list if is_even(n)]" + "\n"
    answer += "[number for number in my_list if is_even(number)]"
    
    print "Question 507 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_507()
    
##=================================================================

def hw_508():
    """
    QUESTION 8
    
    You have the following code. The goal is to display a portion of the image,
    rescaling it to fill the canvas.
    
        import simplegui

        frame_size = [200, 200]
        image_size = [1521, 1818]

        def draw(canvas):
            canvas.draw_image(image, image_size,
                              [image_size[0] / 2, image_size[1] / 2],
                              [frame_size[0] / 2, frame_size[1] / 2],
                              frame_size)

        frame = simplegui.create_frame("test", frame_size[0], frame_size[1])
        frame.set_draw_handler(draw)
        image = simplegui.load_image("http://commondatastorage.googleapis.com/ \
        codeskulptor-assets/gutenberg.jpg")

        frame.start()
        
    Run it and observe that nothing is displayed in the frame. What is the problem?
    
    Option 1
    One or more of the draw_image args are of the wrong type.
    
    Option 2
    The destination args in draw_image are incorrect. We aren't specifying values
    that would draw the image on this size canvas.
    
    Option 3
    The file doesn't exist.
    
    Option 4
    The file is not an image.
    
    Option 5
    The source args in draw_image are incorrect. We are trying to load pixels
    that are not within the image, and thus the draw fails.
    """
    # The syntax of the draw_image canvas method in simplegui is:
    # canvas.draw_image(image, center_src, width_height_src, center_dest, 
    # width_height_dest). The first arg is the image, which is loaded into the
    # var "image" in the above code. The second arg is the center point of the
    # source image, and the third arg is the width and height of the source image.
    # The fourth and fifth args are the destination center and width/height values.
    # These last two args place the image on the canvas and size it.
    
    # Options 3-4 are out as I will assume this image is at that link and is an image.
    # Option 1 is out as the args appear to be of the correct type.
    # Option 2 is out as the destination args appear to be correct. The first is
    # the center of the canvas (dest center) and the second is the size of the
    # canvas (dest width/height values).
    
    # Option 5 is the problem as the center_src and width_height_src args are
    # swapped with each other. If you switch them, the code works. 
    
    answer = "The source args in draw_image are incorrect. We are trying to load "
    answer += "pixels that are not within the image, and thus the draw fails."
    
    print "Question 508 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_508()    
        
##=================================================================

def hw_509():
    """
    QUESTION 9
    
    Write a CodeSkulptor program that loads and draws the following image:
    
    http://commondatastorage.googleapis.com/codeskulptor-assets/alphatest.png
    
    with a source center of [220, 100] and a source size of [100, 100]. What one 
    word apears in the canvas? Enter capital letters as capital letters if applicable.
    """
    # I used the code from question 8 and swapped the link and src args.
    
    answer = "tin"
    
    print "Question 509 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_509()    
            
##=================================================================
##=================================================================