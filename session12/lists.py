[10, 20, 30, 40]
['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']

# the elements of a list don't have to be the same type
# A list within another list is nested
['spam', 2.0, 5, [10, 20]]

AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
numbers = [42, 123]
empty = []
print(AFC_east, numbers, empty)

# Lists are Mutable
AFC_east[3] = 'New York Giants'
print(AFC_east)

# What is the index of 'apple'? 'Lisa'? 'On Rail'?
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby', 'On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']    
    ]

# Traversing a List:

for team in AFC_east:
    print(team)

numbers = [2, 0, 1, 6, 9]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)

my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(my_list))

# List operations:
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

print([0] * 4)

print(['Tom Brady', 'Bill Belichick'] * 3)

# List Slices:

t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
print(t[:-2])
print(t[3:])
print(t)

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)

