"""
Rice University / Coursera: Intro to Interactive Programming in Python (Part 2)
Week 2: Homework 6a
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

##=================================================================

def hw_601():
    """
    QUESTION 1
    
    Every class definition should include an initializer method. What is the name
    of the initializer method? Refer to the first OOP video. While you can get away
    with not having an initializer method, doing so almost always implies using
    techniques beyond the scope of this course or bad program design. So, beginners
    should always define an initializer method.
    
    Option 1
    __init__
    
    Option 2
    _init_
    
    Option 3
    init
    
    Option 4
    The same as the name of the class
    """
    
    answer = "__init__"
    
    print "Question 601 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_601()

##=================================================================

def hw_602():
    """
    QUESTION 2
    
    In Python, what is the main difference between a function and a method?
    
    Option 1
    Methods have a parameter named self, while functions do not.
    
    Option 2
    Functions are defined outside of classes, while methods are defined inside of
    and part of classes.
    
    Option 3
    There is no difference. They are interchangeable terms.
    
    Option 4
    Methods are defined in built-in library modules, while functions are defined
    in your own code.
    """
    
    answer = "Functions are defined outside of classes, while methods are defined "
    answer += "inside of and part of classes."
    
    print "Question 602 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_602()

##=================================================================

def hw_603():
    """
    QUESTION 3
    
    As an example class, consider the following code from one of the videos:
    
    class Character:
        def __init__(self, name, initial_health):
            self.name = name
            self.health = initial_health
            self.inventory = []
            
        def __str__(self):
            s  = "Name: " + self.name
            s += " Health: " + str(self.health)
            s += " Inventory: " + str(self.inventory)
            return s
        
        def grab(self, item):
            self.inventory.append(item)
            
        def get_health(self):
            return self.health
            
    What does the self parameter represent?
    
    Option 1
    The Character class
    
    Option 2
    An object (instance) of the Character class.
    
    Option 3
    Whatever happens to be passed to it.
    
    Option 4
    The method that is being defined.
    """
    
    answer = "An object (instance) of the Character class."
    
    print "Question 603 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_603()

##=================================================================

def hw_604():
    """
    QUESTION 4
    
    Assume you have the following class and method definition, parts of which have
    been omitted.
    
    class My_Class:
        ...

        def my_method(self, value1, value2):
            '''
            Assumes its inputs are two values and does something.
            '''
            ...

    my_object = My_Class()
    
    The last line defines the var my_object as an object of My_Class class. Which
    of the following is proper syntax for using the method on this object?
    
    Option 1
    my_method(my_object, 1, 2)
    
    Option 2
    My_Class.my_object.my_method(1, 2)
    
    Option 3
    my_object.my_method(1, 2)
    
    Option 4
    my_method(My_Class, 1, 2)
    
    Option 5
    My_Class.my_method(my_object, 1, 2)
    """
    
    answer = "my_object.my_method(1, 2)"
    
    print "Question 604 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_604()

##=================================================================

def hw_605():
    """
    QUESTION 5
    
    We want to have balls that move around. Which of the following designs
    represents encapsulation best?
    
    Option 1
    class Ball:
        def __init__(self, c, r):
            self.center = c
            self.radius = r

        def get_position(self):
            return self.center

        def set_position(self, new_position):
            self.center = new_position


    # balls : A list of Ball objects
    balls = ...

    def move(ball, move_vector):
        '''
        Changes the position of the given Ball object by adding the given vector.
        '''
        position = ball.get_position()
        position[0] += move_vector[0]
        position[1] += move_vector[1]
        ball.set_position(position)
    
    Option 2
    # centers : A list of points, the balls' center points
    centers = ...
    # radii : A list of numbers, the balls' radii
    radii = ...

    def move(ball_number, move_vector):
        '''
        Changes the position of the numbered ball by adding the given vector.
        '''
        centers[ball_number][0] += move_vector[0]
        centers[ball_number][1] += move_vector[1]
    
    Option 3
    class Ball:
        def __init__(self, c, r):
            self.center = c
            self.radius = r

        def move(self, move_vector):
            '''
            Changes the position of the ball by the given vector.
            '''
            self.center[0] += move_vector[0]
            self.center[1] += move_vector[1]


    # balls : A list of Ball objects
    balls = ...

    Option 4
    class Ball:
        def __init__(self, c, r):
            self.center = c
            self.radius = r


    # balls : A list of Ball objects
    balls = ...

    def move(ball, move_vector):
        '''
        Changes the position of the given Ball object by adding the given vector.
        '''
        ball.center[0] += move_vector[0]
        ball.center[1] += move_vector[1]
    """
    
    answer = '''
class Ball:
    def __init__(self, c, r):
        self.center = c
        self.radius = r

    def move(self, move_vector):
        """
        Changes the position of the ball by the given vector.
        """
        self.center[0] += move_vector[0]
        self.center[1] += move_vector[1]


# balls : A list of Ball objects
balls = ...
'''
    
    print "Question 605 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_605()

##=================================================================

def hw_606():
    """
    QUESTION 6
    
    A common feature in many OO langs is method overloading. In this quiz question,
    you will learn by example what overloading is and whether or not Python supports it.
    
    Turn the following English description into code:
    * Start a class def. We'll call it Overload.
    * Define an __init__ method. Along with the standard self, it has one parameter.
        The method does nothing useful for this example--use the Python do nothing
        statement pass for the body.
    * Define a second __init__ method. Along with self, it has two parameters. This
        method also does nothing uesful.
        
    Outside of the class, we want to create two Overload objects. If Python supports
    overloading, you will be able to create an Overload object with one arg, and create
    another with two args. Does Python support overloading?
    """
    # Build the class and test it.
    
    class Overload:
        def __init__(self, a):
            pass
        def __init__(self, a, b):
            pass
        
    #f = Overload(1)
    #g = Overload(1, 2)

    ## TypeError: __init__() takes exactly 3 arguments (2 given)

    answer = "No"
    
    print "Question 606 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_606()

##=================================================================

def hw_607():
    """
    QUESTION 7
    
    First, complete the following class definition: (see below)
    
    The deposit and withdraw methods each change the account balance. The withdraw
    method also deducts a fee of 5 dollars from the balance if the withdrawal (before
    any fees) results in a negative balance. Since we also have the method get_fees, 
    you will need to have a var to keep track of the fees paid. 
    
    Here's one possible test of the class. It should print the values 10 and 5,
    respectively, since the withdrawal incurs a fee of 5 dollars (see below).
    
    Copy and paste the much longer test (below, too). What two numbers are printed
    at the end? Enter the two numbers, separated only by spaces.
    """
    # Fill in the BankAccount class methods with working code.
    
    class BankAccount:
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
    
    # Test it using the short test.
    
    my_account = BankAccount(10)
    my_account.withdraw(15)
    my_account.deposit(20)
    print my_account.get_balance(), my_account.get_fees()
    print "-"*10
    
    # The small test was successful. The long test is below.
    
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
    #print my_account.get_balance(), my_account.get_fees()
    
    answer = my_account.get_balance(), my_account.get_fees()
    
    print "Question 607 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_607()

##=================================================================

def hw_608():
    """
    QUESTION 8
    
    We again use the BankAccount class from the previous problem. You should be 
    able to use the same definition for both problems. Of course, a bank with only one
    account will go out of business, so we want our BankAccount class to work with
    many accounts. Naturally, each bank account should have its own balance, with
    deposits and withdrawals going to the appropriate account. Similarly, the penalty
    fees for each account should be kept separate.
    
    Here's one possible test with multiple accounts. It should print the values
    10, 5, 5, and 0 (short test, below).
    
    Copy and paste the longer test (below). What four numbers are printed at the
    end? Enter the four numbers, separated only by spaces.
    """
    # Short test.
    
    class BankAccount:
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
    
    account1 = BankAccount(10)
    account1.withdraw(15)
    account2 = BankAccount(15)
    account2.deposit(10)
    account1.deposit(20)
    account2.withdraw(20)
    print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()
    print "-"*10
    
    # The short test was successful. Long test below:
    
    account1 = BankAccount(20)
    account1.deposit(10)
    account2 = BankAccount(10)
    account2.deposit(10)
    account2.withdraw(50)
    account1.withdraw(15)
    account1.withdraw(10)
    account2.deposit(30)
    account2.withdraw(15)
    account1.deposit(5)
    account1.withdraw(10)
    account2.withdraw(10)
    account2.deposit(25)
    account2.withdraw(15)
    account1.deposit(10)
    account1.withdraw(50)
    account2.deposit(25)
    account2.deposit(25)
    account1.deposit(30)
    account2.deposit(10)
    account1.withdraw(15)
    account2.withdraw(10)
    account1.withdraw(10)
    account2.deposit(15)
    account2.deposit(10)
    account2.withdraw(15)
    account1.deposit(15)
    account1.withdraw(20)
    account2.withdraw(10)
    account2.deposit(5)
    account2.withdraw(10)
    account1.deposit(10)
    account1.deposit(20)
    account2.withdraw(10)
    account2.deposit(5)
    account1.withdraw(15)
    account1.withdraw(20)
    account1.deposit(5)
    account2.deposit(10)
    account2.deposit(15)
    account2.deposit(20)
    account1.withdraw(15)
    account2.deposit(10)
    account1.deposit(25)
    account1.deposit(15)
    account1.deposit(10)
    account1.withdraw(10)
    account1.deposit(10)
    account2.deposit(20)
    account2.withdraw(15)
    account1.withdraw(20)
    account1.deposit(5)
    account1.deposit(10)
    account2.withdraw(20)
    #print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()
    
    answer = account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()
    
    print "Question 608 Answer:"
    print answer
    print "-"*50
    print "\n"
    
hw_608()

##=================================================================
##=================================================================