"""
input
2 3
2 4
16 32 96

output
3

>>>
2 4 divide evenly into 4, 8, 12, 16 --> (GCD, Greatest Common Divisor)
4 8 16 divide evenly into 16, 32, 96 --> (LCM, Least Common Multiple)

output 3 = [4, 8, 16]

>>> 
2 3
2 6 
24 36

two numbers between the arrays: 6 and 12
6%2=0, 6%6=0, 24%6=0, 36%6=0
12%2=0, 12%6=0, 24%12=0, 36%12=0
return 2
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

def getTotalX(a, b):
    # Write your code here
    lcm_result = a[0]
    for i in range(1, len(a)):
        lcm_result = lcm(lcm_result, a[i])
    print(lcm_result)

    gcd_result = b[0]
    for i in range(1, len(b)):
        gcd_result = gcd(gcd_result, b[i])
    print(gcd_result)

    count = 0
    current_multiple = lcm_result
    while current_multiple <= gcd_result:
        print(gcd_result, current_multiple, gcd_result % current_multiple)
        if gcd_result % current_multiple == 0:
            count += 1
        current_multiple += lcm_result

    return count
    
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(str(total) + '\n')
