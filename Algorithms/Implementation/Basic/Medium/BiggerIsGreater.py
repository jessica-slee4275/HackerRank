"""
input
5
ab
bb
hefg
dhck
dkhc

>>>
Test case 1:
ba is the only string which can be made by rearranging ab. It is greater.
Test case 2:
It is not possible to rearrange bb and get a greater string.
Test case 3:
hegf is the next string greater than hefg.
Test case 4:
dhkc is the next string greater than dhck.
Test case 5:
hcdk is the next string greater than dkhc.

output
ba
no answer
hegf
dhkc
hcdk
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#
from itertools import permutations
def biggerIsGreater(w):
    # Write your code here
    cases = [''.join(p) for p in permutations(w)]
    sorted_cases = sorted(set(cases))
    index = sorted_cases.index(w)

    print(sorted_cases, index, len(sorted_cases))
    # print(sorted_cases[index], sorted_cases[index+1])
    if index == len(sorted_cases)-1 or sorted_cases[index] == sorted_cases[index+1]:
        return 'no answer'
    return sorted_cases[index+1]
    
if __name__ == '__main__':
    
    res = []

    T = int(input().strip())

    for T_itr in range(T):

        w = input()

        result = biggerIsGreater(w)

        res.append(result)

    print('\n'.join(res))
