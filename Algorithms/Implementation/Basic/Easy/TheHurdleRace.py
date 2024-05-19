"""
The first line contains two space-separated integers n and k, 
the number of hurdles and the maximum height the character can jump naturally.
The second line contains n space-separated integers height[i] where 0 <= i < n.

input
5 4
1 6 3 5 2

>> can jump max 4, tallest huddle 6
needs to drink 6-4 = 2 doses

output
2

input
5 7
2 5 4 5 2

>> can jump max 7, tallest huddle 5
needs to drink 0 doses

output
0
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    # Write your code here
    if max(height) <= k : return 0
    else: return (max(height) - k)

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print(str(result) + '\n') 