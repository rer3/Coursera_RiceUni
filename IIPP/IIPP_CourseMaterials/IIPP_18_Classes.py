# Python Test 18
# Classes

# A simple Character class
'''There are 4 methods: the initializer, which sets the fields for each instance
of the class; the string method, which generates a string representing the
desired traits of the class instances; the grab method, which adds an elem
to the inventory field; the get_health method, which returns the value of
the health field.'''

class Character:
    def __init__(self, name, initial_health):
        self.name = name
        self.health = initial_health
        self.inventory = []
        
    def __str__(self):
        s  = "Name: " + self.name
        s += " Health: " + str(self.health)
        s += " Inventory: " + str(self.inventory)
        return s
    
    def grab(self, item):
        self.inventory.append(item)
        
    def get_health(self):
        return self.health
    
def example():
    me = Character("Bob", 20)
    print str(me)
    me.grab("pencil")
    me.grab("paper")
    print str(me)
    print "Health:", me.get_health()
    
example()

## 2D Ball Game
# ball physics code for generic 2D domain
# the functions inside() and normal() encode the shape of the ennvironment

import simplegui
import random
import math

# Canvas size
width = 600
height = 400

# Ball traits
radius = 20
color = "White"

# math helper function - dot product
def dot(v, w):
    return v[0] * w[0] + v[1] * w[1]

class RectangularDomain:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.border = 2

    # return if bounding circle is inside the domain    
    def inside(self, center, radius):
        in_width = ((radius + self.border) < center[0] < 
                    (self.width - self.border - radius))
        in_height = ((radius + self.border) < center[1] < 
                     (self.height - self.border - radius))
        return in_width and in_height

    # return a unit normal to the domain boundary point nearest center
    def normal(self, center):
        left_dist = center[0]
        right_dist = self.width - center[0]
        top_dist = center[1]
        bottom_dist = self.height - center[1]
        if left_dist < min(right_dist, top_dist, bottom_dist):
            return (1, 0)
        elif right_dist < min(left_dist, top_dist, bottom_dist):
            return (-1, 0)
        elif top_dist < min(bottom_dist, left_dist, right_dist):
            return (0, 1)
        else:
            return (0, -1)

    # return random location
    def random_pos(self, radius):
        x = random.randrange(radius, self.width - radius - self.border)
        y = random.randrange(radius, self.height - radius - self.border)
        return [x, y]

    # Draw boundary of domain
    def draw(self, canvas):
        canvas.draw_polygon([[0, 0], [self.width, 0], 
                             [self.width, self.height], [0, self.height]],
                             self.border*2, "Red")
        
class CircularDomain:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        self.border = 2
        
    # return if bounding circle is inside the domain    
    def inside(self, center, radius):
        dx = center[0] - self.center[0]
        dy = center[1] - self.center[1]
        dr = math.sqrt(dx ** 2 + dy ** 2)
        return dr < (self.radius - radius - self.border)

    # return a unit normal to the domain boundary point nearest center
    def normal(self, center):
        dx = center[0] - self.center[0]
        dy = center[1] - self.center[1]
        dr = math.sqrt(dx ** 2 + dy ** 2)
        return [dx / dr, dy / dr]
    
    # return random location
    def random_pos(self, radius):
        r = random.random() * (self.radius - radius - self.border)
        theta = random.random() * 2 * math.pi
        x = r * math.cos(theta) + self.center[0]
        y = r * math.sin(theta) + self.center[1]
        return [x, y]
        
    # Draw boundary of domain
    def draw(self, canvas):
        canvas.draw_circle(self.center, self.radius, self.border*2, "Red")
    
class Ball:
    def __init__(self, radius, color, domain):
        self.radius = radius
        self.color = color
        self.domain = domain
        
        self.pos = self.domain.random_pos(self.radius)
        self.vel = [random.random() + .9, random.random() + .9]
        
    # bounce
    def reflect(self):
        norm = self.domain.normal(self.pos)
        norm_length = dot(self.vel, norm)
        self.vel[0] = self.vel[0] - 2 * norm_length * norm[0]
        self.vel[1] = self.vel[1] - 2 * norm_length * norm[1]
    

    # update ball position
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        if not self.domain.inside(self.pos, self.radius):
            self.reflect()

    # draw
    def draw(self, canvas):
        canvas.draw_circle(self.pos, self.radius, 1, 
                           self.color, self.color)
        

# generic update code for ball physics
def draw(canvas):
    ball.update()
    field.draw(canvas)
    ball.draw(canvas)

field = RectangularDomain(width, height)
# field = CircularDomain([width/2, height/2], 180)
ball = Ball(radius, color, field)
        
frame = simplegui.create_frame("Ball physics", width, height)

frame.set_draw_handler(draw)

frame.start()

## Diffusion
# Particle class example used to simulate diffusion of molecules

import simplegui
import random

# global constants
WIDTH = 600
HEIGHT = 400
PARTICLE_RADIUS = 5
COLOR_LIST = ["Red", "Green", "Blue", "White"]
DIRECTION_LIST = [[1,0], [0, 1], [-1, 0], [0, -1]]


# definition of Particle class
class Particle:
    
    # initializer for particles
    def __init__(self, position, color):
        self.position = position
        self.color = color
        
    # method that updates position of a particle    
    def move(self, offset):
        self.position[0] += offset[0]
        self.position[1] += offset[1]
        
    # draw method for particles
    def draw(self, canvas):
        canvas.draw_circle(self.position, PARTICLE_RADIUS, 1, self.color, self.color)
    
    # string method for particles
    def __str__(self):
        return "Particle with position = " + str(self.position) + " and color = " + self.color


# draw handler
def draw(canvas):
    for p in particle_list:
        p.move(random.choice(DIRECTION_LIST))
    
    for p in particle_list:
        p.draw(canvas)


# create frame and register draw handler
frame = simplegui.create_frame("Particle simulator", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# create a list of particles
particle_list = []
for i in range(100):
    p = Particle([WIDTH / 2, HEIGHT / 2], random.choice(COLOR_LIST))
    particle_list.append(p)

# start frame
frame.start()

## Tiled images
# demo for drawing using tiled images

import simplegui

# define globals for cards
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
SUITS = ('C', 'S', 'H', 'D')

# card sprite - 950x392
CARD_CENTER = (36.5, 49)
CARD_SIZE = (73, 98)
card_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")



# define card class
class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def draw(self, canvas, loc):
        i = RANKS.index(self.rank)
        j = SUITS.index(self.suit)
        card_pos = [CARD_CENTER[0] + i * CARD_SIZE[0],
                    CARD_CENTER[1] + j * CARD_SIZE[1]]
        canvas.draw_image(card_image, card_pos, CARD_SIZE, loc, CARD_SIZE)

# define draw handler        
def draw(canvas):
    one_card.draw(canvas, (155, 90))

# define frame and register draw handler
frame = simplegui.create_frame("Card draw", 300, 200)
frame.set_draw_handler(draw)

# createa card
one_card = Card('S', '6')

frame.start()

## Object creation and use

# Mutation with Aliasing
'''Below, p and r point to the same instance (aliasing).'''

class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_x(self, newx):
        self.x = newx
    
    def get_x(self):
        return self.x

p = Point1(4, 5)
q = Point1(4, 5)
r = p

p.set_x(10)

print p.get_x()
print q.get_x()
print r.get_x()

# Mutation of shared state
'''Both p and q are initialized using the same list of coordinates. When p's
fields are directly mutated, q's fields are mutated as well. This is due to
the self.coords field simply pointing to the list called coordinates. When
p's field is changed, it is really changing the original list, which is also
pointed to by q's field.'''

class Point2:
    def __init__(self, coordinates):
        self.coords = coordinates
    
    def set_coord(self, index, value):
        self.coords[index] = value
    
    def get_coord(self, index):
        return self.coords[index]

coordinates = [4, 5]
p = Point2(coordinates)
q = Point2(coordinates)
r = Point2([4, 5])

p.set_coord(0, 10)

print p.get_coord(0)
print q.get_coord(0)
print r.get_coord(0)


# Objects not sharing state

'''To avoid shared state, a new list must be created, a copy of the 
coordinates list, and this is pointed to by an instance's fields.'''

class Point3:
    def __init__(self, coordinates):
        self.coords = list(coordinates)
    
    def set_coord(self, index, value):
        self.coords[index] = value
    
    def get_coord(self, index):
        return self.coords[index]

coordinates = [4, 5]
p = Point3(coordinates)
q = Point3(coordinates)
r = Point3([4, 5])

p.set_coord(0, 10)

print p.get_coord(0)
print q.get_coord(0)
print r.get_coord(0)

