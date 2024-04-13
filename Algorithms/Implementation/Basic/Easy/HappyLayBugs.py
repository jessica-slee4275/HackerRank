"""
returns 'YES' or 'NO'

input
4
7
RBY_YBR
6
X_Y__X
2
__
6
B_RRBR

>>> 
4 = moves
RBY_YBR
RBYY_BR
R_YYBBR
RRYYBB_
-> YES

X_Y__X
-> NO (no way to make 'Y' happy)
__
-> YES (no unhappy ladybug)

B_RRBR
BBRRR_
-> YES

output
YES
NO
YES
YES
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Write your code here
    d = {ele: b.count(ele) for ele in set(b) if ele != '_'}
    
    if 1 in d.values():
        return 'NO'
    
    if '_' not in b:
        for index in range(1, len(b)-1):
            if b[index] != b[index+1] and b[index] != b[index-1]:
                return 'NO'

    return 'YES'

if __name__ == '__main__':

    g = int(input().strip())
    
    result = []

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result.append(happyLadybugs(b))

    print(result)
