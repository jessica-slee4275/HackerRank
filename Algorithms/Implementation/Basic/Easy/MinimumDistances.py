"""
if no value, returns -1
if values, returns min(values)

input
6  
7 1 3 4 1 7 

>>>
a[1]=1 a[4]=1 d[1,4]=|1-4|=3
a[0]=7 a[5]=7 d[0,5]=|0-5|=5
min(3, 5) = 3

STDIN           Function
-----           --------
6               arr[] size n = 6
7 1 3 4 1 7     arr = [7, 1, 3, 4, 1, 7]

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
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    res = max(a)
    d = {i:a.count(i) for i in a if a.count(i) > 1}
    if len(d) == 1:
        return 1
    for num in d.keys():
        indices = [index for index, value in enumerate(a) if value == num]
        res = min(abs(indices[0]-indices[1]), res)
    return '-1' if res == max(a) else res
if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    print(str(result) + '\n')
