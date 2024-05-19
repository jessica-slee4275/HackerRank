"""
Lily may go to the movies on days 20, 21, 22, and 23. 
We perform the following calculations to determine which days are beautiful:

Day 20 is beautiful because the following evaluates to a whole number
: |20-02|/6 = 18/6 = 3
Day 21 is not beautiful because the following doesn't evaluate to a whole number
: |21-12|/6 = 9/6 = 1.5
Day 22 is beautiful because the following evaluates to a whole number
: |22-22|/6 = 0/6 = 0
Day 23 is not beautiful because the following doesn't evaluate to a whole number
: |23-32|/6 = 9/6 = 1.5
Only two days, 20 and 22, in this interval are beautiful. 
Thus, we print 2 as our answer.

input
20 23 6

output
2
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    # Write your code here
    res = 0
    for i in range(i, j+1):
        if (abs(i-int(str(i)[::-1]))/k) == (abs(i-int(str(i)[::-1]))//k):
            res += 1
    return res
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    print(str(result) + '\n')
