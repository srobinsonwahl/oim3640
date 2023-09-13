# 3. Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, plus the number of days since the epoch.

import time

epoch = time.time()
seconds_day = 60 * 60 * 24
seconds_hour = seconds_day / 24
seconds_minute = 60

days = epoch // seconds_day
hours = (epoch % seconds_day) // seconds_hour
minutes = (epoch % seconds_day) % seconds_hour // seconds_minute
seconds = (epoch % seconds_day) % seconds_hour % seconds_minute

if hours > 12:
    zone = 'PM'
else:
    zone = 'AM'

print(f'The current time in GMT is: {hours:01.0f}:{minutes:01.0f}:{seconds:01.0f} {zone}. It has now been {days:.0f} days since the epoch, but who\'s counting, right?')