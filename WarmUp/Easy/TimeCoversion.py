"""
input
07:05:45PM

output
19:05:45
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here

    h, m , sec = map(int, s[:-2].split(':'))
    h = h % 12 + (s[-2:].upper()=='PM')*12
    return "%02d:%02d:%02d" % (h, m, sec) 

    # m = s.split(':')[1]
    # sec = s.split(':')[2][:-2]
    # if 'PM' in s:
    #     hr = '12' if s.split(':')[0] == '12' else str(int(s.split(':')[0])+12)
    # else:
    #     hr = '00' if s.split(':')[0] == '12' else s.split(':')[0]
    # return "{}:{}:{}".format(hr, m, sec)
if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result + '\n')
