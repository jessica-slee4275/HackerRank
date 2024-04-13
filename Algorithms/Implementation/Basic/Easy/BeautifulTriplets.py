"""
a triplet (a[i], a[j], a[k])

input
7 3
1 2 4 5 7 8 10

STDIN           Function
-----           --------
7 3             arr[] size n = 7, d = 3
1 2 4 5 7 8 10  arr = [1, 2, 4, 5, 7, 8, 10]

>>>
(1, 4, 7) 7-4=3, 4-1=3 
(4, 7, 10) 10-7=3, 7-4=3 
(2, 5, 8) 8-5=3, 5-2=3 

output
3
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Write your code here
    res = 0
    for num in arr:
        if num+d in arr and num+(d*2) in arr:
            print(num, num+d, num+(d*2))
            res += 1
    return res
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    print(str(result) + '\n')
