import math

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


def test_square_root():
    print("a\tmysqrt(a)\tmath.sqrt(a)\tdiff")
    
    for a in range(1, 10):
        my_sqrt_result = mysqrt(a)
        math_sqrt_result = math.sqrt(a)
        diff = abs(my_sqrt_result - math_sqrt_result)
        print(f"{a:.1f}\t{my_sqrt_result: <9.6f}\t{math_sqrt_result: <9.6f}\t{diff: <9.6f}")

test_square_root()