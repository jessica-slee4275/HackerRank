"""

input
6
1 4 4 4 5 3

output
4

>> 
type 1: 1 bird
type 2: 0 bird
type 3: 1 bird
type 4: 3 bird
type 5: 1 bird


input
11
1 2 3 4 5 4 3 2 1 3 4

output
3

>> 
type 1: 2 bird
type 2: 2 bird
type 3: 3 bird
type 4: 3 bird
type 5: 1 bird
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    res = []
    for i in range(min(arr), max(arr)+1):
        print(i, arr.count(i))
        res.append(arr.count(i))
    return res.index(max(res))+1

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(str(result) + '\n')