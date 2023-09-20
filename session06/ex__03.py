# 1. 1. Write an appropriately general set of functions that can draw shapes as below. Tips: draw 60 squares, turning right 5 degrees after each square.

import turtle
t = turtle.Turtle()

def draw_shape(y, length):
    """
    This function draws a shape with y number of sides, and specified side length, length.
    """
    for i in range(y):
        t.fd(length)
        t.lt(360/y)

# draw_shape(5, 40)

def rot_shape(x, y, length, angle):
    """
    This function draws x number of shapes, with y number of sides, with side length, length, at a rotating angle, angle.
    """
    for i in range(x):
        draw_shape(y, length)
        t.lt(angle)

# rot_shape(60, 4, 100, 5)

# 2. Draw 60 squares, turning 5 degrees after each square and making each successive square bigger. Start at a length of 30 and increment 4 units every square.

def inc_rot_shape(x, y, length, inc_length, angle):
    """
    This function draws x number of shapes with y number of sides with side lengths, length, increasing the side length by inc_length, and rotating the shapes at an angle, angle each additional shape.
    """
    for i in range(x):
        draw_shape(y, length)
        t.lt(angle)
        length += inc_length

# inc_rot_shape(60, 4, 40, 5, 5)

# 3. Write an appropriately general set of functions that can draw shapes as below.

# inc_rot_shape(60, 3, 100, 30, 5)
# Not sure if this is what you were looking for in terms of a function that can draw shapes like the image listed in problem #3. There are no specific angle degreesw or number of shapes listed in the problem.

# 4. Write an appropriately general set of functions that can draw any other kind of spiral, such as an Archimedian spiral.
import math

def circle(t, r):
    """
    This function draws a circle with a turtle t, with a radius, r.
    """
    n = 360
    for i in range(n):
        t.fd(2 * math.pi * r / n)
        t.lt(360/n)
    
# circle(t, 10)
# t.lt(90)
# t.fd(200)
 
def const_spiral(t, r, x, y):
    """
    This function draws a spiral of constant widening, with turtle t, beginning with a radius, r. Increasing x increases distance between loops, y defines the number of loops within the spiral.
    """
    for i in range(y):
        n = 50
        for i in range(n):
            t.fd(2 * math.pi * r / n)
            t.lt(360/n)
            r = r + x
    
# const_spiral(t, 10, .1, 400)

def inc_spiral(t, r, x, y):
    """
    This function draws a spiral of exponential widening, with turtle t, beginning with a radius, r. Increasing x increases distance between loops, y defines the number of loops within the spiral.
    """
    for i in range(y):
        n = 50
        for i in range(n):
            t.fd(2 * math.pi * r / n)
            t.lt(360/n)
            r = r * x

# inc_spiral(t, 10, 1.01, 5)

turtle.mainloop()