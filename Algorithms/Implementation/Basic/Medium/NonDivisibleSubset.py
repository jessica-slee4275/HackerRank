"""
input
STDIN    Function
-----    --------
4 3      S[] size n = 4, k = 3
1 7 2 4  S = [1, 7, 2, 4]

4 3
1 7 2 4

>>>
1 + 7 = 8
1 + 2 = 3
1 + 4 = 5
7 + 2 = 9
7 + 4 = 11
2 + 4 = 6

The sums of all permutations of two elements from S = {1, 7, 2, 4}
Only S = {1, 7, 4} will not ever sum to a multiple of k=3

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
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    # res = set()
    # for i in range(len(s)-1):
    #     for j in range(i+1, len(s)):
    #         print(s[i], s[j], (s[i]+s[j])%k)
    #         if (s[i] + s[j]) % k != 0:
                
    #             res.add(s[i])
    #             res.add(s[j])

    # return len(res)
    x = [0 for _ in range(k)]
    print(x)
    for ss in s:
        x[ss % k] += 1
        print(ss, '%', k, ss % k)
    res = min(1, x[0])
    print(x)
    x = x[1:]
    for i in range(len(x) // 2):
        print(x, i, x[i], x[-(i+1)])
        res += max(x[i], x[-(i+1)])
    if len(x) % 2 == 1:
        print(len(x) // 2, x[len(x) // 2])
        res += min(1, x[len(x) // 2])
    print(res)
    return res

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(str(result) + '\n')


    