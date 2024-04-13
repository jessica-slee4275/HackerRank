"""
T = the number of test cases
each test case contains 3 lines
n = the number of non-zero stones found
a = 1 possible difference
b = other possible difference

input
2
3
1
2
4
10
100

STDIN   Function
-----   --------
2       T = 2 (test cases)
3       n = 3 (test case 1)
1       a = 1
2       b = 2
4       n = 4 (test case 2)
10      a = 10
100     b = 100

>>> with differences 1 and 2
0,1,2
0,1,3
0,2,3
0,2,4

-> 2 3 4 

with differences 10 and 100
0, 10, 20, 30
0, 10, 20, 120
0, 10, 110, 120
0, 10, 110, 210
0, 100, 110, 120
0, 100, 110, 210
0, 100, 200, 210
0, 100, 200, 300

-> 30 120 210 300

output
2 3 4 
30 120 210 300 
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#

def stones(n, a, b):
    # Write your code here
    res = set()
    for i in range(n):
        
        value = a*(n-1-i)+b*i
        res.add(value)
    
    return sorted(res)

if __name__ == '__main__':

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        print(' '.join(map(str, result)))
