# i = 0

# while i < 3: # as long as this condition is True
#     print('Hi')
#     i += 1

# for i in range(3):
#     print('Hi')

# calculate the sum of integers from 0 - 10:

total = 0

for i in range(10+1):
    print(f'Iteration {i}:')
    print(f'    before adding {i}, the current total is {total}')
    total += i
    print(f'    after adding {i}, the total beomes {total}')
    print()


print(total)

# # repeat asking user to enter password until it is correct

while True:
    password = input('Enter your password: ')
    if password == '123456':
        print('Welcome!')
        break
    else:
        print('Wrong! Please enter again')