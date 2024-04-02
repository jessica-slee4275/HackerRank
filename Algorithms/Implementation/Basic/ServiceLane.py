"""
input
8 5                 
2 3 1 2 3 2 3 3     
0 3                 
4 6
6 7
3 5
0 7

STDIN               Function
-----               --------
8 5                 n = 8, t = 5
2 3 1 2 3 2 3 3     width = [2, 3, 1, 2, 3, 2, 3, 3]
0 3                 cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
4 6
6 7
3 5
0 7

   |HIGHWAY|Lane|    ->    Width

0: |       |--|            2
1: |       |---|           3
2: |       |-|             1
3: |       |--|            2
4: |       |---|           3
5: |       |--|            2
6: |       |---|           3
7: |       |---|           3

1. (0,3) 2, 3, 1, 2 -> 1 can pass all segments
2. (4,6) 3, 2, 3 -> 1 can pass all segments
3. (6,7) 3, 3 -> 3 can pass all segments
4. (3,5) 2, 3, 2 -> 2 can pass all segments
5. (0,7) 2, 3, 1, 2, 3, 2, 3, 3 -> 1 can pass all segments

output
1
2
3
2
1

"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#

def serviceLane(width, cases):
    # Write your code here
    res = []
    for case in cases:
        res.append(min(width[case[0]:case[1]+1]))
    return res

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(width, cases)

    print('\n'.join(map(str, result)))
