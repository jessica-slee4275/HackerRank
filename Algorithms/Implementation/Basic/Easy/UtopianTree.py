"""
The first line contains an integer, t, the number of test cases.
t subsequent lines each contain an integer, n, the number of cycles for that test case.

input
3
0
1
4

>>> 3 tests [0, 1, 4]

n=0 initial height H=1
n=1 grow 2
n=4 (n=2, H=3) (n=3, H=6) (n=4, H=7) 7m

0,  1,  2,  3,  4,  5,  6
1,  2,  3,  6,  7,  14, 15
   1+1 2+1 3+3 6+1  7+7 14+1
       2*1     3*2      7*2
output
1
2
7

input
3
6
5
4

output
15
14
7
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
"""
0,  1,  2,  3,  4,  5,  6,   7    8
0+1 1+1 2+1 3+3 6+1  7+7 14+1 15+15 30+1
1,  2,  3,  6,  7,  14, 15,  30   31
         
3
6
5
4
   """


def utopianTree(n):
    # Write your code here
    # result = []
    # res = [1]
    # for i in range(1, 60):
    #     if i % 2 == 0:
    #         res.append(res[-1]+1)
    #     else:
    #         res.append(res[-1]*2)
    # for nn in n:
    #     result.append(res[nn])
    # return result

    res = [1]
    for i in range(1, 60):
        if i % 2 == 0:
            res.append(res[-1]+1)
        else:
            res.append(res[-1]*2)
    return res[n]
if __name__ == '__main__':

    t = int(input().strip())
    n = []
    for t_itr in range(t):
        n.append(int(input().strip()))

    result = utopianTree(n)
    print('\n'.join(str(num) for num in result))
