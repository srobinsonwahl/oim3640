# 1. Play with functions round(), min(), ord(), chr(). Read documentation.

a = round(78.89)
print(f'This function returns a given integer rounded to the nearest whole number, here it\'s: {a}.')

b = min(92, 54, 25)
print(f'This function returns the minimum value in a given argument, here it\'s {b}.')

c = ord('J')
print(f'This function returns the unicode value for a given character, here it\'s: {c}.')

d = chr(65)
print(f'This function returns the character for a given unicode value, here it\'s: {d}.')

# 2. From the documentation of math module, pick up two functions and play with them.

import math

a = math.ceil(48.327289)
print(f'This function returns the ceiling of a given float, here it\'s: {a}.')

# 3. Define a function to print the absolute value of any given number.

def my_abs_3(a):
    """

    prints the absolute value of any given number
    """
    if a < 0:
        print(-a)
    else:
        print(a)

my_abs_3(-20)
my_abs_3(10)

# 4. Modify the function my_abs_3 to return the absolute value of any number.

def my_abs_4(a):
    """

    returns the absolute value of any given number
    """
    if a < 0:
        return -a
    else:
        return a

print(5 + my_abs_4(8))
print(5 + my_abs_4(-8))

# 5. Modify the function my_abs_3 to first only allow integers and floating numbers, then return the absolute value of any number. You may need a built-in function isinstance().

b = 'test'
def my_abs_5(a):
    """
    
    returns the absolute value of any integer or floating number
    """
    if isinstance(a, int) or isinstance(a, float):
        if a < 0:
           return -a
        else:
           return a
    else:
        print('This function does not support chracters other than integers or floating numbers.')

my_abs_5(b)
print(my_abs_5(70))
print(my_abs_5(-50))

# 6. Define a function quadratic(a, b, c) to solve a quadratic equation and return the values of two roots

def quadratic(a, b, c):
    """
    
    returns the values of two roots of any given value a, b, and c in the quadratic equation
    """
    unknown_1 = ((-b + ((b ** 2 - 4 * (a * c)) ** 0.5)) / 2 * a)
    unknown_2 = ((-b - ((b ** 2 - 4 * (a * c)) ** 0.5)) / 2 * a)
    return unknown_1, unknown_2

a = 1
b = 7
c = 12

print(f'The roots for these a, b, and c values are: {quadratic(a, b, c)}')