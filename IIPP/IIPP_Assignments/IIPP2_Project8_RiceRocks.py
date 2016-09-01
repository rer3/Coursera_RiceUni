"""
Rice University / Coursera: Intro to Interactive Programming in Python (Part 2)
Week 4: Project 8
Rice Rocks (Asteroids)
"""
#=================================================================
# All code for this assignment is shown below with only essential imports.
# Code provided by Rice University has been modified whenever applicable.
# All sections/questions enclosed in functions precede a call to their function.
# Code for this project was run in CodeSkulptor (http://www.codeskulptor.org) and PyCharm.
#=================================================================

# All import statements needed are below in the individual modules.

# Below is the link to the description of this assignment.

COURSE = "https://class.coursera.org/interactivepython2-009/"
DESCRIPTION = COURSE + "human_grading/view/courses/975652/assessments/35/submissions"

#-----------------------------------------------------------------
## Provided template examples-ricerocks_template.py

# # implementation of Spaceship - program template for RiceRocks
# import simplegui
# import math
# import random

# # globals for user interface
# WIDTH = 800
# HEIGHT = 600
# score = 0
# lives = 3
# time = 0
# started = False

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
# # .ogg versions of sounds are also available, just replace .mp3 by .ogg
# soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
# missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
# missile_sound.set_volume(.5)
# ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
# explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# # helper functions to handle transformations
# def angle_to_vector(ang):
    # return [math.cos(ang), math.sin(ang)]

# def dist(p, q):
    # return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# # Ship class
# class Ship:

    # def __init__(self, pos, vel, angle, image, info):
        # self.pos = [pos[0], pos[1]]
        # self.vel = [vel[0], vel[1]]
        # self.thrust = False
        # self.angle = angle
        # self.angle_vel = 0
        # self.image = image
        # self.image_center = info.get_center()
        # self.image_size = info.get_size()
        # self.radius = info.get_radius()
        
    # def draw(self,canvas):
        # if self.thrust:
            # canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]] , self.image_size,
                              # self.pos, self.image_size, self.angle)
        # else:
            # canvas.draw_image(self.image, self.image_center, self.image_size,
                              # self.pos, self.image_size, self.angle)
        # # canvas.draw_circle(self.pos, self.radius, 1, "White", "White")

    # def update(self):
        # # update angle
        # self.angle += self.angle_vel
        
        # # update position
        # self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        # self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

        # # update velocity
        # if self.thrust:
            # acc = angle_to_vector(self.angle)
            # self.vel[0] += acc[0] * .1
            # self.vel[1] += acc[1] * .1
            
        # self.vel[0] *= .99
        # self.vel[1] *= .99

    # def set_thrust(self, on):
        # self.thrust = on
        # if on:
            # ship_thrust_sound.rewind()
            # ship_thrust_sound.play()
        # else:
            # ship_thrust_sound.pause()
       
    # def increment_angle_vel(self):
        # self.angle_vel += .05
        
    # def decrement_angle_vel(self):
        # self.angle_vel -= .05
        
    # def shoot(self):
        # global a_missile
        # forward = angle_to_vector(self.angle)
        # missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        # missile_vel = [self.vel[0] + 6 * forward[0], self.vel[1] + 6 * forward[1]]
        # a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound)
    
    
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
        # canvas.draw_image(self.image, self.image_center, self.image_size,
                          # self.pos, self.image_size, self.angle)

    # def update(self):
        # # update angle
        # self.angle += self.angle_vel
        
        # # update position
        # self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        # self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
  
        
# # key handlers to control ship   
# def keydown(key):
    # if key == simplegui.KEY_MAP['left']:
        # my_ship.decrement_angle_vel()
    # elif key == simplegui.KEY_MAP['right']:
        # my_ship.increment_angle_vel()
    # elif key == simplegui.KEY_MAP['up']:
        # my_ship.set_thrust(True)
    # elif key == simplegui.KEY_MAP['space']:
        # my_ship.shoot()
        
# def keyup(key):
    # if key == simplegui.KEY_MAP['left']:
        # my_ship.increment_angle_vel()
    # elif key == simplegui.KEY_MAP['right']:
        # my_ship.decrement_angle_vel()
    # elif key == simplegui.KEY_MAP['up']:
        # my_ship.set_thrust(False)
        
# # mouseclick handlers that reset UI and conditions whether splash image is drawn
# def click(pos):
    # global started
    # center = [WIDTH / 2, HEIGHT / 2]
    # size = splash_info.get_size()
    # inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    # inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    # if (not started) and inwidth and inheight:
        # started = True

# def draw(canvas):
    # global time, started
    
    # # animiate background
    # time += 1
    # wtime = (time / 4) % WIDTH
    # center = debris_info.get_center()
    # size = debris_info.get_size()
    # canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    # canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    # canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # # draw UI
    # canvas.draw_text("Lives", [50, 50], 22, "White")
    # canvas.draw_text("Score", [680, 50], 22, "White")
    # canvas.draw_text(str(lives), [50, 80], 22, "White")
    # canvas.draw_text(str(score), [680, 80], 22, "White")

    # # draw ship and sprites
    # my_ship.draw(canvas)
    # a_rock.draw(canvas)
    # a_missile.draw(canvas)
    
    # # update ship and sprites
    # my_ship.update()
    # a_rock.update()
    # a_missile.update()

    # # draw splash screen if not started
    # if not started:
        # canvas.draw_image(splash_image, splash_info.get_center(), 
                          # splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          # splash_info.get_size())

# # timer handler that spawns a rock    
# def rock_spawner():
    # global a_rock
    # rock_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
    # rock_vel = [random.random() * .6 - .3, random.random() * .6 - .3]
    # rock_avel = random.random() * .2 - .1
    # a_rock = Sprite(rock_pos, rock_vel, 0, rock_avel, asteroid_image, asteroid_info)
            
# # initialize stuff
# frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# # initialize ship and two sprites
# my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
# a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, .1, asteroid_image, asteroid_info)
# a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)


# # register handlers
# frame.set_keyup_handler(keyup)
# frame.set_keydown_handler(keydown)
# frame.set_mouseclick_handler(click)
# frame.set_draw_handler(draw)

# timer = simplegui.create_timer(1000.0, rock_spawner)

# # get things rolling
# timer.start()
# frame.start()

##=================================================================

DIRECTIONS = '''
Overview
----------
For our last project, we will complete the implementation of RiceRocks, an updated
version of Asteroids. You may start with either your code or the template (above).
If you start with your own code, be sure to add the splash screen that you dismiss
with a mouse click before starting the game.

Development
----------
At the end of the project, your game will have multiple rocks and multiple
missiles. You will lose a life if your ship collides with a rock and you will
score points if your missiles collide with rocks. You will keep track of the
score and lives remaining and end the game at the proper time. You may
optionally add animated explosions when there is a collision.

Phase One: Multiple Rocks
----------
Keep a set of rocks and spawn new rocks into this set. 
1.) Remove a_rock and replace with rock_group. Initialize the rock group
    to an empty set. Modify your rock spawner to create a new rock (an
    instances of a Sprite object) and add it to rock_group.
2.) Modify your rock spawner to limit the total num of rocks in the game at
    any one time. We suggest your limit be 12. With too many rocks, the game
    becomes less fun and the animation slows down.
3.) Create a helper function process_sprite_group. This function should take a 
    set and a canvas and call the update and draw methods for each sprite in
    the group.
4.) Call the process_sprite_group function on rock_group in the draw handler.

Phase Two: Collisions
----------
For this phase, you will detect collisions between the ship and a rock. Upon a
collision, the rock should be destroyed and the player should lose a life. To
implement ship-rock collisions, you need to do the following:
1.) Add a collide method to the Sprite class. This should take an other_object as
    an arg and return True if there is a collision or False otherwise. For now, this
    other object will always be your ship, but we want to be able to use this
    collide method to detect collisions with missiles later as well. Collisions
    can be detected using the radius of the two objects. This requires you to
    implment methods get_position and get_radius on both the Sprite and
    Ship classes.
2.) Implement a group_collide helper function. This function should take a
    set group and a sprite other_object and check for collisions between
    other_object and elements of the group. If there is a collision, the colliding
    object should be removed from the group. To avoid removing an object from
    a set that you are iterating over, iterate over a copy of the set created 
    via set(group). This function should return True or False depending
    on whether there was a collision. Be sure to use collide method from
    part 1 on the sprites in the group to accomplish this task.
3.) In the draw handler, use the group_collide helper to determine if the ship
    hit any of the rocks. If so, decrease the number of lives by one. Note that you
    could have negative lives at this point. Don't worry about that yet.
    
At this point, you should have a game of "dodge 'em". You can fly around trying
to avoid the rocks!

Phase Three: Missiles
----------
For this phase, you will keep a set of missiles and spawn new missiles into the
set when firing using the space bar.
1.) Remove a_missile and replace it with missile_group. Initialize the missile
    group to an empty set. Modify your shoot method of my_ship to create a new
    missile (an instance of the Sprite class) and add it to the missile_group. If
    you use our code, the firing sound should play automatically each time a 
    missile is spawned.
2.) In the draw handler, use your helper function process_sprite_group to process
    missile_group. While you can now shoot multiple missiles, you will notice that
    they stick around forever. To fix this, we need to modify the Sprite class and
    the process_sprite_group function.
3.) In the update method of the Sprite class, increment the age of the sprite every
    time update is called. If the age is greater than or equal to the lifespan of the
    sprite, then we want to remove it. So, return False (meaning we want to
    keep it) if the age is less than the lifespan and True (meaning we want to
    remove it) otherwise.
4.) Modify process_sprite_group to check the return value of update for sprites.
    If it returns True, remove the sprite from the group. Again, you will want to
    iterate over a copy of the sprite group in process_sprite_group to avoid
    deleting from the same set over which you are iterating.
    
Phase Four: Collisions Revisited
----------
Now we want to destroy rocks when they are hit by a missile. We can't quite use
group_collide, because we want to check for collisions between two groups. All
we need to do is add one more helper.
1.) Implement a final helper group_group_collide that takes two groups of objects
    as input. It should iterate through the elements of a copy of the first group
    using a for loop and then call group_collide with each of these elements on the
    second group. It should return the number of elements in the first group that
    collide with the second group as well as delete these elements in the first
    group. You may find the discard method for sets to be useful here.
2.) Call group_group_collide in the draw handler to detect missile/rock collisions.
    Increment the score by the number of missile collisions.
    
Phase Five: Finish it Off
----------
1.) Add code to the draw handler such that if the number of lives becomes 0,
    the game is reset and the splash screen appears. In particular, set the flag to
    False, destroy all rocks and prevent any more rocks from spawning.
2.) When the game starts/restarts, make sure the lives and the score are properly
    initialized. Start spawning rocks. Play/restart the background music loaded in
    the variable soundtrack in the program template.
3.) When you spawn rocks, you want to make sure they are some distance away from
    the ship. Otherwise, you can die when a rock spawns on top of you, which isn't
    much fun. One simple way to achieve this effect is to ignore a rock spawn event
    if the spawned rock is too close to the ship. 
4.) Experiment with varying the vel of rocks based on the score to make game play
    more difficult as the game progresses.
5.) Tweak any constants that you have to make the game play the way you want.

Bonus
----------
The following will not be graded, but feel free to try. Implement explosions!
1.) In the draw method of the Sprite class, check if self.animated is True. If so,
    then choose the correct tile in the image based on the age. The image is tiled
    horizontally. If self.animated is False, it should continue to draw the sprite
    as before.
2.) Create an explosion_group global variable and initialize it to an empty set.
3.) In group_collide, if there is a collision, create a new explosion (an instance of
    the Sprite class) and add it to the explosion_group. Make sure that each 
    explosion plays the explosion sound.
4.) In the draw handler, use process_sprite_group to process explosion_group.

Grading
----------
1 pt - The program spawns multiple rocks.
1 pt - The program correctly determines whether the ship collides with a rock.
1 pt - The program removes a rock when the ship collides with a rock.
1 pt - The number of lives decreases by one when the ship collides with a rock.
1 pt - The program spawns multiple missiles.
1 pt - The program plays the firing sound when each missile is spawned.
1 pt - The program removes a missile that does not collide with a rock after some fixed time period.
1 pt - The program correctly determines whether a missile and a rock collide.
1 pt - The program removes missiles and rocks that collide.
1 pt - The score is updated appropriately after missile/rock collisions.
1 pt - When the lives go to zero, the splash screen reappears and all rocks are removed.
1 pt - When the splash screen is clicked, the lives are reset to 3, score is reset to zero and the background music restarts.
1 pt - The game spawns rocks only when the splash screen is not visible and a game is in progress.
'''

##=================================================================

# Since this will be implemented in PyCharm and ported to CodeSkulptor, the 
# individual modules will be written and imported by the main module that 
# contains the RiceRocksGame class which executes all game logic. The modules
# will be separated like so:

"""
RiceRocks
----------
|--Game
|--GUI
|--GlobalConstants
|--GameObjects
|--HelperFunctions
"""

# If a better (i.e. more effective, cleaner, standard, or otherwise more preferred)
# method of splitting up components into modules is discovered during the dev
# stage, it will be used instead of the above. Imported modules will be dependent
# on the environment and enclosed in a try/except statement. Either simplegui
# or SimpleGUICS2Pygame.simpleguics2pygame will be imported, and either will
# be referenced as "simplegui" in the code. The appropriate block of the try/except
# statement will also import either the named modules or the CodeSkulptor
# url components that link to the uploaded versions.

# All development will be done in PyCharm and pasted here.

##=================================================================

"""
Helper Functions
----------
Helper functions for Rice Rocks game.
CodeSkulptor URL: http://www.codeskulptor.org/#user40_BuDGrDEPzC_3.py
"""

import math

__author__ = 'Bob'
__project__ = 'RiceRocks'


def angle_to_vector(ang):
    """
    Returns a spatial vector in a list from an angle in radians.
    """
    return [math.cos(ang), math.sin(ang)]


def euclidean_dist(point_p, point_q):
    """
    Returns the Euclidean distance between points.
    """
    try:
        diffs = []
        for dim in range(len(point_p)):
            diffs.append((point_q[dim] - point_p[dim])**2)
        return math.sqrt(sum(diffs))
    except TypeError("Points must be each an iterable of same length"):
        return


def process_sprite_group(group, canvas):
    """Update and draw on the canvas all sprites in the group."""
    for sprite in set(group):
        if sprite.update():
            group.remove(sprite)
        sprite.draw(canvas)


class ImageInfo:
    """Class to store the size and attributes of an image."""

    def __init__(self, center, size, radius=0, lifespan=None, animated=False, fraction=1):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated
        self.fraction = fraction

    def get_center(self):
        """Return center of image."""
        return self.center

    def get_size(self):
        """Return size of image."""
        return self.size

    def get_radius(self):
        """Return radius of image."""
        return self.radius

    def get_lifespan(self):
        """Return lifespan of image."""
        return self.lifespan

    def get_animated(self):
        """Return True if image is animated, else False."""
        return self.animated

    def get_fraction(self):
        """Return image size fraction."""
        return self.fraction

##=================================================================

"""
Global Constants
----------
Shared global constants for Rice Rocks game.
Art assets created by Kim Lathrop, may be freely re-used in non-commercial projects
Sound assets purchased from sounddogs.com, please do not redistribute
CodeSkulptor URL: http://www.codeskulptor.org/#user40_3n5TO69Eye_3.py
"""

import random
try:
    import simplegui
    from user40_BuDGrDEPzC_3 import ImageInfo  # RRHelpers
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    from RRHelpers import ImageInfo

__author__ = 'Bob'
__project__ = 'RiceRocks'


# Game dimensions and statuses
DIMS = [800, 600]
START = 1
IN_PLAY = 2
WINNER = 3

# Images and associated image info
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_blue = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")
nebula_brown = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_brown.png")
nebula_images = (nebula_blue, nebula_brown)
nebula_image = random.choice(nebula_images)

debris_info = ImageInfo([320, 240], [640, 480])
debris_brown1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris1_brown.png")
debris_brown2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_brown.png")
debris_brown3 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris3_brown.png")
debris_brown4 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris4_brown.png")
debris_blue1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris1_blue.png")
debris_blue2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")
debris_blue3 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris3_blue.png")
debris_blue4 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris4_blue.png")
debris_blend = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris_blend.png")
debris_images = (debris_brown1, debris_brown2, debris_brown3, debris_brown4,
                 debris_blue1, debris_blue2, debris_blue3, debris_blue4, debris_blend)
debris_image = random.choice(debris_images)

splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

smallmissile_info = ImageInfo([5, 5], [10, 10], 3, 40)
missile_shot1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot1.png")
missile_shot2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
bigmissile_info = ImageInfo([10, 10], [20, 20], 7, 40, fraction=0.7)
missile_shot3 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot3.png")

rock_info = ImageInfo([45, 45], [90, 90], 40)
rock_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png")
bigrock_info = ImageInfo([45, 45], [90, 90], 50, fraction=1.25)
bigrock_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_brown.png")
megarock_info = ImageInfo([45, 45], [90, 90], 60, fraction=1.5)
megarock_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
littlerock_info = ImageInfo([45, 45], [90, 90], 30, fraction=0.75)
littlerock_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

rock_explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
rock_explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")
bigrock_explosion_info = ImageInfo([64, 64], [128, 128], 26, 24, True, 1.5)
bigrock_explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_blue.png")
megarock_explosion_info = ImageInfo([64, 64], [128, 128], 26, 24, True, 1.5)
megarock_explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_blue2.png")
ship_explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True, 0.5)
ship_explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_orange.png")

powercell_info = ImageInfo([329, 360], [658, 720], 30, 300, fraction=0.09)
powercell_image = simplegui.load_image("https://dl.dropboxusercontent.com/s/i24vzjpqb2bq9ho/RRpowercell.png?dl=0")
db_info = ImageInfo([1000, 1000], [2000, 2000], 32, 255, fraction=0.03)
db_image = simplegui.load_image("https://dl.dropboxusercontent.com/s/9qdzbbg4h1ily9q/RRnuke.png?dl=0")
shield_info = ImageInfo([349, 360], [698, 720], 34, 222, fraction=0.11)
shield_image = simplegui.load_image("https://dl.dropboxusercontent.com/s/91pkurb6spkha8x/RRshield.png?dl=0")

# Sounds and volume settings
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
soundtrack.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
ship_thrust_sound.set_volume(.5)
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")
explosion_sound.set_volume(.5)

##=================================================================

"""
Game Objects
----------
Sprite superclass and subclasses for all game object types in Rice Rocks game.
CodeSkulptor URL: http://www.codeskulptor.org/#user40_WcrnchrYB7_3.py
"""

import random
try:
    import simplegui
    from user40_3n5TO69Eye_3 import *  # RRGlobalConstants
    from user40_BuDGrDEPzC_3 import *  # RRHelpers
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    from RRGlobalConstants import *
    from RRHelpers import *

__author__ = 'Bob'
__project__ = 'RMC137'


class Sprite:
    """Class to store the game logic for an image."""

    def __init__(self, pos, vel, ang, ang_vel, image, info, sound=None):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.ang = ang
        self.ang_vel = ang_vel
        self.img = image
        self.img_cen = info.get_center()
        self.img_size = info.get_size()
        self.rad = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.fraction = info.get_fraction()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def get_position(self):
        """Return the sprite position."""
        return self.pos

    def get_velocity(self):
        """Return the sprite velocity."""
        return self.vel

    def get_radius(self):
        """Return the sprite radius."""
        return self.rad

    def close_spawn(self, other_sprite, buffer_zone=50):
        """Return True if spawn is close to other sprite, else False."""
        return euclidean_dist(self.pos, other_sprite.get_position()) < \
            self.rad + other_sprite.get_radius() + buffer_zone

    def collides_with(self, other_sprite):
        """Return True if collision with other sprite, else False."""
        return euclidean_dist(self.pos, other_sprite.get_position()) < \
            self.rad + other_sprite.get_radius()

    def update(self):
        """Update instance variables."""
        for idx in range(2):
            self.pos[idx] += self.vel[idx]
            self.pos[idx] %= DIMS[idx]
        self.ang += self.ang_vel
        self.age += 1
        return self.age >= self.lifespan

    def draw(self, canvas):
        """Draw the sprite."""
        if self.animated:
            img_cen = (self.age * self.img_size[0] + self.img_cen[0],
                       self.img_cen[1])
            canvas.draw_image(self.img, img_cen, self.img_size, self.pos,
                              [d * self.fraction for d in self.img_size], self.ang)
        else:
            canvas.draw_image(self.img, self.img_cen, self.img_size, self.pos,
                              [d * self.fraction for d in self.img_size], self.ang)


class Ship(object):
    """Class to store the game logic for the ship."""

    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.ang = angle
        self.ang_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()

        self.power = 100.0
        self.recharge_rate = 0.1
        self.thrust = False
        self.decelerator = 1.5
        self.dampener = 0.02
        self.turnspeed = 0.07
        self.missile_group = set()
        self.missile_image = missile_shot1
        self.missile_info = smallmissile_info

        self.dbcount = 100.0
        self.dbtimer = simplegui.create_timer(50.0, self.death_blossom)
        self.dbtime = 0

    def get_position(self):
        """Return position of ship."""
        return self.pos

    def get_velocity(self):
        """Return velocity of ship."""
        return self.vel

    def get_radius(self):
        """Return radius of ship."""
        return self.radius

    def get_power(self):
        """Return ship power."""
        return self.power

    def get_missile_group(self):
        """Return the missile group set."""
        return self.missile_group

    def get_dbcount(self):
        """Return the death blossom charge."""
        return self.dbcount

    def set_recharge_rate(self, value):
        """Set recharge rate to value."""
        self.recharge_rate = value

    def set_max_power(self):
        """Set power to 100%."""
        self.power = 100.0

    def set_max_dbcount(self):
        """Set death blossom charge to 100%."""
        self.dbcount = 100.0

    def spin_stop(self):
        """Stop angular movement."""
        self.ang_vel = 0

    def spin_left(self):
        """Turn left."""
        self.ang_vel = -self.turnspeed

    def spin_right(self):
        """Turn right."""
        self.ang_vel = self.turnspeed

    def thruster_on(self):
        """Turn thruster on."""
        self.thrust = True
        ship_thrust_sound.play()
        self.image_center[0] = 135

    def thruster_off(self):
        """Turn thruster off."""
        self.thrust = False
        ship_thrust_sound.pause()
        ship_thrust_sound.rewind()
        self.image_center[0] = 45

    def fire(self):
        """Fire a missile."""
        forward = angle_to_vector(self.ang)
        pos = [self.pos[0] + forward[0] * 42, self.pos[1] + forward[1] * 42]
        vel = [self.vel[0] + forward[0] * 12, self.vel[1] + forward[1] * 12]
        self.missile_group.add(Sprite(pos, vel, self.ang, 0, self.missile_image,
                                      self.missile_info, missile_sound))

    def change_missile(self):
        """Change missile image."""
        if not self.dbtimer.is_running():
            if self.missile_image == missile_shot1:
                self.missile_image = missile_shot2
            elif self.missile_image == missile_shot2:
                self.missile_image = missile_shot3
                self.missile_info = bigmissile_info
            elif self.missile_image == missile_shot3:
                self.missile_image = missile_shot1
                self.missile_info = smallmissile_info

    def red_button(self):
        """Fire up the Death Blossom."""
        if self.dbcount == 100.0:
            self.dbtimer.start()

    def death_blossom(self):
        """Show the Ko-Dan armada that YOU run outer space."""
        if self.dbtime >= 60:
            self.dbtime = 0
            self.dbtimer.stop()
        else:
            if self.dbtime == 0:
                self.dbcount = 1.0
                if random.choice([False] * 7 + [True] * 3):
                    self.power = 1.0
                self.dbcount = 1.0
            self.dbtime += 1
            self.fire()
            self.ang += random.randrange(int(.5 * math.pi), int(1.5 * math.pi))

    def update(self):
        """Update attributes."""
        # Update position and motion
        forward = angle_to_vector(self.ang) if self.thrust else [0, 0]
        for idx in range(2):
            self.vel[idx] += forward[idx] / (1 + self.decelerator)
            self.vel[idx] *= 1 - self.dampener
        for idx in range(2):
            self.pos[idx] += self.vel[idx]
            self.pos[idx] %= DIMS[idx]
        self.ang += self.ang_vel

        # Update power
        if self.thrust:
            if self.power - 0.6 > 0:
                self.power -= 0.6
            else:
                self.thruster_off()
        else:
            if self.power + self.recharge_rate <= 100:
                self.power += self.recharge_rate
            else:
                self.power = 100.0

        # Update Death Blossom
        if not self.dbtimer.is_running() and self.dbcount != 100.0:
            if self.dbcount + self.recharge_rate / 4.0 <= 100:
                self.dbcount += self.recharge_rate / 4.0
            else:
                self.dbcount = 100.0

    def draw(self, canvas):
        """Draw the ship."""
        canvas.draw_image(self.image, self.image_center, self.image_size,
                          self.pos, self.image_size, self.ang)

##=================================================================

"""
GUI
----------
User interface for Rice Rocks game.
CodeSkulptor URL: http://www.codeskulptor.org/#user40_5uSis8KtQZ_3.py
"""

import math
try:
    import simplegui
    from user40_WcrnchrYB7_3 import *  # RRGameObjects
    from user40_3n5TO69Eye_3 import *  # RRGlobalConstants
    from user40_BuDGrDEPzC_3 import *  # RRHelpers
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    from RRGameObjects import *
    from RRGlobalConstants import *
    from RRHelpers import *

__author__ = 'Bob'
__project__ = 'RiceRocks'


class RiceRocksGUI(object):
    """Class to store GUI for Rice Rocks game."""

    def __init__(self, game):
        self.game = game
        self.frame = simplegui.create_frame("Rice Rocks", DIMS[0], DIMS[1])
        self.frame.add_label("Press LEFT and RIGHT to turn, UP to thrust.")
        self.frame.add_label("Your ship's thrust power will recharge when not in use.")
        self.frame.add_label("-----")
        self.frame.add_label("Press SPACE to fire a missile, D to fire Death Blossom super weapon.")
        self.frame.add_label("Press DOWN to change missile type.")
        self.frame.add_label("-----")
        self.frame.add_label("Fire Death Blossom when the small bar is red (fully charged).")
        self.frame.add_label("There is a 30% chance its use will deplete your ship's power.")
        self.frame.add_label("-----")
        self.frame.add_label("Quickly collect special items as they appear.")
        self.frame.add_label("Try to beat all 3 levels!")
        self.frame.set_keydown_handler(self.keydown)
        self.frame.set_keyup_handler(self.keyup)
        self.frame.set_mouseclick_handler(self.click)
        self.frame.set_draw_handler(self.draw)
        self.frame.start()

    def keydown(self, key):
        """Handler for keyboard key press."""
        assert isinstance(self.game.ship, Ship), "Object is not a Ship"
        key_down = {
            "left": self.game.ship.spin_left,
            "right": self.game.ship.spin_right,
            "up": self.game.ship.thruster_on,
            "space": self.game.ship.fire,
            "d": self.game.ship.red_button,
            "down": self.game.ship.change_missile
        }
        for k in key_down:
            if key == simplegui.KEY_MAP[k]:
                key_down[k]()

    def keyup(self, key):
        """Handler for keyboard key up."""
        assert isinstance(self.game.ship, Ship), "Object is not a Ship"
        key_up = {
            "left": self.game.ship.spin_stop,
            "right": self.game.ship.spin_stop,
            "up": self.game.ship.thruster_off
        }
        for k in key_up:
            if key == simplegui.KEY_MAP[k]:
                key_up[k]()

    def click(self, pos):
        """Handler for mouse click."""
        if self.game.get_status() == START or self.game.get_status() == WINNER:
            self.game.new_game()

    def draw(self, canvas):
        """Handler for drawing on canvas."""
        # Animate the background
        time = self.game.get_time()
        wtime = (time / 4) % DIMS[0]
        center = debris_info.get_center()
        size = debris_info.get_size()
        canvas.draw_image(nebula_image, nebula_info.get_center(),
                          nebula_info.get_size(), [d / 2 for d in DIMS], DIMS)
        canvas.draw_image(debris_image, center, size, (wtime - DIMS[0] / 2,
                          DIMS[1] / 2), DIMS)
        canvas.draw_image(debris_image, center, size, (wtime + DIMS[0] / 2,
                          DIMS[1] / 2), DIMS)

        # Draw/update ship, shield, and sprites
        self.game.process_game_objects(canvas)

        assert isinstance(self.game.ship, Ship), "Not a Ship"
        if self.game.has_shield():
            canvas.draw_circle(self.game.ship.get_position(),
                               self.game.ship.get_radius() + 10, 4,
                               'rgba(0, 255, 255, ' + \
                               str(self.game.get_shield_level()) + ')')

        # Draw lives
        for idx in range(self.game.get_lives()):
            canvas.draw_image(ship_image, [45, 45], ship_info.get_size(),
                              [30 + idx * 42, 30],
                              [d / 2 for d in ship_info.get_size()],
                              math.pi * (3.0 / 2))

        # Draw missile type
        canvas.draw_image(self.game.ship.missile_image,
                          self.game.ship.missile_info.get_center(),
                          self.game.ship.missile_info.get_size(),
                          [DIMS[0] / 2 - 144, 30],
                          [d * 3 for d in self.game.ship.missile_info.get_size()])

        # Draw ship's power and death blossom charge
        canvas.draw_line([DIMS[0] / 2 - 100, 20],
                         [(DIMS[0] / 2 - 100) + 2 * self.game.ship.get_power(), 20],
                         20, "orange")
        dbcolor = "red" if self.game.ship.get_dbcount() == 100.0 else "yellow"
        canvas.draw_line([DIMS[0] / 2 - 100, 40],
                         [(DIMS[0] / 2 - 100) + 2 * self.game.ship.get_dbcount(), 40],
                         6, dbcolor)

        # Draw level
        canvas.draw_text("LEVEL:   " + str(self.game.get_level()), [DIMS[0] / 2 + 130,
                         30], 24, "white")

        # Draw score
        stwid = self.frame.get_canvas_textwidth("SCORE", 32)
        str_score = str(self.game.get_score())
        swid = self.frame.get_canvas_textwidth(str_score, 28)
        canvas.draw_text("SCORE", [DIMS[0] - stwid / 2 - 68, 30],
                         32, "white")
        canvas.draw_text(str_score, [DIMS[0] - swid / 2 - 68, 60],
                         28, "white")

        # Draw splash image
        if self.game.get_status() == START:
            canvas.draw_image(splash_image, splash_info.get_center(),
                              splash_info.get_size(), [d / 2 for d in DIMS],
                              splash_info.get_size())
        elif self.game.get_status() == WINNER:
            winwid1 = self.frame.get_canvas_textwidth("YOU WON!", 56)
            canvas.draw_text("YOU WON!", [DIMS[0] / 2 - winwid1 / 2, DIMS[1] / 3],
                             56, "yellow")
            winwid2 = self.frame.get_canvas_textwidth("Click to start a new game", 36)
            canvas.draw_text("Click to start a new game", [DIMS[0] / 2 - winwid2 / 2,
                             DIMS[1] * (2.0 / 3)], 36, "yellow")

##=================================================================

"""
Rice Rocks
Rice University / Coursera
Intro to Interactive Programming in Python (Part 2)
"""

import math
import random

try:
    import simplegui
    from user40_WcrnchrYB7_3 import *  # RRGameObjects
    from user40_3n5TO69Eye_3 import *  # RRGlobalConstants
    from user40_5uSis8KtQZ_3 import *  # RRGUI
    from user40_BuDGrDEPzC_3 import *  # RRHelpers
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    from RRGameObjects import *
    from RRGlobalConstants import *
    from RRGUI import *
    from RRHelpers import *

__author__ = 'Bob'
__project__ = 'RiceRocks'


class RiceRocksGame(object):
    """Class for Rice Rocks game logic."""

    def __init__(self):
        self.lives = 3
        self.score = 0
        self.time = 1
        self.status = START
        self.level = 1

        self.rock_spawntime = 1000.0
        self.rock_timer = simplegui.create_timer(self.rock_spawntime,
                                                 self.rock_spawner)
        self.rock_group = set()
        self.max_rocks = 12
        self.rminvel = 1
        self.rmaxvel = 3
        self.rminangvel = 10
        self.rmaxangvel = 14
        self.explosion_group = set()

        self.ship = Ship([DIMS[0] / 2, DIMS[1] / 2], [0, 0], 0, ship_image, ship_info)
        self.shield = True
        self.shield_level = 1.0

        self.item_group = set()

    def get_lives(self):
        """Return number of lives."""
        return self.lives

    def get_score(self):
        """Return current score."""
        return self.score

    def get_time(self):
        """Return the current time."""
        return self.time

    def get_status(self):
        """Return the game status."""
        return self.status

    def get_level(self):
        """Return the game level."""
        return self.level

    def has_shield(self):
        """Return True if ship has shield, else False."""
        return self.shield

    def get_shield_level(self):
        """Return shield level (alpha value)."""
        return self.shield_level

    def rock_spawner(self):
        """Spawn a rock."""
        if len(self.rock_group) < self.max_rocks:
            # Choose asteroid based on level
            asteroid_image = rock_image
            asteroid_info = rock_info

            if self.level == 2:
                asteroid_image = bigrock_image
                asteroid_info = bigrock_info
            elif self.level == 3:
                asteroid_image = megarock_image
                asteroid_info = megarock_info

            # Randomize asteroid parameters
            pos = [random.randrange(0, DIMS[0]), random.randrange(0, DIMS[1])]
            direction = [random.choice([-1, 1]), random.choice([-1, 1])]
            vel = [0, 0]
            vel[0] = random.randrange(self.rminvel, self.rmaxvel + 1) * direction[0]
            vel[1] = random.randrange(self.rminvel, self.rmaxvel + 1) * direction[1]
            ang = random.randrange(0, int(2 * math.pi))
            angdir = random.choice([-1, 1])
            angvel = random.randrange(self.rminangvel,
                                      self.rmaxangvel) / float(100) * angdir
            rock = Sprite([pos[0], pos[1]], [vel[0], vel[1]], ang, angvel,
                          asteroid_image, asteroid_info)
            if not rock.close_spawn(self.ship):
                self.rock_group.add(rock)

    def add_explosion(self, pos, rock=True, vel=(0, 0)):
        """Add an explosion at the position of the other object."""
        explosion_image = rock_explosion_image if rock else ship_explosion_image
        explosion_info = rock_explosion_info if rock else ship_explosion_info
        explosion = Sprite(pos, vel, 0, 0, explosion_image, explosion_info,
                           explosion_sound)
        self.explosion_group.add(explosion)

    def spawn_item(self, item_type):
        """Add a special item to the group."""
        image, info = None, None
        if item_type == "powercell":
            image = powercell_image
            info = powercell_info
        elif item_type == "db":
            image = db_image
            info = db_info
        elif item_type == "shield":
            image = shield_image
            info = shield_info

        pos = [random.randrange(0, DIMS[0]), random.randrange(0, DIMS[1])]
        direction = [random.choice([-1, 1]), random.choice([-1, 1])]
        vel = [0, 0]
        vel[0] = random.randrange(4) * direction[0]
        vel[1] = random.randrange(4) * direction[1]
        self.item_group.add(Sprite(pos, vel, 0, 0, image, info))

    def use_item(self, radius):
        """Add special item ability to ship."""
        if radius == 30:
            self.ship.set_max_power()
        elif radius == 32:
            self.ship.set_max_dbcount()
        elif radius == 34:
            self.shield = True
            self.shield_level = 1.0

    def process_game_objects(self, canvas):
        """Update and draw game objects, check for collisions, update
        game attributes based on score."""
        # Increment time
        self.time += 1

        # Update/draw game objects
        self.ship.update()
        self.ship.draw(canvas)
        process_sprite_group(self.item_group, canvas)
        process_sprite_group(self.rock_group, canvas)
        missile_group = self.ship.get_missile_group()
        process_sprite_group(missile_group, canvas)
        process_sprite_group(self.explosion_group, canvas)

        # Check for rock/ship collision
        for rock in set(self.rock_group):
            if rock.collides_with(self.ship):
                self.rock_group.discard(rock)
                self.add_explosion(rock.get_position())
                self.add_explosion(self.ship.get_position(), False,
                                   self.ship.get_velocity())
                if self.shield:
                    self.shield_level -= 0.5
                    if self.shield_level < 0.5:
                        self.shield = False
                else:
                    self.lives -= 1
                if self.lives == 0: self.end_game()

        # Check for rock/missile collision
        little_group = set()
        for missile in set(missile_group):
            for rock in set(self.rock_group):
                if missile.collides_with(rock):
                    missile_group.discard(missile)
                    self.score += 10
                    self.update_score_conditions()
                    self.rock_group.discard(rock)
                    self.add_explosion(rock.get_position())
                    if rock.get_radius() == 60:
                        pos = rock.get_position()
                        vel = [v / 3 for v in rock.get_velocity()]

                        ang1 = random.randrange(int(math.pi))
                        fwd1 = angle_to_vector(ang1)
                        littlerock1 = Sprite(pos, [vel[0] + fwd1[0], vel[1] + fwd1[1]],
                                             ang1, 0.4, littlerock_image,
                                             littlerock_info)
                        little_group.add(littlerock1)

                        ang2 = random.randrange(int(math.pi), int(2 * math.pi))
                        fwd2 = angle_to_vector(ang2)
                        littlerock2 = Sprite(pos, [vel[0] + fwd2[0], vel[1] + fwd2[1]],
                                             ang2, 0.5, littlerock_image,
                                             littlerock_info)
                        little_group.add(littlerock2)

        for rock in little_group:
            self.rock_group.add(rock)

        # Check for ship/item collision
        for item in set(self.item_group):
            if item.collides_with(self.ship):
                self.item_group.remove(item)
                self.use_item(item.get_radius())

        # Spawn items at regular intervals based on level
        self.update_level_conditions()

    def update_score_conditions(self):
        """Update game conditions based on score."""
        if self.score == 3000:
            self.end_game(True)
        elif self.score == 2000:
            if self.lives < 5: self.lives += 1
            self.level = 3
            self.rock_spawntime = 100.0
            self.rminvel = 4
            self.rmaxvel = 6
            self.ship.set_recharge_rate(0.3)
        elif self.score == 1000:
            if self.lives < 5: self.lives += 1
            self.rock_spawntime = 200.0
            self.rminvel = 3
            self.rmaxvel = 5
            self.ship.set_recharge_rate(0.2)
        elif self.score == 500:
            if self.lives < 5: self.lives += 1
            self.level = 2
            self.rock_spawntime = 750.0
            self.rminvel = 2
            self.rmaxvel = 4
        elif self.score == 250:
            self.spawn_item("db")
            self.rock_spawntime = 900.0

    def update_level_conditions(self):
        """Spawn items based on level."""
        intervals = {
            1: {"powercell": 1200, "db": 2400, "shield": 3600},
            2: {"powercell": 2400, "db": 3600, "shield": 2700},
            3: {"powercell": 3600, "db": 4800, "shield": 1800}
        }
        if self.time % intervals[self.level]["powercell"] == 0:
            self.spawn_item("powercell")
        if self.time % intervals[self.level]["db"] == 0:
            self.spawn_item("db")
        if self.time % intervals[self.level]["shield"] == 0:
            self.spawn_item("shield")

    def end_game(self, won_game=False):
        """End game and reset variables."""
        for r in set(self.rock_group):
            self.add_explosion(r.get_position())
        self.status = WINNER if won_game else START
        self.level = 1
        self.rock_timer.stop()
        self.rock_spawntime = 1000.0
        self.rock_group = set()
        self.rminvel = 1
        self.rmaxvel = 3
        soundtrack.pause()
        soundtrack.rewind()

    def new_game(self):
        """Start a new game."""
        self.time = 1
        self.lives = 3
        self.score = 0
        self.status = IN_PLAY
        self.ship = Ship([DIMS[0] / 2, DIMS[1] / 2], [0, 0], 0, ship_image, ship_info)
        self.shield = True
        self.shield_level = 1.0
        self.rock_timer.start()
        soundtrack.play()
        self.item_group = set()


RiceRocksGUI(RiceRocksGame())

##=================================================================
##=================================================================