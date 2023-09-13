# What we've learned to this point - tedious, multi-step, not scalable
r1 = 20
r2 = 9
r3 = 13

# area_1 = 3.14 * r1 ** 2
# area_2 = 3.14 * r2 ** 2
# area_3 = 3.14 * r3 ** 2

# print(area_1, area_2, area_3)

# How can we do this better?

# radius is parameter variable
def compute_area(radius):
    """
    (docstring, which is the description of this function)

    return the area of a circle with a given radius
    """
    pi = 3.14159
    area = pi * radius ** 2
    # print(area) # just a side effect
    # if the function does not explicitly return value(S), it will return None
    return area

area_1 = compute_area(r1) # r1 is called an argument
area_2 = compute_area(r2)
area_3 = compute_area(r3)
print(area_1)

print(area_1 + area_2 + area_3)

# Define a function that returns the double of a given number
# then call the function

d_1 = 10
d_2 = 20
d_3 = 30

def compute_double(doubleme):
    """
    (docstring)
    returns the double of a given number
    """
    return doubleme * 2

double_1 = compute_double(d_1)
double_2 = compute_double(d_2)
double_3 = compute_double(d_3)

print(double_1, double_2, double_3)

# Calculate the area of the circle with double of a given number as the radius
print(compute_area(compute_double(3)))

# Define a fnuction to print the absolute value of any given number
def my_abs(a):
    if a < 0:
        print(-a)
    else:
        print(a)

my_abs(-10)
