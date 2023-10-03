# 4). For each function describe what the function does (SEE DOCSTRINGS)

def any_lowercase1(s):
    """
    This function takes in a string, s. The function will return True if the FIRST letter in s is lowercase. If not, then it will return False.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False
        
# print(any_lowercase1(s = 'efes'))

def any_lowercase2(s):
    """
    This function takes in a string, s. The function will return True no matter what because it is checking if the string 'c' is lowercase, not the string that you are passing as a parameter.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
        
# print(any_lowercase2('essdfe'))

def any_lowercase3(s):
    """
    This function takes in a string, s. The function will return True if there are ANY lowercase characters in the string. If not, it will return false.
    """
    for c in s:
        flag = c.islower()
    return flag

# print(any_lowercase3('Seee'))

def any_lowercase4(s):
    """
    This function takes in a string, s. The function will return True if there are ANY lowercase characters in the string. If not, it will return False.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# print(any_lowercase4('SuS'))

def any_lowercase5(s):
    """
    This function takes in a string, s. THe function will return True if the string is ALL lowercase. If not, the string will return false. 
    """
    for c in s:
        if not c.islower():
            return False
    return True

# print(any_lowercase5('ssssS'))