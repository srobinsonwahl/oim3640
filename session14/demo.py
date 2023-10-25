def histogram(s):
    """
    return a dict, key is letter and value is frequency
    """
    d = {}
    for letter in s:

    #     if letter not in d:
    #         d[letter] = 1
    #     else:
    #         d[letter] += 1

        d[letter] = d.get(letter, 0) + 1
    return d

print(histogram('Larry'))