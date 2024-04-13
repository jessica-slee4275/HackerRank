"""
minutes=0 -> o'clock
1 <= minutes <= 30 -> past
30 < minutes -> to

5:00 -> five o'clock
5:01 -> one minute past five
5:10 -> ten minutes past five
5:15 -> quarter past five
5:28 -> twenty eight minutes past five
5:30 -> half past five
5:40 -> twenty minutes to six
5:45 -> quarter to six
5:47 -> thirteen minutes to six

input
5
47

output
thirteen minutes to six

input
3
00

output
three o' clock

input
7
15

output
quarter past seven
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    units = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 
             6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
             11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 
             16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
    tens = {20:"twenty", 30:"thirty", 40:"fourty", 50:"fifty"}

    if m == 0: return units.get(h)+' o\' clock' 
    if m == 15: return 'quarter past ' + units.get(h)
    if m == 30: return 'half past ' + units.get(h)
    if m == 45: return 'quarter to ' + units.get(h+1)

    mins = ''
    if m >= 20 and m < 30:
        mins = tens.get(m//10*10) + ' ' + units.get(m%10)
    elif m > 30:
        if ((60-m)//10*10) >= 20:
            mins = tens.get((60-m)//10*10) + ' ' + units.get((60-m)%10)
        else:
            mins = units.get(60-m)
    else:
        mins = units.get(m) 

    if mins == 'one':
        mins = 'one minute'
    else:
        mins = mins + ' minutes'

    if m > 30:
        return mins + ' to ' + units.get(h+1)
    else:
        return mins + ' past ' + units.get(h)
    
if __name__ == '__main__':

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    print(result + '\n')
