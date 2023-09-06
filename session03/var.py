# Exercise one
print('Hello, please enter your name:')
name = input()
print('Hello, ',name)

# Assignment Statements
message = 'I did something cool today!'
n = 100
pi = 3.14

# Always write statements in .py file

# Expressions and Statements
# Expression = combination of values, variables, and operators. A value
# all by itself is considered an expression, and so is a variable.
# Statement = a unit of code that has an effect, like creating a variable
# or displaying a value

print(n)

# Dynamic Language
a = 123
print(a)
a = 'ABC'
print(a)

# String Operations
first_name = 'John'
last_name = 'Lennon'
print(first_name + last_name)
print('Naah, na na nanana naah, nanana naah, hey Jude.' * 10)

# String Formatting
name = 'world'
print(f'Hello, {name}')

actor = 'Joaquin Phoenix'
year = 2020
movie = 'Joker'
print(f'{actor} wins Best Actor for {movie} at Golden Globes {year}.')

# More f-string formatting
pi = 3.1415926

print(f'Pi equals {pi:.5f}.')
print(f'Pi equals {pi:2.5f}.')
print(f'Pi equals {pi:8.2f}.')

a = 2021

# binary
print(f'{a:b}')

# hexadecimal
print(f"{a:x}")

# octal 
print(f"{a:o}")

# scientific
print(f"{a:e}")

s1 = 'a'
s2 = 'ab'
s3 = 'abc'
s4 = 'abcd'

print(f'{s1:>10}')
print(f'{s2:>10}')
print(f'{s3:>10}')
print(f'{s4:>10}')