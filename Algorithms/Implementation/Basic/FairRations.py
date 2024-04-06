"""
1. every time you give a loaf of bread to some person i.
must give a loaf of bread to the person i+1 or i-1
2. each person must have an even number of loaves.

print min number of loaves you must distribute to satisfy the 2 rules above
if not possible, print NO

input
5
2 3 4 5 6

STDIN       Function
-----       --------
5           B[] size N = 5
2 3 4 5 6   B = [2, 3, 4, 5, 6]   

>>> 
[2, 3, 4, 5, 6]   
[2, 4, 5, 5, 6]   
[2, 4, 6, 6, 6]   

output
4

input
2
1 2

output
NO
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    # Write your code here
    res = 0
    try:
        for index in range(len(B)):
            if B[index] % 2 != 0 :
                B[index] += 1
                B[index+1] += 1
                res += 2
                # print(index, B)
    except:
        return 'NO'
    return str(res)

if __name__ == '__main__':

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    print(result + '\n')