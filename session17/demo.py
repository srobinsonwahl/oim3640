d = {'larry': 1, 'rohan': 2, 'Maria': 3}

# Dictionary basics:
print(sum(d.values())) # Sum of values

print(len(d)) # Number of unique keys

for item in d.items(): # Iterating through dictionary
    print(item)

s = []
for word, freq in d.items(): # Sorting through a dict by item by creating a list
    s.append((freq, word))

print(s)
print(sorted(s, reverse=True))

import string

s = 'immanuel%^$#&%' 
print(s.strip(string.punctuation + string.whitespace)) # Altering a text string by stripping
