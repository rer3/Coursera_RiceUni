"""
Rice University / Coursera: Principles of Computing (Part 1)
Week 1: Homework 1
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

##=================================================================

DIRECTIONS = '''
Homework Philosophy
----------
In IIPP, the focus of the class was to learn the basic of programming in Python.
There was only a minimal emphasis on building code that was well-structured and
efficient. In PoC, we will follow a more disciplined approach that emphasizes the
structure and efficiency of your programs.

While the projects in PoC will focus on coding style and structure, all of the 
homework assignments after this one are designed to hone your mathematical
skills. These skills are a critical part of learning to think like a computer
scientist. To become proficient at solving computational problems, one need not
only be skilled at programming, but also skilled at thinking computationally.

As a finale note, we remind you to read and think about each homework problem
carefully. Several of the problems are "tricky". In particular, your immediate answer
may not necessarily be the correct one. Learn to pay attention to detail.

Assessing Your Knowledge of Python
----------
Our first homework will focus solely on assessing and reviewing your knowledge of
basic programming in Python. The standard prerequisite for this class is IIPP. This
homework (and first project) are designed such that students who have finished
IIPP should be able to complete these assignments.

However, some students may wish to take this class without having taken IIPP.
If you have not taken or completed IIPP, please use your results to help self-assess
whether your knowledge of Python is sufficient to be successful in this class. For
the assessment provided by this homework to be most accurate, we suggest that
you attempt problems 1-8 below WITHOUT testing solutions in Python.
'''

##=================================================================

def hw_101():
    """
    QUESTION 1
    
    Enter the type of the Python expression 3.14159 below. Remember that
    capitalization is important.
    """
    # That is a floating number, of type "float".
    
    answer = "float"
    
    print "Question 101 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_101()

##=================================================================

def hw_102():
    """
    QUESTION 2
    
    An if statement can have at most how many else parts?
    """
    # After the initial condition, the statement can have as many as necessary.
    
    ##################################################
    ## INCORRECT
    ##
    ## answer = "Unlimited, i.e., 0 or more"
    ##################################################
    
    # I didn't think this one through. There can be as many "elif" parts as
    # necessary, but only one "else" part. 
    
    answer = "1"
    
    print "Question 102 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_102()

##=================================================================

def hw_103():
    """
    QUESTION 3
    
    Consider the following Python code snipper:
        def clock_helper(total_seconds):
            '''
            Helper function for a clock
            '''
            seconds_in_minute = total_seconds % 60
    
    Enter the value returned by Python after evaluating the expression
    clock_helper(90) below.
    """
    # There is no return statement, thus the function will not return anything.
    # An assignment is made and nothing else (not even print statements).
    
    answer = "None"
    
    print "Question 103 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_103()
    
##=================================================================

def hw_104():
    """
    QUESTION 4
    
    In Python, what character always appears at the end of the line before the
    start of an indented block of code?
    """
    # A colon appears at the end of a line before an indent, such as in the event
    # of a preceding if conditional, a for loop, or a similar statement.
    
    answer = ":"
    
    print "Question 104 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_104()
        
##=================================================================

def hw_105():
    """
    QUESTION 5
    
    Which of the following expressions returns the last character in the non-empty
    string my_string?
    
    Option 1
    my_string[len(my_string)]
    
    Option 2
    my_string[len(my_string) - 1]
    
    Option 3
    my_string.pop()
    
    Option 4
    my_string.last()
    """
    # Option 1 is out because it references an index that is outside of the range
    # of my_string (length = 5 corresponds to indices 0-4, so the last character
    # is my_string[4].
    # Option 3 is out because pop() is not a string method.
    # Option 4 is out because last() is not a string method.
     
    answer = "my_string[len(my_string) - 1]"
    
    print "Question 105 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_105()
            
##=================================================================

def hw_106():
    """
    QUESTION 6
    
    What is the primary difference between a list and a tuple?
    
    Option 1
    Lists are mutable. Tuples are immutable.
    
    Option 2
    Lists are immutable. Tuples are mutable.
    
    Option 3
    For tuples, all entries must be of the same type. Entries of lists may be
    of different type.
    
    Option 4
    There is no difference. The words "list" and "tuple" are interchangeable in
    Python.
    """
    # Option 1 is correct, but let's look at the others first.
    # Option 2 is out as it is the opposite of option 1.
    # Option 3 is out as either type can hold different types of entries (whether
    # that's a good practice or not is another thing).
    # Option 4 is out because they are obviously different, being two different
    # data types in Python.
    
    answer = "Lists are mutable. Tuples are immutable."
    
    print "Question 106 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_106()
        
##=================================================================

def hw_107():
    """
    QUESTION 7
    
    Consider the following snippet of Python code. What is the value of val2[1] 
    after executing this code?
        val1 = [1, 2, 3]
        val2 = val1[1:]
        val1[2] = 4
    """
    # The first statement initializes a list under the name "val1". The second
    # statement assigns the name val2 to the objects in val1 from the element 
    # at index 1 to the last element in val1. The third statement changes the 
    # element in val1 at index = 2 to the integer 4. At this point, val1 = [1, 2, 4].
    # The question here is whether val2 points to the same objects in val1, or
    # a completely separate list of objects. 
    
    # Remember that slicing (which is executed in the second statement) makes a
    # copy of the sliced list. When val2 is initialized above, a slice of val1 from
    # index 1 to the last index is copied, and that new list is assigned to val2. 
    # Therefore, val2 is assigned to [2, 3], and val2[1] = 3.
    
    answer = 3
    
    print "Question 107 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_107()
            
##=================================================================

def hw_108():
    """
    QUESTION 8
    
    Which of the following Python expressions is a valid key in a Python dictionary?
    
    Options = 0, "", [], None, set([]), {}
    """
    # Recall that dictionary keys can be integers, strings, tuples, or None. Keys can 
    # NOT be lists, sets, or dictionaries as they are mutable containers. 
    
    answer = "0, '', None"
    
    print "Question 108 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_108()
            
##=================================================================

def hw_109():
    """
    QUESTION 9
    
    Write a function in Python that takes a list as input and repeatedly appends
    the sum of the last three elements of the list to the end of the list. Your
    function should loop for 25 times.
        def appendsums(list):
            '''
            Repeatedly append the sum of the current last three elements of list
            to list.
            '''
    
    If your function works correctly, the following code should print 230:
        sum_three = [0, 1, 2]
        appendsums(sum_three)
        print sum_three[10]
        
    Enter the value of sum_three[20] below.
    """
    # This function should first check to ensure that the list is at least three
    # characters long (and if not, return an error). Then for 25 iterations,
    # the sum of the last three elements will be assigned to variable, which
    # is then appended to the list. Since the list is changed by the function,
    # there is no need for a return statement in this implementation.
    
    def appendsums(list):
        """
        Repeatedly append the sum of the current last three elements of list
        to list.
        """
        if len(list) < 3:
            return "Error: list too short"
            
        #test_index = 0
            
        for dummy_idx in range(25):
            sum_last_three = sum([list[idx] for idx in range(-1, -4, -1)])
            list.append(sum_last_three)
            #print "loop:", test_index
            #test_index += 1
        
    # Test it out on sum_three. I added a counting index (commented out after
    # the test ran) to make sure that this ran 25 times. The element in sum_three
    # at index 10 should be 230.
    
    sum_three = [0, 1, 2]
    appendsums(sum_three)
    print sum_three[10]
    print "-"*10
    
    # The function printed 230 and iterated over the list 25 times.
    
    ##################################################
    ## INCORRECT
    ##
    ## answer = sum_three[10]
    ##################################################
    
    # I accidentally submitted the answer to sum_three[10], the value from the
    # example, and not the one at index 20 like asked in the question.
    
    answer = sum_three[20]
    # 101902
    
    print "Question 109 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_109()
            
##=================================================================

def hw_110():
    """
    QUESTION 10
    
    First, complete the following class definition:
        
    class BankAccount:
        ''' Class definition modeling the behavior of a simple bank account '''

        def __init__(self, initial_balance):
            '''Creates an account with the given balance'''
            pass
            
        def deposit(self, amount):
            '''Deposits the amount into the account'''
            pass
            
        def withdraw(self, amount):
            '''
            Withdraws the amount from the account.  Each withdrawal resulting in a
            negative balance also deducts a penalty fee of 5 dollars from the balance.
            '''
            pass
            
        def get_balance(self):
            '''Returns the current balance in the account'''
            pass
            
        def get_fees(self):
            '''Returns the total fees ever deducted from the account'''
            pass
            
    The deposit and withdraw methods each change the account balance. The withdraw
    method also deducts a fee of 5 dollars from the balance if the withdrawal (before
    any fees) results in a negative balance. Since we also have the method get_fees,
    you will need to have a variable to keep track of the fees paid.
    
    Here's one possible test of the class. It should print values 10 and 5, respectively,
    since the withdrawal incurs a fee of 5 dollars.
    
        my_account = BankAccount(10)
        my_account.withdraw(15)
        my_account.deposit(20)
        print my_account.get_balance(), my_account.get_fees()
        
    Copy and paste the following much longer test (found in the code below). What two
    numbers are printed at the end? Enter the two numbers, separated by a space.
    """
    # First, I must implement the BankAccount class. The class must initialize fields
    # for balance and fees. The deposit and withdraw methods are just setters.
    # The remaining two are just getters. This is pretty straightforward. The withdraw
    # method must include a conditional to check for balance and deduct a fee
    # accordingly (5 dollars if balance - withdrawal < 0).
    
    class BankAccount:
        """
        Class definition modeling the behavior of a simple bank account
        """
        def __init__(self, initial_balance):
            """
            Creates an account with the given balance
            """
            self._balance = initial_balance
            self._fees = 0
            
        def deposit(self, amount):
            """
            Deposits the amount into the account
            """
            self._balance += amount
            
        def withdraw(self, amount):
            """
            Withdraws the amount from the account.  Each withdrawal resulting in a
            negative balance also deducts a penalty fee of 5 dollars from the balance.
            """
            if self._balance - amount < 0:
                self._fees += 5
                self._balance -= (amount + 5)
            else:
                self._balance -= amount
                
        def get_balance(self):
            """Returns the current balance in the account"""
            return self._balance
            
        def get_fees(self):
            """Returns the total fees ever deducted from the account"""
            return self._fees
            
    # Now to test. The first test is pulled from the instructions. The print
    # statement below should print "10 5".
    
    my_account = BankAccount(10)
    my_account.withdraw(15)
    my_account.deposit(20)
    print my_account.get_balance(), my_account.get_fees()
    print "-"*10
    
    # The print statements were accurate. Now to test the code from the question:
    
    my_account = BankAccount(10)
    my_account.withdraw(5)
    my_account.deposit(10)
    my_account.withdraw(5)
    my_account.withdraw(15)
    my_account.deposit(20)
    my_account.withdraw(5) 
    my_account.deposit(10)
    my_account.deposit(20)
    my_account.withdraw(15)
    my_account.deposit(30)
    my_account.withdraw(10)
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(50) 
    my_account.deposit(30)
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(5) 
    my_account.deposit(20)
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.deposit(30)
    my_account.withdraw(25) 
    my_account.withdraw(5)
    my_account.deposit(10)
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(10) 
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.deposit(30)
    my_account.withdraw(25) 
    my_account.withdraw(10)
    my_account.deposit(20)
    my_account.deposit(10)
    my_account.withdraw(5) 
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(5) 
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(5) 
    # The answer is stored in a variable.
    #print my_account.get_balance(), my_account.get_fees()
    
    answer = str(my_account.get_balance()) + " " + str(my_account.get_fees())
    # -60 75
    
    print "Question 110 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_110()

##=================================================================
##=================================================================