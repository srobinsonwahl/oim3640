# 1). Write a function that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

def storewords(s):
    openwords = open('data/words.txt')  
    weirdwords = openwords.read()
    words = weirdwords.split()
    t = dict()
    for l in words:
        t[l] = 1
    if s in t:
        return True
    return False
print(storewords('msfsdfs'))

# 2). Write a function named has_duplicates that takes a list as a parameter and returns True if there is any object that appears more than once in the list.

def has_duplicates(s):
    d = dict()
    for item in s:
        d[item] = d.get(item, 0) + 1  
        if d[item] > 1:
            return True

print(has_duplicates([1, 2, 3, 4, 4]))