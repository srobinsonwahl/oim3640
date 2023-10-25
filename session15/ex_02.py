# 1). Write a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at http://en.wikipedia.org/wiki/Letter_frequencies.

def most_frequent(a:str):
    count = {}
    for letter in a:
        count[letter] = count.get(letter, 0) + 1
    
    sorted_count = sorted(count.items())

    print(sorted_count)


most_frequent("sdklfjhaslikuylersvdsdkljfghskljkeruihfkjbvskdjvfghskugevbbrb")