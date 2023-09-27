# 1. Calculate the sum of integers from 1 to 10:

total = 0
for i in range(10 + 1):
    total += i
print(f'The sum of all the integers from 1 to 10 is {total}.')


# 2. Calculate the sum of integers from 1 to 1000:

total = 0
for i in range(1, 1000 + 1):
    total += i
print(f'The sum of all the integers from 1 to 1000 is {total}.')


# 3. Calculate the sum of all the odd numbers from 1 to 1000. Then calculate the sum of all the even numbers.

""" Pseudocode:
is i odd
i is odd, add to the previous i
i is not odd, do not add to the previous i
"""

# Odd Numbers
total = 0
for i in range(1, 1000 + 1):
    if i % 2 == 0:
        total -= 0
    else:
        total += i
print(f'The sum of all the odd numbers from 1 to 1000 is {total}.')

# Even Numbers
total = 0
for i in range(1, 1000 + 1):
    if i % 2 == 0:
        total += i
    else:
        total += 0
print(f'The sum of all the even numbers from 1 to 1000 is {total}.')