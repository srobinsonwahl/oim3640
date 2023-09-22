# 2. Write a program, fibonacci.py to compute the Fibonacci number of an integer , n.

def fibo(n):
    """
    This function computes the Fibonacci number of an integer n.
    """
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
    

# print(fibo(12))