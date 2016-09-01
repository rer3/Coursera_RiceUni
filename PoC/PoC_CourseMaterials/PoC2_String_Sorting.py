"""
Coursera / Rice University
Principles of Computing (Part 2)
String Sorting

Sorting a list of strings using an alphabetical grid
Revised
"""

import random
## Set seed = 1 for consistent results
random.seed(1)

# constants
NUM_CHARS = 26
CHARACTERS = [chr(ord("a") + char_num) for char_num in range(NUM_CHARS)] 


def order_by_letter(string_list, letter_pos):
    """
    Takes a list of strings and order them alphabetically 
    using the letter at the specified position
    """
    buckets = [[] for idx in range(NUM_CHARS)]
    ##print "starting bucket fill"
    for string in string_list:
        char_index = ord(string[letter_pos]) - ord("a")
        ##print "char_index:", char_index
        buckets[char_index] += [string]
        ##print "buckets:", buckets
    
    answer = []
    for char_index in range(NUM_CHARS):
        answer += buckets[char_index]
        ## Below code accomplishes the same thing
        ##answer.extend(buckets[char_index])
    ##print "ANSWER:", answer
    return answer

def string_sort(string_list, length):
    """
    Order a list of strings of the specific length in ascending alphabetical order
    """
    for position in range(length -1 , -1, -1):
        ## Each position is sorted starting with rightmost chr
        ## This ensures that 'hda' occurs before 'hdc'
        ## Or 'wxc' before 'lxh' when the second chr is sorted
        ## Much like 'dfu' being put before 'dps' at the second sort
        ## The final loop sorts by first character
        ##print
        ##print "POSITION FILL:", position
        string_list = order_by_letter(string_list, position)
    return string_list

def run_example():
    """
    Example of string sort
    """
    string_length = 3
    list_length = 50
#    test_list = ["".join([random.choice(CHARACTERS) for _ in range(string_length)]) 
#                 for dummy_index in range(50)]
    ## Set list length to a variable
    test_list = ["".join([random.choice(CHARACTERS) for idx in range(string_length)])
                 for idx in range(list_length)]
    print "Unsorted string list is", test_list
    print "Sorted string list is", string_sort(test_list, string_length)
     
run_example()