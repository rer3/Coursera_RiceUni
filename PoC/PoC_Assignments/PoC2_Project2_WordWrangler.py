"""
Coursera / Rice University: Principles of Computing (Part 2)
Week 2: Project 2
Word Wrangler
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# All import statements needed.

import codeskulptor
import simplegui
import urllib2

# Below is the link to the description of this assignment.

COURSE = "https://class.coursera.org/principlescomputing2-004/"
DESCRIPTION = COURSE + "wiki/view?page=wrangler"

#-----------------------------------------------------------------
## Provided template poc_wrangler_template for this assignment. References
## to poc_wrangler_provided removed. All stubs for the six functions to implement
## are removed as well.

"""
Student code for Word Wrangler game
"""

WORDFILE = "assets_scrabble_words3.txt"

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    run_game(wrangler)

#-----------------------------------------------------------------
## Provided WordWranglerGUI class, draw_word and run_gui function.

"""
Word Wrangler GUI
"""

# Global constants
FONT_SIZE = 20
OFFSET = 4
ROW_HEIGHT = FONT_SIZE + OFFSET
COLUMN_WIDTH = 80
GRID_SIZE = [25, 4]
CANVAS_WIDTH = COLUMN_WIDTH * GRID_SIZE[1]
CANVAS_HEIGHT = ROW_HEIGHT * GRID_SIZE[0]


def draw_word(canvas, word, pos):
    """
    Helper function to draw word on canvas at given position
    """
    box = [pos, 
           [pos[0], pos[1] - ROW_HEIGHT], 
           [pos[0] + COLUMN_WIDTH, pos[1] - ROW_HEIGHT], 
           [pos[0] + COLUMN_WIDTH, pos[1]], 
           pos]
    canvas.draw_text(word, [pos[0] + 2, pos[1] - 4], FONT_SIZE, "White")
    canvas.draw_polyline(box, 1, "White")

class WordWranglerGUI:
    """
    Container for interactive content
    """    
    def __init__(self, game):
        """ 
        Create frame and timers, register event handlers
        """
        self.game = game
        self.frame = simplegui.create_frame("Word Wrangler", 
                                            CANVAS_WIDTH, CANVAS_HEIGHT, 250)
        self.frame.set_canvas_background("Blue")        
               
        self.enter_input = self.frame.add_input("Enter word for new game", 
                                                self.enter_start_word, 250)
        labelmsg = "Stars correspond to hidden words formed using letters "
        labelmsg += "from the entered word. Hidden words are listed in alphabetical order"
        self.frame.add_label(labelmsg, 250)
        self.frame.add_label("", 250)
        self.guess_label = self.frame.add_input("Enter a word", 
                                                self.enter_guess, 250)       
        self.frame.add_label("For a hint, click on a starred word", 250)
        self.frame.set_mouseclick_handler(self.peek)
        self.frame.set_draw_handler(self.draw)

        self.enter_input.set_text("python")
        self.game.start_game("python")
        
    def start(self):
        """
        Start frame
        """
        self.frame.start()
        
    def enter_start_word(self, entered_word):
        """ 
        Event handler for input field to enter letters for new game
        """
        self.game.start_game(entered_word)

    def enter_guess(self, guess):
        """ 
        Event handler for input field to enter guess
        """
        self.game.enter_guess(guess)
        self.guess_label.set_text("")

    def peek(self, pos):
        """ 
        Event handler for mouse click, exposes clicked word
        """
        [index_i, index_j] = [pos[1] // ROW_HEIGHT, pos[0] // COLUMN_WIDTH]
        peek_idx = index_i + index_j * GRID_SIZE[0]
        if peek_idx < len(self.game.get_strings()):
            self.game.peek(peek_idx)
                         
    def draw(self, canvas):
        """
        Handler for drawing subset words list
        """
        string_list = self.game.get_strings()
        
        for col in range(GRID_SIZE[1]):
            for row in range(GRID_SIZE[0]):
                pos = [col * COLUMN_WIDTH, (row + 1) * ROW_HEIGHT]
                idx = row + col * GRID_SIZE[0]
                if idx < len(string_list):
                    draw_word(canvas, string_list[idx], pos)
        # if self.winner_flag:
        #     canvas.draw_text("You win!", 
        #                      [4 * ROW_HEIGHT, COLUMN_WIDTH], 
        #                      2 * FONT_SIZE, "Yellow")

        
# Start interactive simulation    
def run_gui(game):
    """
    Encapsulate frame
    """
    gui = WordWranglerGUI(game)
    gui.start()

#-----------------------------------------------------------------
## Provided WordWrangler game class poc_wrangler_gui. References to GUI
## poc_wrangler_gui removed as it is located in this doc.

"""
Provided code for Word Wrangler game
"""

class WordWrangler:
    """
    Game class for Word Wrangler
    """
    def __init__(self, word_list, remdup, intersect, mergesort, substrs):
        self._word_list = word_list
        self._subset_strings = []
        self._guessed_strings = []
        self._remove_duplicates = remdup
        self._intersect = intersect
        self._merge_sort = mergesort
        self._substrs = substrs

    def start_game(self, entered_word):
        """
        Start a new game of Word Wrangler
        """
        if entered_word not in self._word_list:
            print "Not a word"
            return
        strings = self._substrs(entered_word)
        sorted_strings = self._merge_sort(strings)
        all_strings = self._remove_duplicates(sorted_strings)
        self._subset_strings = self._intersect(self._word_list, all_strings)
        self._guessed_strings = []        
        for word in self._subset_strings:
            self._guessed_strings.append("*" * len(word))
        self.enter_guess(entered_word)           
        
    def enter_guess(self, guess):
        """
        Take an entered guess and update the game
        """        
        if ((guess in self._subset_strings) and 
            (guess not in self._guessed_strings)):
            guess_idx = self._subset_strings.index(guess)
            self._guessed_strings[guess_idx] = self._subset_strings[guess_idx]

    def peek(self, peek_index):
        """
        Exposed a word given in index into the list self._subset_strings
        """
        self.enter_guess(self._subset_strings[peek_index])
        
    def get_strings(self):
        """
        Return the list of strings for the GUI
        """
        return self._guessed_strings
    

def run_game(wrangler):
    """
    Start the game.
    """
    run_gui(wrangler)

##=================================================================

DIRECTIONS = '''
Overview
----------
In this mini-project we will create a simple word game. The game will take an input 
word and then generate all valid words that can be created using the letters in the 
input word. You will then play the game by guessing all of the words. The objective 
of this mini-project is to work with ordered lists and recursion. While it is possible 
to write the functions in other ways, we strongly encourage you to follow the spirit 
of the mini-project. The only way to become more comfortable with recursion is to 
write recursive functions!

We have provided a working GUI and a class to manage the state of the game. You 
will be responsible for writing several helper functions. These functions will be 
used by the provided code in order to build the list of valid words that are composed 
of letters from the input word.

Testing your mini-project
----------
The provided template includes the stubs for the functions that you will need to 
implement for this mini-project. Remember you should be testing each function as 
you write it. Don't try to implement all of the functions. If you do, you will have 
errors that will interact in inexplicable ways making your program hard to debug.

Submit your code (with the calls to run commented out) to this Owltest page. Note 
that trying to debug your mini-project using the tests in OwlTest can be very tedious 
since they are slow and give limited feedback. Instead, we strongly suggest that you 
first test your program using your own test suite. Programs that pass these tests are 
much more likely to pass the OwlTest tests.

Remember that OwlTest uses Pylint to check that you have followed the coding style 
guidelines for this class. Deviations from these style guidelines will result in deductions 
from your final score. Please read the feedback from Pylint closely. If you have 
questions, feel free to consult this page and the class forums.

When you are ready to submit your code to be graded formally, submit your code to 
the CourseraTest page for this mini-project that is linked on the main assignment page.

Implementation
----------
In this mini-project you should not use set, sorted, or sort. Don't be surprised when 
you lose points if you do. Again, the point of the mini-project is for you to improve 
your skills in working with ordered lists and recursion, not to write the most compact 
code possible using Python built-in functions/methods. It is important to understand 
the concepts involved in working with ordered data, as you will be able to apply those 
concepts to a much wider range of problems in the future. Further, not every language 
has efficient support for this type of data, so it is also important to understand how 
these functions might be implemented.

Important: None of these functions should mutate their inputs. You must leave the 
inputs as they are and return new lists.

Phase One
----------
You should first write the functions remove_duplicates(list1) and 
intersect(list1, list2). These functions can both be written iteratively (using loops, 
not recursion). All of the arguments to these functions are lists in ascending order. 
Both functions should return new sorted lists.

* remove_duplicates should return a new sorted list with the same elements as the 
    input, list1, but without any duplicate elements.
* intersect should return a new sorted list that contains only the elements that are in 
    both input lists, list1 and list2.
    
Remember that the input lists will already be sorted. You should exploit this fact to 
make these functions simpler to write than if you had to handle arbitrary lists.

Phase Two
----------
You should next implement merge sorting. To do so, you will need to write two 
functions, merge(list1, list2) and merge_sort(list1). The input lists to merge will 
both be lists in ascending order. The input to merge_sort will be an unsorted list. 
While you could write merge recursively, you should write it iteratively because it 
will generate too many recursive calls for reasonably sized lists. However, you 
must write merge_sort recursively.

* merge should return a new sorted list that contains all of the elements in 
    either list1 and list2.
* merge_sort should return a new sorted list that contains all of the elements 
    in list1 sorted in ascending order.
    
Again, remember that the input lists to merge will already be sorted. You should 
exploit this fact to make it simpler to write. Further, merge_sort should use merge 
to help sort the list!

Phase Three
----------
Now, you should implement gen_all_strings(word). This function is the heart of the 
word wrangler game. It takes a string as input and returns a list of strings. It should 
return all possible strings that can be constructed from the letters in the input word. 
More formally, it should return all strings of length 0 to len(word) that can be 
composed of the letters that occur in word, in any order. Further, each letter should 
be considered distinct, so if the same letter appears twice in the word, then the 
output will have duplicate strings.

For example, if word is "aab", gen_all_strings would return ["", "b", "a", "ab", "ba", 
"a", "ab", "ba", "aa", "aa", "aab", "aab", "aba", "aba", "baa", "baa"]. Notice that 
the string "aa" appears twice in the output. This is because each a is considered 
distinct, so these two strings correspond to the two different orderings of the two 
a letters in the input word. Note that it does not matter in what order the strings 
appear in the list. The functions you have already written will be used afterwards 
to sort and remove duplicates from the final lists (you should not do this within 
gen_all_strings).

Note that this function is similar (but not identical) to something that you have 
previously written in this course. This time, however, ordering of the output list 
is not important, duplicates are allowed, and you must write it recursively. The 
basic idea is as follows:

1.) Split the input word into two parts: the first character (first) and the 
    remaining part (rest).
2.) Use gen_all_strings to generate all appropriate strings for rest. Call this list 
    rest_strings.
3.) For each string in rest_strings, generate new strings by inserting the initial 
    character, first, in all possible positions within the string.
4.) Return a list containing the strings in rest_strings as well as the new strings 
    generated in step 3.

This is a rough outline of one approach that will allow you to generate all strings 
that can be composed from the letters of word. (Remember to think about the base case!)

Final Touches
----------
Finally, you should implement load_words(filename) which will load a "dictionary" 
(not a Python dictionary, but rather a conventional dictionary with valid English 
language words) from a file. The dictionary file is simply one string per line, where 
each string is a valid word in the game. You can see the dictionary file here: 
http://codeskulptor-assets.commondatastorage.googleapis.com/
assets_scrabble_words3.txt. You may use either urllib2.urlopen (either in CodeSkulptor 
or locally) or open (only if you are running locally and have downloaded the file) 
to open the file. Note that this function will not be tested. You only need implement 
it if you wish to play the word wrangler game using the provided GUI.
'''

##=================================================================

# Phase One

# First I must write functions to remove duplicates in a sorted list and to
# return a new list (from two sorted lists) that contains only elements in both
# input lists. I am unable to use set, sorted, or sort in my implementation.
# Also, these functions are not allowed to mutate their inputs. 

# Since we can assume that the input lists in both of these functions are already
# sorted, we can treat them a certain way that allows for the output lists to be
# sorted as well. The remove_duplicates function can simply iterate through the
# input list from the first element to the last and add all unique elements (after
# a quick check using "in") to a separate list, which is then returned. This not
# only returns a sorted list of unique items, but it also does not mutate the input.

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, 
    but with no duplicates.

    This function can be iterative.
    """
    
    unique = []
    for elem in list1:
        if elem not in unique:
            unique.append(elem)
    return unique
    
# The intersect function can work similarly, in that it can iterate through each
# list. Instead of checking for the existence of an element in a separate list,
# instead this function must compare the elements in both lists to one another.
# If there are two equivalent items, one of that item is appended to a separate 
# list that is returned. If the two items being compared are not equal, then the
# loop can move on to the next two items.

# Note that each list's items can't be compared to the analogous item (i.e. the
# item at the same index) in the other list. If you have two lists: [1, 2, 3, 4] and
# [2, 3, 4, 5], comparing i = 1 and j = 1, respectively, returns no match (1 vs. 2). 
# Iterating through the two lists in this manner arrives at zero shared items and
# returns an empty list, even though there are obviously three shared elements
# between the two lists. 

# A healthy approach is to mimic the merge component of the MergeSort algm. 
# In merge, you begin at the first index of both lists and then compare which
# is less than or equal to the other.  As merge too takes two sorted lists, always
# appending the lesser valued item to another list ensures that the ascending
# order is retained and that the running time is efficient (O(n), essentially). Here,
# in intersect, we can use the equivalence condition to not only look for which
# two items are the same (and thus must be appended to our returned list of
# shared items), but also to avoid missteps like the one mentioned in the previous
# paragraph. The list with the lower value in this check can be incremented, while
# the other list index is kept the same. 

# To illustrate, for the two lists: [1, 2, 3, 4] and [2, 3, 4, 5], you have 1v2. 
# Since they are not equal, increment list1 since it has the lesser value. Then
# look at 2v2. Since they are equal, append 2 to the returned list and increment
# both (since now it is known that 2 is shared between the lists and another
# comparison to 2 is unnecessary). Then 3v3, which are equal. Then 4v4. Then
# while list2 has one more element in it, list1 is out of elements and therefore
# can't possibly share any more elements with list2, as there are none to share.
# The loop can stop. This detail can inform the type of loop (a while is a good fit)
# and the condition it checks (as long as BOTH lists have elements to compare).

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that 
    are in both list1 and list2.

    This function can be iterative.
    """
    in_both = []
    idx1, idx2 = 0, 0
    while idx1 < len(list1) and idx2 < len(list2):
        val1, val2 = list1[idx1], list2[idx2]
        if val1 < val2:
            idx1 += 1
        elif val1 > val2:
            idx2 += 1
        else:
            in_both.append(val1)
            idx1 += 1
            idx2 += 1
    return in_both

# A quick test shows that they both work. Uncomment to run.

# list1 = [2, 3, 4, 5, 6]
# list2 = [3, 4, 4, 5, 7]
# print remove_duplicates(list2)
# print intersect(list1, list2)

##=================================================================

# Phase Two

# Next implement merge sorting. First, merge(list1, list2) will work much like
# intersect from Phase One. Here, the conditional statements must look for 
# values being less than or equal to other values. Also, once one list has been
# exhausted, the remaining elements in the other list must be added to the
# returned "merged" list via the extend method. This allows the elems to be added
# without separating them into a distinct list next to the other loose elems. 

# A different (and more fitting, in this case) way to iterate through each list and add 
# items to a returned list is to use the pop method. Instead of using indices to 
# traverse each list, which could be used in this case, pop returns the first
# element of the list--the one that is currently being compared by the conditional--
# and then the elem can easily be added to the returned "merged" list. The 
# conditional, instead of comparing two elems at specified indices, can always just
# compare the elements of both lists at index 0. The one which is less than the
# other can be popped and appended to the returned list. Deciding what to do if
# they are equal is arbitrary; the elem can be popped from either list. 

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements 
    that are in either list1 and list2.

    This function can be iterative.
    """
    merged = []
    copy1, copy2 = list(list1), list(list2)
    while len(copy1) > 0 and len(copy2) > 0:
        if copy1[0] <= copy2[0]:
            merged.append(copy1.pop(0))
        else:
            merged.append(copy2.pop(0))
    if len(copy1) == 0:
        merged.extend(copy2)
    else:
        merged.extend(copy1)
    return merged
    
# For merge_sort(list1), the base case must be identified first. Here, it is when
# the length of a list is one or no items. In each of those cases, the input list
# is already sorted ("a" is a sorted list, as is "") and can be returned. The
# MergeSort algm cuts the input list in half and passes each back to MergeSort
# recursively. The lists returned for each half are then merged at the end and
# this merged list is returned. 

def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) < 2:
        return list1
    left = merge_sort(list1[:len(list1)/2])
    right = merge_sort(list1[len(list1)/2:])
    return merge(left, right)
    

# A quick test shows that they both work. Uncomment to run.

# list1 = [1, 3, 5, 7, 9]
# list2 = [2, 4, 6, 8, 10, 12, 14, 16]
# print merge(list1, list2)

# list3 = [12, 13, 2, 8, 3, 9, 4, 88, 9, 3, 13, 137, 1, 1, 16]
# print merge_sort(list3)

##=================================================================

# Phase Three

# Finally, implement gen_all_strings(word) which takes an input string and 
# returns a list of strings that contains all possible strings that can be constructed
# from the letters in the input word of length 0 to len(word). It is okay that this
# function includes duplicates in the returned list. The directions are pretty
# straightforward and I will follow them closely.

# First, since this is a recursive function, I will identify the base case. Here, it
# is when the length of a word is zero, as the example shows that "" appears
# in the returned string for "aab". In this base case, the function should return
# [""] (a list because that is what we want this function to return, and because
# we want to iterate over the list as string permutations are created). 

# Under the base case, the first step is to split the word into its first char and
# the rest of the chars. A recursive call is made using the rest of the chars
# as input, to be saved in variable "rest_strings". Then for each string in
# rest_strings, new strings are generated by inserting the initial character
# "first" in all possible positions within the string. The list of strings returned
# contains both the strings in rest_strings (as they have already undergone
# this process in recursive steps) and the strings generated by this insertion
# of first into all of the positions within all of the strings in rest_strings.

# Note that when inserting first into the positions within each string in rest_strings,
# the range of indices must be increased by one. This is because for a string with
# three chars (e.g. "abc"), there are four positions in which another char can be
# inserted: before "a", before "b", before "c", and after "c": zabc, azbc, abzc, abcz.
# A range of len(string) would only have indices 0, 1, and 2 in this example, and the
# final configuration would not be computed using the statement that I have in mind
# (string[:i] + first + string[i:]) where i = index.

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters 
    in word in any order.

    Returns a list of all strings that can be formed from the 
    letters in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return [""]
    else:
        first, rest = word[0], word[1:]
        rest_strings = gen_all_strings(rest)
        new_strings = []
        for string in rest_strings:
            for idx in range(len(string) + 1):
                new_string = string[:idx] + first + string[idx:]
                new_strings.append(new_string)    
        ## Below only generates strings of original size len(word).
        # return new_strings
        return rest_strings + new_strings
        
# The function only returned strings of size len(word). I forgot to add the
# strings returned by recursive calls (of length len(word) - 1) to the final
# returned list. This may come in handy at a later time, but here it is an
# unwanted side effect and an error. The return statement was changed,
# and the function now works.

word = "can"
print gen_all_strings(word)

##=================================================================

# Final Touches

# This function must be implemented in order to play the Word Wrangler game
# using the provided GUI. It is fairly simple: load the full url using file2url, 
# open the file using the urlopen method, and return a list of words that includes
# all words in that file (to be iterated over). The run() function, provided and located
# here in the shared area at the top, will reference this function and the provided
# word list. Note that each word has a newline escape char at the end of it, so the
# word list must remove that (e.g. word[:-1]). 

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = codeskulptor.file2url(filename)
    online_file = urllib2.urlopen(url)
    return [word[:-1] for word in online_file]

# OwlTest returned no errors, and the GUI worked just fine. Uncomment call to run
# to play the game.

#run()

##=================================================================
##=================================================================