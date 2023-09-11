# 1. Below is a transcript of a session with the Python shell. For each expression being evaluated, provide the type and the value the expression returns. I encourage you to answer them directly since this will help reinforce your understanding of basic Python expressions.

a = 3
a + 2
print('This output is an integer:', type(a + 2))

a = a + 1.0
a
print('This output is floating-point addition:', type(a))

a = 3
b = a 
b
print('This output is an integer:', type(b))

a = 3
a == 5.0
a
print('This output is an integer:', type(a))

b = 10
c = b > 9
c
print('This output is a Boolean:', type(c))

5 / 2 == 5 / 2.0
print('This output is a Boolean:', type(5 / 2 == 5 / 2.0))

# 2. For each of the following expressions, indicate the value returned. I encourage you to answer them directly since this will help reinforce your understanding of basic Python expressions.

print('This output is a Boolean \'False\':', type(3.0 - 1.0 != 5.0 - 3.0))
print('This output is a Boolean \'False\':', type(3 > 4 or (2 < 3 and 9 > 10)))
print('This output is a Boolean \'False\':', type(4 > 5 or 3 < 4 and 9 > 10))
print('This output is a Boolean \'False\':', type(not(4 > 3 and 100 > 6)))

# 3. The time module provides a function, also named time, that returns the current Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970. Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, plus the number of days since the epoch. You can only use time module.

import time
epoch = time.time()
seconds_day = 60 * 60 * 24
seconds_hour = seconds_day / 24 
seconds_minute = seconds_hour / 60

days = epoch // seconds_day
hours = (epoch % seconds_day) // seconds_hour - 4
minutes = (epoch % seconds_day) % seconds_hour // seconds_minute
seconds = (epoch % seconds_day) % seconds_hour % seconds_minute

print('%s: %s: %s: %s' %(days, hours, minutes, seconds))
# print('The current time in Boston, MA, USA is:', {hours - 12}:{minutes}:{seconds})