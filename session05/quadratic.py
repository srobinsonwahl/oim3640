# If this reads as copy/paste it's because I originally wrote the function in the 'myabs.py' file.

# 6. Define a function quadratic(a, b, c) to solve a quadratic equation and return the values of two roots

def quadratic(a, b, c):
    """
    (docstring)
    
    returns the values of two roots of any given value a, b, and c in the quadratic equation
    """
    unknown_1 = ((-b + ((b ** 2 - 4 * (a * c)) ** 0.5)) / 2 * a)
    unknown_2 = ((-b - ((b ** 2 - 4 * (a * c)) ** 0.5)) / 2 * a)
    return(unknown_1, unknown_2)

a = 1
b = 7
c = 12

print(f'The roots for these a, b, and c values are: {quadratic(a, b, c)}')