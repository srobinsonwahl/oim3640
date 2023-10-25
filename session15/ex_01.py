"""
Write a function called sumall that takes any number of arguments and returns their sum.
"""

def sumall(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sumall(4, 3, 4, 23, 3, 55.0))