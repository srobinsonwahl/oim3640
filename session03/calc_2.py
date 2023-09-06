# Question 1 - What is the volume of a sphere with a radius of 5?
pi = 3.1415926
r = 5
volume = 4 / 3 * pi * r **3
print(f'The volume of a sphere with a radius of 5 is {volume:.1f}.')

# Question 2 - What is the total wholesale cost for 60 copies?
cp = 24.95
bp = cp * 0.6
sc = 3
asc = 0.75
cost = bp * 60 + sc + asc * 59
print(f'The total wholesale cost for 60 copies is ${cost:.2f}.')

# Question 3 - What time do I get home for breakfast?
leave_time = 6 + (52 / 60)
easy_pace = (8 * 60) + 15
tempo_pace = (7 * 60) + 12
run_time = ((2 * easy_pace) + (3 * tempo_pace)) / 60
return_time = leave_time + (run_time / 60)
return_hour = return_time // 1
return_minute = (return_time - return_hour) * 60 
print(f'You will get home for breakfast at {return_hour:.0f}:{return_minute:.0f} AM.')

# Question 4 - What is the percentage of the increase?
low_end = 82
high_end = 89
avg_increase = ((low_end - high_end) / low_end)
print(f'The percentage of the increase is {abs(avg_increase):.1%}.')