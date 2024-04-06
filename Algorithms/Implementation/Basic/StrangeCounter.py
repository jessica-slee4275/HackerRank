"""
There is a strange counter. At the first second, it displays the number 3. 
Each second, the number displayed by decrements by 1 until it reaches 1. 
In next second, the timer resets to 2*the initial number for the prior cycle 
and continues counting down. 
The diagram below shows the counter values for each time t in the first three cycles:

time value
 1     3
 2     2
 3     1

time value
 4     6
 5     5
 6     4
 7     3
 8     2
 9     1

time value
 10    12
 11    11
 12    10
 13    9
 14    8
 15    7
 ...  ...
 21    1

input
4

>>> 2*3=6
output
6
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    # Write your code here
    p = 3 
    while t > p: 
        t -= p
        p *= 2
    return p - t + 1

if __name__ == '__main__':

    t = int(input().strip())

    result = strangeCounter(t)

    print(str(result) + '\n')
