# Python Programs : modules > statements > expressions > objects
#  1. Programs are composed of modules
#  2. Modules contain statements
#  3. Statements contain expressions
#  4. Expressions create and process objects

# NUMBERS:

# Integers have no fractional part
# Floating-point numbers have fractional part

3.14e-2     # Scientific notation

123 + 222   # Integer addition

1.5 * 4     # Floating-point multiplication

2 ** 100    # 2 to the power 100

len(str(2 ** 1000000))  # How many digits in a really BIG number?

import math
print(math.pi)
print(math.sqrt(85))

import random
print(random.random())
random.choice([1, 2, 3, 4])

# STRINGS:

# If there is a quotation mark in the string, use the backslash
print('I\'m \"ok\".')   # use backslash for quotation marks inside strings
print('I\'m learning\nPython.')
print('\\\n\\')

# We could use r'' to avoid the escape character
print('\\\t\\')
print(r'\\\t\\')

# Instead of \n, we could use '''...''' to display multiple lines
print('''line1
... line 2
... line3''')

# BOOLEAN:

# Either true or false
True
False
3 > 2
3 > 5

# Logical operators: and, or, not
# and
True and True
True and False
False and False
5 > 3 and 3 > 1

# or
True or True
True or False
False or False
5 > 3 or 1 > 3

# not
not True
not False
not 1 > 2

# we often use Boolean type in conditional statements:
age = int.input('Please enter your age in years:')
if age >= 21:
    print('Yes, you can.')
else:
    print('Sorry.')

# General Rule: arithmetic > comparison > not > and/or
5 * 7 >= 3 +5 * (7 - 1) and not False
35 >= 3 + 5 * 6 and not False
35 >= 3 + 30 and not False
35 >= 33 and not False
True and not False
True and True
True

# NONETYPE:

# The sole value of the type NoneType, None, is frequently used to represent the absense of a value, as when default arguments ar enot passed to a function.