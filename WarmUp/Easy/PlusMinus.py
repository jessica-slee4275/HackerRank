"""
input
6             
-4 3 -9 0 4 1  

output
0.500000
0.333333
0.166667

>>> There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The proportions of occurrence are positive: 3/6 = 0.500000, 
negative: 2/6 = 0.333333 and zeros: 1/6 = 0.166667.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    res = [0, 0, 0] # positive, negative, zero
    for a in arr:
        res[0] +=1 if a/len(arr) > 0 else 0
        res[1] +=1 if a/len(arr) < 0 else 0
        res[2] +=1 if a/len(arr) == 0 else 0
    for r in res:
        print(r/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
