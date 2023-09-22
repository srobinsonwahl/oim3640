# 3. The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. Write a program, greatest_common_divisor.py to implement this idea recursively. The function gcd() takes in two positive integers and returns one integer.

def gcd(x, y):
    """
    This function takes in two positive integers, x and y, and returns the greatest common divisor of the two integers.
    """
    gcd = 1
    if x % y == 0:
        return y
    for i in range(int(y / 2), 0, -1):

        # finds the common divisor thats not 0, -1, and y/2. Used inspiration from w3resource to come up with this range

        if x % i == 0 and y % i == 0:
            gcd = i
            break 

        # Utilized w3resource tutorial for help with this. If the condition is fulfilled in the for loop, the loop breaks, and the function returns the gcd, if the condition is not fulfilled, it continues to loop until the if statement is true. once it's true, then the loop breaks, and returns the gcd.
        
    return gcd

print(gcd(336, 360))

                