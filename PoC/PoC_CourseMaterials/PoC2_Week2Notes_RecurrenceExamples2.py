"""
Rice University / Coursera: Principles of Computing (Part 2)
Week 2: Class Notes
Recurrence Examples 2: Binary and Gray Numbers
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

#-----------------------------------------------------------------
## Provided code with modifications to minimize code and clarify computations.

def make_binary(length):
    """
    Function that generates ordered list of binary numbers in 
    ascending order
    """
    if length == 0:
        return [""]
    
    all_but_first = make_binary(length - 1)
    
    answer = []
    for bits in all_but_first:
        answer.append("0" + bits)
    for bits in all_but_first:
        answer.append("1" + bits)
    return answer

def bin_to_dec(bin_num):
    """
    Convert a binary number to decimal
    """
    if len(bin_num) == 0:
        return 0
    else:
        return 2* bin_to_dec(bin_num[:-1]) + int(bin_num[-1])                                       
    
def make_gray(length):
    """
    Function that generates ordered list of Gray codes in 
    ascending order
    """
    if length == 0:
        return [""]
    
    all_but_first = make_gray(length - 1)
    
    answer = []
    for bits in all_but_first:
        answer.append("0" + bits)
        
    all_but_first.reverse()
    
    for bits in all_but_first:
        answer.append("1" + bits)
    return answer

def gray_to_bin(gray_code):
    """
    Convert a Gray code to a binary number
    """
    if len(gray_code) <= 1:
        return gray_code
    else:
        significant_bits = gray_to_bin(gray_code[:-1])
        last_bit = (int(gray_code[-1]) + int(significant_bits[-1])) % 2
        return significant_bits + str(last_bit)

def run_examples():
    """
    print out example of Gray code representations
    """
    num = 5
    
    print
    print "Binary numbers of length", num
    bin_list = make_binary(num)
    for item in bin_list:
        print item

    print
    print "Decimal numbers up to", 2 ** num
    for binary_number in bin_list:
        print bin_to_dec(binary_number)

    print
    print "Gray codes of length", num
    gray_list = make_gray(num)
    for item in gray_list:
        print item

    print
    print "Gray codes converted to binary numbers"
    for gray_code in gray_list:
        print gray_to_bin(gray_code)
    
run_examples()

##=================================================================
##=================================================================