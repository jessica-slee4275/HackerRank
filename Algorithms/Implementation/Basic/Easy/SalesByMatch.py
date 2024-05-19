"""
returns the number of pairs

input
9
10 20 20 10 10 30 50 10 20

STDIN                       Function
-----                       --------
9                           n = 9
10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

output
3

>>>


n = 7 
ar = [1, 2, 1, 2, 1, 3, 2]
There is one pair of color 1 and one of color 2. 
There are three odd socks left, one of each color. 
The number of pairs is 2.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#
from collections import Counter
def sockMerchant(n, ar):
    # Write your code here
    res = 0
    for v, c in Counter(ar).items():
        res += c//2 
    return res

    # res  = 0 
    # temp = []
    # for a in ar:
    #     if a not in temp:
    #         temp.append(a)
    #     else:
    #         res += 1
    #         temp.remove(a)
    # return res
    #  return sum([ar.count(i)//2 for i in set(ar)])
if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(str(result) + '\n')

