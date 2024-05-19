"""
longest subarray where the absolute difference 
between any two elements is less than or equal to 1.

a = [1, 1, 2, 2, 4, 4, 5, 5, 5]

[1, 1, 2, 2]
[4, 4, 5, 5, 5]

max length subarray has 5 elements

input
6
4 6 5 3 3 1

|4 - 3| = 1
|3 - 3| = 0

output
3

input
6
1 2 2 3 1 2

output
5
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

from collections import Counter

def pickingNumbers(a):
    # Write your code here
    temp_dict = dict(Counter(sorted(a)).items())
    # if between any two elements is less than 1
    res = max(Counter(sorted(a)).values())
    for i in range(len(list(temp_dict))-1):
        if list(temp_dict)[i]+1 == list(temp_dict)[i+1]:
            res = max(res, temp_dict.get(list(temp_dict)[i]) + temp_dict.get(list(temp_dict)[i+1]))
            # print(list(temp_dict)[i], temp_dict.get(list(temp_dict)[i]), list(temp_dict)[i+1], temp_dict.get(list(temp_dict)[i+1]))
    return res
    
    
if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(str(result) + '\n')