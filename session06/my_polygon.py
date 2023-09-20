import turtle

t = turtle.Turtle()

# leo = turtle.Turtle()
# leo.fd(100)
# leo.lt(90)
# leo.fd(100)
# leo.lt(90)
# leo.fd(100)
# leo.lt(90)
# leo.fd(100)
# leo.lt(90)

# for i in range(4):
#     leo.fd(100)
#     leo.lt(90)

# Exercise 2:

# 2.1
def square(t):
    """
    This function takes a paremeter named t, which is a turtle. It should use the turtle to draw a square.
    """
    for i in range(4):
        t.fd(100)
        t.lt(90)

# square(leo)

# 2.2
def square(t, length):
    """
    This function takes a paremeter named t, which is a turtle, and another parameter, length, which is a float.. It should use the turtle to draw a square with side length, length.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)

# square(leo, 200)

# 2.3
def polygon(t, length, n):
    """
    This function takes a parameter named t, which is a turtle, and parameter length, which is a float, and parameter n, which is the number of sides of a polygon. It uses the turtle to draw a polygon with n sides of length, length.
    """
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

# polygon(t, 200, 6)

# 2.4
import math
def circle(t, r):
    """
    This function takes a parameter named t, which is a turtle, and r, or the radius of a circle. It uses the turtle to draw a circle with a radius of r.
    """
    n = 50
    length = (2 * math.pi * r) / n
    polygon(t, length, n)

# circle(t, 100)

# 2.5
def arc(t, r, angle):
        arc_length = 2 * math.pi * r * angle / 360
        n = int(arc_length / 3) + 1
        step_length = arc_length / n
        step_angle = angle / n
        for i in range(n):
            t.fd(step_length)
            t.lt(angle)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    """
    takes parameter angle, which determines what fraction of a circle to draw, and radius to draw a circle or portion of circle. Angle is in units of degrees, so when angle=360, arc should draw a complete circle.
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

arc(t, 50, 90)

turtle.mainloop()