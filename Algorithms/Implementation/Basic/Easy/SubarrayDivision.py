"""
int s[n]: the numbers on each of the squares of chocolate
int d: Ron's birth day
int m: Ron's birth month

input
5
1 2 1 3 2
3 2

>> User
Lily wants to give Ron m=2  squares summing to d=3
output
2

input
6
1 1 1 1 1 1
3 2

output
0

input
1
4
4 1

output
1
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    if m == 1 : return 1
    res = 0
    print(len(s)-d)
    for index in range(len(s)-m+1):
        if sum(s[index:index+m]) == d: res += 1
        print(index, index+m, s[index:index+m], sum(s[index:index+m]))
    return res       
if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(str(result) + '\n')
