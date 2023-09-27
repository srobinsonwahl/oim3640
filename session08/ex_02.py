# 1. Read the following code and answer the questions

print('\nAt iteration 0, the value of count is 12.')
print('At iteration 1, the value of count is 24.')
print('At iteration 2, the value of count is 36.')
print('At iteration 3, the value of count is 48.')
print('At iteration 4, the value of count is 60. \n')


# 2. Read the following code and answer the questions

print('At iteration 0, the value of variable count is 12.')
print('At iteration 1, the value of variable count is 12.')
print('At iteration 2, the value of variable count is 12.')
print('At iteration 3, the value of variable count is 12.')
print('At iteration 4, the value of variable count is 12. \n')


# 3. 

print('The print statement will print 5 times.')
print('The largest value of iteration that will be printed out is 4.')
print('The largest value of the varibale count that will be printed out is 12.')
print('The smallest value of the variable count that will be printed out is 1. \n')

# Using while, rewrite all the loops in Exercise 01:

# 1. Calculate the sum of integers from 1 to 10:

total = 0
i = 0
while i < 10:
    i += 1
    total += i

print(total)

# 2. Calculate the sum of integers from 1 to 1000:

total = 0
i = 0
while i < 1000:
    i += 1
    total += i

print(total)

# 3a. Calculate the sum of all the odd numbers from 1 to 1000.

total = 0
i = 0
while i < 1000:
    i += 1
    if i % 2 == 0:
        total += 0
    else:
        total += i
print(total)

# 3b. Calculate the sum of all the even numbers from 1 to 1000.

total = 0
i = 0
while i < 1000:
    i += 1
    if i % 2 == 0:
        total += i
    else:
        total += 0
print(total)