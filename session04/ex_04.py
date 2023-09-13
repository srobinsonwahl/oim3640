# 4. Create a program that prompts the user to input two integers, then calculates and prints the sum, difference, product, quotient, and exponentiation of the integers in the format of mathematical equations.

integer_one = int(input('Please enter an integer:'))
integer_two = int(input('Please enter an integer again:'))

add = integer_one + integer_two
subtract = integer_one - integer_two
multiply = integer_one * integer_two
divide = integer_one / integer_two
exponent = integer_one ** integer_two

print(f'{integer_one} + {integer_two} = {add}')
print(f'{integer_one} - {integer_two} = {subtract}')
print(f'{integer_one} * {integer_two} = {multiply}')
print(f'{integer_one} / {integer_two} = {divide}')
print(f'{integer_one} ^ {integer_two} = {exponent}')