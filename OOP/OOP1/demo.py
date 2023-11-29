import math

class Point:
    """"
    Represents a point in 2d space
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_between_points(point1, point2):
        """
        takes two points and finds the distance between them
        """
        dx = point2.x - point1.x
        dy = point2.y - point1.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance
    
point_a = Point(2, 3)
point_b = Point(6, 10)

distance = Point.distance_between_points(point_a, point_b)
print(distance)


class Rectangle:
    """"
    Represents a rectangle
    
    attributes: width, height, corner
    """

    def __init__(self, width, height, corner):
        """"""

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

class Circle:
    """
    represents a circle

    attr: center, radius
    """
    
    def __init__(self, center, radius):
        center = Point()
        radius == 5

    def point_in_circle(self, point):
        """
        takes a circle and a point and returns true if point in circle
        """
        point = Point()
        return point in self
    
    def rect_in_circle(self, rect):
        """
        takes a circle and arectangle and returns true if rect in circle
        """
        rect = Rectangle()
        return rect in self
    
    def rect_circle_overlap(self, rect):
        """
        takes a circle and a rect and returns true if corners of rect fall inside circle
        """
        rect = Rectangle()
        return rect in self

Circle.center = Point(3, 4)