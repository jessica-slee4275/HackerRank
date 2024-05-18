"""
input
5 6 7
3 6 10

output
1 1

>>> 
a[0]>b[0], so Alice receives 1 point.
a[1]=b[1], so nobody receives a point.
a[2]<b[2], so Bob receives 1 point.
Alice's comparison score is 1, and Bob's comparison score is 1. 
Thus, we return the array [1,1].

input
17 28 30
99 16 8

output
2 1

>>>
Comparing the 0th elements, 17 < 99 so Bob receives a point.
Comparing the 1st and 2nd elements, 28>16 and 30>8 so Alice receives two points.
The return array is [2,1].
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    alice = 0 
    bob = 0
    for index in range(len(a)):
        alice += 1 if a[index] > b[index] else 0
        bob += 1 if a[index] < b[index] else 0
    return alice, bob
if __name__ == '__main__':


    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(' '.join(map(str, result)))