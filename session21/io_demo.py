# file = open('data/words.txt', 'r', encoding='utf-8')
# print(file.readline()) # will read line by line

# print(file.read()) # will read entire file as one string

# print(file.readlines()) # will read entire file as list of strings by line

# print(file.read().split('\n')) # will read entire file as list of strings by line and removes \n

file = open('data/output.txt', 'w')
file.write('Hey Jude\n')
file.write('Dont make it bad\n')
file.close()
# list_of_lyrics = ['Hey Jude\n',
                #   'Dont make it bad\n']

# file.writelines(list_of_lyrics)

# COntext manager
# with open('data/output.txt') as file:
#     file.write('hey jude')

import os

cwd = os.getcwd()
# print(cwd)

# print(os.listdir(cwd))

# print(os.path.isdir('data'))
# print(os.path.isdir('data/output.txt'))
# print(os.path.isfile('data/output.txt'))

for name in os.listdir('data'):
    path = os.path.join('data', name)
    if os.path.isfile(path) and 'output' in name:
        print(name)