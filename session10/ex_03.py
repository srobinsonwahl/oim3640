# 3). You might want to experiment with some of them to make sure you understand how they work. split, strip and replace are particularly useful.

team = 'New England Patriots'
split_team = team.split()
print(split_team)\

team = '    New England Patriots    '
strip_team = team.strip()
print(strip_team)

team = 'New England Patriots'
replace_team = team.replace('Patriots', 'Memers')
print(replace_team)