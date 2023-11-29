class Time:
    """
    represents the time of day

    attr: hour, minute, second
    """

    def __str__(self):
        return f"The time is {self.hour:02}:{self.minute:02}:{self.second:02}"
    
    def add_time(t1, t2):
        sum = Time()
        sum.hour = t1.hour + t2.hour
        sum.minute = t1.minute + t2.minute
        sum.second = t1.second + t2.second
        return sum
    
start = Time()
start.hour = 9
start.minute = 45
start.second = 0

print(start)

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

print(duration)

done = start + duration
print(done)

# # done = add_time(start, duration)
# print(done)
# a = Time(1, 30, 30)

# print(a)


