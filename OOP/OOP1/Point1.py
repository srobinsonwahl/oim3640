class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

    def __init__(self, x, y):
        """Initialize a Point object with given x and y"""
        self.x = x
        self.y = y

    def __str__(self):
        """Return a human readable representation of the object"""
        # (1, 2)
        return f'({self.x}, {self.y})'
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy


# # Idea three
# p1 = Point(1, 2) # create an object/instance of Point class


# # print(p1.x, p1.y)
# print(p1)
# p1.move(10, 10)
# print(p1)


# # print(p2.x, p2.y)
# p2 = Point(3, 4) # create an object/instance of Point class
# # print(p2)



class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'{self.name}, age = {self.age}'
    
    def talk(self):
        if self.age >= 21:
            print(f'{self.name} says: "Nice to meet you! I am {self.age} years old! Where is drink?"')
        else:  
            print(f'{self.name} says: "Nice to meet you! I am {self.age} years old!"')

    def greet(self, other):
        print(f'{self.name} says: "Hi, {other.name}!"')

    def rob(self, other):
        """"""

    def shoot(self, other_object, weapon):
        """"""
    
    def ride(self, vehicle):
        """"""


class Weapon:
    """"""

class Vehicle:
    """"""

ajay = Human('Ajay', 20)
alec = Human('Alec', 21)

print(ajay)
print(alec)

ajay.talk()
alec.talk()
ajay.greet(alec)