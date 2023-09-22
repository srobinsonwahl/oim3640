# 1. Write a function named check_fermat that takes four parameters — a, b, c and n — and checks to see if Fermat’s theorem holds. If n is greater than 2 and  a n +b n =c n , the program should print: “Holy smokes, Fermat was wrong!” Otherwise the program should print:> “No, that doesn’t work.”

def check_fermat(a, b, c, n):
    """
    This function takes four parameters, a, b, c, and n, and checks to see if a^n + b^n = c^n is true.
    """
    equation = (a**n) + (b**n)
    if n > 2 and equation == (c**n):
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn\'t work.')

# check_fermat(1, 1, 1, 3)

# 2. Write another function that prompts the user to input values for a, b, c and n, converts them to integers, and uses check_fermat to check whether they violate Fermat’s theorem

def user_check_fermant():
    """
    This function prompts the user to input values for a, b, c, and n, converts them to integers, and then checks to see if a^n + b^n = c^n is true.
    """
    a = int(input("Input a value for a:"))
    b = int(input("Input a value for b:"))
    c = int(input("Input a value for c:"))
    n = int(input("Input a value for n:"))
    check_fermat(a, b, c, n)

# user_check_fermant()

# 3. Write a function, calculate_bmi that takes two parameters, weight and height, to return BMI value. Write another function, get_bmi_category that prompts user to input values for weight and height, converts them to floats, uses calculate_bmi to calculate BMI value, and returns the corresponding BMI category

def calculate_bmi(weight, height):
    """
    This function takes two parameters, weight and height, and returns a BMI value for these values.
    """
    bmi = 703 * (weight / height ** 2)
    return bmi

# print(calculate_bmi(189, 72))

def get_bmi_category():
    """
    This function prompts the user to input values for weight in lbs, and height in inches, and converts these numbers to floats, calculates BMI with these values, and then returns the bmi category for the provided measurements.
    """
    weight = float(input('Input a value for weight in lbs:'))
    height = float(input('Input a value for height in inches:'))
    bmi = calculate_bmi(weight, height)
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 < bmi < 24.9:
        return 'Normal weight'
    elif 25 < bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obesity'

# print(get_bmi_category())