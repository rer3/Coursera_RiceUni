"""
Rice University / Coursera: Principles of Computing (Part 2)
Week 1: Class Notes
Inheritance
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

#-----------------------------------------------------------------
## Provided code.

class Base:
    """
    Simple base class.
    """    
    def __init__(self, num):
        self._number = num

    def __str__(self):
        """
        Return human readable string.
        """
        return str(self._number)
        

class Sub(Base):
    """
    Simple sub class.
    """
    def __init__(self, num):
        Base.__init__(self, num)
    
obj = Sub(42)
print obj
print "\n"

##=================================================================

# Testing Grounds

# 'object' parameter not needed, but is used in some examples.
class Carbon(object):
    """
    Class for the element carbon.
    """
    def __init__(self, amount, density):
        self.amount = amount
        self.density = density
        self.atomic_number = 6
        self.electron_config = {"1s": 2, "2s": 2, "2p":2}
        
    def __str__(self):
        """
        Return human readable string.
        """
        string = "Element: carbon" + "\n"
        string += "Atomic Number: " + str(self.atomic_number) + "\n"
        string += "Electron Configuration: " + str(self.electron_config) + "\n"
        string += "Amount: " + str(self.amount) + "g" + "\n"
        string += "Density: " + str(self.density) + "g/cm**3" + "\n"
        return string
        
    def get_amount(self):
        """
        Return the amount of the element.
        """
        return self.amount
        
        
class Diamond(Carbon):
    """
    Class for the diamond allotrope of carbon.
    """
    def __init__(self, amount, density):
        self.amount = amount
        self.density = density
        
        
class Graphite(Carbon):
    """
    Class for the graphite allotrope of carbon.
    """
    def __init__(self, amount):
        Carbon.__init__(self, amount, 2.2)

        
carbon = Carbon(16.4, 3.5)
print carbon

#diamond = Diamond(12.3, 3.5)
#print diamond
# Diamond subclass has no attribute 'atomic_number'.
# This is due to a lack of inheritance of that field from the base.

graphite = Graphite(5.5)
print graphite
print "Amount of graphite:", graphite.get_amount()

##=================================================================
##=================================================================