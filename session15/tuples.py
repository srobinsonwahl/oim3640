t = 'a', 'b', 'c', 'd', 'e'
t = ('a', 'b', 'c', 'd', 'e')

t1 = 'a',
print(type(t1))

t = tuple('babson')
print(t)

t = ('a', 'b', 'c', 'd', 'e')
print(t[0])
print(t[1:3])

# t[0] = 'a'
# print(t)

t = ('A',) + t[1:]
print(t)

# Tuple Assignment

a = 10
b = 90
temp = a
a = b
b = temp
print(a, b)

a, b = b, a

email = 'srobinsonwahl1@babson.edu'
id, domain = email.split('@')
print(id)
print(domain)

t = divmod(7, 3)
print(t)

# Variable-length argument tuples

def printall(*args):
    print(args)

printall(1, 2.0, '3')
printall(1, 2.0, '3', None, True)

t = (7, 3)
print(divmod(*t))

# Lists and Tuples
s = 'abc'
t = [0, 1, 2]
zip(s, t)
print(zip(s, t))

for pair in zip(s, t):
    print(pair)

print(list(zip(s, t)))

def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

print(has_match('123', '32a'))
print(has_match('125', '39a'))

for index, element in enumerate('abc'):
    print(index, element)

# Dictionaries and Tuples:

d = {'a':0, 'b':1, 'c':2}
t = d.items()
print(t)

for key, value in d.items():
    print(key, value)

# Sequences of Sequences:

