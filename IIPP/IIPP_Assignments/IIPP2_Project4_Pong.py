"""
Rice University / Coursera: Intro to Interactive Programming in Python (Part 1)
Week 4: Project 4
Pong
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

##=================================================================

# All code was pasted from the original python file containing project code.

import simplegui
import math
import random

##############################
# GLOBAL VARIABLES
##############################

# Canvas dimensions
C_WIDTH = 800
C_HEIGHT = 500
C_CENTER = [C_WIDTH / 2, C_HEIGHT / 2]
C_LMARGIN = 50
C_RMARGIN = 50

# World variables

# Game attributes
g_running = False
g_lastpoint = ""
g_msg = ""
g_round = 0
rain = []
r_vel = [4,12]
r_len = 4
r_girth = 3
r_clr = "#00BFFF"

balls = []
b_acc = 1
b_accboost = 0.1

p_acc = [0,5]
p_brake = 0.3
p_length = 100
p_width = 32

p1_pos = [p_width/2, C_CENTER[1] - p_length/2]
p1_vel = [0,0]
p1_clr = "bisque"
p1_up = False
p1_down = False
p1_score = 0

p2_pos = [C_WIDTH - p_width/2, C_CENTER[1] - p_length/2]
p2_vel = [0,0]
p2_clr = "bisque"
p2_up = False
p2_down = False
p2_score = 0

##############################
# HELPER FUNCTIONS
##############################

def newgame():
    global g_msg
    g_msg = "Press SPACE to start"
    t_p1move.start()
    t_p2move.start()
    t_pbump.start()
    t_spawnball.start()
    t_bbump.start()
            
def reset():
    global balls, g_lastpoint, g_round, g_running, p1_pos, p1_score, p2_pos, p2_score
    balls = []
    g_lastpoint = ""
    g_round = 0
    g_running = False
    p1_pos = [p_width/2, C_CENTER[1] - p_length/2]
    p1_score = 0
    p2_pos = [C_WIDTH - p_width/2, C_CENTER[1] - p_length/2]
    p2_score = 0
    newgame()

##############################
# DEFINE CLASSES
##############################

class Ball:
    global balls
    
    def __init__(self, pos = [C_CENTER[0], C_CENTER[1]], 
                 rad = 20, clr = "white"):
        self.pos = pos
        self.rad = 20
        self.clr = clr 
        
        if g_round == 0:
            randvel = random.choice(["UL", "UR"])
            if randvel == "UL":
                self.vel = [-(2 + random.random()),-(2 + random.random())]
            elif randvel == "UR":
                self.vel = [2 + random.random(),-(2 + random.random())]
        else:
            if g_lastpoint == "p1":
                self.vel = [-(2 + random.random()),-(2 + random.random())]
            else:
                self.vel = [2 + random.random(),-(2 + random.random())]
                
        balls.append([self.pos[0], self.pos[1], self.vel[0],
                      self.vel[1], self.rad, self.clr, b_acc, b_accboost])
        # BALLS    0      1      2       3    4   5   6
        # LIST:  pos[0] pos[1] vel[0] vel[1] rad clr acc

##############################
# EVENT HANDLERS
##############################

def draw(c):
    
    # RAIN   0    1     2    3    4     5
    # LIST: posx posy velx vely girth color
    # Draw optional background
    if not not rain:
        for drop in rain:
            c.draw_line((drop[0], drop[1]), (drop[0] + r_len + drop[2], drop[1] + drop[3]), drop[4], drop[5])
                
    # Draw table
    c.draw_line((p_width - 1, 0), (p_width - 1,C_HEIGHT), 1, "orange")
    c.draw_line((C_WIDTH - (p_width - 1), 0), (C_WIDTH - (p_width - 1), C_HEIGHT), 1, "orange")
    
    # BALLS    0      1      2       3    4   5   6
    # LIST:  pos[0] pos[1] vel[0] vel[1] rad clr acc
    
    # Update ball position and draw ball
    if not not balls:
        for ball in balls:
            ball[0] += ball[2]*ball[6]
            ball[1] += ball[3]*ball[6]
            c.draw_circle((ball[0], ball[1]), ball[4], 1, ball[5], ball[5])
    
    # Update paddle position
    p1_pos[1] += p1_vel[1]
    p2_pos[1] += p2_vel[1]
    
    # Draw paddles
    c.draw_line((p1_pos[0], p1_pos[1]), (p1_pos[0], p1_pos[1] + p_length), 
                p_width, p1_clr)
    c.draw_line((p2_pos[0], p2_pos[1]), (p2_pos[0], p2_pos[1] + p_length), 
                p_width, p2_clr)
    
    # Game text
    p1len = frame.get_canvas_textwidth("Player 1", 24)
    c.draw_text("Player 1", (C_CENTER[0] - p1len - 250, 30), 24, "white")
    p1sclen = frame.get_canvas_textwidth(str(p1_score), 42)
    c.draw_text(str(p1_score), (C_CENTER[0] - p1sclen - 140, 40), 42, "white")
    
    p2len = frame.get_canvas_textwidth("Player 2", 24)
    c.draw_text("Player 2", (C_CENTER[0] + 250, 30), 24, "white")
    p2sclen = frame.get_canvas_textwidth(str(p2_score), 42)
    c.draw_text(str(p2_score), (C_CENTER[0] + 140, 40), 42, "white")   
    
    ponglen = frame.get_canvas_textwidth("PONG", 36, "sans-serif")
    c.draw_text("PONG", (C_CENTER[0] - ponglen/2, 40), 36, "white", "sans-serif")
    gmsglen = frame.get_canvas_textwidth(g_msg, 30)
    c.draw_text(str(g_msg), (C_CENTER[0] - gmsglen/2, C_CENTER[1]), 30, "white")
    
## Keyboard and mouse 

def keydown(key):
    global g_msg, g_running, p1_up, p1_down, p2_up, p2_down
    if key == simplegui.KEY_MAP["space"]:
        g_msg = ""
        g_running = True
    if g_running:
        if key == simplegui.KEY_MAP["w"]:
            p1_up = True
        if key == simplegui.KEY_MAP["s"]:
            p1_down = True
        if key == simplegui.KEY_MAP["up"]:
            p2_up = True
        if key == simplegui.KEY_MAP["down"]:
            p2_down = True

def keyup(key):
    global p1_up, p1_down, p2_up, p2_down
    if g_running:
        if key == simplegui.KEY_MAP["w"]:
            p1_up = False
        if key == simplegui.KEY_MAP["s"]:
            p1_down = False
        if key == simplegui.KEY_MAP["up"]:
            p2_up = False
        if key == simplegui.KEY_MAP["down"]:
            p2_down = False
        
def click(pos):
    global rain
    if g_running:
        if t_storm.is_running():
            t_storm.stop()
            t_rdrop.stop()
            rain = []
        else:
            t_storm.start()
            t_rdrop.start()
    
## Buttons

def addball():
    if g_running:
        bc = random.choice(["#FA8072", "#FF69B4", "#FF7F50", "#FFD700",
                            "#F0E68C", "#DDA0DD", "#9932CC", "#ADFF2F",
                            "#00FF7F", "#9ACD32", "#00FFFF", "#7FFFD4",
                            "#B0E0E6", "#FFEBCD", "#DAA520", "#F5F5F5",
                            "#F5F5DC", "#FFFFF0", "#FFF0F5", "#FFE4E1"])
        Ball(clr = bc)

## Timers

def p1move():
    if g_running:
        if p1_up:
            p1_vel[1] -= p_acc[1]
        if p1_down:
            p1_vel[1] += p_acc[1]
        if not (p1_up or p1_down) and p1_vel != 0:
            p1_vel[1] *= p_brake

def p2move():
    if g_running:
        if p2_up:
            p2_vel[1] -= p_acc[1]
        if p2_down:
            p2_vel[1] += p_acc[1]
        if not (p2_up or p2_down) and p2_vel != 0:
            p2_vel[1] *= p_brake
                 
def pbump():
    if g_running:
        if p1_pos[1] + p1_vel[1] <= 0:
            p1_pos[1] = 0
            p1_vel[1] = 0
        if p1_pos[1] + p1_vel[1] + p_length >= C_HEIGHT - 1:
            p1_pos[1] = C_HEIGHT - p_length
            p1_vel[1] = 0
        if p2_pos[1] + p2_vel[1] <= 0:
            p2_pos[1] = 0
            p2_vel[1] = 0
        if p2_pos[1] + p2_vel[1] + p_length >= C_HEIGHT - 1:
            p2_pos[1] = C_HEIGHT - p_length
            p2_vel[1] = 0

def spawnball():
    if g_running and not balls:
        bc = random.choice(["#FA8072", "#FF69B4", "#FF7F50", "#FFD700",
                            "#F0E68C", "#DDA0DD", "#9932CC", "#ADFF2F",
                            "#00FF7F", "#9ACD32", "#00FFFF", "#7FFFD4",
                            "#B0E0E6", "#FFEBCD", "#DAA520", "#F5F5F5",
                            "#F5F5DC", "#FFFFF0", "#FFF0F5", "#FFE4E1"])
        Ball(clr = bc)

# BALLS    0      1      2       3    4   5   6
# LIST:  pos[0] pos[1] vel[0] vel[1] rad clr acc
def bbump():
    global p1_score, p2_score, g_lastpoint, g_round
    if g_running and (not not balls):
        for ball in balls:
            if ball[1] - ball[4] <= 0:
                ball[3] = 1 + random.random()
                ball[6] += b_accboost
            elif ball[1] + ball[4] >= C_HEIGHT - 1:
                ball[3] = - (1 + random.random())
                ball[6] += b_accboost
            elif ball[0] + ball[4] >= p2_pos[0] - p_width/2:
                if p2_pos[1] < ball[1] and p2_pos[1] + p_length > ball[1]:
                    ball[2] = - (2 + 2*random.random())
                    ball[6] += b_accboost
                else:
                    del balls[balls.index(ball)]
                    p1_score += 1
                    g_lastpoint = "p1"
                    g_round += 1
            elif ball[0] - ball[4] <= p1_pos[0] + p_width/2:
                if p1_pos[1] < ball[1] and p1_pos[1] + p_length > ball[1]:
                    ball[2] = 2 + 2*random.random()
                    ball[6] += b_accboost
                else:
                    del balls[balls.index(ball)]
                    p2_score += 1
                    g_lastpoint = "p2"
                    g_round += 1

# RAIN   0    1     2    3    4     5
# LIST: posx posy velx vely girth color
def storm():
    global rain
    if random.randint(0,100) < 30:
        px = random.randint(0, C_WIDTH - 10)
        py = random.randint(0, 50)
        vx = r_vel[0]
        vy = r_vel[1]
        g = r_girth
        c = r_clr
        rain.append([px,py,vx,vy,g,c])

def rdrop():
    if not not rain:
        for drop in rain:
            if drop[1] + drop[3] < C_HEIGHT:
                drop[0] += drop[2]
                drop[1] += drop[3]
            else:
                del rain[rain.index(drop)]
            
##############################
# CREATE FRAME
##############################

frame = simplegui.create_frame("PONG", C_WIDTH, C_HEIGHT, 250)

##############################
# REGISTER EVENT HANDLERS 
##############################

# Set handlers #############################
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)

# Buttons and labels #######################
frame.add_label("=========  PONG  =========")
frame.add_label("Play the classic Atari game!")
frame.add_label("")
frame.add_label("> Player 1 use W and S keys to move your paddle up and down.")
frame.add_label("> Player 2 use up and down keys to move your paddle.")
frame.add_label("")
frame.add_label("Click below to reset game progress and launch a new game.")
frame.add_button("Restart", reset, 150)
frame.add_label("")
frame.add_label("For a significant challenge, click the button to add a ball.")
frame.add_button("Add a ball", addball, 150)
frame.add_label("")
frame.add_label("Click the canvas to make it rain.")

# Set timers ##############################
t_p1move = simplegui.create_timer(50, p1move)
t_p2move = simplegui.create_timer(50, p2move)
t_pbump = simplegui.create_timer(50, pbump)
t_spawnball = simplegui.create_timer(50, spawnball)
t_bbump = simplegui.create_timer(50, bbump)
t_storm = simplegui.create_timer(50, storm)
t_rdrop = simplegui.create_timer(50, rdrop)

##############################
# START GAME 
##############################

newgame()
frame.start()

##=================================================================
##=================================================================