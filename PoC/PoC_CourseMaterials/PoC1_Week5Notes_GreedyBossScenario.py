"""
Rice University / Coursera: Principles of Computing (Part 1)
Week 5: Class Notes
The Greedy Boss Scenario and Simulator
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# All import statements needed.

import codeskulptor
import math
import simpleplot
codeskulptor.set_timeout(60)

#-----------------------------------------------------------------
## Provided solution to Greedy Boss Simulator. Here it has been encapsulated
## in a function to avoid references to its functions and constants by my
## implementation. This is here only for reference and comparison post-completion.

def poc_greedy_solution():
    """
    Simulator for greedy boss scenario.
    """
    STANDARD = True
    LOGLOG = False

    # constants for simulation
    INITIAL_SALARY = 100
    SALARY_INCREMENT = 100
    INITIAL_BRIBE_COST = 1000

    def greedy_boss(days_in_simulation, bribe_cost_increment, plot_type = STANDARD):
        """
        Simulation of greedy boss
        """
        # initialize necessary local variables
        current_day = 0
        current_savings = 0
        total_salary_earned = 0
        current_bribe_cost = INITIAL_BRIBE_COST
        current_salary = INITIAL_SALARY
        
        # initialize list consisting of days vs. total salary earned for analysis
        days_vs_earnings = [(0, 0)]

        # Each iteration of this while loop simulates one bribe
        while current_day < days_in_simulation:
            
            # check whether we have enough savings to bribe without waiting
            if current_savings > current_bribe_cost:
                days_to_next_bribe = 0
            else:
                time_to_next_bribe = (current_bribe_cost - current_savings) / float(current_salary)
                days_to_next_bribe = int(math.ceil(time_to_next_bribe))
            
            # advance current_day to day of next bribe (DO NOT INCREMENT BY ONE DAY)
            current_day += days_to_next_bribe

            # update state of simulation to reflect bribe
            current_savings += days_to_next_bribe * current_salary
            current_savings -= current_bribe_cost
            total_salary_earned += days_to_next_bribe * current_salary
            current_bribe_cost += bribe_cost_increment
            current_salary += SALARY_INCREMENT

            # update list with days vs total salary earned for most recent bribe
            # use plot_type to control whether regular or log/log plot
            if plot_type == STANDARD:
                days_vs_earnings.append((current_day, total_salary_earned))
            else:
                days_vs_earnings.append([math.log(current_day), math.log(total_salary_earned)])
            
        return days_vs_earnings

    def run_simulations():
        """
        Run simulations for several possible bribe increments
        """
        plot_type = STANDARD
        days = 70
        inc_0 = greedy_boss(days, 0, plot_type)
        inc_500 = greedy_boss(days, 500, plot_type)
        inc_1000 = greedy_boss(days, 1000, plot_type)
        inc_2000 = greedy_boss(days, 2000, plot_type)
        simpleplot.plot_lines("Greedy boss", 600, 600, "days", "total earnings", 
                              [inc_0, inc_500, inc_1000, inc_2000], False,
                             ["Bribe increment = 0", "Bribe increment = 500",
                              "Bribe increment = 1000", "Bribe increment = 2000"])

    run_simulations()

    print greedy_boss(35, 100)
    # should print [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), 
    # (29, 7900), (31, 9300), (33, 10900), (35, 12700)]

    print greedy_boss(35, 0)
    # should print [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), 
    # (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), 
    # (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900)]
   
#-----------------------------------------------------------------
## Provided template for greedy boss sim (poc_greedy_template).

STANDARD = True
LOGLOG = False

# constants for simulation
INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000


def greedy_boss(days_in_simulation, bribe_cost_increment, plot_type = STANDARD):
    """
    Simulation of greedy boss
    """
    """
    Simulation of greedy boss
    """
    salary = INITIAL_SALARY
    savings = 0
    earnings = 0
    bribe_cost = INITIAL_BRIBE_COST
    current_day = 0
    days_vs_earnings = [(0, 0)]

    while current_day < days_in_simulation:
    
        if savings >= bribe_cost:
            days_to_next_bribe = 0
        else:
            days_to_next_bribe = int(math.ceil((bribe_cost - savings) / float(salary)))

        current_day += days_to_next_bribe

        savings += salary * days_to_next_bribe
        savings -= bribe_cost
        bribe_cost += bribe_cost_increment
        earnings += salary * days_to_next_bribe
        salary += SALARY_INCREMENT
        
        if plot_type == STANDARD:
            days_vs_earnings.append((current_day, earnings))
        else:
            days_vs_earnings.append([math.log(current_day), math.log(earnings)])
       
    return days_vs_earnings

def run_simulations():
    """
    Run simulations for several possible bribe increments
    """
    plot_type = STANDARD
    days = 70
    inc_0 = greedy_boss(days, 0, plot_type)
    inc_500 = greedy_boss(days, 500, plot_type)
    inc_1000 = greedy_boss(days, 1000, plot_type)
    inc_2000 = greedy_boss(days, 2000, plot_type)
    simpleplot.plot_lines("Greedy boss", 600, 600, "days", "total earnings", 
                          [inc_0, inc_500, inc_1000, inc_2000], False,
                         ["Bribe increment = 0", "Bribe increment = 500",
                          "Bribe increment = 1000", "Bribe increment = 2000"])

# Uncomment function calls below to run.

#run_simulations()

#print greedy_boss(35, 100)
# should print [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), 
# (29, 7900), (31, 9300), (33, 10900), (35, 12700)]

#print greedy_boss(35, 0)
# should print [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), 
# (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), 
# (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900)]

##=================================================================

DIRECTIONS = '''
In life, you are often faced with a fundamental choice: do I enjoy the benefits
of the resources that I have earned or invest those resources so as to improve
my life in the long-term? For example, if you've graduated from college, you may
have been faced with the choice: do I find a job and enjoy the immediate benefits
of earning a reasonable salary, or do I go to graduate school with the prospect
of getting a better job in the future but while I pay more tuition and have no
money? 

One of the reasons for the popularity of the real-time strategy games like Warcraft
and Starcraft is that they allowed the player to experiment with different strategies
for resources allocation. One strategy might be to immediately generate lots of
weak low cost  units and try to overwhelm an opponent who is investing in developing
the technological capability to build more powerful (and costly) units.

This week's project involves building a sim for the web-based game Cookie Clicker.
In that game, your goal is to bake as many cookies as possible in a given period
of time (or, alternatively, bake a fixed number of cookies as quickly as possible).
Game play in Cookie Clicker involves choosing strategically among several methods
of upgrading your ability to bake cookies with the goal of baking as many cookies
as quickly as possible.

The Greedy Boss Scenario
----------
Since the sim that makes up Cookie Clicker is fairly complex, this practice activity
considers a simpler scenario as described in the following forum post from the first
session of Principles of Computing.
    "Let's say you have a job that pays a salary of $100/day. You know your boss
    can be bribed to increase your salary to $200/day if you pay him $1000. How long
    would it take you to earn $1000 for the bribe? How much would you be paid after
    the bribe? If you bribed your boss as soon as you have enough money saved up
    for the bribe, how much money would you have earned (bribes included) in 20 days?
    Now what happens if your boss is really greedy and will increase your salary by
    $100/day every time you give him $1000? How fast would your salary increase?
    Finally, let say that your boss is both greedy and smart. He wants a bigger bribe
    every time he increases your salary. What would happen? This is Cookie Clicker."

Implementing a Greedy Boss Sim
----------
Your task in this activity is to write a sim for the greedy boss scenario described
above. This sim will follow a simple strategy designed to increase your current salary
as quickly as possible. In particular, the sim should bribe the boss at the end of
the first day where your current savings is sufficient to afford the cost of the 
bribe. To get you started, we have created a program template (found above) that
implements some of the non-essential parts of the sim.

In your sim, you should assume that your initial salary is $100/day and that each
bribe paid to your boss increases your salary by $100/day. You can also assume that
the cost of the initial bribe is $1000. Your main task is to complete the body of the
function greedy_boss(days_in_simulation, bribe_cost_increment, plot_type) which
takes as input the number of days in the sim (an integer) and the amount by which
your boss increases the cost of a bribe after each bribe (an integer). The final
parameter has either the constant value STANDARD or LOGLOG and specifies whether
the returned list is in standard scale or log/log scale.

The function greedy_boss() should return the list days_vs_earnings. To signal the
start of the sim, the return list days_vs_earnings is initialized with the tuple
(0,0). Earnings from your daily salary should then accumulate starting at day 1
and so forth. Subsequent tuples added to the list should consist of the day when
a bribe takes place and the total salary earned up to and including that day.
This total salary earned should include money spent on the current day's bribe as
well as all previous bribes.

More Details of the Implementation
----------
While implementing greedy_boss(), you should settle on the various quantities that
the sim will need to maintain as part of the sim and then initialize those quantities
appropriately. You should then implement the body of the while loop in the template.
Note that this loop should increment the variable current_days during each execution
of its body. However, each iteration of the loop should advance the current day
directly to the day of the next bribe instead of incrementing the current day by a
single day. Advancing the current day directly to the day of the next bribe makes the
resulting sim more efficient since nothing interesting happens while waiting to 
accumulate enough savings to afford a bribe. We will take this same approach in
Cookie Clicker. 

One important feature of the greedy boss scenario is that the boss accepts bribes 
only at the end of the day after your daily salary has been paid. As a result, any
daily earnings that are unspent on the bribe should be retained for future bribes.
Also, in some situations, your salary may be large enough that you can afford to
pay the boss several bribes at the end of the day.  Your boss will happily accept
them and this behavior should be incorporated into your implementation.

The bottom of the template includes two example inputs and outputs designed to
help in debugging your code. Note that the second example includes two bribes
being paid at the end of day 34. We suggest that you make a substantial attempt
at completing this activity on your own. While peeking at our sample solution of
the greedy boss sim is very tempting, working through this problem on your own
is worthwhile. The behavior of the greedy boss sim is designed to mimic the behavior
of the simulatore that you will build for Cookie Clicker. Time spent here is time
saved working on that project.

Experimenting With the Greedy Boss Sim
----------
Once you are satisfied with your implementation of greedy_boss(), you are welcome
to consult our implementation (found above in the shared area). The function 
run_simulation calls the simulator for a specified number of days with various values
for the cost increments of a bribe. If you examine the plots for total salary earned
as a function of days passed, you will note (not surprisingly) that, if the boss
doesn't ask for any increase in the cost of the bribe, total salary earned (including
the cost of the bribes) increases fastest as a function of days past. As the size of
the increments to the bribe increases, total salary earned increases at a slower
rate. Much of Homework 5 will consider the behavior of the greedy boss sim.
'''

##=================================================================

# The provided template is sparse. The constants are defined. Inside the greedy_boss
# function, the days_vs_earnings local var is initialized to [(0,0)], and the first
# line of the while loop is provided (while current_day <= days_in_simulation:). 
# The run_simulations function, its call below, and the two calls to greedy_boss
# are also provided. Only comment lines giving instruction are left.

# Updates to the function will be made to the template in the shared area. The calls
# to run_simulations and greedy_boss will be commented out until I have implemented
# the function and tested it to verify that it works. To avoid scrolling up and down
# through this doc, dummy functions will be built below, and their contents pasted
# into the greedy_boss function in the shared area.

# First I will initialize the variables. These will be, at minimum, salary and bribe
# cost, respectively $100 and $1000 at the start. The current_day used by the
# while loop will also have to be initialized, presumably to 1 since you can't
# work on your zeroth day, not to mention days_vs_earnings already has the
# tuple (0,0) that would correspond to this pre-work state (i.e. day 0). Also,
# savings will need to be tracked, as that decides when a bribe can be made.
# Also, since total earnings is stored in the tuple for analysis via simpleplot,
# this should probably be initialized (duh).

# Next, the meat of this function--the while loop--must be developed. It will 
# execute up to and including the number of days specified by days_in_simulation.
# The first step is to go through a typical day and then increase the savings and
# earnings by the salary (since bribes can't be made until the end of the day after
# payment is made to you for services rendered). Second, as per the comment
# in the template, check whether we have enough savings to bribe without waiting.
# I will put a statement here to bribe as many times as you can.

# To advance the days to the next bribe, I'll rearrange the simple equation:
# savings + salary*days >= bribe_cost. This seems like the obvious relationship
# to me since you want your savings plus future earnings to be >= bribe cost so
# that you can afford it. You want to find the smallest number of days to achieve
# this. If savings = 100 and bribe cost is 500, with a salary of 100, you calculate:
# 1 day: 100 + 100*1 >= 500? NO.
# 2 days: 100 + 100*2 >= 500? NO.
# 3 days: 100 + 100*3 >= 500? NO.
# 4 days: 100 + 100*4 >= 500? YES.
# So the answer here is 4 days. Plug that into:
# days = (bribe_cost - savings) / salary
# days = (500 - 100) / 100 = 4 (correct!).
#
# Note that this will automatically round down, so the result will have to be evaluated
# as a float, rounded up, and then converted to an integer. I stole this from the
# solution, to be perfectly frank.

# The comment "update state of simulation to reflect bribe" wasn't obvious
# to me at first, but a quick (I mean quick) peak at the reference solution showed
# the local variables being updated to reflect the jump across multiple days until
# the next bribe. So that is what I will attempt to do there. Since this includes
# a change to the salary and earnings variables, I can either remove the increments
# to salary and earnings at the top of the while loop, or I can update the variables
# minus one day. I will choose the latter since it is different from what's been
# implemented in the reference solution.

# The final step is to update days_vs_earnings to include the number of days it
# took to get to the current bribe and the earnings up to that point. 

def gb01(days_in_simulation, bribe_cost_increment, plot_type = STANDARD):
    """
    Simulation of greedy boss
    """
    # initialize necessary local variables
    salary = 100
    savings = 0
    earnings = 0
    bribe_cost = 1000
    current_day = 1
    
    # initialize list consisting of days vs. total salary earned for analysis
    days_vs_earnings = [(0, 0)]

    # Each iteration of this while loop simulates one bribe
    while current_day <= days_in_simulation:
        # make those dollars first
        savings += salary
        earnings += salary
        
        # check whether we have enough savings to bribe without waiting
        if savings >= bribe_cost:
            while savings >= bribe_cost:
                savings -= bribe_cost
                salary += 100
                bribe_cost += bribe_cost_increment
        
        # advance current_day to day of next bribe (DO NOT INCREMENT BY ONE DAY)
        days_to_next_bribe = int(math.ceil((bribe_cost - savings) / float(salary)))
        current_day += days_to_next_bribe

        # update state of simulation to reflect bribe
        savings += salary * (days_to_next_bribe - 1)
        earnings += salary * (days_to_next_bribe - 1)

        # update list with days vs total salary earned for most recent bribe
        days_vs_earnings.append((current_day, earnings))
        # use plot_type to control whether regular or log/log plot
       
    return days_vs_earnings
    
# Without implementing the final step involving the plot, I will test out this
# implementation below using examples from the template. Uncomment to run tests.

print "Testing gb01"
print "ACTUAL:", gb01(35, 100)
print "EXPECT:", [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), \
                  (29, 7900), (31, 9300), (33, 10900), (35, 12700)]

print "ACTUAL:", gb01(35, 0)
print "EXPECT:", [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), 
                  (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), 
                  (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900)]
print "-"*10

# The two lists returned were, respectively:

# [(0, 0), (10, 900), (16, 2000), (20, 3100), (23, 4200), (26, 5600), (29, 7300), 
# (31, 8600), (33, 10100), (35, 11800), (37, 13700)]

# [(0, 0), (10, 900), (15, 1800), (19, 2900), (21, 3600), (23, 4500), (25, 5600), 
# (27, 6900), (28, 7600), (29, 8400), (30, 9300), (31, 10300), (32, 11400), 
# (33, 12600), (34, 13900), (35, 15300), (36, 16900)]

# I can see already that my decision to not include the final salary bump in the
# block that updates savings and earnings at the end of the loop has affected
# the results. Though this *may* still show roughly accurate estimates when the
# data points are plotted, this is still inaccurate and must be fixed. My second
# attempt below will have these savings and earnings increments removed from the
# top of the loop and dependent statements will be updated to reflect this.
# I will also initialize current_day to 0.


def gb02(days_in_simulation, bribe_cost_increment, plot_type = STANDARD):
    """
    Simulation of greedy boss
    """
    # initialize necessary local variables
    salary = 100
    savings = 0
    earnings = 0
    bribe_cost = 1000
    current_day = 0
    
    # initialize list consisting of days vs. total salary earned for analysis
    days_vs_earnings = [(0, 0)]

    # Each iteration of this while loop simulates one bribe
    while current_day <= days_in_simulation:
        
        # check whether we have enough savings to bribe without waiting
        if savings >= bribe_cost:
            while savings >= bribe_cost:
                savings -= bribe_cost
                salary += 100
                bribe_cost += bribe_cost_increment
        
        # advance current_day to day of next bribe (DO NOT INCREMENT BY ONE DAY)
        days_to_next_bribe = int(math.ceil((bribe_cost - savings) / float(salary)))
        current_day += days_to_next_bribe

        # update state of simulation to reflect bribe
        savings += salary * (days_to_next_bribe)
        earnings += salary * (days_to_next_bribe)

        # update list with days vs total salary earned for most recent bribe
        days_vs_earnings.append((current_day, earnings))
        # use plot_type to control whether regular or log/log plot
       
    return days_vs_earnings
    
print "Testing gb02"
print "ACTUAL:", gb02(35, 100)
print "EXPECT:", [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), \
                  (29, 7900), (31, 9300), (33, 10900), (35, 12700)]

print "ACTUAL:", gb02(35, 0)
print "EXPECT:", [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), 
                  (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), 
                  (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900)]
print "-"*10

# The two lists returned were, respectively:

# [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), (29, 7900), 
# (31, 9300), (33, 10900), (35, 12700), (37, 14700)]

# [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), (25, 6200), 
# (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), (32, 12600), 
# (33, 13900), (34, 15300), (35, 16900), (36, 18600)]

# The first returned list is accurate up to the last element in it, but it includes
# a final element, (37, 14700), that is not in the expected list.
# The second returned list is accurate up until day 34, when it ceases to store
# TWO bribe increments for that day. Either I can do what is done in the solution
# (which I can't recall because I refuse to look at it before finishing this), or I
# could add a num_bribes variable and append that many tuples to the days
# vs. earnings list. I will do that. Also, the actual list includes an ADDITIONAL
# element, (36, 18600), that is not in the expected list.

# Each actual list appended one final tuple that was outside the range of days_in_sim
# passed to the function. I can add a check here to see if days_to_next_bribe is 
# beyond the days in the sim and, if so, replace it with days_in_sim - current_day.
# Note, however, that a tuple would not be appended to the days vs earnings list
# if the latter value is used to increment the local variables.

def gb03(days_in_simulation, bribe_cost_increment, plot_type = STANDARD):
    """
    Simulation of greedy boss
    """
    salary = 100
    savings = 0
    earnings = 0
    bribe_cost = 1000
    current_day = 0
    days_vs_earnings = [(0, 0)]

    while current_day <= days_in_simulation:
    
        num_bribes = 1
        
        if savings >= bribe_cost:
            while savings >= bribe_cost:
                savings -= bribe_cost
                salary += 100
                bribe_cost += bribe_cost_increment
                num_bribes += 1
        
        days_to_next_bribe = int(math.ceil((bribe_cost - savings) / float(salary)))
        current_day += days_to_next_bribe
        
        if days_to_next_bribe > days_in_simulation - current_day:
            savings += salary * (days_in_simulation - current_day)
            earnings += salary * (days_in_simulation - current_day)
        else:
            savings += salary * (days_to_next_bribe)
            earnings += salary * (days_to_next_bribe)
            for dummy_idx in range(num_bribes):
                days_vs_earnings.append((current_day, earnings))
       
    return days_vs_earnings
    
print "Testing gb03"
print "ACTUAL:", gb03(35, 100)
print "EXPECT:", [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), \
                  (29, 7900), (31, 9300), (33, 10900), (35, 12700)]

print "ACTUAL:", gb03(35, 0)
print "EXPECT:", [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), 
                  (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), 
                  (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900)]
print "-"*10

# Note only did I realize that I'm not using the constants INITIAL_SALARY, 
# SALARY_INCREMENT, and INITIAL_BRIBE_COST, but the results were atrocious. 
# When num_bribes was initialized to 0, the first and last days vs earnings tuples
# were not added. When num_bribes was init'd to 1, the first tuple was now included,
# but the last was still not included, and now all of the tuples in between were
# added twice. Something is seriously wrong. Resist urge to copy solution...

# I will begin with a copy of gb02 and replace all of the appropriate values of
# the initialized variables with those of the constants. I have to rethink this.
# Let's look at what's happening here. First, the conditional that checks
# for savings >= bribe_cost does a round of updating. I know from memory that
# the solution merely uses this to change the value of days_to_next_bribe and
# leaves the updating to the block at the bottom. This is the first change I 
# will make, and it makes sense. If days_to_next_bribe = 0, the salary and
# earnings will not be changed, but the days vs earnings list will be upated.
# However, the tuple will be upated with an incorrect earnings value. I will
# make this change and see what happens.

def gb04(days_in_simulation, bribe_cost_increment, plot_type = STANDARD):
    """
    Simulation of greedy boss
    """
    salary = INITIAL_SALARY
    savings = 0
    earnings = 0
    bribe_cost = INITIAL_BRIBE_COST
    current_day = 0
    days_vs_earnings = [(0, 0)]

    while current_day < days_in_simulation:
    
        if savings >= bribe_cost:
            days_to_next_bribe = 0
        else:
            days_to_next_bribe = int(math.ceil((bribe_cost - savings) / float(salary)))

        current_day += days_to_next_bribe

        savings += salary * days_to_next_bribe
        savings -= bribe_cost
        salary += SALARY_INCREMENT
        bribe_cost += bribe_cost_increment
        earnings += salary * days_to_next_bribe

        days_vs_earnings.append((current_day, earnings))
       
    return days_vs_earnings

print "Testing gb04"
print "ACTUAL:", gb04(35, 100)
print "EXPECT:", [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), \
                  (29, 7900), (31, 9300), (33, 10900), (35, 12700)]

print "ACTUAL:", gb04(35, 0)
print "EXPECT:", [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), 
                  (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), 
                  (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900)]
print "-"*10

# SO, the template had a "<=" in the while loop instead of a "<", so I was always
# going to compute one extra round. I changed that. Plus my implementation is 
# very close to the solution, but the results are way off. I had to cheat, and now
# I see my big issue: I incremented the salary BEFORE incrementing the earnings.
# This calculated earnings with the next salary bump. This update brings all of
# the local vars up to speed, not projects them across the next leap. The attempt
# gb04 with that change will be pasted into my implementation of greedy_boss.

# The last bit that appends (day, earnings) to the days vs earnings list depending
# on plot type is taken straight from the solution. The only difference is for
# STANDARD, the values are kept the same, and for LOGLOG, the values are first
# converted with math.log(). The simulation is called below.

# Uncomment to run.
#run_simulations()

# A look at the standard plot shows a very steep increase in earnings that begins
# at day 30 and becomes very steep by day 70 when the bribe cost is kept constant.
# The increase appears to be quadratic. As the salary increases, more and more bribes
# can be made each day. When salary = 1000, one bribe is made each day. After
# 10 days, 2 bribes can be made each day since salary = 2000. After 5 days, 3 bribes
# can be made each day since salary = 3000. After 4 days, salary = 4000, and 4 bribes
# can be made each day. After 3 days, 5 bribes can be made each day. After 2 days,
# 6 bribes can be made each day. After 2 days, 7 bribes, 2 days, 8 bribes, 2 days, 9
# bribes, and 2 days, 10 bribes where salary = 10000. At this point, each day
# brings the ability to buy 10 more bribes, and it takes off from there.

# In the standard plot, the lines corresponding to earnings as a function of bribe
# increment all look to be linear and not very different. A loglog plot may change
# this comparison for us. Below is the run_simulations_loglog() function that
# produces the same plot but using loglog values. Note that the original
# run_simulations function could've been updated to have plot_type = LOGLOG.

def run_simulations_loglog():
    """
    Run simulations for several possible bribe increments
    """
    plot_type = LOGLOG
    days = 120
    inc_0 = greedy_boss(days, 0, plot_type)
    inc_500 = greedy_boss(days, 500, plot_type)
    inc_1000 = greedy_boss(days, 1000, plot_type)
    inc_2000 = greedy_boss(days, 2000, plot_type)
    simpleplot.plot_lines("Greedy boss", 600, 600, "days", "total earnings", 
                          [inc_0, inc_500, inc_1000, inc_2000], False,
                         ["Bribe increment = 0", "Bribe increment = 500",
                          "Bribe increment = 1000", "Bribe increment = 2000"])
                          
run_simulations_loglog()

# The loglog plot for the bribe increases sheds little light on the differences. 
# I will go back and change the number of days to 200 (from 70).
# Okay, 200 days times out. I will set days = 120.

# There is no big change. The implementation works, though. It is a bit too
# similar to the solution for my taste (since I had to reference it several times
# as I was working on my implementation). At least I tried...

##=================================================================
##=================================================================