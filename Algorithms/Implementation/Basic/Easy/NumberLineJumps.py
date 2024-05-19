"""
input
0 3 4 2

output
YES

>>>
start from 0, jump distance 3
start from 4, jump distance 2

meet at jump[4] == 12 -> YES

input
0 2 5 3

output
NO

never catchup -> NO
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    res = "NO"
    if v2 < v1:
        if (x1 - x2) % (v2 - v1) == 0: 
            res = "YES"
    return res

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result + '\n')


