"""
Rice University / Coursera: Principles of Computing (Part 1)
Week 5 Mini-Project
Cookie Clicker Simulator
"""

import simpleplot
import math
import random

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0
#SIM_TIME = 1000000000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._current_time = 0.0
        self._current_cookies = 0.0
        self._total_cookies_earned = 0.0
        self._current_cps = 1.0
        
        # Initialize list consisting of time, item purchased at time,
        # cost of item, and total cookies at time.
        self._game_history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return "\n" + "Time: " + str(self._current_time) + "\n" + "Cookies:" + \
                str(self._current_cookies) + "\n" + "Total Cookies:" + \
                str(self._total_cookies_earned) + "\n" + "CPS:" + \
                str(self._current_cps)
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self._game_history)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        time_needed = math.ceil((cookies - self._current_cookies) / self._current_cps)
        if cookies - self._current_cookies >= 0:
            return time_needed
        else:
            return 0.0
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0.0:
            self._current_time += time
            self._current_cookies += self._current_cps * time
            self._total_cookies_earned += self._current_cps * time
        else:
            return
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._current_cookies >= cost:
            self._current_cookies -= cost
            self._current_cps += additional_cps
            self._game_history.append((self._current_time, item_name,
                                       cost, self._total_cookies_earned))
        else:
            return
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    # Clone build_info object and create ClickerState() object
    build = build_info.clone()
    state = ClickerState()
    
    # Loop until the time in state reaches duration of simulation
    while state.get_time() <= duration:
        # Determine which item to purchase next
        next_item = strategy(state.get_cookies(), state.get_cps(), 
                             state.get_history(), duration - state.get_time(), 
                             build)
        if next_item is None:
            break
        
        next_item_cost = build.get_cost(next_item)
        next_item_cps = build.get_cps(next_item)
        
        # Determine how much time must elapse until next purchase
        time_until_purchase = state.time_until(next_item_cost)
        if (state.get_time() + time_until_purchase) > duration:
            break
        
        # Wait until that time
        state.wait(time_until_purchase)
        
        # Buy the item
        state.buy_item(next_item, next_item_cost, next_item_cps)
        
        # Update the build information
        build.update_item(next_item)
        
    # If exited the loop, wait until end of simulation
    state.wait(duration - state.get_time())
    
    # Return ClickerState() object
    return state

def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    # Get the item names and costs and combine in a list
    item_names = build_info.build_items()
    item_details = []
    for item in item_names:
        item_details.append((build_info.get_cost(item), item))
    
    # Return the most expensive yet affordable item for remaining time  
    for item in item_details:
        if item[0] <= cookies + (cps * time_left):
            return item[1]      
    
    # Return None if there is no affordable item
    return None

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    # Get the item names and costs and combine in a list
    item_names = build_info.build_items()
    item_details = []
    for item in item_names:
        item_details.append((build_info.get_cost(item), item))
    
    # Sort the list of item costs and names in reverse (decr) order
    item_details.sort(reverse = True)
    
    # Return the most expensive yet affordable item for remaining time  
    for item in item_details:
        if item[0] <= cookies + (cps * time_left):
            return item[1]      
    
    # Return None if there is no affordable item
    return None

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    This strategy will consider CPS/cost for each item and will
    purchase the item with the highest CPS/cost ratio in a given round.
    """
    # Get the item names, CPS/cost, and cost and combine in a list
    item_names = build_info.build_items()
    item_details = []
    for item in item_names:
        item_details.append((build_info.get_cps(item) / build_info.get_cost(item), 
                             build_info.get_cost(item), item))
    # Sort the list of item CPS/cost and item names in reverse (decr) order
    item_details.sort(reverse = True)
    
    # Return the item with biggest ROI (i.e. highest CPS/cost) that 
    # is affordable for remaining time
    for item in item_details:
        if item[1] <= cookies + (cps * time_left):
            return item[2]
    
    # Return None if there is no affordable item
    return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    history = state.get_history()
    history = [(item[0], item[3]) for item in history]
    #simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)
    
    ## Extra code for plotting all strategies on one graph
    #print history[1:]
    history = state.get_history()
    history = [(math.log(item[0]), math.log(item[3])) for item in history[1:]]
    #print history
    return history

def run():
    """
    Run the simulator.
    """    
    #run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    #run_strategy("Cheap", SIM_TIME, strategy_cheap)
    #run_strategy("Expensive", SIM_TIME, strategy_expensive)
    #run_strategy("Best", SIM_TIME, strategy_best)
    
    ## Extra code to plot all strategies on one graph
    cursor = run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)
    cheap = run_strategy("Cheap", SIM_TIME, strategy_cheap)
    expensive = run_strategy("Expensive", SIM_TIME, strategy_expensive)
    best = run_strategy("Best", SIM_TIME, strategy_best)
    simpleplot.plot_lines("Clicker Strategies", 1000, 400, "Time", "Total Cookies",
                          [cursor, cheap, expensive, best], True, 
                          ["Cursor", "Cheap", "Expensive", "Best"])
    
run()
    

## poc_clicker_provided shown below
# """
# Cookie Clicker Simulator Build Information
# """

# BUILD_GROWTH = 1.15

# class BuildInfo:
    # """
    # Class to track build information.
    # """
    
    # def __init__(self, build_info = None, growth_factor = BUILD_GROWTH):
        # self._build_growth = growth_factor
        # if build_info == None:
            # self._info = {"Cursor": [15.0, 0.1],
                          # "Grandma": [100.0, 0.5],
                          # "Farm": [500.0, 4.0],
                          # "Factory": [3000.0, 10.0],
                          # "Mine": [10000.0, 40.0],
                          # "Shipment": [40000.0, 100.0],
                          # "Alchemy Lab": [200000.0, 400.0],
                          # "Portal": [1666666.0, 6666.0],
                          # "Time Machine": [123456789.0, 98765.0],
                          # "Antimatter Condenser": [3999999999.0, 999999.0]}
        # else:
            # self._info = {}
            # for key, value in build_info.items():
                # self._info[key] = list(value)

        # self._items = sorted(self._info.keys())
            
    # def build_items(self):
        # """
        # Get a list of buildable items
        # """
        # return list(self._items)
            
    # def get_cost(self, item):
        # """
        # Get the current cost of an item
        # Will throw a KeyError exception if item is not in the build info.
        # """
        # return self._info[item][0]
    
    # def get_cps(self, item):
        # """
        # Get the current CPS of an item
        # Will throw a KeyError exception if item is not in the build info.
        # """
        # return self._info[item][1]
    
    # def update_item(self, item):
        # """
        # Update the cost of an item by the growth factor
        # Will throw a KeyError exception if item is not in the build info.
        # """
        # cost, cps = self._info[item]
        # self._info[item] = [cost * self._build_growth, cps]
        
    # def clone(self):
        # """
        # Return a clone of this BuildInfo
        # """
        # return BuildInfo(self._info, self._build_growth)

###########
# TESTING #
###########
#print "*"*40
#clicker = ClickerState()
#print "New ClickerState() object, clicker", clicker
#print "-"*20
#print "Cookies:", clicker.get_cookies()
#print "CPS:", clicker.get_cps()
#print "Time:", clicker.get_time()
#print "History:", clicker.get_history()
#print "Time until 100 cookies:", clicker.time_until(100)
#print "-"*20