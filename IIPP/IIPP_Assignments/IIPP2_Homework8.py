"""
Rice University / Coursera: Intro to Interactive Programming in Python (Part 2)
Week 4: Homework 8
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

##=================================================================

def hw_801():
    """
    QUESTION 1
    
    Which of the following (choose all) is valid notation for a set in CodeSkulptor?
    
    Options: {1,2,3}, set([1,2,3]), set()
    """
    # Option 1 does not work in CodeSkulptor.
    
    answer = "set([1,2,3]), set()"
    
    print "Question 801 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_801()

##=================================================================

def hw_802():
    """
    QUESTION 2
    
    Which of the following operations can mutate set s? You may want to try
    some examples in CodeSkulptor and refer to the docs (choose all).
    
    Option 1
    s.add(x)
    
    Option 2
    t.difference_update(s)
    
    Option 3
    s.union(t)
    
    Option 4
    t.symmetric_difference(s)
    
    Option 5
    s = t
    
    Option 6
    s.intersection_update(t)
    """
    # Option 2 is out because it mutates t, not s.
    # Option 3 is out because it returns the union set instead of mutating s.
    # Option 4 is out because it also returns a set (difference between set and an iter).
    # Option 5 is a reassignment not a mutation.
    
    answer = "s.add(x)" + "\n"
    answer += "s.intersection_update(t)"
    
    print "Question 802 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_802()

##=================================================================

def hw_803():
    """
    QUESTION 3
    
    Which of the following (choose all) always give the same result as s.union(t)?
    
    Option 1
    s.union(s.symmetric_difference(t))
    
    Option 2
    t.union(t.difference(s))
    
    Option 3
    s.intersection(s.union(t))
    
    Option 4
    t.union(s)
    """
    # Let's parse what s.union(t) is exactly. This statement returns the union
    # of s and t which is all unique elements in both. Neither is mutated.
    
    # Option 1 performs a union on s and the set returned by symmetric_difference
    # of s and t, which is a set with all elements in exactly one of the sets.
    # This set does not include overlap, which means that missing elements are
    # in both s and t. A union of s with this list will always include the missing
    # elements since they are already in s (and t both). Option 1 is okay.
    
    # Option 2 performs a union on t and the set returned by difference of t 
    # and s, which is a set with all elements from t that are not in s. This means
    # the set is elements unique to t. The union of t with elements that are
    # already in t will not produce a set with any elements in s. Option 2 is out.
    
    # Option 3 returns an intersection of s and the union of s and t. The
    # intersection set includes elements that overlap between each. The
    # s.union(t) returns what you want, but then taking the intersection
    # of that with s simply returns the set s again. Option 3 is out.
    
    # Option 4 should return the same thing since neither set is mutated and
    # the same actions are performed (returning a set with all unique elems
    # between the two).
    
    answer = "s.union(s.symmetric_difference(t))" + "\n"
    answer += "t.union(s)"
    
    print "Question 803 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_803()

##=================================================================

def hw_804():
    """
    QUESTION 4
    
    A set is an unordered collection of distinct elements. Which of the following
    problem contexts represent instances of this idea? (Choose all).
    
    Options: Phonebook, Alphabetized names, Rooms in a building
    """
    answer = "Rooms in a buliding"
    
    print "Question 804 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_804()

##=================================================================

def hw_805():
    """
    QUESTION 5
    
    How many fps are typically projected in modern movies? How many times per 
    second is the draw handler typically called in CodeSkulptor? Enter two numbers
    separated by a space. 
    """
    
    answer = "24 60"
    
    print "Question 805 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_805()
  
##=================================================================

def hw_806():
    """
    QUESTION 6
    
    The bonus portion of this week's mini-project defines and uses a Sprite class
    to support animations. Each animated sprite includes an associated tiled image,
    each of whose sub-images are drawn in turn during the process of animating
    the sprite. What attribute (also known as a field) of this Sprite class can be
    used to select the appropriate sub-image to draw during this animation process?
    """
    
    answer = "age"
    
    print "Question 806 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_806()
  
##=================================================================

def hw_807():
    """
    QUESTION 7
    
    Consider a horizontally-tiled image where each sub-image has the same size.
    If each sub-image is of size 60x90 (in pixels), what is the horizontal distance
    (in pixels) between the centers of adjacent sub-images?
    
    Options: 90, 180, 60, 120
    """
    
    answer = 60
    
    print "Question 807 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_807()
  
##=================================================================

def hw_808():
    """
    QUESTION 8
    
    How many distinct numbers are printed by the following code? Enter the count.
        def next(x):
            return (x ** 2 + 79) % 997
            
        x = 1
        for i in range(1000):
            print x
            x = next(x)
    Hint: Consider how editing the code to use a set could help solve this.
    """
    # I actually have to write some code for this one. First let's start with
    # the function in the question and the following code.
    
    def _next(x):
        return (x ** 2 + 79) % 997
        
    count = set()
        
    x = 1
    for i in range(1000):
        print x
        count.add(x)
        x = _next(x)
        
    # Now just after the function definition, I will add code to add numbers
    # returned by the function to a set, then return the length of the set.
    
    answer = len(count)
    # 46
    
    print "Question 808 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_808()
  
##=================================================================

def hw_809():
    """
    QUESTION 9
    
    Which instructor exhibits the best coding style?
    
    Options: Scott, Stephen, Joe, John
    """
    # Obviously Scott.
    
    answer = "Scott"
    
    print "Question 809 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_809()
  
##=================================================================
##=================================================================