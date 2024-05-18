"""
input
3
11 2 4
4 5 6
10 8 -12

output
15

11
   5
     -12
11 + 5 - 12 = 4

     4
   5
10
4 + 5 + 10 = 19

|4-19| = 15
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    primary_diagonal = 0
    secondary_diagonal = 0

    len_arr = len(arr)
    for index in range(len_arr):
        primary_diagonal += arr[index][index] 
        secondary_diagonal += arr[index][len_arr-(index+1)] 
    return abs(primary_diagonal-secondary_diagonal)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(str(result) + '\n')
