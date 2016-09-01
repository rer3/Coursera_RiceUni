"""
Rice University / Coursera: Principles of Computing (Part 1)
Week 5: Homework 5
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
## Greedy Boss Sim taken from PoC1_Week5Notes_GreedyBossScenario. Note that
## the run_simulations function has been changed to accept a plot_type parameter.

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
       
    #return days_vs_earnings
    #--------------------------------------------------
    # Returns only the total earnings for days_in_simulation. This corresponds
    # to the final tuple in days_vs_earnings, second value. Uncomment to use.
    return days_vs_earnings[-1][1]
    #--------------------------------------------------

def run_simulations(plot_type):
    """
    Run simulations for several possible bribe increments
    """
    days = 120
    inc_0 = greedy_boss(days, 0, plot_type)
    inc_500 = greedy_boss(days, 500, plot_type)
    inc_1000 = greedy_boss(days, 1000, plot_type)
    inc_2000 = greedy_boss(days, 2000, plot_type)
    simpleplot.plot_lines("Greedy boss", 600, 600, "days", "total earnings", 
                          [inc_0, inc_500, inc_1000, inc_2000], False,
                         ["Bribe increment = 0", "Bribe increment = 500",
                          "Bribe increment = 1000", "Bribe increment = 2000"])

##=================================================================

DIRECTIONS = '''
Analyzing the Greedy Boss Scenario
----------
In this week's project, we will investigate various strategies for the simple
(but popular) game "Cookie Clicker". As a warmup, this week's Practice Activity,
The Case of the Greedy Boss, considers a simple scenario that is very similar to
Cookie Clicker in which you can repeatedly bribe your boss to have him increase
your salary. This homework will analyze the behavior of the greedy boss sim for
several simple cases. If you have not taken a look at this practice activity, you
should work through it first before attempting this homework.
'''

##=================================================================

def hw_501():
    """
    QUESTION 1
    
    Use the function run_simulation in the greedy boss simulator to plot the graph
    of total salary earned as a function of the number of days for bribe_cost_increment
    equal to 0, 500, 1000, 2000. Which value for bribe_cost_increment generates
    the fastest growth in total salary earned in the simulation?
    """
    # The greedy boss simulator code is above in the shared area. The plots show
    # a very fast growth when bribe cost = 0. Look at a standard plot.
    
    # Uncomment to run.
    #run_simulations(STANDARD)
    
    answer = 0
    
    print "Question 501 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_501()

##=================================================================

def hw_502():
    """
    QUESTION 2
    
    One scenario that the greedy boss simulator does not cover is the situation
    when you refuse to provide a bribe. Which of the following arithmetic sums
    evaluates to your total salary earned after d days?
    
    Option 1
    1 + 2 + ... + (d-1) + d
    
    Option 2
    100 + 200 + ... + 100*(d-1) + 100*d
    
    Option 3
    100 + 100 + ... + 100 + 100 (with d terms in sum)
    
    Option 4
    1 + 1 + ... + 1 + 1 (with d terms in sum)
    """
    # Your initial salary is $100. If you don't provide a bribe, your salary
    # does not change (in this scenario) and you earn $100 for each day of
    # work. 
    
    answer = "100 + 100 + ... + 100 + 100 (with d terms in sum)"
    
    print "Question 502 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_502()

##=================================================================

def hw_503():
    """
    QUESTION 3
    
    Reduce the arithmetic sum that you selected in question 2 to a polynomial
    expression in the number of days d using the rules for arithmetic sums specified
    in the Math notes. This expression should evaluate to your total salary earned
    after d days. Enter the answer as a math expression below.
    """
    # When d = 1, you earn 100. When d = 2, you earn 100 + 100 = 200. You
    # always earn 100 * d, a linear growth rate.
    
    answer = "d * 100"
    
    print "Question 503 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_503()

##=================================================================

def hw_504():
    """
    QUESTION 4
    
    For the next three problems, we will consider the case when bribe_cost_increment
    is equal to 1000. First, convert the output of greedy_boss() into log/log form
    by taking the log of both current_day and the total salary earned using math.log().
    (Note that this is already done in the code).
    
    The plot of the resulting graph approaches a straight line as the number of
    days increase. This observation signals that the function might be a polynomial
    function. Compute the slope of this line and round it to the nearest integer
    to estimate the degree of this polynomial.
    """
    # I modified the run_simulations function to accept a plot_type parameter.
    # Here, I just need to look at the LOGLOG plot and estimate the slope of
    # the line for bribe_cost_increment == 1000. The days was increased from
    # 70 to 120 (greater than that and the function runs very slowly).
    
    # Uncomment to run.
    #run_simulations(LOGLOG)
    
    # All lines for bribe increments overlap until log(day) == 2.25. After that point,
    # the line for bribe increment == 1000 appears to have a slope of around 
    # 2.5 / 1.5 or 2. 
    
    answer = 2
    
    print "Question 504 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_504()

##=================================================================

def hw_505():
    """
    QUESTION 5
    
    Examine the output of the sim greedy_boss(50, 1000). Note you accumulate enough
    savings to pay a bribe once every 10 days. Which of the arithmetic sums below
    evaluates to the total salary earned after n bribes? 
    
    Option 1
    1000 + 1000 + ... + 1000
    
    Option 2
    1000 + 1000/2 + 1000/2**2 + ... + 1000/2**n
    
    Option 3
    1000 + 2000 + 3000 + ... + 1000*n
    
    Option 4
    1000 + 1000/2 + 1000/3 + ... + 1000/n
    """
    # The output is computed to be:
    
    print greedy_boss(50, 1000)
    # [(0, 0), (10, 1000), (20, 3000), (30, 6000), (40, 10000), (50, 15000)]
    print "-"*10
    
    # Note that these values result from 10*100 (the salary increment) == 1000,
    # so for each increase in salary by 100, you have an extra 1000 dollars every
    # 10 days (in addition to what you'd have if you had no salary increase)
    # but bribe costs rises by 1000 each time. Your earnings are 1000 at bribe 1, 
    # 3000 at bribe 2, 6000 at bribe 3, 10000 at bribe 4, and 15000 at bribe 5.
    
    # The first term(s) in each earnings value is, in order: 1, 3, 6, 10, and 15 at
    # bribes 1, 2, 3, 4, and 5. If bribe number corresponds to n and i to this unknown
    # multiplier, you find that when n=1:i=1, n=2:i=2+1=3, n=3:i=3+2+1=6, n=4:
    # i=4+3+2+1=10, n=5:i=5+4+3+2+1=15. These are known as triangular numbers. 
    # Now update that sequence to reflect the $1000 you have when n=1 to get 
    # the answer. Here, the multiplier i is equal to 1, so this is like a basic case.
    
    # It helps to clarify that this is an arithmetic sum, so when n=2, you can find
    # the sum when n = 4 by adding 1000*1 + 1000*2 + 1000*3 + 1000*4,
    # or 10000, which is what is observed at day 40 when the 4th bribe is paid.
    # The multiplier comes into play wen you want to multiply the (for lack of a
    # better term, which I'm sure exists) basic case of $1000 by some number
    # in order to find the answer without evaluating a series of additions. So,
    # when n = 4, your multiplier, as shown above, is 10, and you simply multiply
    # 1000 by 10 to get 10000 at the 4th bribe. This multiplier is produced by 
    # some closed-form expression in n (see next question).
    
    answer = "1000 + 2000 + 3000 + ... + 1000*n"
    
    print "Question 505 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_505()

##=================================================================

def hw_506():
    """
    QUESTION 6
    
    Reduce the arithmetic sum that you selected in question 5 to a closed-form
    expression in n using the rules of arithmetic sums specified in the Math notes.
    This expression should relate total salary earned to the number of bribes.
    
    Finally, use the fact that each bribe happens once every 10 days to derive
    a polynomial expression for total salary earned in terms of the number of
    days d. As a check, this expression in d should evaluate exactly to the total
    salary earned by the end of the day of each bribe. Enter this expression in d
    as a math expression below.
    """
    # The arithmetic sum from question 5, for triangular numbers, reduces to
    # the form n * (n + 1) / 2 for the nth number in the sequence. Recall that
    # the n term from question 5 corresponds to a bribe, which occurs every 10
    # days. When n = 1, d = 10. When n = 2, d = 20. You can see that n = d / 10.
    # You can replace the n in the triangular closed-form expression with (d / 10).
    
    # Remember too that you have $1000 when you pay 1 bribe. This is your basic
    # case. The closed-form expression increases the i multiplier (1, 3, 6, 10, 15)
    # in the expression 1000 * i which yields the total earnings made up to the
    # corresponding nth bribe. This "* 1000" must be appended to the closed-form
    # expression--with (d / 10) replacing n--to return the total earnings and not
    # just the multiplier.
    
    answer = "((d / 10) * ((d / 10) + 1) / 2) * 1000"
    
    print "Question 506 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_506()

##=================================================================

def hw_507():
    """
    QUESTION 7
    
    The next two questions will examine the case when the cost of a bribe does not
    increase, i.e. bribe_cost_increment == 0. Our first task is to check whether the
    total salary earned is a polynomial function of the number of days in this case.
    To this end, create a log/log plot of the output of greedy_boss and examine the
    resulting graph. Does the graph approach a straight line as the number of days 
    increases?
    
    Option 1
    No, the graph does not approach a straight line.
    
    Option 2
    Yes, the graph approaches a straight line.
    """
    # Look at the simulation with the 4 bribe cost increments. The log/log graph
    # shows the line corresponding to bribe cost == 0 increasing very steeply. 
    # It is not linear therefore not quadratic and must be exponential in nature.
    # My comments in the py doc for Greedy Boss Scenario illustrate the reason
    # for this fast growth; essentially, as your salary increases, you can pay for
    # more and more bribes at a time, and at the end of each day, that number
    # of bribes that you can pay for only increases. As you are able to pay for 
    # more bribes in a day, your salary increases more and more each time.
    
    # Uncomment to run.
    #run_simulations()
    
    answer = "No, the graph does not approach a straight line."
    
    print "Question 507 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_507()

##=================================================================

def hw_508():
    """
    QUESTION 8
    
    To conclude our analysis of this case, we will do some manual experimentation
    to locate an expression in d that grows at a similar rate to total salary earned
    when bribe_cost_increment == 0.
    
    Compare the growth rates of the expression below to the growth rate of total
    salary earned using the plotting technique described in the Math notes. Which
    expression grows at approximately the same rate as total salary earned?
    
    Option 1
    9.5 * d**4
    
    Option 2
    e**(9.5 * d)
    
    Option 3
    e**(0.095 * d)
    
    Option 4
    95 * d**2
    """
    # The best way to approach this problem is to build those four expressions
    # into functions and to run them the same amount of times to collect data
    # for each value of n = 1 to 70. Then I will run greedy_boss(70, 0, LOGLOG) and
    # collect its data. All data points will be plotted and compared. The one that
    # fits best will be chosen. Since we are looking for growth rates, the log of
    # n and the log of the result of the expression for the given n will be
    # returned (as a list of tuples for each n). 
    
    # def opt1(days):
        # return [(math.log(d), math.log(9.5 * d**4)) for d in range(days)]

    # def opt2(days):
        # return [(math.log(d), math.log(math.e ** (9.5 * d))) for d in range(days)]

    # def opt3(days):
        # return [(math.log(d), math.log(math.e ** (.095 * d))) for d in range(days)]

    # def opt4(days):
        # return [(math.log(d), math.log(95 * d**2)) for d in range(days)]
        
    # plot_type = LOGLOG
    # days = 70
    # plot1 = opt1(days)
    # plot2 = opt2(days)
    # plot3 = opt3(days)
    # plot4 = opt4(days)
    # greedyplot = greedy_boss(days, 0, plot_type)
    
    # simpleplot.plot_lines("Question 8: Greedy Boss vs. Four Options, Bribe Inc == 0",
                          # 600, 600, "Days", "Total Earnings", [plot1, plot2, plot3,
                          # plot4, greedyplot], False, ["Opt1", "Opt2", "Opt3", "Opt4",
                          # "greedy_boss"])
    
    # A look at the results shows option 2 growing in the same manner as observed
    # in the run_simulations plot for bribe increment == 0.
    
    ##################################################
    ## INCORRECT: Partially correct. Total salary earned is growing exponentially,
    ## but more slowly than this expression.
    ##
    ## answer = "e**(9.5 * d)"
    ##################################################
    
    # I made the mistake of running the log/log plots instead of running comparisons
    # of function to function. When I immediately saw a curve matching that observed
    # for bribe increment == 0 in run_simulations, I assumed that was the winner. I
    # missed the fact that the greedy_boss line was in fact at the bottom of the 
    # graph calculated here, growing at a very similar rate as the other expressions.
    # This obviously means that e**(9.5 * d) grows extremely fast compared to
    # greedy_boss when bribe cost == 0. 
    
    # A better way to do this is to write 4 more functions that, instead of computing
    # values for each n using the expressions in each option, compute the fraction
    # f(n) / g(n) where g(n) = greedy_boss at bribe_cost == 0 and f(n) = the 
    # expression. If the line tends toward a linear growth in a horizontal direction,
    # that signifies both functions growing at the same rate (and is what I am
    # looking for in this problem). If the slope increases with no upper bound, then
    # greedy_boss function grows at a much faster rate; the inverse is true if the line
    # converges toward zero.
    
    # def opt1(n):
        # return math.log(9.5 * n**4)

    # def opt2(n):
        # return math.log(math.e ** (9.5 * n))

    # def opt3(n):
        # return math.log(math.e ** (.095 * n))

    # def opt4(n):
        # return math.log(95 * n**2)
        
    # Now that those 4 expressions have been reduced to their simplest form
    # (minus any business creating lists of values to be plotted, which will be
    # done separately), how do we get greedy_boss to return its core function
    # for each n so that the outcome can be the numerator in our fraction? 
    # Think about what we are looking for: for any given n, what is the result
    # of the function for that value of n? greedy_boss computes a total earnings
    # for each bribe payment. For 100 days, with bribe increment == 0, the
    # greedy_boss function returns a very long list of tuples. 
    
    # The greedy_boss function will have to be rewritten to return only the final
    # earnings value of the last tuple in the list. I will add this to the
    # implementation found in the shared area and comment it out when I am 
    # finished with this problem. Note that the days_vs_earnings list is only
    # updated when there is a bribe; however, the returned list is always
    # updated for the next bribe regardless of whether or not it is within
    # the specified days_in_simulation. For example, for n = 1 to 9, your
    # earnings are 100 to 900, but the function (as implemented in the solution
    # to this function that was provided to us) inserts (10, 1000) into the list
    # when you pass days_in_simulation values of 1 to 10. When you pass a value
    # of 11 to the function, it immediately appends (15, 2000) to the list,
    # which corresponds to the next raise at day 15.
    
    # This inaccuracy can be dismissed, for when bribe increment == 0, at higher
    # values of n (days in sim), the earnings is updated AT LEAST daily, eventually
    # several times per day. While the early data points may be erroneous, the
    # plotted lines will eventually become very accurate.
    
    # The simplest way (i.e. least lines of code) to generates these lists of 
    # data is to store everything in one giant list of lists that is updated by
    # nested for loops and indexed in the call to simpleplot.
    
    # plots = [[], [], []]
    # opts = [opt1, opt3, opt4]
    # days = 120
    
    # for day in range(1, days + 1):
        # for idx in range(len(opts)):
            # frac = float(opts[idx](day)) / greedy_boss(day, 0, LOGLOG)
            # plots[idx].append((math.log(day), frac))
    
    # Now let's plot them and see if it worked.
    
    # simpleplot.plot_lines("Question 8: Greedy Boss vs. Four Optoins, Bribe Inc == 0",
                      # 600, 600, "n", "opt(n) / greedy_boss(n)", [plots[0], plots[1], 
                      # plots[2]], False, ["Opt1", "Opt3", "Opt4"])
                      
    # Option 2 is right out (which I already knew!!!). The problem is that for 
    # large values of n, an OverflowError is returned. I will go back and remove
    # this option from my computations and increase days to 120 to see if the
    # remaining options show clear differences.
    
    # Already the computation involved in the greedy_boss sim is showing signs
    # of inefficiency, as that computation took at least 10-15 seconds. Still, there
    # was very little resolution between lines. I just realized that I was not 
    # appending math.log(day)...I changed that and tried again.
    
    # Still weirdness...the greedy_boss function is returning the log value of
    # earnings. (Incidentally, I also noticed that it is still increasing the size
    # of days_vs_earnings and I just return the last element's second element,
    # so that explains the slowness). The four functions compute log values.
    # It makes sense to me that equality exists between 5 / 5 and log(5) / log(5). 
    # Still, I will change the three opt functions to return a value, then take the
    # log of the fraction of this value over the STANDARD output of greedy_boss.
    
    def opt1(n):
        return 9.5 * n**4

    def opt2(n):
        return math.e ** (9.5 * n)

    def opt3(n):
        return math.e ** (.095 * n)

    def opt4(n):
        return 95 * n**2
    
    plots = [[], [], []]
    opts = [opt1, opt3, opt4]
    days = 120
    
    ## Uncomment next two code blocks to run.
    # for day in range(1, days + 1):
        # for idx in range(len(opts)):
            # frac = float(opts[idx](day)) / greedy_boss(day, 0)
            # plots[idx].append((math.log(day), math.log(frac)))
    
    # simpleplot.plot_lines("Question 8: Greedy Boss vs. Four Optoins, Bribe Inc == 0",
                     # 600, 600, "n", "opt(n) / greedy_boss(n)", [plots[0], plots[1], 
                     # plots[2]], False, ["Opt1", "Opt3", "Opt4"])  
                      
    # This actually may have fixed the problem. The line for opt3/gb is linear
    # and horizontal. The other two look like mounds (suggesting they are
    # converging toward zero). I will choose option 3. I should have just rewritten
    # greedy_boss to update a local variable that holds the earnings, and then
    # just return that. Next time!
        
    answer = "e**(0.095 * d)"
    
    print "Question 508 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_508()

##=================================================================

def hw_509():
    """
    QUESTION 9
    
    In the next two questions, we will consider a simple version of Cookie Clicker
    in which there is only one possible upgrade option. Instead of increasing the
    cost of an upgrade by some fixed amount after each upgrade as done in the
    greedy boss sim, each upgrade in Cookie Clicker costs 15% more than the cost
    of the previous upgrade. Note that this cost compounds in the same manner
    that interest does.
    
    If the first upgrade costs one unit, enter a math expression that models
    the cost of the nth upgrade. 
    """
    # Let's look at this like compound interest. A = P * (1 + (r / n)) **(n * t)
    # where A is the annual compound interest, P = principal, r = interest rate, 
    # n = number of times interested is compounded per year, and t = number
    # of years for which the money is borrowed. Continuous compounding interest
    # is calculated by the expression A = P * e**(r * t) where e is Euler's constant.
    # And last but not least, when n = 1 (interest compounded once per year),
    # the formula A = P * (1 + r)**t is used.
    
    # So how does this relate to the problem here? Your first upgrade costs 1,
    # so when n = 1, A = 1. I will start by looking at the simple expression for
    # compound interest, where its compounded once yearly. Here, t = number
    # of upgrades, so n (from the expressions) would be 1 since the rate increases
    # once per upgrade (corresponding to once/year compound interest increase). 
    # So now I have A = 1 = (1 + r) **1. My rate from the problem is 0.15. 
    # Plugging that in for r yields (1 + 0.15) ** 1 = 1.15 for the first upgrade.
    # But I know that the first upgrade costs 1. The second upgrade costs 15%
    # more than 1, which is 1.15. 
    
    # The expression seems like it can be changed to A = (1 + r) ** (u - 1)
    # where r = rate and u = upgrade number. At u = 1, A = (1 + .15) **0,
    # which evaluates to 1. At u = 2, A = (1 + .15) ** 1 = 1.15. Remember
    # that there is a P = 1 that I am leaving out, where A = P * (1 + r)**(u-1).
    # Since it is 1, I can ignore it, but I won't when I submit my answer.
    # Full disclosure, I got this wrong on the first go, but I don't remember
    # my reasoning exactly. I did not subtract 1 from the exponent, though.
    
    answer = "1 * (1 + 0.15) ** (n - 1)"
    
    print "Question 509 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_509()

##=================================================================

def hw_510():
    """
    QUESTION 10
    
    For the case when bribe_cost_increment == 1000, the cost of the nth bribe was
    exactly 1000 * n. Which expression in n grows faster (as defined in the Math
    notes), 1000 * n or your answer to question 9?
    
    You may want to plot some examples using simpleplot for large values of n
    to help in making this comparison.
    
    Option 1
    Both expressions grow at the same rate.
    
    Option 2
    The cost of an upgrade in Cookie Clicker grows faster than the cost of a 
    bribe in the greedy boss scenario.
    
    Option 3
    The cost of an upgrade in Cookie Clicker grows more slowly than the cost of a 
    bribe in the greedy boss scenario.
    """
    # Like in question 8, I will implement a function that evaluates the expression
    # from question 9, then plot the fraction of greedy_boss(days, 1000) to the
    # function for days = 1 to 100 (log/log plot, of course).
    
    def upgrade_rate(n):
        return 1.15**(n - 1)
        
    plot = []
    days = 100
    
    ## Uncomment to run.
    
    # for day in range(1, days + 1):
        # frac = float(upgrade_rate(day)) / greedy_boss(day, 1000)
        # plot.append((math.log(day), math.log(frac)))
        
    # simpleplot.plot_lines("Question 10: Upgrade Rate vs. Greedy Boss", 600, 600,
                          # "n", "upgradate_rate(n) / greedy_boss(n)", [plot], False)
                          
    # The plot line extended upward with no upper bound. The numerator (in this
    # case, the upgrade rate function) increased at a higher rate than the greedy
    # boss function.
    
    answer = "The cost of an upgrade in Cookie Clicker grows faster than the cost of a "
    answer += "bribe in the greedy boss scenario."
    
    print "Question 510 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_510()

##=================================================================

def hw_511():
    """
    QUESTION 11
    
    For your final homework problem in this part of PoC, your task is to create
    a collection of tests for the function gen_all_holds() that you implemented
    for Yahtzee. This OwlTest (http://codeskulptor.appspot.com/owltest/
    ?urlTests=poc.poc_gah_tests_machine.py&urlPylintConfig=skip) will 
    automatically assess how effective your list of test cases is in detecting
    erroneous programs from a suite of implementations of gen_all_holds() that
    we have compiled. Tests that detect more erroneous programs from this suite
    receive a higher score. The max score on this problem is 10 points.
    
    To complete this problem, visit the OwlTest page linked above and follow
    the directions for creating and submitting a list of test cases. Once OwlTest
    has successfully assessed your test case, you will see the message "TEST CASES
    successfully assessed." Following this message is a seven-digit number that you
    should enter in the form below. For this task, please ignore the fact that this
    message appears under the red Unit Test Failures tab.
    
    Note that OwlTest will reject test cases that do not following the guidelines.
    You will only know your score on this problem once you submit the quiz to
    Coursera. This is to encourage you to put thought into this problem.
    
    OwlTest Directions
    ----------
    Your input file should contain a single Python definition:
    * A list TEST_CASES containing at most 10 test cases for the function
        gen_all_holds().
    * Each test case in this list should be a sorted tuple of length at most
        six whose entries are integers in the range 1 to 8 (inclusive).
    
    These tuples will be used as input to gen_all_holds(). You do not need to
    provide the corresponding output. We will compute it from our reference
    implementation. 
    
    OwlTest will assess the completeness of the test cases using a hidden suite
    of incorrect implementations of gen_all_holds(). If an incorrect implementation
    returns a correct answer on all tests in TEST_CASES, OwlTest will record that
    the program incorrectly passed the provided tests. If an incorrect implementation
    returns an incorrect answer on at least one of the tests in TEST_CASES, OwlTest
    will record that the implementation correctly failed the provided tests.
    
    The code returned after submission will be entered into Homework 5 Question 11.
    The score you receive is based on this code (i.e. the results are obfuscated until
    you submit the code to Coursera).
    """
    # First let's look at the recursive implementation of gen_all_holds:
    
    def gen_all_holds(hand):
        """
        Generate all possible choices of dice from hand to hold.
        hand: full yahtzee hand
        Returns a set of tuples, where each tuple is dice to hold
        """
        def gen_all_hold_recur(hand, length):
            """
            Recursive function to generate all permutations from all 
            possible dice choices of length 1 to len(hand).
            """
            if length == 0:
                return set([()])
            
            drop = hand[0]
            perms = gen_all_hold_recur(hand[1:], length-1)
            new_perms = set([])
            
            for perm in perms:
                store = list(perm)
                store.append(drop)
                new_perms.add(tuple(sorted(store)))
            new_perms.update(perms)
            
            return new_perms
        
    # Regardless of how the gen_all_holds function operates, my instinct is to
    # create 10 different tuples that correspond to 10 unique types of permutations
    # encountered in a game like Yahtzee (with these modified conditions that
    # would correspond to 8-sided dice and a hand of length 6). Since I only have
    # 10 cases in which to represent as many unique permutation types as 
    # possible, I have to think about this tightly.
    
    # Case 1: Every number is unique.
    # Case 2: One pair.
    # Case 3: Two pairs.
    # Case 4: Three pairs.
    # Case 5: Three of a kind + one pair.
    # Case 6: Three of a kind + three of a kind.
    # Case 7: Four of a kind.
    # Case 8: Four of a kind + one pair.
    # Case 9: Five of a kind.
    # Case 10: Every number is the same.
    
    # Of course, this leaves out certain types, such as just one three of a kind,
    # or rearrangements such as one pair + three of a kind. I have to trust
    # that these are sufficient to stump all of the erroroneous implementations.
    
    TEST_CASES = [(1, 2, 3, 4, 5, 6), (1, 1, 3, 5, 6, 7), 
                  (1, 1, 4, 4, 6, 7), (1, 1, 5, 5, 7, 7), 
                  (2, 2, 2, 5, 5, 6), (2, 2, 2, 6, 6, 6), 
                  (4, 4, 4, 4, 5, 6), (4, 4, 4, 4, 6, 6),
                  (3, 3, 3, 3, 3, 7), (5, 5, 5, 5, 5, 5)]
              
    # 10 points! My instincts were right.
    
    ## I finally found the TEST_CASES initially used:
    
    TEST_CASES_ORIGINAL = [(2, 3, 5, 6, 7, 8), (3, 3, 4, 5, 6, 8),
                  (5, 5, 6, 6, 7, 8), (3, 3, 4, 4, 7, 7), (5, 5, 5, 6, 7, 8),
                  (6, 6, 6, 7, 7, 8), (3, 3, 3, 3, 4, 8), (4, 4, 5, 5, 5, 5),
                  (1, 6, 6, 6, 6, 6), (2, 2, 2, 2, 2, 2)]
    
    answer = "Code: " + "4232645" + "\n"
    answer += "returned for TEST_CASES:"
    for case in TEST_CASES:
        answer += "\n" + str(case)
    
    print "Question 511 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_511()

##=================================================================
##=================================================================