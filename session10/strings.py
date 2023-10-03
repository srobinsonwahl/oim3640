# Strings are not like  integers, floats, and booleans. A string is a sequence, which means it is an ordered collection of other values.

team = 'New England Patriots'
letter = team[1]
print(letter)

"""
Q. What's the first letter?

A. The first letter is the 0th letter.
"""

print(team[0])
# print(team[1.5])

# len
# len is a built in function that returns the number of characters in a string:
len(team)

# Q. How do we find the last letter?
last = team[len(team) - 1]
print(last)

last = team[-1]
print(last)

# Traversal with a for loop
"""
lots of computations involve processing a string one character at a time. Often they start at the beginning, select each character in turn, do something to it, and continue until the end. This pattern of processing is called a traversal. One way to write a traversal is with a while loop:
"""

index = 0
while index < len(team):
    letter = team[index]
    print(letter)
    index += 1

for letter in team:
    print(letter)

# String Slicing:
# A segment of a string is called a slice. Selecting a slice is similar to selecting a character:

team = 'New England Patriots'
print(team[0:11])
print(team[12:20])

"""
If you omit the first index (before the colon), the slice starts at the beginning of the string. If you omit the second index, the slice goes to the end of the string:
"""

print(team[:11])
print(team[12:])
print(team[:])

"""
A string slice can take a third index that specifies the "step size"; that is, the number of spaces between successive characters. A step size of 2 means every other character; 3 means every third, etc.
"""

print(team[::2])

# Strings are immmutable

# team = 'New England Patriots'
# team[12:20] = 'Seahawks'
# print(team)

"""
Strings are immutable, this means you can't change an existing string. The best you can do is create a new string that is a variation on the original:
"""

new_team = team[:12] + 'Seahawks'
print(new_team)

# Searching

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find(team, 'E'))

"""
This pattern of computation -- traversing a sequence and returning when we find what we are looking for -- is called a search.
"""

# Looping and counting:

word = 'New England Patriots'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1

print(count)

"""
This program demonstrates another pattern of computation called a counter. The variable count is initialized to 0 and then incremented each time an a is found. When the loop exits, count contains the result -- the total number of a's.
"""

# String Methods:
"""
Strings provide methods that perform a variety of useful operations. A method is similar to a function -- it takes arguments and returns a value -- but the syntax is different. For example, the method upper takes a string and returns a new string with all uppercase letters. 
"""

team = 'New England Patriots'
new_team = team.upper()
print(new_team)

"""
This form of dot notation specifies the name of the method, upper, and the name of the string to apply the method to team. The empty parentheses indicate that this method takes no arguments.

A method call is called an invocation; in the case, we would say we are invoking upper on team.
"""

team = 'New England Patriots'
index = team.find('a')
print(index)
print(team.find('En'))
print(team.find('a', 10))

name = 'bob'
print(name.find('b', 1, 2))

# The in operator
"""
The word in is a boolean operator that takes two strings and returns True if the first appears as a substring in the second
"""

'a' in team
'Boston' in team

def in_both(word1 = 'Meow', word2 = 'Kitten uwu'):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both()