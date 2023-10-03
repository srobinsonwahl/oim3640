# 2). Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

def count(word = 'stephen', letter = 'e'):
    x = 0
    for c in word:
        if c == letter:
            x += 1
    print(x)

count()