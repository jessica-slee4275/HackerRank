"""
input
8
UDDDUDUU

>>> 
U: up, D: down
_//\\         _
    \\      // 
     \\//\\//  
print the number of valleys walked through

12
DDUUDDUDUUUD
>>> 
_               //\\_
 \\  //\\      //
  \\//  \\//\\//  
output
1

"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    seaLevel = valley = 0
    for p in path:
        if p == 'U':
            seaLevel += 1
        else:
            seaLevel -= 1
        if p == 'U' and seaLevel == 0:
            valley += 1
    return valley

if __name__ == '__main__':

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(str(result) + '\n')
