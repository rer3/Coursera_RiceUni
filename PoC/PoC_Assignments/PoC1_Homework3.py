"""
Rice University / Coursera: Principles of Computing (Part 1)
Week 3: Homework 3
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# All import statements needed.

import math
import random

##=================================================================

DIRECTIONS = '''
In this week's material, we cover the basics of probability including trials,
outcomes, and events. We also consider some simple applications of Monte Carlo
sim. This week's homework will focus on these topics.
'''

##=================================================================

def hw_301():
    """
    QUESTION 1: Basic probability
    
    What is the sum of the probabilities associated with all possible outcomes of a
    single trial? Enter the number in the box below.
    """
    # All probabilities of outcomes of a single trial sum to 1.
    
    answer = 1
    
    print "Question 301 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_301()

##=================================================================

def hw_302():
    """
    QUESTION 2
    
    Which term refers to the set of possible outcomes associated with a trial?
    Review this weeks' math notes on basic probability if necessary.
    
    Option 1
    Event
    
    Option 2
    Experiment
    
    Option 3
    Sample space
    
    Option 4
    Probability
    """
    # A quick look at the notes shows that sample space is the term for the set of
    # possible outcomes associated with a trial.
    
    answer = "Sample space"
    
    print "Question 302 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_302()
    
##=================================================================

def hw_303():
    """
    QUESTION 3: Single trials
    
    You are dealt a single card from a standard deck of 52 playing cards (4 suits
    with 13 cards in each suit). What is the probability that the card will be of a 
    specific suit? Enter the probability as a decimal number below.
    """
    # The odds of choosing a single card of a specific suit are merely 13 / 52, or
    # 1 in 4. 
    
    answer = 0.25
    
    print "Question 303 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_303()
        
##=================================================================

def hw_304():
    """
    QUESTION 4
    
    Consider a trial with 36 possible outcomes where each outcome has equal
    probability. How many outcomes correspond to an event that has probability
    1/9? Enter the number of outcomes below.
    """
    # If there are 36 possible outcomes all with probability 1/36 of occurring, we
    # determine how many outcomes correspond to an event with p = 1/9 by 
    # multiplying p * num_outcomes. Event-outcomes = prob * total-outcomes.
    
    answer = 36 / 9
    
    print "Question 304 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_304()
            
##=================================================================

def hw_305():
    """
    QUESTION 5
    
    Which Python expressions below simulate a single trial corresponding to the
    roll of a fair six-sided die whos faces are numbered 1 to 6? (Choose all).
    
    Option 1
    random.randrange(1,6)
    
    Option 2
    random.randrange(1,7)
    
    Option 3
    random.randrange(6) + 1
    
    Option 4
    random.randrange(6)
    """
    # The possible outcomes are numbers 1-6. 
    # Option 1 is out because it does not include the number 6.
    # Option 4 is out because it will choose a number between 0-5.
    # Option 2 is correct, and option 3 is a different way of coming to the
    # correct answer (it computes 0-5 then adds 1).
    
    answer = "random.randrange(1, 7)" + "\n"
    answer += "random.randrange(6) + 1"
    
    print "Question 305 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_305()    
    
##=================================================================

def hw_306():
    """
    QUESTION 6
    
    Given a standard deck of 52 cards, what is the probability that two cards drawn
    at random will have the same rank? Note that first card drawn is NOT added
    back into the deck when the second card is drawn.
    """
    # Note that you do not multiply probabilities here. You simply remove one card,
    # leaving behind 51. Out of the 51, there are 3 cards left that have the same
    # rank as the one you just drew. The probability of choosing one is 3/51, which
    # reduces to 1/17.
    
    answer = "1/17"
    
    print "Question 306 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_306()        
    
##=================================================================

def hw_307():
    """
    QUESTION 7: Expected value
    
    What is the mean GPA of class where 30% of the students have a 4.0 GPA, 40% have
    a 3.0 GPA, 20% have a 2.0 GPA, and 10% have a 1.0 GPA? Review this week's math
    if necessary. Enter the number below.
    """
    # You simply multiply the fraction of each GPA times the GPA. This is like
    # multiplying the probability of a die roll by the die number.
    
    answer = 0.3 * 4 + 0.4 * 3 + 0.2 * 2 + 0.1 * 1
    
    print "Question 307 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_307()            
    
##=================================================================

def hw_308():
    """
    QUESTION 8
    
    Consider a dice game in which you roll two dice. If the sum of the dice is odd,
    you win $1. If the sum of the dice is even, you lose $1. What is the expected
    value (in terms of your winnings) of a single roll in this game?
    
    Option 1
    The expected value is positive. If I play this game a lot, I expect to win money.
    
    Option 2
    The expected value is negative. If I play a lot, I expect to lose money.
    
    Option 3
    The expected value is zero. If I play this game a lot, I expect to break even.
    """
    # Remember that Expected Value of a trial = SIG_i=1 to k(p_i * x_i) where
    # p_i is the probability of an outcome and x_i is an outcome, and k = total
    # number of outcomes. So, you sum the p*x values for each outcome to
    # find expected value. For a fair die roll, the probability of each trial is 1/6.
    # Exp Val = (1/6)*1 + (1/6)*2 + (1/6)*3 + (1/6)*4 + (1/6)*5 + (1/6)*6,
    # which equals 3.5, which you'll notice is not a possible outcome. 
    
    # If you roll two dice, the expected value of the sum evalutes to 7 through the 
    # expression (1/36)*2 + (2/36)*3 + (3/36)*4 + (4/36)*5 + (5/36)*6 + 
    # (6/36)*7 + (5/36)*8 + (4/36)*9...(1/36)*12 where 1/36 is the probability 
    # of each pair of dice--(1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,1), (2,2), etc.
    # Since multiple pairs can equate to the same sum, as (1,2) and (2,1) both
    # sum to 3, then the probability of reaching a certain sum increases, 1/36
    # times the number of pairs that equal that sum. Multiply those probabilities
    # by the sums and then sum all of those products to get an expected value of 7.
    
    # Since the expected value = 7, it appears that the odds are in the favor of
    # a negative value being rolled.
    
    ##################################################
    ## INCORRECT: Consider the probability of rolling an even sum vs. the prob
    ## of rolling an odd sum.
    ##
    ## answer = "The expected value is positive. "
    ## answer += "If I play this game a lot, I expect to win money."
    ##################################################

    # I made a huge mistake in factoring in just what the expected value of 7 meant.
    # That meant that out of all two dice rolls, the scales tip toward a 7 popping
    # up. Though it appears that would mean a 7 might pop up the most times
    # on a longest enough timeline, that is wrong. The problem occurs similar to
    # that pointed out for single die rolls where EV = 3.5, which is not a possible
    # outcome. The EV skews what is the most likely result.
    
    # Since there are 3 even and 3 odd numbers on each die, the ration of even
    # to odd numbers if 1:1. There is a 50% chance that the die will be even or
    # odd. This is the intuitive answer and the correct one. 
    
    answer = "The expected value is zero. "
    answer += "If I play this game a lot, I expect to break even."
    
    print "Question 308 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_308()        

##=================================================================

def hw_309():
    """
    QUESTION 9
    
    What is the expected value of trial(n) as a function of n? Here, assume that n 
    is a positive integer). Enter the answer below as a math expression in n.
    
        def trial(n):
            val = random.randrange(n)
            return val
            
    As a hint, note that the arithmetic sum 0 + 1 + 2 + ... + k has a value
    1/2 * k * (k + 1).
    """
    # An analysis of the function with a few n values can clearly show the
    # sequence that results from n = 1 and beyond. At n = 1, the function chooses
    # a number between 0 and n-1, so 0 and 0. When n = 1, 0 is always returned. 
    # When n = 2, the result is either 0 or 1. EV = .5 * 0 + .5 * 1 = 0.5. When
    # n = 3, the EV is (1/3)*0 + (1/3)*1 + (1/3)*2 = 3/3 = 1. When n = 4, 
    # EV is .25*0 + .25*1 + .25*2 + .25*3 = 6/4 = 1.5. And when n = 5, EV is
    # (1/5)*0 + (1/5)*1 + (1/5)*2 + (1/5)*3 + (1/5)*4 = 10/5 = 2.
    
    # So we have the n:EV pairs from n = 1 to 5: 1:0, 2: 1/2, 3:1, 4:4/2, 5:2.
    # The EV begins at 0 when n = 1 and then increments by 1/2 each time n
    # increases by 1. The increase is n - 1 halves, so the EV as a function of n
    # must be (n - 1) / 2.
    
    answer = "(n - 1) / 2"
    
    print "Question 309 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_309()    

##=================================================================

def hw_310():
    """
    QUESTION 10: Monte Carlo sims
    
    In all of the previous problems, the sample space (space of all possible 
    outcomes) had a finite number of outcomes. However, conducting trials where
    the outcomes lies in a continuous space is perfectly reasonable.
    
    Consider the following mystery program (provided below). This program uses
    random.random() to generate a random set of points that are uniformly
    distributed over the square with corners at (1,1), (-1,1), (1,-1) and (-1,-1).
    (Here, being uniformly distributed means that each point in the square has an
    equal chance of being generated). The method then tests whether these points
    lie inside a unit circle.
    
    As one increases the number of trials, the value returned by estimate_mystery
    tends toward a specific value that has a simple expression involving a well-known
    constant. Enter this value as a math expression below (do not enter a floating
    point number). You can consult this guide (https://class.coursera.org/
    principlescomputing1-004/wiki/view?page=math_expressions) if you would like
    to see a list of math constants that Coursera's quiz system recognizes.
    """
    # The code from the mystery program is found below.

    def inside_unit_circle(point):
        """
        Compute distance of point from origin
        """
        distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
        return distance < 1                              

    def estimate_mystery(num_trials):
        """
        Main function
        """
        num_inside = 0
        
        for dumm_idx in range(num_trials):
            new_point = [2 * random.random() - 1, 2 * random.random() - 1]
            if inside_unit_circle(new_point):
                num_inside += 1
        
        return float(num_inside) / num_trials

    print estimate_mystery(10000)
    print "-"*10
    
    # The first function computes the distance of the point from (0,0). The second
    # runs num_trials trials where at each iteration, a new point is generated
    # and a conditional checks whether that point is located within the unit circle. 
    # If True, the num_inside counter is updated. The ratio of num_inside to
    # num_trials is returned (fraction that were generated inside of the square).
    # Running 10000 trials a few times generates a fraction between 0.77 and 0.79.
    
    # The mystery function generates a very large number of points all within a 
    # square, and then checks whether those points fall within a circle that is
    # perfectly embedded in the square (where d = 2). The points falling outside
    # of the circle, near the corners of the square, are not counted. Since the
    # ratio of num_inside to num_trials seems to stay roughly the same, this
    # must correspond to the ratio of the area of a circle to the area of the 
    # square in which it is embedded. 
    
    # If the radius of the circle is r, and the height and width of the square are
    # both 2 * r, then we can use that common length to generate a value
    # when comparing them. A_circle = pi * r**2, and A_square = 2r**2. The
    # ratio seems then to be (pi * r**2) / (2r * 2r) or (pi * r**2) / (4 * r**2).
    # The r**2 can be factored out, leaving pi/4. A quick check of pi/4 = 0.7854,
    # which is the ratio that was being returned by the mystery function.
    
    answer = "pi / 4"
    
    print "Question 310 Answer:"
    print answer
    print "-"*50
    print "\n"

hw_310()

##=================================================================
##=================================================================