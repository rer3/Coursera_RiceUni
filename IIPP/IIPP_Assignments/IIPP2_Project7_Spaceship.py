"""
Rice University / Coursera: Intro to Interactive Programming in Python (Part 2)
Week 3: Project 7
Spaceship
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org).
#=================================================================

# All import statements needed.

import math
import random
import simplegui

# Below is the link to the description of this assignment.

COURSE = "https://class.coursera.org/interactivepython2-009/"
DESCRIPTION = COURSE + "human_grading/view/courses/975652/assessments/34/submissions"

#-----------------------------------------------------------------
## Provided template examples-spaceship_template
# # program template for Spaceship
# import simplegui
# import math
# import random

# # globals for user interface
# WIDTH = 800
# HEIGHT = 600
# score = 0
# lives = 3
# time = 0

# class ImageInfo:
    # def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        # self.center = center
        # self.size = size
        # self.radius = radius
        # if lifespan:
            # self.lifespan = lifespan
        # else:
            # self.lifespan = float('inf')
        # self.animated = animated

    # def get_center(self):
        # return self.center

    # def get_size(self):
        # return self.size

    # def get_radius(self):
        # return self.radius

    # def get_lifespan(self):
        # return self.lifespan

    # def get_animated(self):
        # return self.animated

    
# # art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# # debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
# #                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
# debris_info = ImageInfo([320, 240], [640, 480])
# debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# # nebula images - nebula_brown.png, nebula_blue.png
# nebula_info = ImageInfo([400, 300], [800, 600])
# nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# # splash image
# splash_info = ImageInfo([200, 150], [400, 300])
# splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# # ship image
# ship_info = ImageInfo([45, 45], [90, 90], 35)
# ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# # missile image - shot1.png, shot2.png, shot3.png
# missile_info = ImageInfo([5,5], [10, 10], 3, 50)
# missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# # asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
# asteroid_info = ImageInfo([45, 45], [90, 90], 40)
# asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# # animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
# explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
# explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# # sound assets purchased from sounddogs.com, please do not redistribute
# soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
# missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
# missile_sound.set_volume(.5)
# ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
# explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# # helper functions to handle transformations
# def angle_to_vector(ang):
    # return [math.cos(ang), math.sin(ang)]

# def dist(p,q):
    # return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# # Ship class
# class Ship:
    # def __init__(self, pos, vel, angle, image, info):
        # self.pos = [pos[0],pos[1]]
        # self.vel = [vel[0],vel[1]]
        # self.thrust = False
        # self.angle = angle
        # self.angle_vel = 0
        # self.image = image
        # self.image_center = info.get_center()
        # self.image_size = info.get_size()
        # self.radius = info.get_radius()
        
    # def draw(self,canvas):
        # canvas.draw_circle(self.pos, self.radius, 1, "White", "White")

    # def update(self):
        # pass
    
    
# # Sprite class
# class Sprite:
    # def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        # self.pos = [pos[0],pos[1]]
        # self.vel = [vel[0],vel[1]]
        # self.angle = ang
        # self.angle_vel = ang_vel
        # self.image = image
        # self.image_center = info.get_center()
        # self.image_size = info.get_size()
        # self.radius = info.get_radius()
        # self.lifespan = info.get_lifespan()
        # self.animated = info.get_animated()
        # self.age = 0
        # if sound:
            # sound.rewind()
            # sound.play()
   
    # def draw(self, canvas):
        # canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
    
    # def update(self):
        # pass        

           
# def draw(canvas):
    # global time
    
    # # animiate background
    # time += 1
    # wtime = (time / 4) % WIDTH
    # center = debris_info.get_center()
    # size = debris_info.get_size()
    # canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    # canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    # canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # # draw ship and sprites
    # my_ship.draw(canvas)
    # a_rock.draw(canvas)
    # a_missile.draw(canvas)
    
    # # update ship and sprites
    # my_ship.update()
    # a_rock.update()
    # a_missile.update()
            
# # timer handler that spawns a rock    
# def rock_spawner():
    # pass
    
# # initialize frame
# frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# # initialize ship and two sprites
# my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
# a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)
# a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# # register handlers
# frame.set_draw_handler(draw)

# timer = simplegui.create_timer(1000.0, rock_spawner)

# # get things rolling
# timer.start()
# frame.start()

#-----------------------------------------------------------------
## Provided code...

#-----------------------------------------------------------------
## Provided code...

#-----------------------------------------------------------------
## Provided code...

#-----------------------------------------------------------------
## Provided code...

#-----------------------------------------------------------------
## Provided code...

##=================================================================

DIRECTIONS = '''
Overview
----------
In our last two mini-projects, we will build a 2D space game RiceRocks that is 
inspired by the classic arcade game Asteroids (1979). Asteroids is a relatively 
simple game by today's standards, but was still immensely popular during its 
time. (Joe spent countless quarters playing it.) In the game, the player controls 
a spaceship via four buttons: two buttons that rotate the spaceship clockwise 
or counterclockwise (independent of its current velocity), a thrust button that 
accelerates the ship in its forward direction and a fire button that shoots missiles.
Large asteroids spawn randomly on the screen with random velocities. The player's 
goal is to destroy these asteroids before they strike the player's ship. In the 
arcade version, a large rock hit by a missile split into several fast moving small 
asteroids that themselves must be destroyed. Occasionally, a flying saucer also 
crosses the screen and attempts to destroy the player's spaceship. Searching for 
"asteroids arcade" yields links to multiple versions of Asteroids that are available 
on the web (including an updated version by Atari, the original creator of Asteroids).

Development Process
----------
For this mini-project, you will implement a working spaceship plus add a single
asteroid and a single missile. We have provided art for your game so its look is
that of a more modern game. You should begin by loading the provided template.
The program template includes all necessary image and audio files. Since no audio
format is supported by all major browsers, we have decided to provide sounds in
the mp3 format (Chrome supports, Firefox on some systems). ogg versions are also
available. We recommend using Chrome for the last two weeks of class.

Phase One: Spaceship
----------
Here, you will implement the control scheme for the spaceship. This includes a
complete Spaceship class and the appropriate keyboard handlers to control the
spaceship. Your spaceship should behave as follows:
* The left and right arrows should control the orientation of the ship. While
    the left arrow is held down, your spaceship should turn CCW. While the right
    arrow is down, it should turn CW. When neither key is down, it maintains
    its orientation. Pick some regular ang vel at which your ship turns.
* The up arrow should control the thrusters of your spaceship. The thrusts should
    be on when the up arrow is down and off when it is up. When the thrusters are
    one, you should draw the ship with thrust flames. When off, draw it without.
* When thrusting, the ship should accelerate in the direction of its vector. This
    vector can be computed from the orientation/angle of the ship using the
    provided helper function angle_to_vector. You will need to experiment with
    scaling each component of this acceleration vector to generate a reasonable
    acceleration. 
* Remember that while the ship accelerates in its forward direction, the ship
    always moves in the direction of its velocity vector. Being able to accelerate
    in a direction different than the direction that you are moving is a hallmark
    of Asteroids.
* Your ship should always experience some amount of friction (even in Space).
    This choice means that the vel should always be multiplied by a constant
    factor less than one to slow the ship down. It will then come to a stop
    eventually after you stop the thrusters.
    
Some hints:
1.) Modify the draw method for the Ship class to draw the ship image (without 
    thrust flames) instead of a circle. This method should incorporate the ship's 
    position and angle. Note that the angle should be in radians, not degrees. 
    Since a call to the ship's draw method already exists in the draw handler, 
    you should now see the ship image. Experiment with different positions and 
    angles for the ship.
2.) Implement an initial version of the update method for the ship. This version 
    should update the position of the ship based on its velocity. Since a call to 
    the update method also already exists in the draw handler, the ship should 
    move in response to different initial velocities.
3.) Modify the update method for the ship to increment its angle by its angular 
    velocity.
4.) Make your ship turn in response to the left/right arrow keys. Add keydown 
    and keyup handlers that check the left and right arrow keys. Add methods to the 
    Ship class to increment and decrement the angular velocity by a fixed amount. 
    (There is some flexibility in how you structure these methods.) Call these 
    methods in the keyboard handlers appropriately and verify that you can turn 
    your ship as you expect.
5.) Modify the keyboard handlers to turn the ship's thrusters on/off. Add a 
    method to the Ship class to turn the thrusters on/off (you can make it take a 
    Boolean argument which is True or False to decide if they should be on or off).
6.) Modify the ship's draw method to draw the thrust image when it is on. (The 
    ship image is tiled and contains both images of the ship.)
7.) Modify the ship's thrust method to play the thrust sound when the thrust is on. 
    Rewind the sound when the thrust turns off.
8.) Add code to the ship's update method to use the given helper angle_to_vector
    to compute the forward vector pointing in the direction the ship is facing
    based on the ship's angle.
9.) Next, add code to the ship's update method to accelerate the ship in the 
    direction of this forward vector when the ship is thrusting. You will need to 
    update the velocity vector by a small fraction of the forward acceleration 
    vector so that the ship does not accelerate too fast.
10.) Then, modify the ship's update method such that the ship's position wraps 
    around the screen when it goes off the edge (use modular arithmetic!).
11.) Up to this point, your ship will never slow down. Finally, add friction to the 
    ship's update method as shown in the "Acceleration and Friction" video by
    multiplying each component of the velocity by a number slightly less than 1 
    during each update.
    
Phase Two: Rocks
----------
To implement rocks, we will use the provided Sprite class. Note that the update
method for the sprite will be very similar to the update method for the ship.
The primary difference is that the ship's vel and rotation are controlled by keys,
whereas sprites have these set randomly when they are created. Rocks should screen
wrap in the same manner as the ship.

In the template, the global variable a_rock is created at the start with zero vel.
Instead, we want to create version of a_rock once every second in the timer
handler. Next week, we will add multiple rocks. This week, the ship will not die
if it hits a rock. We'll add that next week. To implement rocks, we suggest the
following:
1.) Complete the Sprite class by modifying the draw handler to draw the actual
    image and the update handler to make the sprite move and rotate. Rocks do not
    accelerate or experience friction, so the sprite update method should be simpler
    than the ship update method. Test this by giving a_rock different starting
    parameters and ensuring it behaves as you expect.
2.) Implementing the timer handler rock_spawner. In particular, set a_rock to be
    a new rock on every tick. Don't forget to declare a_rock as a global in the timer
    handler. Choose a vel, pos, and angvel randomly for the rock. You will want to
    tweak the ranges of these random numbers, as that will affect how fun the
    game is to play. Make sure you generate rocks that spin in both directions
    and, likewise, move in all directions.
    
Phase Three: Missiles
----------
To implement missiles, we will use the same sprite class as for rocks. Missiles will
always have a zero angular velocity. They wlil also have a lifespan, but we will
ignore that this week. For this week only, we will allow a single missile to exist
and it will not blow up rocks.

Your missile should be created when you press the spacebar, not on a timer like
rocks. They should screen wrap just as the ship and rocks do. Otherwise, the
process is very similar:
1.) Add a shoot method to your ship class. This should spawn a new missile (for
    now just replace the old missile in a_missile). The missile's initial pos should
    be the tip of your ship's "cannon". Its vel should be the sum of the ship's vel
    and a multiple of the ship's forward vector.
2.) Modify the keydown handler to call this shoot method when space is pressed.
3.) Make sure that the missile sound is passed to the sprite initializer so that
    the shooting sound is played whenever you shoot a missile.
    
Phase Four: Interface
----------
Our user interface for RiceRocks simply shows the number of lives remaining and
the score. This week neither of those elements ever change, but they will next
week. Add code to the draw event handler to draw these on the canvas. Use the
lives and score global vars as the current lives remaining and score. 

Grading
----------
When testing the functionality of your peer's projects, remember that some 
keyboards don't register more three or more simultaneous key presses correctly. 
So please assess based on single key presses or combinations of two key presses. 
Also, please assess your peer's mini-projects in Chrome. If, for some reason, you 
must use Firefox or another browser (or had issues playing sounds in Chrome), 
please give your peers full credit on the two sound-related rubric items.

1 pt - The program draws the ship as an image.
1 pt - The ship flies in a straight line when not under thrust.
1 pt - The ship rotates at a constant angular velocity in a counter clockwise 
    direction when the left arrow key is held down.
1 pt - The ship rotates at a constant angular velocity in the clockwise direction 
    when the right arrow key is held down.
1 pt - The ship's orientation is independent of its velocity.
1 pt - The program draws the ship with thrusters on when the up arrow is held down.
1 pt - The program plays the thrust sound only when the up arrow key is held down.
1 pt - The ship accelerates in its forward direction when the thrust key is held down.
1 pt - The ship's position wraps to the other side of the screen when it crosses the 
    edge of the screen.
1 pt - The ship's velocity slows to zero while the thrust is not being applied.
1 pt - The program draws a rock as an image.
1 pt - The rock travels in a straight line at a constant velocity.
1 pt - The rock is respawned once every second by a timer.
1 pt - The rock has a random spawn position, spin direction and velocity.
1 pt - The program spawns a missile when the space bar is pressed.
1 pt - The missile spawns at the tip of the ship's cannon.
1 pt - The missile's velocity is the sum of the ship's velocity and a multiple of its 
    forward vector.
1 pt - The program plays the missile firing sound when the missile is spawned.
1 pt - The program draws appropriate text for lives on the upper left portion 
    of the canvas.
1 pt - The program draws appropriate text for score on the upper right portion 
    of the canvas.
'''

##=================================================================

# First I'll list out the globals, ImageInfo class (provided), image loading
# statements, and helper functions.

WIDTH = 800
HEIGHT = 600
DIMENSIONS = [WIDTH, HEIGHT]
score = 0
lives = 3
time = 0

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated
        
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)
    
# Then I'll initialize the draw handler and frame.

def draw(canvas):
    global time
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), 
                      [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), 
                      (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), 
                      (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    for missile in missile_group:
        missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    for missile in missile_group:
        missile.update()
    
    # Draw lives
    ltwid = frame.get_canvas_textwidth("LIVES", 32)
    if lives >= 100000:
        str_lives = "Lots!"
    else:
        str_lives = str(lives)
    lwid = frame.get_canvas_textwidth(str_lives, 36)
    canvas.draw_text("LIVES", [55 - ltwid/2,30], 32, "white")
    canvas.draw_text(str_lives, [55 - lwid/2, 64], 36, "white")
    
    # Draw score
    stwid = frame.get_canvas_textwidth("SCORE", 32)
    str_score = str(score)
    if score >= 10000000:
        str_score = "So many points!"
        ssize = 18
    else:
        str_score = str(score)
        ssize = 28
    swid = frame.get_canvas_textwidth(str_score, ssize)
    canvas.draw_text("SCORE", [WIDTH - stwid/2 - 68, 30], 32, "white")
    canvas.draw_text(str_score, [WIDTH - swid/2 - 68, 60], ssize, "white")
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# register handlers
frame.set_draw_handler(draw)

##=================================================================

# Phase One

# First I'll implement the new draw method for the Ship class so that the image
# of the ship is displayed and I can see whether or not my thrust/spin methods work.

class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.decelerator = 1
        self.dampener = .03
        
    def spin_stop(self):
        self.angle_vel = 0
        
    def spin_left(self):
        self.angle_vel = -.1
        
    def spin_right(self):
        self.angle_vel = .1
        
    def thruster(self):
        self.thrust = not self.thrust
        if self.thrust:
            ship_thrust_sound.play()
            self.image_center[0] = 45 + 90
        else:
            ship_thrust_sound.pause()
            ship_thrust_sound.rewind()
            self.image_center[0] = 45
            
    def fire(self):                    
        global missile_group
        missile_group = set()
        forward = angle_to_vector(self.angle)
        pos = [self.pos[0] + forward[0]*42, self.pos[1] + forward[1]*42]
        vel = [self.vel[0] + forward[0]*12, self.vel[1] + forward[1]*12]
        missile_group.add(Sprite(pos, vel, self.angle, 0, missile_image, missile_info, missile_sound))
        
    def draw(self,canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, 
                          self.pos, self.image_size, self.angle)

    def update(self):
        forward = angle_to_vector(self.angle) if self.thrust else [0,0]
        for idx in range(2):
            self.vel[idx] += forward[idx]/(1 + self.decelerator)
            self.vel[idx] *= 1 - self.dampener
        for idx in range(2):
            self.pos[idx] += self.vel[idx]
            self.pos[idx] %= DIMENSIONS[idx]
        self.angle += self.angle_vel

# Initialize a ship and draw it.
        
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
#frame.start()

# So far, so good. The ship is drawn. Now, the angvel needs to be changed by
# pressing the L and R arrow keys. The update method will be updated to 
# reflect a change in pos and ang. self.angle_vel is set to 1. Thrust will use
# the example from the relevant course video and implement a forward var
# that converts angle to a vector if the ship is thrusting, else [0,0]. The update
# method will first update the velocity by adding this forward motion divided
# by a constant (decelerator) that slows it down to something manageable for
# regular gameplay. A dampener var is initialized and multiplied by the velocity
# to introduce intertial dampening. The higher the dampener, the higher the
# dampening.

# The sound controls for thrust were added to the thruster method. The rewind
# statement was required, but it eliminates the immediate sound noise, with a
# gap at the beginning. I will remove this in the final version of the game,
# where I can control thrust duration so that a player does not play the mp3
# to its end in the middle of a continuous thrust (confirmed for occurring). 

# The image wrapping in the window is controlled by a for loop which updates
# position by incrementing by corresponding vel value, then by taking the pos
# mod corresponding dimension value to return the wrapped position.

KEYDOWN = {
    "left":my_ship.spin_left,
    "right":my_ship.spin_right,
    "up":my_ship.thruster,
    "space":my_ship.fire
    }
    
KEYUP = {
    "left":my_ship.spin_stop,
    "right":my_ship.spin_stop,
    "up":my_ship.thruster
    }

def keydown(key):
    """
    Handler for key press.
    """
    for k in KEYDOWN:
        if key == simplegui.KEY_MAP[k]:
            KEYDOWN[k]()
            
def keyup(key):
    """
    Handler for key up.
    """
    for k in KEYUP:
        if key == simplegui.KEY_MAP[k]:
            KEYUP[k]()

frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
#frame.start()

##=================================================================

# Phase Two

# Below is the Sprite class and rock_spawner timer and handler, updated as I go
# through the directions.

# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size,
                          self.pos, self.image_size, self.angle)
    
    def update(self):
        for idx in range(2):
            self.pos[idx] += self.vel[idx]
            self.pos[idx] %= DIMENSIONS[idx]
        self.angle += self.angle_vel
        
a_rock = Sprite([WIDTH/3, HEIGHT/3], [1,1], 0, 0, asteroid_image, asteroid_info)
r_minvel = 1
r_maxvel = 6
r_minangvel = 10
r_maxangvel = 20

def rock_spawner():
    global a_rock
    
    pos = [random.randrange(0,WIDTH), random.randrange(0,HEIGHT)]
    
    direction = [random.choice([-1,1]), random.choice([-1,1])]
    vel = [0,0]
    vel[0] = random.randrange(r_minvel, r_maxvel+1) * direction[0]
    vel[1] = random.randrange(r_minvel, r_maxvel+1) * direction[1]
    
    ang = random.randrange(0,int(2*math.pi))
    angdir = random.choice([-1,1])
    angvel = random.randrange(r_minangvel, r_maxangvel)/float(100)*angdir
    
    a_rock = Sprite([pos[0],pos[1]], [vel[0],vel[1]], ang, angvel,
                    asteroid_image, asteroid_info)
    
timer = simplegui.create_timer(1000.0, rock_spawner)

# First I will implement the timer handler rock_spawner. The var a_rock is
# recommended as a global var that is updated via rock_spawner, so I will 
# comply with that. The handler will choose a random vel, pos, and angvel
# within reasonable/necessary ranges and, instead of updating a list with
# several rocks, will reinitialize the a_rock sprite with these new parameters.
# Note that the rock is on top of the ship in the canvas layers (update draw).

# The update for the Sprite will use the same for loop as from Ship to update
# the pos by incrementing with vel values. The Ship could be a sub of Sprite
# but I will save that for the actual game. It will also update ang with angvel.

timer.start()
#frame.start()

##=================================================================

# Phase Three

# For missiles, first I'll update the draw function to include calls to draw and
# update the missile. I'll draw the missile in the center like the ship to see 
# where it lines up with that sprite. The magic number 42 added to the horiz
# position seems to work well, placing it at the tip of the ship (the ship tip).

# a_missile = Sprite([WIDTH/2+42, HEIGHT/2], [0,0], 0, 0, missile_image, missile_info)
# frame.start()

# Now I will go back to the Ship class and update the fire() method with an
# instantiation statement for a missile with vel equal to the sum of the ship's
# vel and a multiple of the forward vector. The missile sound will be passed
# to the initializer. When initializing the a_missile sprite (to be updated by
# the call to thruster, I will draw it off the canvas.

# That didn't work, so I implemented a missile_group set.

missile_group = set()
#frame.start()
##=================================================================

# Phase Four

# The draw method is updated with the score and lives.

#frame.start()

##=================================================================

# Final version

"""
Rice University / Coursera: Intro to Interactive Programming in Python (Part 2)
Week 3: Project 7
Spaceship
"""

import math
import random
import simplegui

# Global constants
WIDTH = 800
HEIGHT = 600
DIMENSIONS = [WIDTH, HEIGHT]
score = 0
lives = 3
time = 0
    
# Rock constants
r_minvel = 1
r_maxvel = 6
r_minangvel = 10
r_maxangvel = 20

    
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated
        
        
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

    
# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.decelerator = 1
        self.dampener = .03
        
    def spin_stop(self):
        self.angle_vel = 0
        
    def spin_left(self):
        self.angle_vel = -.1
        
    def spin_right(self):
        self.angle_vel = .1
        
    def thruster(self):
        self.thrust = not self.thrust
        if self.thrust:
            ship_thrust_sound.play()
            self.image_center[0] = 45 + 90
        else:
            ship_thrust_sound.pause()
            ship_thrust_sound.rewind()
            self.image_center[0] = 45
            
    def fire(self):                    
        global missile_group
        missile_group = set()
        forward = angle_to_vector(self.angle)
        pos = [self.pos[0] + forward[0]*42, self.pos[1] + forward[1]*42]
        vel = [self.vel[0] + forward[0]*12, self.vel[1] + forward[1]*12]
        missile_group.add(Sprite(pos, vel, self.angle, 0, missile_image, missile_info, missile_sound))
        
    def draw(self,canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, 
                          self.pos, self.image_size, self.angle)

    def update(self):
        forward = angle_to_vector(self.angle) if self.thrust else [0,0]
        for idx in range(2):
            self.vel[idx] += forward[idx]/(1 + self.decelerator)
            self.vel[idx] *= 1 - self.dampener
        for idx in range(2):
            self.pos[idx] += self.vel[idx]
            self.pos[idx] %= DIMENSIONS[idx]
        self.angle += self.angle_vel
        
        
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size,
                          self.pos, self.image_size, self.angle)
    
    def update(self):
        for idx in range(2):
            self.pos[idx] += self.vel[idx]
            self.pos[idx] %= DIMENSIONS[idx]
        self.angle += self.angle_vel

# Timer handler
def rock_spawner():
    global a_rock
    
    pos = [random.randrange(0,WIDTH), random.randrange(0,HEIGHT)]
    
    direction = [random.choice([-1,1]), random.choice([-1,1])]
    vel = [0,0]
    vel[0] = random.randrange(r_minvel, r_maxvel+1) * direction[0]
    vel[1] = random.randrange(r_minvel, r_maxvel+1) * direction[1]
    
    ang = random.randrange(0,int(2*math.pi))
    angdir = random.choice([-1,1])
    angvel = random.randrange(r_minangvel, r_maxangvel)/float(100)*angdir
    
    a_rock = Sprite([pos[0],pos[1]], [vel[0],vel[1]], ang, angvel,
                    asteroid_image, asteroid_info)

# Event handlers    
def keydown(key):
    """
    Handler for key press.
    """
    for k in KEYDOWN:
        if key == simplegui.KEY_MAP[k]:
            KEYDOWN[k]()
            
def keyup(key):
    """
    Handler for key up.
    """
    for k in KEYUP:
        if key == simplegui.KEY_MAP[k]:
            KEYUP[k]()

# Draw handler
def draw(canvas):
    global time
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), 
                      [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), 
                      (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), 
                      (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    for missile in missile_group:
        missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    for missile in missile_group:
        missile.update()
    
    # Draw lives
    ltwid = frame.get_canvas_textwidth("LIVES", 32)
    if lives >= 100000:
        str_lives = "Lots!"
    else:
        str_lives = str(lives)
    lwid = frame.get_canvas_textwidth(str_lives, 36)
    canvas.draw_text("LIVES", [55 - ltwid/2,30], 32, "white")
    canvas.draw_text(str_lives, [55 - lwid/2, 64], 36, "white")
    
    # Draw score
    stwid = frame.get_canvas_textwidth("SCORE", 32)
    str_score = str(score)
    if score >= 10000000:
        str_score = "So many points!"
        ssize = 18
    else:
        str_score = str(score)
        ssize = 28
    swid = frame.get_canvas_textwidth(str_score, ssize)
    canvas.draw_text("SCORE", [WIDTH - stwid/2 - 68, 30], 32, "white")
    canvas.draw_text(str_score, [WIDTH - swid/2 - 68, 60], ssize, "white")
    
# Initialize game variablesa
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
a_rock = Sprite([WIDTH/3, HEIGHT/3], [1,1], 0, 0, asteroid_image, asteroid_info)
missile_group = set()

# Key handler dictionaries
KEYDOWN = {
    "left":my_ship.spin_left,
    "right":my_ship.spin_right,
    "up":my_ship.thruster,
    "space":my_ship.fire
    }
    
KEYUP = {
    "left":my_ship.spin_stop,
    "right":my_ship.spin_stop,
    "up":my_ship.thruster
    }
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# Initialize timer
timer = simplegui.create_timer(1000.0, rock_spawner)

# Start timer and frame
timer.start()
frame.start()

##=================================================================
##=================================================================