# define a class to represent fractional number

# 1.5  
# 3/2

class Fraction:
    """
    attributes:
        numerator (x): int
        denominator (y): int
    
    Methods:
        __init__, __str__
        __add__, __sub__
    """

    def __init__(self, a, b):
        """"""
        if b == 0:
            raise ZeroDivisionError('Denominator cannot be 0')

        # represent the fraction number in a reduced format

        import math

        gcd = math.gcd(a, b)
        if gcd > 1:
            a //= gcd
            b //= gcd

        self.x = a
        self.y = b

    def __str__(self):
        """Return human readable representation of this fraction object"""
        return f'{self.x:^3}\n---\n{self.y:^3}'
    
    def __add__(self, other):
        """Overload + operator"""
        new_x = self.x * other.y + other.x * self.y
        new_y = self.y * other.y
        return Fraction(new_x, new_y)
    
    def __sub__(self, other):
        """Overload - operator"""
        new_x = self.x * other.y - other.x * self.y
        new_y = self.y * other.y
        return Fraction(new_x, new_y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        # return self.to_float() == other.to_float()
        # diff = self - other
        # return diff.x == 0
    
    def to_float(self):
        return self.x / self.y
    
    # def __mul__(self, other):
    #     """"""
    #     if isinstance(other, int):
    #         pass
    #     if isinstance(other, Fraction):
    #         pass
        

        


frac_1 = Fraction(3, 2)
print(frac_1)
frac_2 = Fraction(1, 3)

print(frac_1 + frac_2) # 11/6
print(frac_1 - frac_2) # 7/6
# print(frac_1 * frac_2) # 

frac_3 = Fraction(6, 4)
print(frac_3)
print(frac_1 == frac_3)

# try:
#     frac_2 = Fraction(2, 0)
# except ZeroDivisionError as e:
#     print(e)
# print(frac_2)