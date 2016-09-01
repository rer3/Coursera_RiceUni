"""
Rice University / Coursera: Intro to Interactive Programming in Python (Part 2)
Week 2: Project 6
Blackjack
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# All import statements needed.

import random
import simplegui

# Below is the link to the description of this assignment.

COURSE = "https://class.coursera.org/interactivepython2-009/"
DESCRIPTION = COURSE + "human_grading/view/courses/975652/assessments/33/submissions"

#-----------------------------------------------------------------
## Provided Blackjack template (examples-blackjack_template), commented out.

# # Mini-project #6 - Blackjack

# import simplegui
# import random

# # load card sprite - 936x384 - source: jfitz.com
# CARD_SIZE = (72, 96)
# CARD_CENTER = (36, 48)
# card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

# CARD_BACK_SIZE = (72, 96)
# CARD_BACK_CENTER = (36, 48)
# card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# # initialize some useful global variables
# in_play = False
# outcome = ""
# score = 0

# # define globals for cards
# SUITS = ('C', 'S', 'H', 'D')
# RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
# VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# # define card class
# class Card:
    # def __init__(self, suit, rank):
        # if (suit in SUITS) and (rank in RANKS):
            # self.suit = suit
            # self.rank = rank
        # else:
            # self.suit = None
            # self.rank = None
            # print "Invalid card: ", suit, rank

    # def __str__(self):
        # return self.suit + self.rank

    # def get_suit(self):
        # return self.suit

    # def get_rank(self):
        # return self.rank

    # def draw(self, canvas, pos):
        # card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    # CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        # canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# # define hand class
# class Hand:
    # def __init__(self):
        # pass  # create Hand object

    # def __str__(self):
        # pass  # return a string representation of a hand

    # def add_card(self, card):
        # pass  # add a card object to a hand

    # def get_value(self):
        # # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # pass  # compute the value of the hand, see Blackjack video
   
    # def draw(self, canvas, pos):
        # pass  # draw a hand on the canvas, use the draw method for cards
 
      
# # define deck class 
# class Deck:
    # def __init__(self):
        # pass  # create a Deck object

    # def shuffle(self):
        # # shuffle the deck 
        # pass    # use random.shuffle()

    # def deal_card(self):
        # pass  # deal a card object from the deck
    
    # def __str__(self):
        # pass  # return a string representing the deck


# #define event handlers for buttons
# def deal():
    # global outcome, in_play

    # # your code goes here
    
    # in_play = True

# def hit():
    # pass  # replace with your code below
 
    # # if the hand is in play, hit the player
   
    # # if busted, assign a message to outcome, update in_play and score
       
# def stand():
    # pass  # replace with your code below
   
    # # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # # assign a message to outcome, update in_play and score

# # draw handler    
# def draw(canvas):
    # # test to make sure that card.draw works, replace with your code below
    
    # card = Card("S", "A")
    # card.draw(canvas, [300, 300])

# # initialization frame
# frame = simplegui.create_frame("Blackjack", 600, 600)
# frame.set_canvas_background("Green")

# #create buttons and canvas callback
# frame.add_button("Deal", deal, 200)
# frame.add_button("Hit",  hit, 200)
# frame.add_button("Stand", stand, 200)
# frame.set_draw_handler(draw)

# # get things rolling
# deal()
# frame.start()

# # remember to review the gradic rubric

#-----------------------------------------------------------------
## Provided testing template for the Card class (examples-card_template).
## Commented out.

# # Testing template for the Card class

# import random

# # define globals for cards
# SUITS = ['C', 'S', 'H', 'D']
# RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
# VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# #################################################
# # Student should insert the implementation of the Card class here

    
# ###################################################
# # Test code

# c1 = Card("S", "A")
# print c1
# print c1.get_suit(), c1.get_rank()
# print type(c1)

# c2 = Card("C", "2")
# print c2
# print c2.get_suit(), c2.get_rank()
# print type(c2)

# c3 = Card("D", "T")
# print c3
# print c3.get_suit(), c3.get_rank()
# print type(c3)


# ###################################################
# # Output to console

# #SA
# #S A
# #<class '__main__.Card'>
# #C2
# #C 2
# #<class '__main__.Card'>
# #DT
# #D T
# #<class '__main__.Card'>

#-----------------------------------------------------------------
## Provided code for joining string lists (exercises_mouse_join_solution).

# # String list joining problem

# ###################################################
# # Student should enter code below

# def string_list_join(string_list):
    # ans = ""
    # for i in range(len(string_list)):
        # ans += string_list[i]
    # return ans

# ###################################################
# # Test data

# print string_list_join([])
# print string_list_join(["pig", "dog"])
# print string_list_join(["spam", " and ", "eggs"])
# print string_list_join(["a", "b", "c", "d"])

# ###################################################
# # Output

# #
# #pigdog
# #spam and eggs
# #abcd

#-----------------------------------------------------------------
## Provided testing code for the Hand class (examples-hand_template).

# # Testing template for the Hand class

# import random

# # define globals for cards
# SUITS = ['C', 'S', 'H', 'D']
# RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
# VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# # define card class
# class Card:
    # def __init__(self, suit, rank):
        # if (suit in SUITS) and (rank in RANKS):
            # self.suit = suit
            # self.rank = rank
        # else:
            # print "Invalid card: ", suit, rank

    # def __str__(self):
        # return self.suit + self.rank

    # def get_suit(self):
        # return self.suit

    # def get_rank(self):
        # return self.rank

    # def draw(self, canvas, pos):
        # card_loc = (card_size[0] * (0.5 + RANKS.index(self.rank)), card_size[1] * (0.5 + SUITS.index(self.suit)))
        # canvas.draw_image(card_images, card_loc, card_size, [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)


# #####################################################
# # Student should insert code for Hand class here


    
# ###################################################
# # Test code

# c1 = Card("S", "A")
# c2 = Card("C", "2")
# c3 = Card("D", "T")
# print c1, c2, c3
# print type(c1), type(c2), type(c3)

# test_hand = Hand()
# print test_hand

# test_hand.add_card(c1)
# print test_hand

# test_hand.add_card(c2)
# print test_hand

# test_hand.add_card(c3)
# print test_hand

# print type(test_hand)

# ###################################################
# # Output to console
# # note that the string representation of a hand will 
# # vary based on how you implemented the __str__ method

# #SA C2 DT
# #<class '__main__.Card'> <class '__main__.Card'> <class '__main__.Card'>
# #Hand contains 
# #Hand contains SA 
# #Hand contains SA C2 
# #Hand contains SA C2 DT 
# #<class '__main__.Hand'>

#-----------------------------------------------------------------
## Provided testing template for Deck class (examples-deck_template).

# # Testing template for the Deck class

# import random

# # define globals for cards
# SUITS = ['C', 'S', 'H', 'D']
# RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
# VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# # define card class
# class Card:
    # def __init__(self, suit, rank):
        # if (suit in SUITS) and (rank in RANKS):
            # self.suit = suit
            # self.rank = rank
        # else:
            # print "Invalid card: ", suit, rank

    # def __str__(self):
        # return self.suit + self.rank

    # def get_suit(self):
        # return self.suit

    # def get_rank(self):
        # return self.rank

    # def draw(self, canvas, pos):
        # card_loc = (card_size[0] * (0.5 + RANKS.index(self.rank)), card_size[1] * (0.5 + SUITS.index(self.suit)))
        # canvas.draw_image(card_images, card_loc, card_size, [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)


# #####################################################
# # Student should insert code for Deck class here
        

    
# ###################################################
# # Test code

# test_deck = Deck()
# print test_deck
# print type(test_deck)

# c1 = test_deck.deal_card()
# print c1
# print type(c1)
# print test_deck

# c2 = test_deck.deal_card()
# print c2
# print type(c2)
# print test_deck

# test_deck = Deck()
# print test_deck
# test_deck.shuffle()
# print test_deck
# print type(test_deck)

# c3 = test_deck.deal_card()
# print c3
# print type(c3)
# print test_deck

# ###################################################
# # Output to console
# # output of string method for decks depends on your implementation of __str__
# # note the output of shuffling is randomized so the exact order of cards
# # need not match

# #Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ DK 
# #<class '__main__.Deck'>
# #DK
# #<class '__main__.Card'>
# #Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ 
# #DQ
# #<class '__main__.Card'>
# #Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ 
# #Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ DK 
# #Deck contains CT H6 C4 H9 D6 HJ D2 S5 D8 H2 ST H4 HQ HK S8 D3 CJ D5 DK DQ DA S9 S6 S2 DJ C8 SJ C9 D4 C7 SK CK S3 CA SA S4 CQ S7 HA H3 C5 D9 DT H7 HT C2 SQ H8 C6 D7 C3 H5 
# #<class '__main__.Deck'>
# #H5
# #<class '__main__.Card'>
# #Deck contains CT H6 C4 H9 D6 HJ D2 S5 D8 H2 ST H4 HQ HK S8 D3 CJ D5 DK DQ DA S9 S6 S2 DJ C8 SJ C9 D4 C7 SK CK S3 CA SA S4 CQ S7 HA H3 C5 D9 DT H7 HT C2 SQ H8 C6 D7 C3 

#-----------------------------------------------------------------
## Provided testing template for the get_value method for Hands
## (examples-getvalue_template).

# # Testing template for the get_value method for Hands

# import random

# # define globals for cards
# SUITS = ['C', 'S', 'H', 'D']
# RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
# VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# # define card class
# class Card:
    # def __init__(self, suit, rank):
        # if (suit in SUITS) and (rank in RANKS):
            # self.suit = suit
            # self.rank = rank
        # else:
            # print "Invalid card: ", suit, rank

    # def __str__(self):
        # return self.suit + self.rank

    # def get_suit(self):
        # return self.suit

    # def get_rank(self):
        # return self.rank

    # def draw(self, canvas, pos):
        # card_loc = (card_size[0] * (0.5 + RANKS.index(self.rank)), card_size[1] * (0.5 + SUITS.index(self.suit)))
        # canvas.draw_image(card_images, card_loc, card_size, [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)


# #####################################################
# # Student should insert code for Hand class here
        

    
# ###################################################
# # Test code

# c1 = Card("S", "A")
# c2 = Card("C", "2")
# c3 = Card("D", "T")
# c4 = Card("S", "K")
# c5 = Card("C", "7")
# c6 = Card("D", "A")

# test_hand = Hand()
# print test_hand
# print test_hand.get_value()

# test_hand.add_card(c2)
# print test_hand
# print test_hand.get_value()

# test_hand.add_card(c5)
# print test_hand
# print test_hand.get_value()

# test_hand.add_card(c3)
# print test_hand
# print test_hand.get_value()

# test_hand.add_card(c4)
# print test_hand
# print test_hand.get_value()

# test_hand = Hand()
# print test_hand
# print test_hand.get_value()

# test_hand.add_card(c1)
# print test_hand
# print test_hand.get_value()

# test_hand.add_card(c6)
# print test_hand
# print test_hand.get_value()

# test_hand.add_card(c4)
# print test_hand
# print test_hand.get_value()

# test_hand.add_card(c5)
# print test_hand
# print test_hand.get_value()

# test_hand.add_card(c3)
# print test_hand
# print test_hand.get_value()

# ###################################################
# # Output to console
# # note that the string representation of a hand may vary
# # based on your implementation of the __str__ method

# #Hand contains 
# #0
# #Hand contains C2 
# #2
# #Hand contains C2 C7 
# #9
# #Hand contains C2 C7 DT 
# #19
# #Hand contains C2 C7 DT SK 
# #29
# #Hand contains 
# #0
# #Hand contains SA 
# #11
# #Hand contains SA DA 
# #12
# #Hand contains SA DA SK 
# #12
# #Hand contains SA DA SK C7 
# #19
# #Hand contains SA DA SK C7 DT 
# #29

#-----------------------------------------------------------------
## My original implementation of the Blackjack game.

# ###########################################
# ################ BLACKJACK ################
# ###########################################

# import simplegui
# import random

# # Load card sprite
# CARD_SIZE = (72, 96)
# CARD_CENTER = (36, 48)
# card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

# CARD_BACK_SIZE = (72, 96)
# CARD_BACK_CENTER = (36, 48)
# card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# # Initialize global game vars
# WIDTH = 850
# HEIGHT = 550

# in_play = False
# outcome = ""
# score = 100
# game_msg = ""
# deck = []
# dealt_card = []
# player = []
# dealer = []
# wager = 10

# # Global vars for cards
# SUITS = ('C', 'S', 'H', 'D')
# RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
# VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# # Card class - draws cards on the canvas
# class Card:
    # def __init__(self, suit, rank):
        # if (suit in SUITS) and (rank in RANKS):
            # self.suit = suit
            # self.rank = rank
        # else:
            # self.suit = None
            # self.rank = None
            # print "Invalid card: ", suit, rank

    # def __str__(self):
        # return self.suit + self.rank

    # def get_suit(self):
        # return self.suit

    # def get_rank(self):
        # return self.rank

    # def draw(self, canvas, pos):
        # card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    # CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        # canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# # Hand class - add card object from Deck class and return value of hand
# class Hand:
    # def __init__(self):
        # self.player_hand = []

    # def __str__(self):
        # s = ""
        # for card in self.player_hand:
            # s = s + str(card) + " "
        # return s

    # def add_card(self, card):
        # self.player_hand.append(card)

    # def get_value(self):
        # value = 0
        # has_ace = False
        # for card in self.player_hand:
            # rank = card.get_rank()
            # value += VALUES[rank]
            # if rank == "A":
                # has_ace = True
        # if has_ace:
            # if value <= 11:
                # value += 10
        # return value
   
    # def draw(self, canvas, pos):
        # for card in self.player_hand:
            # card.draw(canvas, pos)
            # pos[0] = pos[0] + 100
        # if in_play:
            # canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [95.5,214], CARD_BACK_SIZE) #115.5, 184
        
# # Deck class - shuffle and deal card objects
# class Deck:
    # def __init__(self):
        # dealt_card = []
        # self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        # self.shuffle()

    # def shuffle(self):
        # random.shuffle(self.cards)

    # def deal_card(self):
        # dealt_card = self.cards.pop(0)
        # return dealt_card
    
    # def __str__(self):
        # s = ""
        # for card in self.cards:
            # s = s + str(card) + " "
        # return s

# # Button event handlers

# def deal():
    # global in_play, outcome, score, game_msg, deck, player, dealer
    # if score <= 0:
        # game_msg = "You're broke! Click RESET to regain funds."
    # elif wager > score:
        # game_msg = "You must decrease your bet!"
    # else:
        # if in_play:
            # score -= wager
        # in_play = True
        # outcome = ""
        # game_msg = "Hit or stand?"
        # deck = Deck()
        # player = Hand()
        # dealer = Hand()
        # player.add_card(deck.deal_card())
        # dealer.add_card(deck.deal_card())
        # player.add_card(deck.deal_card())
        # dealer.add_card(deck.deal_card())

# def hit():
    # global in_play, outcome, score, game_msg
    # if in_play:
        # player.add_card(deck.deal_card())
        # if player.get_value() > 21:
            # in_play = False
            # outcome = "Dealer: " + str(dealer.get_value()) + "      Player: " + str(player.get_value())
            # score -= wager
            # game_msg = "Player busted! Dealer wins! Click DEAL to play again."

# def stand():
    # global in_play, outcome, score, game_msg
    # if in_play:
        # while dealer.get_value() < 17:
            # dealer.add_card(deck.deal_card())
        # if dealer.get_value() > 21:
            # score += wager
            # game_msg = "Dealer busted! You win! Click DEAL to play again."
        # elif dealer.get_value() > player.get_value():
            # score -= wager
            # game_msg = "Dealer wins! Click DEAL to play again."
        # elif dealer.get_value() == player.get_value():
            # score -= wager
            # game_msg = "Draw! Dealer wins! Click DEAL to play again."
        # else:
            # score += wager
            # game_msg = "You win! Click DEAL to play again."
        # outcome = "Dealer: " + str(dealer.get_value()) + "      Player: " + str(player.get_value())
        # in_play = False
        
# def reset():
    # global in_play, outcome, score, game_msg, wager
    # in_play = False
    # outcome = ""
    # score = 100
    # game_msg = "Click DEAL to begin a new game."
    # deck = []
    # dealt_card = []
    # player = []
    # dealer = []
    # wager = 10
        
# def maxbet():
    # global wager
    # if score > 0:
        # wager = score
        
# # Text input handler

# def bet(text):
    # global wager
    # if not text.isdigit():
        # feedback.set_text("You must enter a number")
    # elif int(text) > score:
        # feedback.set_text("You don't have enough funds")
    # elif int(text) > 1000:
        # feedback.set_text("Max bet is 1,000")
    # else:
        # wager = int(text)
        # feedback.set_text("")
        
# # Draw handler

# def draw(canvas):
    # titlelen = frame.get_canvas_textwidth("Blackjack", 50)
    # canvas.draw_text("Blackjack", [WIDTH/2 - titlelen/2,50], 50, "white")
    
    # canvas.draw_text("Dealer :", [60,140], 30, "white")
    # dealer.draw(canvas, [60,165])
    # canvas.draw_text("Player :", [60,310], 30, "white")
    # player.draw(canvas, [60,335])
    
    # msglen = frame.get_canvas_textwidth(game_msg, 36)
    # canvas.draw_text(game_msg, [WIDTH/2 - msglen/2,484], 36, "yellow")
    # outlen = frame.get_canvas_textwidth(outcome, 34)
    # canvas.draw_text(outcome, [WIDTH/2 - outlen/2,530], 34, "white")
    
    # moneylen = frame.get_canvas_textwidth("Your Money", 34)
    # scorelen = frame.get_canvas_textwidth(str(score), 34)
    # canvas.draw_polygon([[24, 30], [34 + moneylen,30], [34 + moneylen, 100],
                        # [24, 100]], 1, "black", "#0f9d58")
    # canvas.draw_text("Your Money", [30, 60], 34, "black")
    # canvas.draw_text(str(score), [30 + moneylen/2 - scorelen/2, 92], 34, "yellow")
    
    # betlen = frame.get_canvas_textwidth("Your Bet", 34)
    # wagerlen = frame.get_canvas_textwidth(str(wager), 34)
    # canvas.draw_polygon([[WIDTH - 30 - betlen - 10, 30],
                         # [WIDTH - 30 + 10, 30],
                         # [WIDTH - 30 + 10, 100],
                         # [WIDTH - 30 - betlen - 10, 100]], 1, "black", "#8ca7c6")    
    # canvas.draw_text("Your Bet", [WIDTH - 30 - betlen, 60], 34, "black")
    # canvas.draw_text(str(wager), [WIDTH - 30 - betlen/2 - wagerlen/2, 92], 34, "yellow")

# # Initialize frame
# frame = simplegui.create_frame("Blackjack", WIDTH, HEIGHT)
# frame.set_canvas_background("green")

# # Add buttons
# inp = frame.add_input("Type your new wager here and hit enter to change your bet:", bet, 100)
# feedback = frame.add_label("")
# frame.add_button("MAX BET", maxbet, 100)
# frame.add_label("")
# frame.add_button("DEAL", deal, 100)
# frame.add_button("HIT", hit, 100)
# frame.add_button("STAND", stand, 100)
# frame.add_button("RESET", reset, 100)
# frame.set_draw_handler(draw)

# # Start game and frame
# deal()
# frame.start()

##=================================================================

DIRECTIONS = '''
Description
----------
Blackjack is a simple, popular card game that is played in many casinos. Cards in 
Blackjack have the following values: I already know them. The game logic for our
simplified version of BJ is as follows. The player and the dealer are each dealt two
cards initially with one of the dealer's cards being dealt face down (hole card).
The player may then ask for the dealer to repeatedly "hit" his hand by dealing him
another card. Yadda yadda, same old rules. The dealer wins ties in this version.
Also, aces count as 11 for the dealer unless it causes their hand to bust.

Development Process
----------
We suggest you develop this game in two phases. First, concentrate on implementing
the basic logic of BJ, then focus on building a more full-featured version. First use
print statements, then replace them with statements that draw images and text
on the canvas.

In phase one, we will provide testing templates for four of the steps. The templates
are designed to check whether your class ipmlementations work correctly. You should
copy your class definition into the testing template and compare the console output
generated by running the template with the provided output. If the output matches,
it is likely that your implementation of the class is correct. DO NOT PROCEED TO THE
NEXT STEP UNTIL YOUR CODE WORKS WITH THE TESTING TEMPLATE. Debugging code that
uses incorrectly implemented classes is extremely difficult. Avoid this problem by
using our provided testing templates.

Phase One
----------
1.) Download the program template (above) for this project and review the class
    definition for the Card class. The class is already implemented. Past the Card 
    class definition into the provided testing template (above) and verify that
    our implementation works as expected.
2.) Implement the methods __init__, __str__, add_card for the Hand class. We suggest
    modeling a hand as a list of Card objs that are stored in a field in the Hand
    object. The __init__ method should initialize the Hand object to have an empty list
    of Card objects. The add_card should append a Card obj to the list of cards. The
    __str__ method hsould return a string representation of a Hand obj.

    For help in implementing the __str__ method, refer back to the solution to
    question 4 in the practice exercises for week 5a (above). Remember to use the
    string method for Card objects to convert each card in the hand's list of cards
    into a string. (Don't covert a Card object into a string in add_card to make 
    your string method work). Once you have implemented the Hand class, test it using
    the provided testing template (above). 
3.) Implement the methods for the Deck class listed in the project template. We 
    suggest modeling a deck of cards as a list of cards. You can generate this list 
    using a pair of nested for loops or a list comprehension. Remember to use the
    Card initializer to create your cards. Use random.shuffle() to shuffle the deck
    of cards. Once you have implemented the Deck class, test your Deck class using
    the provided testing template (above). Remember that the deck is randomized after
    shuffling, so the output of the testing template should match the output in the
    comments in form but not in exact value.
4.) Implement the handler for a "Deal" button that shuffles the deck and deals
    the two cards to both the dealer and player. The event handler deal for this
    button should shuffle the deck (stored as a global variable), create new player
    and dealer hands (stored as global variables), and add two cards to each hand.
    To transfer a card from the deck to a hand, you should use the deal_card method
    of the Deck class and the add_card method of Hand class in combination. The
    resulting hands should be printed to the console with an appropriate message
    indicating which hand is which.
5.) Implement the get_value method for the Hand class. You should use the provided
    VALUE dictionary to look up the value of a single card in conjunction with the 
    logic explained in the video lecture for this project to compute the value of
    a hand. Once you have implemented get_value, test it using the provided testing
    template (above).
6.) Implement the handler for a "Hit" button. If the value of the hand is less than
    or equal to 21, clicking this button adds an extra card to player's hand. If the
    value exceeds 21 aftering being hit, print "You have busted".
7). Implement the handler for a "Stand" button. If the player has busted, remind
    the player that they have busted. Otherwise, repeatedly hit the dealer until his
    hand has value 17 or more (using a while loop). If the dealer busts, let the
    player know. Otherwise, compare the value of the player's and dealer's hands.
    If the value of the player's hand is less than or equal to the dealer's hand, the
    dealer wins. Otherwise, the player has won. The dealer wins ties.
    
In our version of BJ, a hand is automatically dealt to the player and dealer when
the program starts. In particular, the program template includes a call to the deal()
function during initialization. At this point, we would suggest testing your
implementation of BJ extensively.

Phase Two
----------
In the second phase of your implementation, you will add five features. For those
involving drawing with global variables, remember to initialize these variables to
appropriate values (like creating empty hands for the player and dealer) just before
starting the frame.

1.) Implement your own draw method for the Hand class using the draw method of the
    Card class. We suggest drawing a hand as a horizontal sequence of cards where the
    parameter pos is the pos of the upper left corner of the leftmost card. To simplify
    your code, you may assume that only the first five cards of a player's hand need
    to be visible on the canvas.
2.) Replace printing in the console by drawing text messages on the canvas. We suggest
    adding a global outcome string that is drawn in the draw handler using draw_text. 
    These messages should prompt the player to take some required action and have a
    form similar to "Hit or stand?" and "New deal?". Also, draw the title of the game,
    "Blackjack", somewhere on the canvas.
3.) Add logic using the global variable in_play that keeps track of whether the player's
    hand is still being played. If the round is still in play, you should draw an image
    on the back of a card (provided in the template) over the dealer's first card
    (the hole) to hide it. Once the round is over, the dealer's hole card should be
    displayed.
4.) Add a score counter that keeps track of wins and losses for your BJ session.
    In the simplest case, the program displays wins minus losses. However, you are
    welcome to implement a more sophisticated betting/scoring system.
5.) Modify the logic for the "Deal" button to create and shuffle a new deck (or restock
    and shuffle an existing deck) each time the "Deal" button is clicked. This change
    avoids the situation where the deck becomes empty during play.
6.) Finally, modify the deal function such that, if the "Deal" button is clicked during
    the middle of a round, the program reports that the player lost the round
    and updates the score appropriately.
    
Congrats, you have just built BJ. To wrap up, please review the demo of our version
of BJ in the video lecture to ensure that your version has full functionality. 

Grading Rubric (18 pts total)
----------
You must adhere to the game logic required in this project. After the deadline, you
are welcome to enhance your implementation with more realistic game logic such as
pushes on ties, splitting pairs, and doubling down.
* 1 pt - The program displays the title "Blackjack" on the canvas.
* 1 pt - The program displays 3 buttons ("Deal", "Hit", and "Stand") in the control area.
* 2 pts - The program graphically displays the player's hand using card images.
* 2 pts - The program graphically displays the dealer's hand using card images.
* 1 pt - The dealer's hole card is hidden until the current round is over.
* 2 pts - Pressing "Deal" deals out two cards each to player and dealer.
* 1 pt - Pressing "Deal" in the middle of the round causes the player to lose the
    current round.
* 1 pt - Pressing the "Hit" button deals another card to the player.
* 1 pt - Pressing "Stand" deals cards to the dealer as necessary.
* 1 pt - The program correctly recognizes the player busting.
* 1 pt - The program correctly recognizes the dealer busting.
* 1 pt - The program correctly computes hand values and declares a winner. Evaluate
    based on messages.
* 2 pts - The program accurately prompts the player for an action with messages
    similar to "Hit or stand?" and "New deal?".
* 1 pt - The program implements a scoring system that correctly reflects wins and
    losses. Please be generous in evaluating this item.
'''

##=================================================================

# Let's look at the constants. First there are those that correspond to the card size.
 
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# The global variables for cards must be initialized. My VALUES variable uses 
# a better method to pair each rank with its corresponding value.

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = dict(zip(RANKS, range(1, 11)+[10]*3))

# My initial implementation is really good, in my not so humble opinion. I will
# use almost the same GUI layout, but I will encapsulate the game functions and
# the GUI in separate classes. I will also implement a realistic version that will not
# be submitted at this time. The full code will be below. All of the tests will be
# encapsulated as well and run after each updated implementation of the Card,
# Hand, and Deck classes, as well as the get_value method for the Hand class.

def class_tester(subject):
    """
    Function to test implementations of classes and class methods.
    """
    def card_test():
        """
        Test Card class.
        """
        c1 = Card("S", "A")
        print c1
        print c1.get_suit(), c1.get_rank()
        print type(c1)

        c2 = Card("C", "2")
        print c2
        print c2.get_suit(), c2.get_rank()
        print type(c2)

        c3 = Card("D", "T")
        print c3
        print c3.get_suit(), c3.get_rank()
        print type(c3)
        
        print
        print "."*20
        print "Expected Output:"
        output = '''
        SA
        S A
        <class '__main__.Card'>
        C2
        C 2
        <class '__main__.Card'>
        DT
        D T
        <class '__main__.Card'>
        '''
        print output
        print "."*20
        print
        
    def hand_test():
        """
        Test Hand class.
        """
        c1 = Card("S", "A")
        c2 = Card("C", "2")
        c3 = Card("D", "T")
        print c1, c2, c3
        print type(c1), type(c2), type(c3)

        test_hand = Hand()
        print test_hand

        test_hand.add_card(c1)
        print test_hand

        test_hand.add_card(c2)
        print test_hand

        test_hand.add_card(c3)
        print test_hand

        print type(test_hand)

        print
        print "."*20
        print "Expected Output:"
        output = '''
        SA C2 DT
        <class '__main__.Card'> <class '__main__.Card'> <class '__main__.Card'>
        Hand contains 
        Hand contains SA 
        Hand contains SA C2 
        Hand contains SA C2 DT 
        <class '__main__.Hand'>
        '''
        print output
        print "."*20
        print

    def deck_test():
        """
        Test Deck class.
        """
        test_deck = Deck()
        print test_deck
        print type(test_deck)

        c1 = test_deck.deal_card()
        print c1
        print type(c1)
        print test_deck

        c2 = test_deck.deal_card()
        print c2
        print type(c2)
        print test_deck

        test_deck = Deck()
        print test_deck
        test_deck.shuffle()
        print test_deck
        print type(test_deck)

        c3 = test_deck.deal_card()
        print c3
        print type(c3)
        print test_deck
        
        print
        print "."*20
        print "Expected Output:"
        output = '''
        Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ DK 
        <class '__main__.Deck'>
        DK
        <class '__main__.Card'>
        Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ 
        DQ
        <class '__main__.Card'>
        Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ 
        Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ DK 
        Deck contains CT H6 C4 H9 D6 HJ D2 S5 D8 H2 ST H4 HQ HK S8 D3 CJ D5 DK DQ DA S9 S6 S2 DJ C8 SJ C9 D4 C7 SK CK S3 CA SA S4 CQ S7 HA H3 C5 D9 DT H7 HT C2 SQ H8 C6 D7 C3 H5 
        <class '__main__.Deck'>
        H5
        <class '__main__.Card'>
        Deck contains CT H6 C4 H9 D6 HJ D2 S5 D8 H2 ST H4 HQ HK S8 D3 CJ D5 DK DQ DA S9 S6 S2 DJ C8 SJ C9 D4 C7 SK CK S3 CA SA S4 CQ S7 HA H3 C5 D9 DT H7 HT C2 SQ H8 C6 D7 C3 
        '''
        print output
        print "."*20
        print
        
    def get_value_test():
        """
        Test get_value method for Hand class.
        """
        c1 = Card("S", "A")
        c2 = Card("C", "2")
        c3 = Card("D", "T")
        c4 = Card("S", "K")
        c5 = Card("C", "7")
        c6 = Card("D", "A")

        test_hand = Hand()
        print test_hand
        print test_hand.get_value()

        test_hand.add_card(c2)
        print test_hand
        print test_hand.get_value()

        test_hand.add_card(c5)
        print test_hand
        print test_hand.get_value()

        test_hand.add_card(c3)
        print test_hand
        print test_hand.get_value()

        test_hand.add_card(c4)
        print test_hand
        print test_hand.get_value()

        test_hand = Hand()
        print test_hand
        print test_hand.get_value()

        test_hand.add_card(c1)
        print test_hand
        print test_hand.get_value()

        test_hand.add_card(c6)
        print test_hand
        print test_hand.get_value()

        test_hand.add_card(c4)
        print test_hand
        print test_hand.get_value()

        test_hand.add_card(c5)
        print test_hand
        print test_hand.get_value()

        test_hand.add_card(c3)
        print test_hand
        print test_hand.get_value()

        print
        print "."*20
        print "Expected Output:"
        output = '''
        Hand contains 
        0
        Hand contains C2 
        2
        Hand contains C2 C7 
        9
        Hand contains C2 C7 DT 
        19
        Hand contains C2 C7 DT SK 
        29
        Hand contains 
        0
        Hand contains SA 
        11
        Hand contains SA DA 
        12
        Hand contains SA DA SK 
        12
        Hand contains SA DA SK C7 
        19
        Hand contains SA DA SK C7 DT 
        29
        '''
        print output
        print "."*20
        print
        
    if subject == "Card":
        card_test()
    elif subject == "Hand":
        hand_test()
    elif subject == "Deck":
        deck_test()
    elif subject == "get_value":
        get_value_test()

# Now I can begin to implement the classes. First, Card. Since it's been implemented,
# that work is finished. There is a check to make sure that the suit and rank are
# valid (i.e. from the lists assigned to the constants that hold the suit and rank
# options). The draw() method takes a pos argument so that the card can be placed
# at a distinct location on the canvas. The card_loc var pinpoints the card on the
# singular image where the card is located. It chooses the initial center plus the
# card size times the index of the card's rank. The cards are shown from A to K,
# so 0 to 12. At index 0, the Ace is chosen. At SUITS index 2, the Ace of Hearts
# is chosen in a similar fashion. Then a call to the canvas.draw_image method
# draws the card. Note that the card_loc is used for the src center and CARD_SIZE
# constant is used for the src width/height. The pos arg passed to this draw method
# for the Card class has to it the CARD_CENTER values added to it in order to set
# the dest center. As mentioned in the directions, this is due to setting card pos
# from the pixel in the upperleft corner. 

# Underscores are added to the beginning of my fields.

        
class Card:
    """
    Class to store a playing card.
    """
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self._suit = suit
            self._rank = rank
        else:
            self._suit = None
            self._rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        """
        Return string representation of the card.
        """
        return self._suit + self._rank

    def get_suit(self):
        """
        Return the suit of the card.
        """
        return self._suit

    def get_rank(self):
        """
        Return the rank of the card.
        """
        return self._rank

    def draw(self, canvas, pos):
        """
        Draw method for the card.
        """
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self._rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self._suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], 
                          pos[1] + CARD_CENTER[1]], CARD_SIZE)
     
        
# Uncomment to run
#class_tester("Card")

# The test completed successfully. Now to implement Hand. The string representation
# in the tester will dictate how I implement my __str__ method for the Hand class.
# The individual Card.__str__ methods will be called with spaces in between (e.g. 
# "HA C2 D3". The get_value for the Hand class must take into account aces and
# update the value of a hand accordingly. Once method of doing this is to check 
# the value and, if it is <= 11 and there is an Ace in hand, add 10 points. This
# takes advantage of the fact that there will never be two Aces counted as 11
# as that will bust your hand (= 22). I will use a list comprehension this time.

# At this time, the draw method will remain unchanged. The in_play variable is
# used several times throughout (and may stick around in its current form if
# not eliminated or updated to reflect BlackjackGame/GUI class variable--or some
# constant). The positions are based on tweaking the GUI. After the class, I will
# test both the Hand class, as well as the get_value method.

        
class Hand:
    """
    Class to store a hand of cards.
    """
    def __init__(self):
        self._hand = []

    def __str__(self):
        """
        Return string representation of the hand.
        """
        s = "Hand contains "
        for card in self._hand:
            s = s + str(card) + " "
        return s

    def add_card(self, card):
        """
        Add a card to the hand.
        """
        self._hand.append(card)

    def get_value(self):
        """
        Return the value of the hand.
        """
        ranks = [card.get_rank() for card in self._hand]
        value = sum(VALUES[card] for card in ranks)
        if "A" in ranks and value <= 11:
            value += 10
        return value
        
    def num_cards(self):
        return len(self._hand)
   
    def draw(self, canvas, pos):
        """
        Draw method for the hand.
        """
        for card in self._hand:
            card.draw(canvas, pos)
            pos[0] = pos[0] + 30


# Uncomment to run.
#class_tester("Hand")
#class_tester("get_value")

# The Hand class tested successfully. I added a "Hand contains " component to the
# beginning of the string to mimic the expected output of the tests. Now to implement
# the Deck class. This is fairly simple. The _cards field is initialized as a list of all
# cards, iterating over every suit for every rank. The shuffle method is called to 
# shuffle this initial deck. The shuffle method simply calls random.shuffle on the 
# cards. Dealing a card pops a card from the front of the list. The string method
# was written like the previous __str__ methods, and to mimic the tester.
# I may come back and implement a draw method for the Deck that draws it on
# the canvas and shows the cards being taken from it and dealt (I WILL do this).


class Deck:
    """
    Class to store a deck of cards.
    """
    def __init__(self):
        self._cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self._cards)

    def deal_card(self):
        return self._cards.pop(0)
    
    def __str__(self):
        s = "Deck contains "
        for card in self._cards:
            s = s + str(card) + " "
        return s
        
        
# Uncomment to run
#class_tester("Deck")

# The Deck class tested successfully. Now to implement the game logic. In the
# previous implementation (and in the directions), everything is written in global
# functions. Instead, BlackjackGame and BlackjackGUI will split up the game logic
# and GUI, respectively. The buttons will be implemented in the GUI, but the functions
# that they call will be found within the game logic. The BlackjackGame object will
# be passed to the GUI object.

# Status constants
INPLAY = 1
PLAYERWIN = 2
DEALERWIN = 3
DRAW = 4
PLAYERBUST = 5
DEALERBUST = 6
GAMEOVER = 7
OVERBET = 8
BETTING = 9

# Message for each status
STATUSMSG = {
    INPLAY: "Hit or stand?",
    PLAYERWIN: "Player wins! Change bet or click DEAL.",
    DEALERWIN: "Dealer wins! Change bet or click DEAL.",
    DRAW: "Draw! You lose! Change bet or click DEAL.",
    PLAYERBUST: "Player busted! You lose! Change bet or click DEAL.",
    DEALERBUST: "Dealer busted! You win! Change bet or click DEAL.",
    GAMEOVER: "You're broke! Click RESET to regain funds.",
    OVERBET: "Your bet is too big!",
    BETTING: "Click Deal to begin."
    }
    
STATUSCOLOR = {
    INPLAY: "yellow",
    PLAYERWIN: "#00ff00",
    DEALERWIN: "black",
    DRAW: "black",
    PLAYERBUST: "black",
    DEALERBUST: "#00ff00",
    GAMEOVER: "black",
    OVERBET: "#ff7f00",
    BETTING: "#00008b"
    }
    
STACKCOLOR = {
    0: "white",
    1: "red",
    2: "yellow",
    3: "aqua",
    4: "pink",
    5: "purple",
    6: "black"
    }
    
INITIAL_MONEY = 1000
INITIAL_WAGER = 10
MAXBET = 1000


class BlackjackGame:
    """
    Class to play a game of Blackjack.
    """
    def __init__(self):
        self._money = INITIAL_MONEY
        self._wager = INITIAL_WAGER
        self._status = INPLAY
        self._deck = Deck()
        self._player = Hand()
        self._dealer = Hand()
        self._player_turn = False
        
    def get_money(self):
        """
        Return player money.
        """
        return self._money
        
    def get_wager(self):
        """
        Return player wager.
        """
        return self._wager
        
    def get_status(self):
        """
        Return round status.
        """
        return self._status
        
    def set_wager(self, value):
        """
        Set wager to new value.
        """
        if not self._player_turn:
            if value <= self._money:
                self._wager = value
                self._status = BETTING
            
    def max_wager(self):
        """
        Bet all money.
        """
        if not self._player_turn:
            if self._money <= MAXBET:
                self._wager = self._money
            elif self._money > MAXBET:
                self._wager = MAXBET
            self._status = BETTING
        
    def is_penniless(self):
        """
        Check if money is zero or below.
        """
        return self._money <= 0
    
    def deal(self):
        """
        Deal two cards each to player and dealer at the start of a round.
        """
        if self.is_penniless():
            self._status = GAMEOVER
            self._player_turn = False
        elif self._money - self._wager >= 0:
            self._status = INPLAY
            self._money -= self._wager
            self._deck = Deck()
            self._player = Hand()
            self._dealer = Hand()
            self._player.add_card(self._deck.deal_card())
            self._dealer.add_card(self._deck.deal_card())
            self._player.add_card(self._deck.deal_card())
            self._dealer.add_card(self._deck.deal_card())
            self._player_turn = True
        else:
            self._status = OVERBET
            self._player_turn = False
        
    def hit(self):
        """
        Player hits, add a card to player hand.
        """
        if self._status == INPLAY and self._player_turn:
            self._player.add_card(self._deck.deal_card())
            self.update_status()
            
    def stand(self):
        """
        Player stands, dealer hits until 17 or bust.
        """
        if self._status == INPLAY and self._player_turn:
            self._player_turn = False
            while self._dealer.get_value() < 17:
                self._dealer.add_card(self._deck.deal_card())
            self.update_status()
            
    def update_status(self):
        """
        Check outcome of game once all cards have been dealt.
        """
        player = self._player.get_value()
        dealer = self._dealer.get_value()
            
        if self._player_turn:
            if player > 21:
                self._status = PLAYERBUST
                self._player_turn = False
        else:
            if dealer > 21:
                self._status = DEALERBUST
                self._money += 2 * self._wager
            elif player > dealer:
                self._status = PLAYERWIN
                self._money += 2 * self._wager
            elif player < dealer:
                self._status = DEALERWIN
            elif player == dealer:
                self._status = DRAW
            self._player_turn = False
            
    def reset(self):
        """
        Reset all game fields.
        """
        self._money = INITIAL_MONEY
        self._wager = INITIAL_WAGER
        self._deck = Deck()
        self._player = Hand()
        self._dealer = Hand()
        self._player_turn = False
        
        
# The Memory game GUI had many more instructions in it than the MemoryGame class.
# I will try to reverse that and keep most of the game logic where it belongs with the
# game class. The BlackjackGUI class will focus on the interactive elements of the
# game, such as input fields and feedback messages.

CANVASWIDTH = 850
CANVASHEIGHT = 550
CONTROLWIDTH = 150
        
        
class BlackjackGUI:
    """
    Class to run the GUI for a game of Blackack.
    """
    def __init__(self, game):
        self._game = game
        self._message = STATUSMSG[self._game.get_status()]
        
        self._frame = simplegui.create_frame("Blackjack", CANVASWIDTH, CANVASHEIGHT,
                                             CONTROLWIDTH)
        self._frame.set_canvas_background("green")
        
        self._frame.add_label("Enter your wager below and hit enter.")
        self._frame.add_label("")
        inp_msg = "Wager:"
        self._inp_wager= self._frame.add_input(inp_msg, self.bet, 100)
        self._wager_msg = self._frame.add_label("")
        self._frame.add_button("MAX BET", self.maxbet, 100)
        self._frame.add_label("")
        self._frame.add_button("DEAL", self.deal, 100)
        self._frame.add_button("HIT", self.hit, 100)
        self._frame.add_button("STAND", self.stand, 100)
        self._frame.add_button("RESET", self.reset, 100)
        self._frame.set_draw_handler(self.draw)
        self.deal()
        self._frame.start()
        
    def bet(self, text):
        """
        Update wager by input amount.
        """
        if not text.isdigit():
            self._wager_msg.set_text("Enter a number!")
        elif int(text) > MAXBET:
            self._wager_msg.set_text("Max bet is 1000!")
        elif int(text) > self._game.get_money():
            self._wager_msg.set_text("Not enough funds!")
        else:
            self._game.set_wager(int(text))
            self._wager_msg.set_text("")
            
    def maxbet(self):
        """
        Update wager to max bet.
        """
        if self._game.is_penniless():
            self._wager_msg.set_text("You have no funds!")
        else:
            self._game.max_wager()
            self._wager_msg.set_text("MAX BET!")
            
    def deal(self):
        """
        Deal cards to each player.
        """
        self._game.deal()
            
    def hit(self):
        """
        Player hits.
        """
        self._game.hit()
        
    def stand(self):
        """
        Player stands. Dealer draws until 17 or bust.
        """
        self._game.stand()
        
    def reset(self):
        """
        Game is reset.
        """
        self._game.reset()
        
    def draw(self, canvas):
        """
        Draw handler.
        """
        money = self._game.get_money()
        wager = self._game.get_wager()
        status = self._game.get_status()
        self._message = STATUSMSG[status]
        
        # Draw the title in the top center of the canvas.
        titlewid = self._frame.get_canvas_textwidth("Blackjack", 50)
        canvas.draw_circle([CANVASWIDTH/2, -60], 600, 6, "white", "green")
        canvas.draw_circle([CANVASWIDTH/2, -130], 400, 6, "white", "green")
        canvas.draw_text("Blackjack", [CANVASWIDTH/2 - titlewid/2, 50], 50, "white")
        
        # Draw the dealer and player labels and cards.
        dealerwid = self._frame.get_canvas_textwidth("Dealer", 30)
        canvas.draw_text("Dealer", [CANVASWIDTH/2 - dealerwid/2, 260], 30, "white")
        num_dealer = self._game._dealer.num_cards() - 1
        self._game._dealer.draw(canvas, [CANVASWIDTH/2 - CARD_SIZE[0]/2 - 15*num_dealer,
                                164 - CARD_SIZE[1]/2])
        playerwid = self._frame.get_canvas_textwidth("Player", 30)
        canvas.draw_text("Player", [CANVASWIDTH/2 - playerwid/2, CANVASHEIGHT-28], 
                         30, "white")
        num_player = self._game._player.num_cards() - 1
        self._game._player.draw(canvas, [CANVASWIDTH/2 - CARD_SIZE[0]/2 - 15*num_player,
                                424 - CARD_SIZE[1]/2])
        
        # Draw the outcome.
        outwid = self._frame.get_canvas_textwidth(self._message, 34)
        canvas.draw_text(self._message, [CANVASWIDTH/2 - outwid/2, 334], 34,
                         STATUSCOLOR[self._game.get_status()])
        
        # Draw chips, bet value, and table features.
        chipswid = self._frame.get_canvas_textwidth("Chips", 34)
        canvas.draw_text("Chips: " + str(money), [20, CANVASHEIGHT - 10], 34, "yellow")
        
        pile = money
        if status == BETTING:
            pile = money if (money - wager) < 0 else money - wager
        stacktypes = str(pile)[::-1]
        for stack in range(len(stacktypes)):
            for chip in range(int(stacktypes[stack])):
                canvas.draw_circle([234 - 34*stack, 470 - 4*chip - 2*stack], 18, 2, 
                                   "black", STACKCOLOR[stack])
        
        if status == BETTING or status == INPLAY:
            wagertypes = str(self._game.get_wager())[::-1]
            for stack in range(len(wagertypes)):
                for chip in range(int(wagertypes[stack])):
                    canvas.draw_circle([188 - 28*stack, 280 - 4*chip - 2*stack], 16, 2, 
                                       "black", STACKCOLOR[stack])
        
        betwid = self._frame.get_canvas_textwidth(str(self._game.get_wager()), 34)
        canvas.draw_circle([62, 68], 52, 6, "white", "green")
        canvas.draw_text("BET", [34, 60], 30, "white")
        canvas.draw_text(str(self._game.get_wager()), [60 - betwid/2, 92], 34, "yellow")
        
        # Draw hole card back.
        if self._game.get_status() == INPLAY:
            canvas.draw_line([CANVASWIDTH/2 - 35, 118], [CANVASWIDTH/2 - 35, 210], 
                             30, "white")
            canvas.draw_image(card_back, CARD_BACK_CENTER, [26, CARD_BACK_SIZE[1]], 
                              [CANVASWIDTH/2 - 34, 164], [26, CARD_BACK_SIZE[1]])
                              
        # Draw deck.
        for card in range(len(self._game._deck._cards)):
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, 
                              [790, 56 + card*4], CARD_BACK_SIZE)
                              
        # Draw chip values.
        for stack in range(len(STACKCOLOR)):
            value = "10e" + str(stack)
            canvas.draw_circle([650 + stack*30, 530], 14, 2, "black", STACKCOLOR[stack])
            canvas.draw_text(value, [634 + stack*30, 514], 14, "black")
            
        # Draw max bet.
        canvas.draw_circle([770, 430], 52, 6, "white", "green")
        canvas.draw_text("MAX", [742, 410], 24, "white")
        canvas.draw_text("BET", [748, 430], 24, "white")
        maxwid = self._frame.get_canvas_textwidth(str(MAXBET), 26)
        canvas.draw_text(str(MAXBET), [CANVASWIDTH - maxwid/2 - 80, 458], 26, "white")
                            

BlackjackGUI(BlackjackGame())

# Below is the final version submitted to Coursera. After a lot of headaches, I
# was able to split up the game logic and GUI. The biggest challenge was determining
# what to put into each class regarding game messages and status checks. I opted
# to store all messages and colors in dictionaries and tie them to the game statuses.
# These are referenced by the GUI draw method. The control panel messages regarding
# betting are the only messages directly changed by the GUI class. Otherwise, the GUI
# references the status message using STATUSMSG[self._game.get_status()]. 
# The control panel messages may be a little weak and unnecessary.

# One of my biggest concerns is referencing the dealer and player (instances of 
# the Hand class) draw methods using self._game._player.draw(canvas, pos). This
# is a directly reference to the field and ignores the purpose of encapsulation. 
# A better method may be to implement get_player() and get_dealer() methods in
# the BlackjackGame class and call those using self._game.get_player().draw(). 

# The card back was drawn on top of the dealer's hole card by accessing only 26
# pixels of it from the left border rightward and finding the best destination
# on the canvas where it covered the hole. Unfortunately, the card back is not 
# completely opaque, so a thick white square (line) was drawn underneath it to
# provide a solid white background. Since the hole card is exposed just before
# the dealer begins to add cards to his hand, finding a moving pos was not
# necessary, as its location would be static throughout every game.

# Some variables ran away from me and I had difficulty using them in conditionals
# and updating them at the appropriate places. For example, the player_turn var
# in the game class was used to indicate that while the game was INPLAY, it is
# the player's turn and not the dealer's. While its the player's turn, he can not
# increase his wager. When it's not his turn, he can't use the hit or stand buttons.
# This may be overused in a small handful of places, but I can assure you (and myself)
# that every addition led to a change in the functionality (for the better).

# The game statuses began with only five and blossomed to twice that. These were
# necessary as distinct messages were tied to each status. A loss is not a loss in
# either case of a player busting or a dealer's score being lower than the player's
# score. Resultantly, the BETTING and OVERBET statuses were needed so that the
# messages could display when players attempted to bet or overbet, respectively.

# With this scaffolding, it would be simple to extend functionality to include
# double downs, splitting, insurance, and decks not shuffling after every round.
# Changes made from this point on will be to the code below. The url of the original
# submission to Coursera is mentioned at the top of this section.

# Originalish version: http://www.codeskulptor.org/#user40_3cQ9HN5KU8tGrqf_1.py
    
##=================================================================

"""
Rice University / Coursera: Intro to Interactive Programming in Python (Part 2)
Week 2: Project 6
Blackjack

For an alternate version outside of the context of this project, visit the link
below. Realistic rules implemented, including doubles and splits.

http://www.codeskulptor.org/#user40_5x87VG1m2b_11.py
"""

import math
import random
import simplegui

# Global variables. -----------------------------------------------------------#

# GUI frame size.
CANVASWIDTH = 850
CANVASHEIGHT = 620
CONTROLWIDTH = 150
    
# Game init betting.
INITIAL_MONEY = 1000
INITIAL_WAGER = 10
MAXBET = 10000
MINBET = 1

# Card src images.
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
CARD_URL = "http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png"
CARD_IMAGES = simplegui.load_image(CARD_URL)
CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
CARD_BACK_URL = "http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png"
CARD_BACK = simplegui.load_image(CARD_BACK_URL) 

# Card properties.
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = dict(zip(RANKS, range(1, 11)+[10]*3))

# Game statuses.
BETTING = 0
INPLAY = 1
PLAYERWIN = 2
DEALERWIN = 3
PUSH = 4
PLAYERBUST = 5
DEALERBUST = 6
BLACKJACK = 7
GAMEOVER = 8
HOUSEBROKE = 9
SPLIT1 = 10
SPLIT2 = 11
SPLIT1BUST = 12
SPLITBUSTBOTH = 13

# Game status messages.
STATUSMSG = {
    BETTING: "Click DEAL to begin.",
    INPLAY: "Click HIT or STAND, or DEAL to forfeit round.",
    PLAYERWIN: "Player wins! Change bet or DEAL.",
    DEALERWIN: "Dealer wins! Change bet or DEAL.",
    PUSH: "Push! Change bet or DEAL.",
    PLAYERBUST: "Player busted! Change bet or DEAL.",
    DEALERBUST: "Dealer busted! Change bet or DEAL.",
    BLACKJACK: "You have Blackjack! Change bet or DEAL.",
    GAMEOVER: "You've lost everything! Click RESET.",
    HOUSEBROKE: "You broke the house! Go home.",
    SPLIT1: "First hand: HIT or STAND",
    SPLIT2: "Second hand: HIT or STAND?",
    SPLIT1BUST: "First hand busted! Second: HIT or STAND?",
    SPLITBUSTBOTH: "Both hands busted! Change bet or DEAL."
    }
    
# Game status message colors.
STATUSCOLOR = {
    BETTING: "#00008b",
    INPLAY: "yellow",
    PLAYERWIN: "#00ff00",
    DEALERWIN: "black",
    PUSH: "cyan",
    PLAYERBUST: "black",
    DEALERBUST: "#00ff00",
    BLACKJACK: "white",
    GAMEOVER: "#00008b",
    HOUSEBROKE: "white",
    SPLIT1: "#f2e5ff",
    SPLIT2: "#cc99ff",
    SPLIT1BUST: "black",
    SPLITBUSTBOTH: "black"
    }
    
# Game wagering.
BLANK = 0
NOTENOUGH = 1
MINIMUMIS = 2
MAXIMUMIS = 3
FINISHRESET = 4

# Game wagering messages.
BETMSG = {
    BLANK: "",
    NOTENOUGH: "Not enough funds, lower bet.",
    MINIMUMIS: "Minimum bet is " + str(MINBET) + ".",
    MAXIMUMIS: "Maximum bet is " + str(MAXBET) + ".",
    FINISHRESET: "Finish round or reset game."
    }

# Chip value colors.
STACKCOLOR = {
    0: "white",
    1: "red",
    2: "yellow",
    3: "aqua",
    4: "pink",
    5: "purple",
    6: "black"
    }

# Card, Hand, and Deck classes ------------------------------------------------#

class Card:
    """
    Class to store a playing card.
    """
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self._suit = suit
            self._rank = rank
        else:
            self._suit = None
            self._rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        """
        Return string representation of the card.
        """
        return self._suit + self._rank

    def get_suit(self):
        """
        Return the suit of the card.
        """
        return self._suit

    def get_rank(self):
        """
        Return the rank of the card.
        """
        return self._rank

    def draw(self, canvas, pos):
        """
        Draw method for the card.
        """
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self._rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self._suit))
        canvas.draw_image(CARD_IMAGES, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], 
                          pos[1] + CARD_CENTER[1]], CARD_SIZE)


class Hand:
    """
    Class to store a hand of cards.
    """
    def __init__(self):
        self._hand = []

    def __str__(self):
        """
        Return string representation of the hand.
        """
        s = ""
        for card in self._hand:
            s = s + str(card) + " "
        return s

    def get_value(self):
        """
        Return the value of the hand.
        """
        ranks = [card.get_rank() for card in self._hand]
        value = sum(VALUES[card] for card in ranks)
        if "A" in ranks and value <= 11:
            value += 10
        return value
        
    def num_cards(self):
        """
        Return the number of cards in a hand.
        """
        return len(self._hand)
        
    def add_card(self, card):
        """
        Add a card to the hand.
        """
        self._hand.append(card)
   
    def draw(self, canvas, pos):
        """
        Draw method for the hand.
        """
        for card in self._hand:
            card.draw(canvas, pos)
            pos[0] = pos[0] + 30

            
class Deck:
    """
    Class to store a deck of cards.
    """
    def __init__(self):
        self._cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.shuffle()
        
    def __str__(self):
        """
        Returns string representation of the deck.
        """
        s = ""
        for card in self._cards:
            s = s + str(card) + " "
        return s
    
    def num_cards(self):
        """
        Returns the number of cards in the deck.
        """
        return len(self._cards)

    def shuffle(self):
        """
        Shuffles deck.
        """
        random.shuffle(self._cards)

    def deal_card(self):
        """
        Deals next card from the deck. If all cards have been dealt,
        a new deck is created and shuffled, and its first card returned.
        """
        if self.num_cards() > 0:
            return self._cards.pop(0)
        else:
            self._cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
            self.shuffle()
            return self._cards.pop(0)


# Blackjack game class --------------------------------------------------------#

class BlackjackGame:
    """
    Class to play a game of Blackjack.
    """
    def __init__(self):
        self._money = INITIAL_MONEY
        self._wager = INITIAL_WAGER
        self._pot = 0
        self._status = BETTING
        self._betmsg = BLANK
        self._deck = Deck()
        self._player = Hand()
        self._dealer = Hand()
        
    def get_money(self):
        """
        Return player money.
        """
        return self._money
        
    def get_wager(self):
        """
        Return player wager.
        """
        return self._wager
    
    def get_pot(self):
        """
        Return pot value.
        """
        return self._pot
        
    def get_status(self):
        """
        Return round status.
        """
        return self._status
        
    def get_betmsg(self):
        """
        Return bet message for bet feedback.
        """
        return BETMSG[self._betmsg]
        
    def get_deck_num_cards(self):
        """
        Return the number of cards left in the deck.
        """
        return self._deck.num_cards()
    
    def get_hand_num_cards(self):
        """
        Return the number of cards in a hand.
        """
        return self._player.num_cards()
        
    def get_player_value(self):
        """
        Return player hand value.
        """
        return self._player.get_value()
    
    def get_dealer_value(self):
        """
        Return dealer hand value.
        """
        return self._dealer.get_value()

    def check_gameover(self):
        """
        Check if the game is over and reset status accordingly.
        """
        if self._money == 0:
            self._status = GAMEOVER
        elif self._money > 1000000:
            self._status = HOUSEBROKE       
        
    def increase_wager(self, value):
        """
        Increase wager by specified amount.
        """
        if self._status != INPLAY and self._status != GAMEOVER and \
        self._status != HOUSEBROKE:
            self._status = BETTING
            if self._wager + value <= self._money:
                if self._wager + value <= MAXBET:
                    self._wager += value
                else:
                    self._betmsg = MAXIMUMIS
            else:
                self._betmsg = NOTENOUGH
        else:
            self._betmsg = FINISHRESET
            
    def decrease_wager(self, value):
        """
        Decrease wager by specified amount.
        """
        if self._status != INPLAY and self._status != GAMEOVER and \
        self._status != HOUSEBROKE:
            self._status = BETTING
            if self._wager - value >= 1:
                self._wager -= value
            else:
                self._betmsg = MINIMUMIS
        else:
            self._betmsg = FINISHRESET
                
    def max_wager(self):
        """
        Bet all money.
        """
        if self._status != INPLAY and self._status != GAMEOVER and \
        self._status != HOUSEBROKE:
            self._status = BETTING
            if self._money < MAXBET:
                self._wager = self._money
            elif self._money >= MAXBET:
                self._wager = MAXBET
        else:
            self._betmsg = FINISHRESET

    def deal(self):
        """
        Deal a round.
        """
        if self._status != GAMEOVER and self._status != HOUSEBROKE:
            if self._money - self._wager < 0:
                self._betmsg = NOTENOUGH
            else:
                self._status = INPLAY
                self._money -= self._wager
                self._pot = self._wager
                self._deck = Deck()
                self._player = Hand()
                self._dealer = Hand()
                self._player.add_card(self._deck.deal_card())
                self._dealer.add_card(self._deck.deal_card())
                self._player.add_card(self._deck.deal_card())
                self._dealer.add_card(self._deck.deal_card())
                
                if self._player.get_value() == 21:
                    if self._dealer.get_value() == 21:
                        self._status = PUSH
                        self._money += self._wager
                        self._pot = 0
                    else:
                        self._status = BLACKJACK
                        self._money += int(float(5)/2 * self._wager)
                        self._pot = 0
                elif self._dealer.get_value() == 21:
                    self._status = DEALERWIN
                    self._pot = 0
                    self.check_gameover()
        
    def hit(self):
        """
        Player hits, add a card to player hand.
        """
        if self._status == INPLAY:
            self._player.add_card(self._deck.deal_card())
            if self._player.get_value() > 21:
                self._status = PLAYERBUST
                self._pot = 0
                self.check_gameover()
                                            
    def stand(self):
        """
        Player stands, dealer hits until 17 or bust.
        """
        if self._status == INPLAY:
        
            while self._dealer.get_value() < 17:
                self._dealer.add_card(self._deck.deal_card())
            
            player = self._player.get_value()
            dealer = self._dealer.get_value()
        
            if dealer > 21:
                self._status = DEALERBUST
                self._money += 2 * self._wager
            elif player > dealer:
                self._status = PLAYERWIN
                self._money += 2 * self._wager
            elif player == dealer:
                self._status = PUSH
                self._money += self._wager
            else:
                self._status = DEALERWIN

            self._doubledown = False
            self._pot = 0
            self.check_gameover()

    def clear_betmsg(self):
        """
        Set bet message back to an empty string.
        """
        self._betmsg = BLANK

    def reset(self):
        """
        Reset all game fields.
        """
        self._money = INITIAL_MONEY
        self._wager = INITIAL_WAGER
        self._pot = 0
        self._status = BETTING
        self._betmsg = BLANK
        self._deck = Deck()
        self._player = Hand()
        self._dealer = Hand()
        
    def draw_player(self, canvas, pos):
        """
        Draw player.
        """
        self._player.draw(canvas, pos)
        
    def draw_dealer(self, canvas, pos):
        """
        Draw dealer.
        """
        self._dealer.draw(canvas, pos)
        
        
# Blackjack GUI class ---------------------------------------------------------#
        
class BlackjackGUI:
    """
    Class to run the GUI for a game of Blackack.
    """
    def __init__(self, game):
        self._game = game
        self._increment = 1
        
        self._frame = simplegui.create_frame("Blackjack", CANVASWIDTH, CANVASHEIGHT,
                                             CONTROLWIDTH)
        self._frame.set_canvas_background("green")
        self._frame.add_label("Use the buttons below to play.")
        self._frame.add_label("")
        self._frame.add_label("Use the BET MAX and arrow buttons on the canvas to change bet.")
        self._frame.add_label("Use the multi-colored buttons to change bet increments.")
        self._frame.add_label("")
        self._frame.add_label("Use the RESET button on the canvas to start over.")
        self._frame.add_label("")
        self._frame.add_button("HIT", self.hit, CONTROLWIDTH)
        self._frame.add_label("")
        self._frame.add_button("STAND", self.stand, CONTROLWIDTH)
        self._frame.add_label("")
        self._frame.add_button("DEAL", self.deal, CONTROLWIDTH)
        self._frame.set_mouseclick_handler(self.click)
        self._frame.set_draw_handler(self.draw)
        self._game.deal()
        self._frame.start()
        
    def hit(self):
        """
        Hit.
        """
        self._game.clear_betmsg()
        self._game.hit()
        
    def stand(self):
        """
        Stand.
        """
        self._game.clear_betmsg()
        self._game.stand()
        
    def deal(self):
        """
        Deal.
        """
        self._game.clear_betmsg()
        self._game.deal()
        
    def dist(self, p, q):
        """
        Compute Euclidean distance between points.
        """
        return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)
        
    def click(self, pos):
        """
        Mouse click handler.
        """
        x = pos[0]
        y = pos[1]
        halfwid = CANVASWIDTH/2
        height = CANVASHEIGHT
        
        self._game.clear_betmsg()

        if self.dist(pos, (790, 560)) <= 44:
            self._game.reset()
            self._increment = 1
            
        elif self.dist(pos, (130,50)) <= 16:
            self.increase_by_increment()
            
        elif self.dist(pos, (130, 90)) <= 16:
            self.decrease_by_increment()
            
        elif self.dist(pos, (170, 114)) <= 14:
            self._increment = 10**0
            
        elif self.dist(pos, (170, 84)) <= 14:
            self._increment = 10**1
            
        elif self.dist(pos, (170, 54)) <= 14:
            self._increment = 10**2
            
        elif self.dist(pos, (170, 24)) <= 14:
            self._increment = 10**3
            
        elif self.dist(pos, (60, 160)) <= 40:
            self.maxbet()
                    
    def maxbet(self):
        """
        Update wager to max bet.
        """
        self._game.max_wager()
            
    def increase_by_increment(self):
        """
        Increase wager by increment.
        """
        self._game.increase_wager(self._increment)
        
    def decrease_by_increment(self):
        """
        Decrease wager by increment.
        """
        self._game.decrease_wager(self._increment)
        
    def draw(self, canvas):
        """
        Draw handler.
        """
        money = self._game.get_money()
        wager = self._game.get_wager()
        pot = self._game.get_pot()
        status = self._game.get_status()
        message = STATUSMSG[status]
        message_color = STATUSCOLOR[status]
        
        # Draw the title in the top center of the canvas and white circles on table.
        titlewid = self._frame.get_canvas_textwidth("Blackjack", 50)
        canvas.draw_circle([CANVASWIDTH/2, -60], 600, 6, "white", "green")
        canvas.draw_circle([CANVASWIDTH/2, -130], 400, 6, "white", "green")
        canvas.draw_text("Blackjack", [CANVASWIDTH/2 - titlewid/2, 50], 50, "white")
        altmsg = "For a better, alternate version, see the project docstring."
        altwid = self._frame.get_canvas_textwidth(altmsg, 20)
        canvas.draw_text(altmsg, [CANVASWIDTH/2 - altwid/2, CANVASHEIGHT - 20], 20, "white")
        
        # Draw the dealer and player labels and cards.
        
        dealerwid = self._frame.get_canvas_textwidth("Dealer", 30)
        canvas.draw_text("Dealer", [CANVASWIDTH/2 - dealerwid/2, 260], 30, "white")
        num_dealer = self._game._dealer.num_cards()
        self._game.draw_dealer(canvas, [CANVASWIDTH/2 - CARD_SIZE[0]/2 - 15*(num_dealer-1),
                               164 - CARD_SIZE[1]/2])
        
        if status != INPLAY and status != BETTING:
            dwid = self._frame.get_canvas_textwidth(str(self._game.get_dealer_value()), 30)
            canvas.draw_text(str(self._game.get_dealer_value()), [CANVASWIDTH/2 - dwid/2, 
                             236], 30, "white")
                                
        playerwid = self._frame.get_canvas_textwidth("Player", 30)
        canvas.draw_text("Player", [CANVASWIDTH/2 - playerwid/2, CANVASHEIGHT-94], 
                         30, "white")
        
        num_player = self._game.get_hand_num_cards()
        self._game.draw_player(canvas,[CANVASWIDTH/2 - CARD_SIZE[0]/2 - 15*(num_player-1),
                               424 - CARD_SIZE[1]/2])
        pwid = self._frame.get_canvas_textwidth(str(self._game.get_player_value()), 30)
        if status != BETTING:
            canvas.draw_text(str(self._game.get_player_value()), [CANVASWIDTH/2 - pwid/2, 
                             CANVASHEIGHT - 120], 30, "white")
        
        # Draw the messages.
        msgwid = self._frame.get_canvas_textwidth(message, 34)
        canvas.draw_text(message, [CANVASWIDTH/2 - msgwid/2, 334], 34, message_color)
        canvas.draw_text(self._game.get_betmsg(), [54, 370], 26, "pink")
        
        # Draw funds, chip stack, wagered chips, and bet text.
        
        chipswid = self._frame.get_canvas_textwidth("Chips", 34)
        canvas.draw_text("Chips:", [12, CANVASHEIGHT - 20], 34, "white")
        canvas.draw_text(str(money), [108, CANVASHEIGHT - 20], 34, "yellow")
        
        if status == BETTING:
            pile = money - wager
        else:
            pile = money
        stacktypes = str(pile)[::-1]
        for stack in range(len(stacktypes)):
            for chip in range(int(stacktypes[stack])):
                canvas.draw_circle([234 - 34*stack, 470 - 4*chip - 2*stack], 18, 2, 
                                   "black", STACKCOLOR[stack])
          
        bet = wager if status == BETTING else pot
        wagertypes = str(bet)[::-1]
        for stack in range(len(wagertypes)):
            for chip in range(int(wagertypes[stack])):
                canvas.draw_circle([188 - 28*stack, 280 - 4*chip - 2*stack], 16, 2, 
                                   "black", STACKCOLOR[stack])
        canvas.draw_polygon([[54, 218],[210, 218],[210, 300],[54, 300]], 4, "white")
        
        betwid = self._frame.get_canvas_textwidth(str(self._game.get_wager()), 34)
        canvas.draw_circle([62, 68], 52, 6, "white", "green")
        canvas.draw_text("BET", [34, 60], 30, "white")
        canvas.draw_text(str(self._game.get_wager()), [60 - betwid/2, 92], 34, "yellow")
        
        # Draw chip values.
        canvas.draw_text("CHIP VALUES", [74, 506], 12, "white")
        for stack in range(len(STACKCOLOR)):
            value = "10e" + str(stack)
            canvas.draw_circle([204 - stack*30, 544], 14, 2, "black", STACKCOLOR[stack])
            canvas.draw_text(value, [190 - stack*30, 524], 14, "white")
        
        # Draw hole card back.
        if status == INPLAY:
            canvas.draw_line([CANVASWIDTH/2 - 35, 118], [CANVASWIDTH/2 - 35, 210], 
                             30, "white")
            canvas.draw_image(CARD_BACK, CARD_BACK_CENTER, [26, CARD_BACK_SIZE[1]], 
                              [CANVASWIDTH/2 - 34, 164], [26, CARD_BACK_SIZE[1]])
                              
        # Draw deck.
        for card in range(self._game.get_deck_num_cards()):
            canvas.draw_image(CARD_BACK, CARD_BACK_CENTER, CARD_BACK_SIZE, 
                              [790, 56 + card*4], CARD_BACK_SIZE)
            
        # Draw max bet.
        canvas.draw_circle([770, 430], 52, 6, "white", "green")
        canvas.draw_text("MAX", [742, 410], 24, "white")
        canvas.draw_text("BET", [748, 430], 24, "white")
        maxwid = self._frame.get_canvas_textwidth(str(MAXBET), 26)
        canvas.draw_text(str(MAXBET), [CANVASWIDTH - maxwid/2 - 80, 458], 24, "white")
        
        # Draw hit, stand, double down, split, deal, reset, and bet max buttons.

        canvas.draw_circle([790, 560], 44, 2, "purple", "red")
        canvas.draw_text("RESET", [751, 569], 24, "black", 'sans-serif')
        
        # Draw increment buttons and label.
        
        canvas.draw_circle([134, 50], 16, 2, "purple", "orange")
        canvas.draw_circle([134, 90], 16, 2, "purple", "orange")
        canvas.draw_polygon([[124, 84], [144, 84], [134, 100]], 1, "black", "red")
        canvas.draw_polygon([[124, 56], [144, 56], [134, 38]], 1, "black", "#7FFF00")
        canvas.draw_circle([62, 168], 40, 2, "purple", "orange")
        canvas.draw_text("BET", [36, 164], 28, "black")
        canvas.draw_text("MAX", [30, 188], 28, "black")
        
        for idx in range(4):
            outline_color = "purple" if self._increment != 10**idx else "orange"
            dot_color = STACKCOLOR[idx] if self._increment != 10**idx else "green"
            canvas.draw_circle([170, 114 - idx*30], 14, 2, outline_color, STACKCOLOR[idx])
            canvas.draw_circle([170, 114 - idx*30], 4, 3, dot_color, dot_color)
            canvas.draw_text("10e" + str(idx), [188, 122 - idx*30], 16, "white")
            
        word = "INCREMENTS"
        for letter in range(len(word)):
            letwid = self._frame.get_canvas_textwidth(word[letter], 12)
            canvas.draw_text(word[letter], [224 + 5 - letwid/2, 20 + letter*12], 12, "white")
        

# Call to run game.
BlackjackGUI(BlackjackGame())

##=================================================================

"""
Blackjack
Real World Rules
"""

import math
import random
import simplegui

# Global variables. -----------------------------------------------------------#

# GUI frame size.
CANVASWIDTH = 850
CANVASHEIGHT = 620
CONTROLWIDTH = 150
    
# Game init betting.
INITIAL_MONEY = 1000
INITIAL_WAGER = 10
MAXBET = 10000
MINBET = 1

# Card src images.
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
CARD_URL = "http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png"
CARD_IMAGES = simplegui.load_image(CARD_URL)
CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
CARD_BACK_URL = "http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png"
CARD_BACK = simplegui.load_image(CARD_BACK_URL) 

# Card properties.
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = dict(zip(RANKS, range(1, 11)+[10]*3))

# Game statuses.
BETTING = 0
INPLAY = 1
PLAYERWIN = 2
DEALERWIN = 3
PUSH = 4
PLAYERBUST = 5
DEALERBUST = 6
BLACKJACK = 7
GAMEOVER = 8
HOUSEBROKE = 9
SPLIT1 = 10
SPLIT2 = 11
SPLIT1BUST = 12
SPLITBUSTBOTH = 13

# Game status messages.
STATUSMSG = {
    BETTING: "Click DEAL to begin.",
    INPLAY: "Click HIT or STAND, or DEAL to forfeit round.",
    PLAYERWIN: "Player wins! Change bet or DEAL.",
    DEALERWIN: "Dealer wins! Change bet or DEAL.",
    PUSH: "Push! Change bet or DEAL.",
    PLAYERBUST: "Player busted! Change bet or DEAL.",
    DEALERBUST: "Dealer busted! Change bet or DEAL.",
    BLACKJACK: "You have Blackjack! Change bet or DEAL.",
    GAMEOVER: "You've lost everything! Click RESET.",
    HOUSEBROKE: "You broke the house! Go home.",
    SPLIT1: "First hand: HIT or STAND",
    SPLIT2: "Second hand: HIT or STAND?",
    SPLIT1BUST: "First hand busted! Second: HIT or STAND?",
    SPLITBUSTBOTH: "Both hands busted! Change bet or DEAL."
    }
    
# Game status message colors.
STATUSCOLOR = {
    BETTING: "#00008b",
    INPLAY: "yellow",
    PLAYERWIN: "#00ff00",
    DEALERWIN: "black",
    PUSH: "cyan",
    PLAYERBUST: "black",
    DEALERBUST: "#00ff00",
    BLACKJACK: "white",
    GAMEOVER: "#00008b",
    HOUSEBROKE: "white",
    SPLIT1: "#f2e5ff",
    SPLIT2: "#cc99ff",
    SPLIT1BUST: "black",
    SPLITBUSTBOTH: "black"
    }
    
# Game wagering.
BLANK = 0
NOTENOUGH = 1
MINIMUMIS = 2
MAXIMUMIS = 3
FINISHRESET = 4

# Game wagering messages.
BETMSG = {
    BLANK: "",
    NOTENOUGH: "Not enough funds, lower bet.",
    MINIMUMIS: "Minimum bet is " + str(MINBET) + ".",
    MAXIMUMIS: "Maximum bet is " + str(MAXBET) + ".",
    FINISHRESET: "Finish round or reset game."
    }

# Chip value colors.
STACKCOLOR = {
    0: "white",
    1: "red",
    2: "yellow",
    3: "aqua",
    4: "pink",
    5: "purple",
    6: "black"
    }

# Card, Hand, and Deck classes ------------------------------------------------#

class Card:
    """
    Class to store a playing card.
    """
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self._suit = suit
            self._rank = rank
        else:
            self._suit = None
            self._rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        """
        Return string representation of the card.
        """
        return self._suit + self._rank

    def get_suit(self):
        """
        Return the suit of the card.
        """
        return self._suit

    def get_rank(self):
        """
        Return the rank of the card.
        """
        return self._rank

    def draw(self, canvas, pos):
        """
        Draw method for the card.
        """
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self._rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self._suit))
        canvas.draw_image(CARD_IMAGES, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], 
                          pos[1] + CARD_CENTER[1]], CARD_SIZE)


class Hand:
    """
    Class to store a hand of cards.
    """
    def __init__(self):
        self._hand = []

    def __str__(self):
        """
        Return string representation of the hand.
        """
        s = ""
        for card in self._hand:
            s = s + str(card) + " "
        return s

    def get_value(self):
        """
        Return the value of the hand.
        """
        ranks = [card.get_rank() for card in self._hand]
        value = sum(VALUES[card] for card in ranks)
        if "A" in ranks and value <= 11:
            value += 10
        return value
        
    def num_cards(self):
        """
        Return the number of cards in a hand.
        """
        return len(self._hand)
    
    def get_card_value(self, index):
        """
        Return the rank of the card at the specified index in the hand.
        """
        return VALUES[self._hand[index].get_rank()]
        
    def add_card(self, card):
        """
        Add a card to the hand.
        """
        self._hand.append(card)
    
    def pull_card(self):
        """
        Pull the first card from the hand.
        """
        return self._hand.pop(0)
   
    def draw(self, canvas, pos):
        """
        Draw method for the hand.
        """
        for card in self._hand:
            card.draw(canvas, pos)
            pos[0] = pos[0] + 30

            
class Deck:
    """
    Class to store a deck of cards.
    """
    def __init__(self):
        self._cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.shuffle()
        
    def __str__(self):
        """
        Returns string representation of the deck.
        """
        s = ""
        for card in self._cards:
            s = s + str(card) + " "
        return s
    
    def num_cards(self):
        """
        Returns the number of cards in the deck.
        """
        return len(self._cards)

    def shuffle(self):
        """
        Shuffles deck.
        """
        random.shuffle(self._cards)

    def deal_card(self):
        """
        Deals next card from the deck. If all cards have been dealt,
        a new deck is created and shuffled, and its first card returned.
        """
        if self.num_cards() > 0:
            return self._cards.pop(0)
        else:
            self._cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
            self.shuffle()
            return self._cards.pop(0)


# Blackjack game class --------------------------------------------------------#

class BlackjackGame:
    """
    Class to play a game of Blackjack.
    """
    def __init__(self):
        self._money = INITIAL_MONEY
        self._wager = INITIAL_WAGER
        self._pot = 0
        self._status = BETTING
        self._betmsg = BLANK
        self._deck = Deck()
        self._player = Hand()
        self._dealer = Hand()
        self._doubledown = False
        self._splitpair = False
        self._split_hands = []
        self._splitdouble1 = False
        self._splitdouble2 = False
        
    def get_money(self):
        """
        Return player money.
        """
        return self._money
        
    def get_wager(self):
        """
        Return player wager.
        """
        return self._wager
    
    def get_pot(self):
        """
        Return pot value.
        """
        return self._pot
        
    def get_status(self):
        """
        Return round status.
        """
        return self._status
        
    def get_betmsg(self):
        """
        Return bet message for bet feedback.
        """
        return BETMSG[self._betmsg]
        
    def get_deck_num_cards(self):
        """
        Return the number of cards left in the deck.
        """
        return self._deck.num_cards()
    
    def get_hand_num_cards(self):
        """
        Return the number of cards in specified hand.
        """
        if not self._splitpair:
            return self._player.num_cards()
        else:
            return self._split_hands[0].num_cards()
        
    def get_player_value(self):
        """
        Return player hand value.
        """
        return self._player.get_value()
    
    def get_dealer_value(self):
        """
        Return dealer hand value.
        """
        return self._dealer.get_value()
    
    def get_split1_value(self):
        """
        Return split hand 1 value.
        """
        return self._split_hands[0].get_value()
    
    def get_split2_value(self):
        """
        Return split hand 2 value.
        """
        return self._split_hands[1].get_value()
                
    def is_split(self):
        """
        Return True if player split a pair, False if not.
        """
        return self._splitpair

    def check_gameover(self):
        """
        Check if the game is over and reset status accordingly.
        """
        if self._money == 0:
            self._status = GAMEOVER
        elif self._money > 1000000:
            self._status = HOUSEBROKE       
        
    def increase_wager(self, value):
        """
        Increase wager by specified amount.
        """
        if self._status != INPLAY and self._status != GAMEOVER and \
        self._status != HOUSEBROKE:
            self._status = BETTING
            if self._wager + value <= self._money:
                if self._wager + value <= MAXBET:
                    self._wager += value
                else:
                    self._betmsg = MAXIMUMIS
            else:
                self._betmsg = NOTENOUGH
        else:
            self._betmsg = FINISHRESET
            
    def decrease_wager(self, value):
        """
        Decrease wager by specified amount.
        """
        if self._status != INPLAY and self._status != GAMEOVER and \
        self._status != HOUSEBROKE:
            self._status = BETTING
            if self._wager - value >= 1:
                self._wager -= value
            else:
                self._betmsg = MINIMUMIS
        else:
            self._betmsg = FINISHRESET
                
    def max_wager(self):
        """
        Bet all money.
        """
        if self._status != INPLAY and self._status != GAMEOVER and \
        self._status != HOUSEBROKE:
            self._status = BETTING
            if self._money < MAXBET:
                self._wager = self._money
            elif self._money >= MAXBET:
                self._wager = MAXBET
        else:
            self._betmsg = FINISHRESET

    def deal(self):
        """
        Deal a round.
        """
        if self._status != GAMEOVER and self._status != HOUSEBROKE:
            if self._money - self._wager < 0:
                self._betmsg = NOTENOUGH
            else:
                self._status = INPLAY
                self._splitpair = False
                self._split_hands = []
                
                self._money -= self._wager
                self._pot = self._wager
                self._player = Hand()
                self._dealer = Hand()
                self._player.add_card(self._deck.deal_card())
                self._dealer.add_card(self._deck.deal_card())
                self._player.add_card(self._deck.deal_card())
                self._dealer.add_card(self._deck.deal_card())
                
                if self._player.get_value() == 21:
                    if self._dealer.get_value() == 21:
                        self._status = PUSH
                        self._money += self._wager
                        self._pot = 0
                    else:
                        self._status = BLACKJACK
                        self._money += int(float(5)/2 * self._wager)
                        self._pot = 0
                elif self._dealer.get_value() == 21:
                    self._status = DEALERWIN
                    self._pot = 0
                    self.check_gameover()
        
    def hit(self):
        """
        Player hits, add a card to player hand.
        """
        if self._status == INPLAY:
            self._player.add_card(self._deck.deal_card())
            if self._player.get_value() > 21:
                self._status = PLAYERBUST
                self._pot = 0
                self.check_gameover()
                
        elif self._status == SPLIT1:
            self._split_hands[0].add_card(self._deck.deal_card())
            if self._split_hands[0].get_value() > 21:
                self._status = SPLIT1BUST
                self._split_hands[1].add_card(self._deck.deal_card())
                
        elif self._status == SPLIT2 or self._status == SPLIT1BUST:
            self._split_hands[1].add_card(self._deck.deal_card())
            if self._split_hands[1].get_value() > 21:
                if self._split_hands[0].get_value() > 21:
                    self._status = SPLITBUSTBOTH
                    self._pot = 0
                    self.check_gameover()
                else:
                    self.stand()
                                            
    def stand(self):
        """
        Player stands, dealer hits until 17 or bust.
        """
        if self._status == INPLAY:
        
            while self._dealer.get_value() < 17:
                self._dealer.add_card(self._deck.deal_card())
            
            player = self._player.get_value()
            dealer = self._dealer.get_value()
        
            if dealer > 21:
                self._status = DEALERBUST
                self._money += 2 * self._wager if not self._doubledown else 4 * self._wager
            elif player > dealer:
                self._status = PLAYERWIN
                self._money += 2 * self._wager if not self._doubledown else 4 * self._wager
            elif player == dealer:
                self._status = PUSH
                self._money += self._wager if not self._doubledown else 2 * self._wager
            else:
                self._status = DEALERWIN

            self._doubledown = False
            self._pot = 0
            self.check_gameover()
            
        elif self._status == SPLIT1:
            self._status = SPLIT2
            self._split_hands[1].add_card(self._deck.deal_card())
            
        elif self._status == SPLIT2 or self._status == SPLIT1BUST:
            
            while self._dealer.get_value() < 17:
                self._dealer.add_card(self._deck.deal_card())
                
            hand1 = self._split_hands[0].get_value()
            hand2 = self._split_hands[1].get_value()
            dealer = self._dealer.get_value()
            result = [0,0]

            if dealer > 21:
                result[0] = 0 if hand1 > 21 else 2 if not self._splitdouble1 else 4
                result[1] = 0 if hand2 > 21 else 2 if not self._splitdouble2 else 4
            else:
                
                if hand1 == 21 and self._split_hands[0].num_cards() == 2:
                    result[0] = float(5)/2
                elif dealer < hand1 < 22:
                    result[0] = 2 if not self._splitdouble1 else 4
                elif hand1 == dealer:
                    result[0] = 1 if not self._splitdouble1 else 2
                else:
                    result[0] = 0
                
                if hand2 == 21 and self._split_hands[1].num_cards() == 2:
                    result[1] = float(5)/2
                elif dealer < hand2 < 22:
                    result[1] = 2 if not self._splitdouble2 else 4
                elif hand2 == dealer:
                    result[1] = 1 if not self._splitdouble2 else 2
                else:
                    result[1] = 0
                    
            winnings = int(result[0] * self._wager + result[1] * self._wager)
            if winnings > self._pot:
                self._status = PLAYERWIN
            elif winnings == self._pot:
                self._status = PUSH
            elif winnings < self._pot:
                self._status = DEALERWIN
            self._money += winnings

            self._splitdouble1 = False
            self._splitdouble2 = False
            self._pot = 0
            self.check_gameover()

    def double_down(self):
        """
        Player doubles down.
        """
        if self._money - self._wager >= 0:
        
            if self._status == INPLAY and self._player.num_cards() == 2:
                self._money -= self._wager
                self._pot += self._wager
                self._player.add_card(self._deck.deal_card())
                if self._player.get_value() > 21:
                    self._status = PLAYERBUST
                    self._pot = 0
                    self.check_gameover()
                else:
                    self._doubledown = True
                    self.stand()
                        
            elif self._status == SPLIT1 and self._split_hands[0].num_cards() == 2:
                self._money -= self._wager
                self._pot += self._wager
                self._split_hands[0].add_card(self._deck.deal_card())
                self._splitdouble1 = True
                self._status = SPLIT1BUST if self._split_hands[0].get_value() > 21 else SPLIT2
                self._split_hands[1].add_card(self._deck.deal_card())
            
            elif (self._status == SPLIT2 or self._status == SPLIT1BUST) and \
            self._split_hands[1].num_cards() == 2:
                self._money -= self._wager
                self._pot += self._wager
                self._split_hands[1].add_card(self._deck.deal_card())
                self._splitdouble2 = True
                if self._split_hands[1].get_value() > 21 and \
                self._split_hands[0].get_value() > 21:
                    self._status = SPLITBUSTBOTH
                    self._pot = 0
                    self.check_gameover()
                else:
                    self.stand()
                
    def split_pair(self):
        """
        Player splits pair.
        """
        if self._status == INPLAY and self._player.num_cards() == 2 and \
        self._money - self._wager >= 0 and not self._splitpair:
            if self._player.get_card_value(0) == self._player.get_card_value(1):
                self._status = SPLIT1
                self._splitpair = True
                self._money -= self._wager
                self._pot += self._wager
                
                hand1 = Hand()
                hand1.add_card(self._player.pull_card())
                hand1.add_card(self._deck.deal_card())
                self._split_hands.append(hand1)

                hand2 = Hand()
                hand2.add_card(self._player.pull_card())
                self._split_hands.append(hand2)
                
    def clear_betmsg(self):
        """
        Set bet message back to an empty string.
        """
        self._betmsg = BLANK

    def reset(self):
        """
        Reset all game fields.
        """
        self._money = INITIAL_MONEY
        self._wager = INITIAL_WAGER
        self._pot = 0
        self._status = BETTING
        self._betmsg = BLANK
        self._deck = Deck()
        self._player = Hand()
        self._dealer = Hand()
        self._doubledown = False
        self._splitpair = False
        self._split_hands = []
        self._splitdouble1 = False
        self._splitdouble2 = False
        
    def draw_player(self, canvas, pos):
        """
        Draw player.
        """
        self._player.draw(canvas, pos)
        
    def draw_dealer(self, canvas, pos):
        """
        Draw dealer.
        """
        self._dealer.draw(canvas, pos)
        
    def draw_split1(self, canvas, pos):
        """
        Draw split 1.
        """
        self._split_hands[0].draw(canvas, pos)
        
    def draw_split2(self, canvas, pos):
        """
        Draw split 2.
        """
        self._split_hands[1].draw(canvas, pos)
        
        
# Blackjack GUI class ---------------------------------------------------------#
        
class BlackjackGUI:
    """
    Class to run the GUI for a game of Blackack.
    """
    def __init__(self, game):
        self._game = game
        self._increment = 1
        
        self._frame = simplegui.create_frame("Blackjack", CANVASWIDTH, CANVASHEIGHT,
                                             CONTROLWIDTH)
        self._frame.set_canvas_background("green")
        self._frame.add_label("Use the buttons on the canvas to play.")
        self._frame.add_label("")
        self._frame.add_label("Use the BET MAX and arrow buttons on the canvas to change bet.")
        self._frame.add_label("Use the multi-colored buttons to change bet increments.")
        self._frame.add_label("")
        self._frame.add_label("Use the RESET button on the canvas to start over.")
        self._frame.add_label("")
        self._frame.set_mouseclick_handler(self.click)
        self._frame.set_draw_handler(self.draw)
        self._frame.start()
        
    def dist(self, p, q):
        """
        Compute Euclidean distance between points.
        """
        return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)
        
    def click(self, pos):
        """
        Mouse click handler.
        """
        x = pos[0]
        y = pos[1]
        halfwid = CANVASWIDTH/2
        height = CANVASHEIGHT
        
        self._game.clear_betmsg()

        if halfwid - 190 < x < halfwid - 101 and height - 60 < y < height - 20:
            self._game.hit()
            
        elif halfwid - 95 < x < halfwid - 3 and height - 60 < y < height - 20:
            self._game.stand()
            
        elif halfwid + 3 < x < halfwid + 92 and height - 60 < y < height - 20:
            self._game.double_down()
            
        elif halfwid + 98 < x < halfwid + 185 and height - 60 < y < height - 20:
            self._game.split_pair()
            
        elif self.dist(pos, (690, 560)) <= 44:
            self._game.deal()
            
        elif self.dist(pos, (790, 560)) <= 44:
            self._game.reset()
            self._increment = 1
            
        elif self.dist(pos, (130,50)) <= 16:
            self.increase_by_increment()
            
        elif self.dist(pos, (130, 90)) <= 16:
            self.decrease_by_increment()
            
        elif self.dist(pos, (170, 114)) <= 14:
            self._increment = 10**0
            
        elif self.dist(pos, (170, 84)) <= 14:
            self._increment = 10**1
            
        elif self.dist(pos, (170, 54)) <= 14:
            self._increment = 10**2
            
        elif self.dist(pos, (170, 24)) <= 14:
            self._increment = 10**3
            
        elif self.dist(pos, (60, 160)) <= 40:
            self.maxbet()
                    
    def maxbet(self):
        """
        Update wager to max bet.
        """
        self._game.max_wager()
            
    def increase_by_increment(self):
        """
        Increase wager by increment.
        """
        self._game.increase_wager(self._increment)
        
    def decrease_by_increment(self):
        """
        Decrease wager by increment.
        """
        self._game.decrease_wager(self._increment)
        
    def draw(self, canvas):
        """
        Draw handler.
        """
        money = self._game.get_money()
        wager = self._game.get_wager()
        pot = self._game.get_pot()
        status = self._game.get_status()
        message = STATUSMSG[status]
        message_color = STATUSCOLOR[status]
        
        # Draw the title in the top center of the canvas and white circles on table.
        titlewid = self._frame.get_canvas_textwidth("Blackjack", 50)
        canvas.draw_circle([CANVASWIDTH/2, -60], 600, 6, "white", "green")
        canvas.draw_circle([CANVASWIDTH/2, -130], 400, 6, "white", "green")
        canvas.draw_text("Blackjack", [CANVASWIDTH/2 - titlewid/2, 50], 50, "white")
        
        # Draw the dealer and player labels and cards.
        
        dealerwid = self._frame.get_canvas_textwidth("Dealer", 30)
        canvas.draw_text("Dealer", [CANVASWIDTH/2 - dealerwid/2, 260], 30, "white")
        num_dealer = self._game._dealer.num_cards()
        self._game.draw_dealer(canvas, [CANVASWIDTH/2 - CARD_SIZE[0]/2 - 15*(num_dealer-1),
                               164 - CARD_SIZE[1]/2])
        
        if status != INPLAY and status != BETTING and status != SPLIT1 and \
        status != SPLIT1BUST and status != SPLIT2:
            dwid = self._frame.get_canvas_textwidth(str(self._game.get_dealer_value()), 30)
            canvas.draw_text(str(self._game.get_dealer_value()), [CANVASWIDTH/2 - dwid/2, 
                             236], 30, "white")
                                
        playerwid = self._frame.get_canvas_textwidth("Player", 30)
        canvas.draw_text("Player", [CANVASWIDTH/2 - playerwid/2, CANVASHEIGHT-94], 
                         30, "white")
        
        if not self._game.is_split():
            num_player = self._game.get_hand_num_cards()
            self._game.draw_player(canvas,[CANVASWIDTH/2 - CARD_SIZE[0]/2 - 15*(num_player-1),
                                   424 - CARD_SIZE[1]/2])
            pwid = self._frame.get_canvas_textwidth(str(self._game.get_player_value()), 30)
            if status != BETTING:
                canvas.draw_text(str(self._game.get_player_value()), [CANVASWIDTH/2 - pwid/2, 
                                 CANVASHEIGHT - 120], 30, "white")
        else:
            num_hand1 = self._game.get_hand_num_cards()
            self._game.draw_split1(canvas, [372 - CARD_SIZE[0]/2 - 15*(num_hand1-1),
                                   424 - CARD_SIZE[1]/2])
            self._game.draw_split2(canvas, [516, 424 - CARD_SIZE[1]/2])
            if status != BETTING:
                canvas.draw_text(str(self._game.get_split1_value()), [372 - CARD_SIZE[0]/2 - \
                                 15*(num_hand1 - 1), 500], 30, "white")
                canvas.draw_text(str(self._game.get_split2_value()), [516, 500], 30, "white")
        
        # Draw the messages.
        msgwid = self._frame.get_canvas_textwidth(message, 34)
        canvas.draw_text(message, [CANVASWIDTH/2 - msgwid/2, 334], 34, message_color)
        canvas.draw_text(self._game.get_betmsg(), [54, 370], 26, "pink")
        
        # Draw funds, chip stack, wagered chips, and bet text.
        
        chipswid = self._frame.get_canvas_textwidth("Chips", 34)
        canvas.draw_text("Chips:", [12, CANVASHEIGHT - 20], 34, "white")
        canvas.draw_text(str(money), [108, CANVASHEIGHT - 20], 34, "yellow")
        
        if status == BETTING:
            pile = money - wager
        else:
            pile = money
        stacktypes = str(pile)[::-1]
        for stack in range(len(stacktypes)):
            for chip in range(int(stacktypes[stack])):
                canvas.draw_circle([234 - 34*stack, 470 - 4*chip - 2*stack], 18, 2, 
                                   "black", STACKCOLOR[stack])
          
        bet = wager if status == BETTING else pot
        wagertypes = str(bet)[::-1]
        for stack in range(len(wagertypes)):
            for chip in range(int(wagertypes[stack])):
                canvas.draw_circle([188 - 28*stack, 280 - 4*chip - 2*stack], 16, 2, 
                                   "black", STACKCOLOR[stack])
        canvas.draw_polygon([[54, 218],[210, 218],[210, 300],[54, 300]], 4, "white")
        
        betwid = self._frame.get_canvas_textwidth(str(self._game.get_wager()), 34)
        canvas.draw_circle([62, 68], 52, 6, "white", "green")
        canvas.draw_text("BET", [34, 60], 30, "white")
        canvas.draw_text(str(self._game.get_wager()), [60 - betwid/2, 92], 34, "yellow")
        
        # Draw chip values.
        canvas.draw_text("CHIP VALUES", [74, 506], 12, "white")
        for stack in range(len(STACKCOLOR)):
            value = "10e" + str(stack)
            canvas.draw_circle([204 - stack*30, 544], 14, 2, "black", STACKCOLOR[stack])
            canvas.draw_text(value, [190 - stack*30, 524], 14, "white")
        
        # Draw hole card back.
        if status == INPLAY or status == SPLIT1 or status == SPLIT1BUST or \
        status == SPLIT2:
            canvas.draw_line([CANVASWIDTH/2 - 35, 118], [CANVASWIDTH/2 - 35, 210], 
                             30, "white")
            canvas.draw_image(CARD_BACK, CARD_BACK_CENTER, [26, CARD_BACK_SIZE[1]], 
                              [CANVASWIDTH/2 - 34, 164], [26, CARD_BACK_SIZE[1]])
                              
        # Draw deck.
        for card in range(self._game.get_deck_num_cards()):
            canvas.draw_image(CARD_BACK, CARD_BACK_CENTER, CARD_BACK_SIZE, 
                              [790, 56 + card*4], CARD_BACK_SIZE)
            
        # Draw max bet.
        canvas.draw_circle([770, 430], 52, 6, "white", "green")
        canvas.draw_text("MAX", [742, 410], 24, "white")
        canvas.draw_text("BET", [748, 430], 24, "white")
        maxwid = self._frame.get_canvas_textwidth(str(MAXBET), 26)
        canvas.draw_text(str(MAXBET), [CANVASWIDTH - maxwid/2 - 80, 458], 24, "white")
        
        # Draw hit, stand, double down, split, deal, reset, and bet max buttons.
        
        canvas.draw_polygon([[CANVASWIDTH/2 - 190, CANVASHEIGHT - 60],
                            [CANVASWIDTH/2 - 101, CANVASHEIGHT - 60],
                            [CANVASWIDTH/2 - 101, CANVASHEIGHT - 20],
                            [CANVASWIDTH/2 - 190, CANVASHEIGHT - 20]], 2,
                            "purple", "cyan")
        canvas.draw_text("HIT", [CANVASWIDTH/2 - 165, CANVASHEIGHT - 30],
                         26, "black", 'sans-serif')

        canvas.draw_polygon([[CANVASWIDTH/2 - 95, CANVASHEIGHT - 60],
                            [CANVASWIDTH/2 - 3, CANVASHEIGHT - 60],
                            [CANVASWIDTH/2 - 3, CANVASHEIGHT - 20],
                            [CANVASWIDTH/2 - 95, CANVASHEIGHT - 20]], 2,
                            "purple", "#ffff80")
        canvas.draw_text("STAND", [CANVASWIDTH/2 - 93, CANVASHEIGHT - 30],
                         26, "black", 'sans-serif')
                         
        canvas.draw_polygon([[CANVASWIDTH/2 + 3, CANVASHEIGHT - 60],
                            [CANVASWIDTH/2 + 92, CANVASHEIGHT - 60],
                            [CANVASWIDTH/2 + 92, CANVASHEIGHT - 20],
                            [CANVASWIDTH/2 + 3, CANVASHEIGHT - 20]], 2,
                            "purple", "#ff6600")
        canvas.draw_text("DOUBLE", [CANVASWIDTH/2 + 6, CANVASHEIGHT - 32],
                         20, "black", 'sans-serif')
        
        canvas.draw_polygon([[CANVASWIDTH/2 + 98, CANVASHEIGHT - 60],
                            [CANVASWIDTH/2 + 185, CANVASHEIGHT - 60],
                            [CANVASWIDTH/2 + 185, CANVASHEIGHT - 20],
                            [CANVASWIDTH/2 + 98, CANVASHEIGHT - 20]], 2,
                            "purple", "#ccccff")
        canvas.draw_text("SPLIT", [CANVASWIDTH/2 + 105, CANVASHEIGHT - 30],
                         26, "black", 'sans-serif')
                         
        canvas.draw_circle([690, 560], 44, 2, "purple", "salmon")
        canvas.draw_text("DEAL", [656, 569], 26, "black", 'sans-serif')
        canvas.draw_circle([790, 560], 44, 2, "purple", "red")
        canvas.draw_text("RESET", [751, 569], 24, "black", 'sans-serif')
        
        # Draw increment buttons and label.
        
        canvas.draw_circle([134, 50], 16, 2, "purple", "orange")
        canvas.draw_circle([134, 90], 16, 2, "purple", "orange")
        canvas.draw_polygon([[124, 84], [144, 84], [134, 100]], 1, "black", "red")
        canvas.draw_polygon([[124, 56], [144, 56], [134, 38]], 1, "black", "#7FFF00")
        canvas.draw_circle([62, 168], 40, 2, "purple", "orange")
        canvas.draw_text("BET", [36, 164], 28, "black")
        canvas.draw_text("MAX", [30, 188], 28, "black")
        
        for idx in range(4):
            outline_color = "purple" if self._increment != 10**idx else "orange"
            dot_color = STACKCOLOR[idx] if self._increment != 10**idx else "green"
            canvas.draw_circle([170, 114 - idx*30], 14, 2, outline_color, STACKCOLOR[idx])
            canvas.draw_circle([170, 114 - idx*30], 4, 3, dot_color, dot_color)
            canvas.draw_text("10e" + str(idx), [188, 122 - idx*30], 16, "white")
            
        word = "INCREMENTS"
        for letter in range(len(word)):
            letwid = self._frame.get_canvas_textwidth(word[letter], 12)
            canvas.draw_text(word[letter], [224 + 5 - letwid/2, 20 + letter*12], 12, "white")
         
        # TESTING GROUNDS ############################################
        
        # Display fields.
#        REFS = {0:"betting", 1:"inplay", 2:"playerwin", 3:"dealerwin", 4:"push",
#               5:"playerbust", 6:"dealerbust", 7:"blackjack", 8:"gameover", 
#                9:"housebroke", 10:"split1", 11:"split2", 12:"split1bust", 
#                13:"split2bust", 14:"splitbustboth"}
#       
#        canvas.draw_text(REFS[status], [CANVASWIDTH/2 - 100, 100], 40, "blue")
#        canvas.draw_text("DD:" + str(self._game._doubledown), 
#                         [CANVASWIDTH/2 + 100, 100], 30, "blue")
#        canvas.draw_text("SP:" + str(self._game._splitpair), 
#                         [CANVASWIDTH/2 + 100, 130], 30, "blue")
#        canvas.draw_text("SD1:" + str(self._game._splitdouble1), 
#                         [CANVASWIDTH/2 + 100, 160], 30, "blue")
#        canvas.draw_text("SD2:" + str(self._game._splitdouble2), 
#                         [CANVASWIDTH/2 + 100, 190], 30, "blue")
        

class BlackjackTester:
    """
    Class to test Blackjack logic.
    """
    
    def __init__(self, game, num_runs, splits_only = False):
        self._game = game
        self.run_sim(num_runs, splits_only)
        
    def run_sim(self, nruns, splits_only):
        """
        Completes nruns rounds of Blackjack.
        """
        REFS = {0:"betting", 1:"inplay", 2:"playerwin", 3:"dealerwin", 4:"push",
                5:"playerbust", 6:"dealerbust", 7:"blackjack", 8:"gameover", 
                9:"housebroke", 10:"split1", 11:"split2", 12:"split1bust", 
                13:"split2bust", 14:"splitbustboth"}
        
        print "Initial money:", self._game.get_money()
        print "Initial wager:", self._game.get_wager()
        isdouble = False
        atdouble = []
        
        while nruns > 0 and self._game.get_money() > 0:
            init_money = self._game.get_money()
            print "-"*40
            print "NEW ROUND:", nruns
            self._game.deal()
            print "Player:", self._game.get_player_value()
            print self._game._player
            print "-"*3
            
            if self._game.get_player_value() == 21 or \
            self._game.get_dealer_value() == 21:
                print "Dealer:", self._game.get_dealer_value()
                print self._game._dealer
                print "-"*3
                print "STATUS:", REFS[self._game.get_status()]
                print "Money:", self._game.get_money()
                print "Winnings:", self._game.get_money() - init_money
                nruns -= 1
                continue
                
            self._game.split_pair()
            if self._game.is_split():
                print "Hand 1(pre):", self._game.get_split1_value()
                print self._game._split_hands[0]
                if self._game.get_split1_value() == 10:
                    print "<<<DOUBLE>>>"
                    isdouble = True
                    atdouble.append(nruns)
                    self._game.double_down()
                else:
                    while self._game.get_split1_value() < 17:
                        self._game.hit()
                    if self._game.get_split1_value() < 22:
                        self._game.stand()
                print "Hand 1(post):", self._game.get_split1_value()
                print self._game._split_hands[0]
                print "-"
                    
                print "Hand 2(pre):", self._game.get_split2_value()
                print self._game._split_hands[1]
                if self._game.get_split2_value() == 10:
                    print "<<<DOUBLE>>>"
                    isdouble = True
                    atdouble.append(nruns)
                    self._game.double_down()
                else:
                    while self._game.get_split2_value() < 17:
                        self._game.hit()
                    if self._game.get_split2_value() < 22:
                        self._game.stand()
                print "Hand 2(post):", self._game.get_split2_value()
                print self._game._split_hands[1]
                print "-"*3
                    
            else:
                if splits_only:
                    nruns -= 1
                    print "Money:", self._game.get_money()
                    continue
                if self._game.get_player_value() == 10:
                    print "<<<DOUBLE>>>"
                    self._game.double_down()
                else:
                    while self._game.get_player_value() < 17:
                        self._game.hit()
                print "Player:", self._game.get_player_value()
                print self._game._player
                print "-"*3
                if self._game.get_player_value() < 22:
                    self._game.stand()
                    
            print "Dealer:", self._game.get_dealer_value()
            print self._game._dealer
            print "-"*3
            print "STATUS:", REFS[self._game.get_status()]
            print "Money:", self._game.get_money()
            print "Winnings:", self._game.get_money() - init_money
            nruns -= 1
            
        print "_"*50
        print "DOUBLE:", isdouble, "at", atdouble


# Run simulations. 
#NUM_SIMS = 50
#SPLITS_ONLY = True
#BlackjackTester(BlackjackGame(), NUM_SIMS, SPLITS_ONLY)
            
# Call to run game.
BlackjackGUI(BlackjackGame())

##=================================================================
##=================================================================