# 1). Modify the program to fix the names of Ouack and Quack.

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O':
        new_pref = prefixes[-3] + 'u' + suffix
        print(new_pref)
    elif letter == 'Q':
        new_pref = prefixes[-1] + 'u' + suffix
        print(new_pref)
    else:
        print(letter + suffix)