import random
import math

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(is_leap_year(2020))
print(is_leap_year(2021))
print(is_leap_year(2022))
print(is_leap_year(2023))
print(is_leap_year(2024))
