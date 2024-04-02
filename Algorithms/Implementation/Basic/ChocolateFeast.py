
"""
n: initial amount of money
c: chocolate bar cost 
m: the number of wrapper he can turn in for a free chocolate bar
15 3 2

>>>
15//3 = 5 chocolate bars
5//2 = 2 more chocolate bars + 1 wrapper
(2+1)//2 = 1 more chocolate bars + 1 wrapper
(1+1)//2 = 1 more chocolate bars
5+2+1+1 = 9 bars

input
3
10 2 5
12 4 4
6 2 2

STDIN   Function
-----   --------
3       t = 3 (test cases)
10 2 5  n = 10, c = 2, m = 5 (first test case)
12 4 4  n = 12, c = 4, m = 4 (second test case)
6 2 2   n = 6,  c = 2, m = 2 (third test case)

output
6
3
5
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#
"""
n: initial amount of money
c: chocolate bar cost 
m: the number of wrapper he can turn in for a free chocolate bar
"""
def chocolateFeast(n, c, m):
    # Write your code here
    chcolate_bars = n//c
    wraps = chcolate_bars
    while wraps >= m:
        chcolate_bars += wraps//m
        wraps = (wraps%m) + (wraps//m)
        # print(chcolate_bars, wraps)

    return chcolate_bars
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        print(str(result) + '\n')

