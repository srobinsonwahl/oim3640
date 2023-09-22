# 1. Write a program, factorial.py to compute a factorial of an integer, n.

def factorial(n):
    """
    This function takes an integer n, and computes the factorial of n. The following sequence represents the factorial: n * (n-1) * (n-2)... * 1
    """
    if n == 1:
        return n
    else: 
        return n * factorial(n - 1)

# print(factorial(5))