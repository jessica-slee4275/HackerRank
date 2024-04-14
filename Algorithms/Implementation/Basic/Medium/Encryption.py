"""
input
haveaniceday

>>>
√12 = between 3 and 4
rewritten with 3 rows and 4 columns
have
anic
eday

output
hae and via ecy
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
import textwrap

def encryption(s):
    # Write your code here
    column = math.ceil(math.sqrt(len(s)))
    grid = textwrap.wrap(s, column)
    encoded = ""
    for i in range(column):
        for value in grid:
            try:
                encoded += value[i]
            except IndexError:
                continue
        encoded += " "
    print(encoded+"hey")    
    return encoded.rstrip()+"hey"
if __name__ == '__main__':

    s = input()

    result = encryption(s)

    print(result)