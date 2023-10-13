# import os
# print(os.getcwd())


# Assume words.txt is under data folder
# f = open('data/words.txt')
# line = f.readline()
# print(line)


# f = open('data/words.txt')

# number_of_words = 0

# for line in f:
#     word = line.strip()
#     number_of_words += 1

# print(number_of_words)


def find_long_words():
    """
    prints only the words with more than 20 characters
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder

    for line in f:
        word = line.strip()
        if len(word) > 20:
            print(word, len(word))


# find_long_words()


def has_no_e(word):
    """
    returns True if the given word doesn't have the letter "e" in it
    """
    for letter in word:
        if letter == 'e':
           return False 
    return True

    # return 'e' not in word.lower()


# print(has_no_e('Babson'))
# print(has_no_e('College'))
# print(has_no_e('EA sports'))


def find_words_no_e():
    """
    returns the percentage of the words that don't have the letter "e"
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder

    counter_no_e = 0
    counter_total = 0

    for line in f:
        word = line.strip()
        counter_total +=1
        if has_no_e(word):
            counter_no_e += 1

    return counter_no_e / counter_total


# perc_no_e = find_words_no_e()
# print(f'The percentage of the words with no "e" is {perc_no_e*100:.2f}%.')


def avoids(word, forbidden):
    """
    returns True if the given word does not use any of the forbidden letters
    """
    for c in word:
        if c in forbidden:
            return False
    return True


# print(avoids('Babson', 'abcde'))
# print(avoids('College', 'e'))
# print(avoids('Boston', 'xyz'))


def find_words_no_vowels():
    """
    returns the percentage of the words that don't have vowel letters
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder
    counter_no_value = 0
    counter_total = 0

    for line in f:
        word = line.strip()
        counter_total += 1
        if avoids(word, 'aeiouAEIOU'):
            counter_no_value += 1
        
    return counter_no_value / counter_total


# perc_no_vowel = find_words_no_vowels()
# print(f'The percentage of the words without vowel letters is {perc_no_vowel*100:.2f}%.')


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the string available.
    """

    for c in word:
        if c not in available:
            return False
        return True


# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))


def find_words_only_use_planet():
    """
    This function searches the list of words for words that could be formed using the letters in word 'planets'. It counts these words, and prints them.
    """

    f = open('data/words.txt')  # Assume words.txt is under data folder
    counter_planet = 0
    counter_total = 0

    for line in f:
        word = line.strip()
        if uses_only(word, 'planets'):
            counter_planet += 1
        else:
            counter_total += 1
    
    return counter_planet


# print('Number of words that use only letters from "planets" is', find_words_only_use_planet())


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for c in required:
        if c not in word:
            return False
    return True
   

# print(uses_all('babson', 'abson'))
# print(uses_all('ephen', 'sephn'))
# print(uses_all('test', 'wowe'))
# print(uses_all('meow', 'woemmmeeeooowwwww'))


def find_words_using_all_vowels():
    """
    return the number of the words that use all the vowel letters
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder
    counter_all_vowels = 0

    for line in f:
        word = line.strip()
        if uses_all(word, 'aeiou'):
            counter_all_vowels += 1
        
    return counter_all_vowels


# print('The number of words that use all the vowels:', find_words_using_all_vowels())


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
        
    return True


# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))


def find_abecedarian_words():
    """
    returns the number of abecedarian words
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder
    counter_abec_words = 0
    
    for line in f:
        word = line.strip()
        if is_abecedarian(word):
            counter_abec_words += 1
    
    return counter_abec_words


# print(find_abecedarian_words())

def find_long_abecedarian():
    """
    returns the largest abecedarian word in the list
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder

    curr_max_length = 0
    curr_longest = ''
    
    for line in f:
        word = line.strip()
        if is_abecedarian(word) and len(word) > curr_max_length:
            curr_max_length = len(word)
            curr_longest = word

    return curr_longest 


print(find_long_abecedarian())




def is_abecedarian_using_recursion(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass


# print(is_abecedarian_using_recursion('abcdef'))


def is_abecedarian_using_while(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass

# print(is_abecedarian_using_while('abcdef'))