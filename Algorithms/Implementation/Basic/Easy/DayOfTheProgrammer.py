"""
the 256th day of the year


From 1700 to 1917, Russia's official calendar was the Julian calendar; 
leap years are divisible by 4;

since 1919 they used the Gregorian calendar system. 
Divisible by 400.
Divisible by 4 and not divisible by 100.

The transition from the Julian to Gregorian calendar system occurred in 1918,
 when the next day after January 31st was February 14th. 
 This means that in 1918, February 14th was the 32nd day of the year in Russia.

input
2017

output
13.09.2017

>>>  format dd.mm.yyyy
the given year = 1984. 1984 is divisible by 4, so it is a leap year. 
The 256th day of a leap year after 1918 is September 12, 
so the answer is 12.09.1984.
we get 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 = 243

input
2016

output
12.09.2016
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    if year == 1918: return '26.09.1918'
    if year >= 1700 and year <= 1917:
        if year%4==0:
            return f'12.09.{year}'
    if year >= 1919:
        if year%400 ==0 or (year%4 == 0 and year%100 != 0):
            return f'12.09.{year}'
    return f'13.09.{year}'

if __name__ == '__main__':
    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result + '\n')
