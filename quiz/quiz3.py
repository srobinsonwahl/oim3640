def matching_ratio(s: str):
    """
    This function returns the ratio of the number of matching words in English that must: be the same length as the given string, s, and start or end in the same letter as s.
    """
    counter_ratio = 0
    counter_total = 0
    f = open('data/words.txt')
    for line in f:
        word = line.strip()
        if len(word) == len(s) and word[0] == s[0] or word[-1] == s[-1]:
            counter_ratio += 1
            counter_total += 1
        else:
            counter_total += 1
    
    return counter_ratio / counter_total

ratio = matching_ratio('Meow')
print(f'The percentage of matching words is {ratio:.2%}.')