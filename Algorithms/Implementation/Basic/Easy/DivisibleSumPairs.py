"""
ar = [1, 2, 3, 4, 5, 6]
k = 5

[1, 4], [2, 3], [4, 6]
>> Given an array of integers and a positive integer k, 
determine the number of (i,j) pairs where i<j and ar[i]+ ar[j] is divisible by k.

input
6 3
1 3 2 6 1 2

STDIN           Function
-----           --------
6 3             n = 6, k = 3
1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]

output
5

>>> 
(0, 2) -> ar[0] + ar[2] = 1 + 2 = 3
(0, 5) -> ar[0] + ar[5] = 1 + 2 = 3
(1, 3) -> ar[1] + ar[3] = 3 + 6 = 9
(2, 4) -> ar[2] + ar[4] = 2 + 1 = 3
(4, 5) -> ar[4] + ar[5] = 1 + 2 = 3
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    res = 0
    for first_index in range(len(ar)-1):
        for second_index in range(first_index+1, len(ar)):
            if (ar[first_index] + ar[second_index]) % k == 0:
                res += 1
                print(f'ar[{first_index}]={ar[first_index]} ar[{second_index}]={ar[second_index]}', ar[first_index] + ar[second_index])
    
    return res
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(str(result) + '\n')
