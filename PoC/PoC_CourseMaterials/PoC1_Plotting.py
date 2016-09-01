#http://www.codeskulptor.org/#user40_yDCmZljwid_2.py
"""
Rice University / Coursera: Principles of Computing (Part 1)
Week 2 Lecture
Example of creating a plot using simpleplot
    
Input is a list of point lists (one per function)
Each point list is a list of points of the form 
[(x0, y0), (x1, y1, ..., (xn, yn)]
"""

import simpleplot

class Plotzilla:
    """
    Class that performs the function of this example,
    but encapsulated now 
    """

    # create three sample functions

    def double(self, num):
        """
        Example of linear function
        """
        return 2 * num

    def square(self, num):
        """
        Example of quadratic function
        """
        return num ** 2

    def exp(self, num):
        """
        Example of exponential function
        """
        return 2 ** num
        
    def create_plots(self, begin, end, stride):
        """ 
        Plot the function double, square, and exp
        from beginning to end using the provided stride

        The x-coordinates of the plotted points start
        at begin, terminate at end and are spaced by 
        distance stride
        """

        # generate x coordinates for plot points
        x_coords = []
        current_x = begin
        while current_x < end:
            x_coords.append(current_x)
            current_x += stride
            
        # compute list of (x, y) coordinates for each function
        double_plot = [(x_val, self.double(x_val)) for x_val in x_coords]
        square_plot = [(x_val, self.square(x_val)) for x_val in x_coords]
        exp_plot = [(x_val, self.exp(x_val)) for x_val in x_coords]
        
        # plot the list of points
        simpleplot.plot_lines("Plots of three functions", 600, 400, "x", "f(x)",
                             [double_plot, square_plot, exp_plot], 
                             True, ["double", "square", "exp"])
    
plotz = Plotzilla()
plotz.create_plots(0, 10, .1)
                          