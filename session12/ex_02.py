# Exercise 2 - List methods

# Append
t = ['a', 'b', 'c']
t.append('d')
print(t)

# Extend
t = ['a', 'b', 'c']
s = ['d', 'e', 'f']
t.extend(s)
print(t)

# Sort
t = [2, 5, 1, 3, 9]
t.sort()
print(t)

# Remove
bad_letter = 'h'
t = ['a', 'h', 'c', 'f', 'e']
t.remove(bad_letter)
print(t)

# Count
count_these = 's'
t = ['d', 's', 'f', 's', 'f', 's', 's', 'e', 'f']
print(t.count(count_these))