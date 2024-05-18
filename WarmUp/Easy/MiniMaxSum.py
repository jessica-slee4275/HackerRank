"""
input
1 2 3 4 5

>>>
Sum everything except 1, the sum is 14.
Sum everything except 2, the sum is 13.
Sum everything except 3, the sum is 12.
Sum everything except 4, the sum is 11.
Sum everything except 5, the sum is 10.

min = 10, max = 14

output
10 14
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    res = []
    for a in arr:
        res.append(sum(arr) - a)
    print(min(res), max(res))

    # res_min = sum(arr)
    # res_max = 0
    
    # for a in arr:
    #     res_min = min(sum(arr)-a, res_min)
    #     res_max = max(sum(arr)-a, res_max)
    # print(res_min, res_max)    
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
