grades = dict()
print(grades)

grades['John'] = 90
print(grades)

grades = {'John': 90, 'Paul': 75, 'George': 85}
print(grades)

print(grades['Paul'])
# print(grades['Ringo'])

print(len(grades))

l = 'Paul' in grades
print(l)

f = 90 in grades.values()
print(f)

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('Bookkeeper')
print(h)

# Get Method - Takes a key and default value. if the key appears in the dictionary, get returns the corresponding value; otherwise it returns the default value, for example:

number_of_e = h.get('e', 0)
number_of_a = h.get('a', 0)
print(number_of_e)
print(number_of_a)

# Looping and Dictionaries:

def print_hist(h):
    for c in h:
        print(c, h[c])

h = histogram('Massachusetts')
print_hist(h)

for key in sorted(h):
    print(key, h[key])

# Reverse Lookup:
# Given a dictionary d and a key k, it is easy to find the corresponding value, v = d[k]. This operation is called a lookup. But what if you have v and you want to find k?

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('value does not appear in the dictionary')

h = histogram('Massachusetts')
key = reverse_lookup(h, 2)
print(key)

# Dictionaries and lists:
# Lists can appear as values in an dictionary. To invert a dictionary:

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

hist = histogram('parrot')
print(hist)
inverse = invert_dict(hist)
print(inverse)


# Memos:

known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]
    
    res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res

for i in range(10):
    print(fibonacci(i), end = ", ")