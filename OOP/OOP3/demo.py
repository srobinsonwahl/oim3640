#  Methods are defined inside a class definition in order to make the relationship between the class and the method explicit
# The syntax for invoking a method is different from the syntax for calling a function

# Printing objects

class Time:
    """
    Represents the time of day 
    """

    def __init__(self, hour=0, minute=0, second=0):
        # The default values ^ allow u to initiate an object without predefined values
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        # This is much different from the print_time function
        return f'{self.hour:02}:{self.minute:02}:{self.second:02}'
    
    def __add__(self, other):
        """ Low effort add function """
        endhr = self.hour + other.hour
        endmn = self.minute + other.minute
        endsc = self.second + other.second
        return f'{endhr:02}:{endmn:02}:{endsc:02}'
    
# start = Time(9, 45)
# end = Time(11)
# print(start + end)

# start = Time()
# This initializes an object of the Time class
# start.hour = 9
# start.minute = 45
# start.second = 0

# Time.print_time(start)
# start.print_time()

# In non-OOP, print_time(start) ***This is wrong btw*** suggests that the function is the active agent. It says something like "Hey print_time, heres an object for you to print"

# In OOP, the objects are the active agents. 
# A method invocation like start.print_time() says "Hey start! Please print yourself"


#  The init method
# Gets involed when an object is instantiated.

# SEE PRINT STATEMENTS BELOW 

time = Time()
# time.print_time()
time = Time(9)
# time.print_time()
time = Time(9, 45)
# print(time)
# time.print_time()
