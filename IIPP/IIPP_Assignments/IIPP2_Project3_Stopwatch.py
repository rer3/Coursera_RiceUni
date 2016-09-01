"""
Rice University / Coursera: Intro to Interactive Programming in Python (Part 1)
Week 3: Project 3
Stopwatch
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

##=================================================================

# All code was pasted from the original python file containing project code.

# Simple Timre

import simplegui

# Define global variables

current = 0
tries = 0
wins = 0
streak = 0

# Define helper functions

def format(t):
    """
    Formats current time to A:BC.D, where a=minutes, bc=seconds, 
    d=deciseconds, and returns the string. 
    """
    a = t / 600
    b = t % 600 / 100
    c = t / 10 % 10
    d = t % 10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)

def score(wins, tries):
    """
    Formats current score to show 'wins/tries'
    """
    return str(wins) + " / " + str(tries)

# Define event handlers for 'Start', 'Stop', and 'Reset' buttons

def start():
    """
    Starts the timer
    """
    timer.start()

def reset():
    """
    Resets all global variables and stop the timer
    """
    global current, tries, wins
    current  = 0
    tries = 0
    wins = 0
    timer.stop()

def stop():
    """
    Checks if the timer is running, if True, stops the timer, increments 
    tries, and checks if the timer is stopped at zero tenths of a second, 
    if True, increments wins
    """
    if(timer.is_running() == True):
        timer.stop()
        global tries
        tries += 1
        if (current % 10 == 0):
            global wins
            wins += 1

# Define event handler for timer

def tick():
    """
    Increments current time by one tenth of a second
    """
    global current
    current += 1
    
# Define draw handler

def draw(c):
    """
    Draws timer and score
    """
    c.draw_text(format(current), (75, 190), 60, "yellow")
    c.draw_text("Score", (200, 40), 28, "white", "sans-serif")
    c.draw_text(score(wins, tries), (208, 70), 30, "white", "sans-serif")

# Create frame

frame = simplegui.create_frame("Stopwatch: The Game", 300, 300, 300)
frame.set_canvas_background("#0066FF")

# Register event handlers

timer = simplegui.create_timer(100, tick)
title = frame.add_label("----------STOPWATCH: THE GAME----------")
directions = frame.add_label("Try to stop the timer at zero tenths of a second")
labelspace = frame.add_label("")
label1 = frame.add_label("#Click 'Start' to start the timer")
label2 = frame.add_label("#Click 'Stop' to stop the timer")
label3 = frame.add_label("#Click 'Reset' to reset timer and score")
labelspace = frame.add_label("")
startbutton = frame.add_button("Start", start, 50)
stopbutton = frame.add_button("Stop", stop, 80)
resetbutton = frame.add_button("Reset", reset, 50)
frame.set_draw_handler(draw)

# Start frame

frame.start()

##=================================================================

# Complex timer

import simplegui

# Define global variables

#Timer
current = 0

#Single player
tries = 0
wins = 0
winstreak = 0
losestreak = 0
mood = "#FFF8DC"
scorepos = (250, 140)

#Two player
p1score = 0
p1ws = 0
p1ls = 0
p1mood = "#FFF8DC"
p1scorepos = (132,510)
p2score = 0
p2ws = 0
p2ls = 0
p2mood = "#FFF8DC"
p2scorepos = (426,510)
result2pline = 0.1
result2p = ""

# Define helper functions

def format(t):
    """
    Formats current timer time to A:BC.D, where A=minutes, BC=seconds, 
    D=deciseconds, and returns the string
    """
    a = t / 600
    b = t % 600 / 100
    c = t / 10 % 10
    d = t % 10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)

def score(wins, tries):
    """
    Formats current single player score to show 'wins/tries'
    """
    return str(wins) + " / " + str(tries)

def score_string(score):
    """
    Converts a numerical score into a string for the canvas
    """
    return str(score)

def goodmood(streak):
    """
    Changes background color based on the number of consecutive successful tries
    """
    if streak == 1:
        return "#FFF8DC"
    elif streak == 2:
        return "#CCFFCC"
    elif streak == 3:
        return "#99FFCC"
    elif streak == 4:
        return "#99FF99"
    elif streak == 5:
        return "#66FF99"
    else:
        return "#00FF66"

def badmood(streak):
    """
    Changes background color based on the number of consecutive failed tries
    """
    if streak == 1:
        return "#FFF8DC"
    elif streak == 2:
        return "#FFB5B5"
    elif streak == 3:
        return "#FF7373"
    elif streak == 4:
        return "#FF4848"               
    elif streak == 5:
        return "#FF2626"
    else:
        return "#FF0000"    

# Define event handlers for buttons

def start():
    """
    Starts the timer 
    """
    timer.start()
    global result2pline, result2p
    result2pline = 0.1
    result2p = ""

def stop():
    """
    Stops the timer, updates score and background color
    """
    if timer.is_running():
        timer.stop()
        global tries, wins, winstreak, losestreak, mood, scorepos
        tries += 1
        if current % 10 == 0:
            wins += 1
            winstreak += 1
            losestreak = 0
            mood = goodmood(winstreak)
        else:
            winstreak = 0
            losestreak += 1
            mood = badmood(losestreak)
        if tries > 9:
            scorepos = (241, 140)
        if wins > 9:
            scorepos = (228, 140)
                
def stop2p():
    """
    Stops the timer and updates the result for a 2-player game
    """
    if timer.is_running():
        timer.stop()
        global result2pline, result2p
        result2pline = 60
        if p1score > p2score:
            result2p = "Player 1 wins!"
        elif p2score > p1score:
            result2p = "Player 2 wins!"
        else:
            result2p = "Nobody wins!"

def reset():
    """
    Resets all global variables and stops the timer
    """
    global current, tries, wins, winstreak, losestreak, mood, scorepos
    global p1score, p1ws, p1ls, p1mood, p2score, p2ws, p2ls, p2mood
    global p1scorepos, p2scorepos, result2pline, result2p
    
    current  = 0
    tries = 0
    wins = 0
    winstreak = 0
    losestreak = 0
    mood = "#FFF8DC"
    scorepos = (250, 140)
    
    p1score = 0
    p1ws = 0
    p1ls = 0
    p1mood = "#FFF8DC"
    p1scorepos = (132,510)
    p2score = 0
    p2ws = 0
    p2ls = 0
    p2mood = "#FFF8DC"
    p2scorepos = (426,510)
    result2pline = 0.1
    result2p = ""
    
    timer.stop()

# Define event handler for keyboard input

def keystop(key):
    """
    Updates scores, streaks, and background colors for 2-player games
    """
    global p1score, p1ws, p1ls, p1mood, p1scorepos
    if key == 81:
        if timer.is_running():
            if current % 10 == 0:
                p1score += 3
                p1ws += 1
                p1ls = 0
                p1mood = goodmood(p1ws)
            else:
                p1score -= 1
                p1ws = 0
                p1ls += 1
                p1mood = badmood(p1ls)
            if p1score > 9:
                p1scorepos = (118,510)
            elif p1score < -9:
                p1scorepos = (112,510)
            else:
                p1scorepos = (132,510)
            
    global p2score, p2ws, p2ls, p2mood, p2scorepos
    if key == 80:
        if timer.is_running():
            if current % 10 == 0:
                p2score += 3
                p2ws += 1
                p2ls = 0
                p2mood = goodmood(p2ws)
            else:
                p2score -= 1
                p2ws = 0
                p2ls += 1
                p2mood = badmood(p2ls)
            if p2score > 9:
                p2scorepos = (412,510)
            elif p2score < -9:
                p2scorepos = (406,510)
            else: 
                p2scorepos = (426,510)
            
# Define event handler for timer

def tick():
    """
    Increments current time by one (at 0.1s intervals)
    """
    global current
    current += 1
    
# Define draw handler

def draw(c):
    """
    Draws timer, scores, and background effects
    """
    c.draw_line((0,130), (580,130), 200, mood)
    c.draw_line((0,450), (290,450), 200, p1mood)
    c.draw_line((290,450), (580,450), 200, p2mood)
    c.draw_line((0,290), (580,290), 200, "black")
    c.draw_text(format(current), (150, 330), 110, "yellow")
    
    c.draw_line((193,108), (387,108), 120, "#000080")
    c.draw_line((0,25), (580,25), 50, "#00FFFF")
    c.draw_text("SINGLE PLAYER", (20, 34), 30, "#191970")
    c.draw_text("Score", (250, 90), 30, "white", "sans-serif")
    c.draw_line((250,96), (329,96), 4, "white")
    c.draw_text(score(wins, tries), scorepos, 40, "white", "sans-serif")
    
    c.draw_line((66,472), (220,472), 120, "#556B2F")
    c.draw_line((360,472), (514,472), 120, "#4B0082")    
    c.draw_line((0,555), (580,555), 50, "#F4A460")
    c.draw_text("TWO PLAYER", (20, 566), 30, "#800000")
    c.draw_text("Player 1", (90, 454), 30, "#F0E68C", "sans-serif")
    c.draw_line((90,464), (200,464), 4, "#F0E68C")
    c.draw_text(score_string(p1score), p1scorepos, 40, "#F0E68C", "sans-serif")
    c.draw_text("Player 2", (380,454), 30, "#E6E6FA", "sans-serif")
    c.draw_line((380,464), (490,464), 4, "#E6E6FA")
    c.draw_text(score_string(p2score), p2scorepos, 40, "#E6E6FA", "sans-serif")
    c.draw_line((0,440), (580,440), result2pline, "#F7DE00")
    c.draw_text(result2p, (180,450), 35, "black")


# Create frame

frame = simplegui.create_frame("Stopwatch: The Game", 580, 580, 325)

# Register event handlers

label_title = frame.add_label("----------STOPWATCH: THE GAME----------")
label_directions = frame.add_label("Try to stop the timer at zero tenths of a second")
labelspace = frame.add_label("")

labela0 = frame.add_label("Single Player")
labela1 = frame.add_label("Score 1 pt for each good stop")
labela2 = frame.add_label("# Click 'Start' to start or resume the timer")
labela3 = frame.add_label("# Click 'STOP' to stop the timer and score a point")
labelspace = frame.add_label("")
button_start = frame.add_button("Start", start, 100)
button_stop = frame.add_button("----------- STOP -----------", stop, 100)
labelspace = frame.add_label("")

labelb0 = frame.add_label("Two Player")
labelb1 = frame.add_label("Good stops are 3 pts, bad stops are -1 pts")
labelb2 = frame.add_label("# Click 'Start' to start or resume the timer")
labelb3 = frame.add_label("# Player 1: press the 'Q' key to score")
labelb4 = frame.add_label("# Player 2: press the 'P' key to score")
labelb5 = frame.add_label("# Click 'Stop' to stop the timer and show results")
labelspace = frame.add_label("")
button_start = frame.add_button("Start", start, 100)
button_stop2p = frame.add_button("Stop", stop2p, 100)
frame.set_keydown_handler(keystop)
labelspace = frame.add_label("")

labelc0 = frame.add_label("Click to clear all game data and reset the clock")
labelspace = frame.add_label("")
button_reset = frame.add_button("Reset", reset, 100)

frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# Start frame

frame.start()

##=================================================================
##=================================================================