def any_uppercase(s):
    for c in s:
        if c.isupper():
            return True
        else:
            return False
        
print(any_uppercase('iPhone'))
print(any_uppercase('Babson'))
print(any_uppercase('NBA'))

def any_uppercase3(s):
    for c in s:
        flag = c.isupper()
    return flag

print(any_uppercase3('iPhone'))
print(any_uppercase3('Babson'))
print(any_uppercase3('NBA'))

def any_uppercase4(s):
    flag = False
    for c in s:
        flag = flag or c.isupper()
    return flag

print(any_uppercase4('iPhone'))
print(any_uppercase4('Babson'))
print(any_uppercase4('NBA'))

def any_uppercase5(s):
    for c in s:
        if not c.isupper():
            return False
    return True

print(any_uppercase5('iPhone'))
print(any_uppercase5('Babson'))
print(any_uppercase5('NBA'))

def any_uppercase6(s):
    for c in s:
        if c.isupper():
            break
            return True
    return False

print(any_uppercase6('iPhone'))
print(any_uppercase6('Babson'))
print(any_uppercase6('NBA'))