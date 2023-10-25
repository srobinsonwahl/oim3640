# 1). Rewrite histogram using get. Eliminate the if statement

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

print(histogram('Bookkeeper'))

# 2). Use function histogram to count the frequency of each word in your favorite song.

lyrics = open('data/lyrics.txt')
words = lyrics.read()
countem = words.split()

print(histogram(countem))
