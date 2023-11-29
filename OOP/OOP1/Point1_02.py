class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

    def __init__(self, x=0, y=0):
        """Initialize a Point object with given x and y, also called constructor"""
        self.x = x
        self.y = y

    def __str__(self):
        """Return a human-readable representation of the object"""
        # (1, 2)
        return f"({self.x}, {self.y})"

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    # def distance_to(self, other_point):
    #     return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def __add__(self, other):
        """
        overload the plus operator +
        return a new point object
        """
        result = Point()
        result.x = self.x + other.x
        result.y = self.y + other.y
        return result
    
    def __sub__(self, other):
        """
        overload the subtract operator - 
        """
        result = Point()
        result.x = self.x - other.x
        result.y = self.y - other.y
        return result
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# idea 3
p1 = Point()  # create an object/instance of Point class

# # print(p1.x, p1.y)
# print(p1)
p1.move(1, 1)
# print(p1)


p2 = Point(3, 4)  # create an object/instance of Point class
# print(p2)

p3 = p1 + p2 # This should be 4 5
# print(p3)

p4 = p2 - p1 # This would be 1 1
# print(p4)

# print(p4 == p2)

# print(p2.x, p2.y)


# Define a human character in GTA

class Human:
    def __init__(self, name, age, initial_weapons =[]):
        self.name = name
        self.age = age
        if initial_weapons is None:
            self.weapons = []
        else:
            self.weapons = initial_weapons

    def purchase(self, weapon):
        self.weapons.append(weapon)

    def __contains__(self, weapon):
        """Overload in operator"""
        return weapon in self.weapons
    
    def __iter__(self):
        """"""
        yield 'A weapon'

    def __str__(self):
        return f"{self.name}, age = {self.age}"

    def talk(self):
        if self.age >= 21:
            print(
                f'{self.name} says: "Nice to meet you! I am {self.age} years old! Where is the drink?"'
            )

        else:
            print(f'{self.name} says: "Nice to meet you! I am {self.age} years old!"')


    def __add__(self, other):
        """
        add name
        """

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


ajay = Human("Ajay", 20, initial_weapons=['machine gun', 'shotgun' 'handgun'])
alec = Human("Alec", 21)

ajay.purchase('handgun')

print(alec.weapons)
print('handgun' in ajay)



# print(ajay)
# print(alec)

# ajay.talk()
# alec.talk()
# ajay.greet(alec)


class Superpower(Human):
    """"""
