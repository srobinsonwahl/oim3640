import math
import pandas as pd

def mysqrt(a):
    x = 4
    epsilon = 0.0000001
    while True:
        print(x)
        y = (x + a/x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return x

# Utilized pandas documentation and w3schools to help with this:

def test_square_root():
    data = []

    for a in range(1, 10):
        my_sqrt_result = mysqrt(a)
        math_sqrt_result = math.sqrt(a)
        diff = abs(my_sqrt_result - math_sqrt_result)
        data.append([a, my_sqrt_result, math_sqrt_result, diff])

    df = pd.DataFrame(data, columns = ["a", "mysqrt(a)", "math.sqrt(a)", "diff"])
    print(df)

test_square_root()