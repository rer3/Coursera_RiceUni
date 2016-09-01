#http://www.codeskulptor.org/#user40_P1WE1BlhtuAExmu_2.py
"""
Rice University / Coursera: Algorithmic Thinking (Part 1)
Week 1/2 Lecture
Test suite for format function in "Stopwatch - The Game"
"""

import poc_simpletest as tester

def run_test(format_function):
    """
    Some informal testing code
    """
    
    # Create a TestSuite object
    suite = tester.TestSuite()
    
    # Test format_function on various inputs
    suite.run_test(format_function(0), "0:00.0", "Test #1:")
    suite.run_test(format_function(7), "0:00.7", "Test #2:")
    suite.run_test(format_function(17), "0:01.7", "Test #3:")    
    suite.run_test(format_function(60), "0:06.0", "Test #4:")
    suite.run_test(format_function(63), "0:06.3", "Test #5:")
    suite.run_test(format_function(214), "0:21.4", "Test #6:")
    suite.run_test(format_function(599), "0:59.9", "Test #7:")
    suite.run_test(format_function(600), "1:00.0", "Test #8:")
    suite.run_test(format_function(602), "1:00.2", "Test #9:")
    suite.run_test(format_function(1325), "2:12.5", "Test #10:")
    suite.run_test(format_function(5999), "9:59.9", "Test #11:")
	
	suite.report_results()
##########################################
#http://www.codeskulptor.org/#user40_RzCT1NBvE0QsNor_1.py
"""
Format function for a stopwatch
"""

import user40_ZBPCfbWRbAAQiFE_0 as tester

def stopwatch_format(ticks):
    """
    Convert tenths of seconds to formatted time
    """
    
    minutes = ticks // 600
    tens_seconds = (ticks // 100) %6
    seconds = (ticks // 10) % 10
    tenths = ticks % 10
    return str(minutes) + ':' + str(tens_seconds) + \
           str(seconds) + '.' + str(tenths)
    
# run the testing suite for our format function
tester.run_test(stopwatch_format)