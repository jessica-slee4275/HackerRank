"""
Given a grid of size n*m, each cell in the grid is either good or bad.
G: good, B: bad
A valid plus is defined here as the crossing of two segments (horizontal and vertical) of equal lengths. 
These lengths must be odd, 
and the middle cell of its horizontal segment must cross the middle cell of its vertical segment.
1      5         9
                 []
       []        []
[]   [][][]  [][][][][] ...
       []        []
                 []
input
5 6
GGGGGG
GBBBGB
GGGGGG
GGBBGB
GGGGGG

>>> 1*5
output
5

input
6 6
BGBBGB
GGGGGG
BGBBGB
GGGGGG
BGBBGB
BGBBGB

>>> 5*5
output
25
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def twoPluses(grid):
    list_temp = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'G':
                set_temp = set()
                set_temp.add((r, c))
                i = 1
                while i > 0:
                    if r+i < len(grid) and r-i >= 0 and c+i < len(grid[0]) and c-i >= 0 \
                    and grid[r][c-i] == 'G' and grid[r][c+i] == 'G' and grid[r-i][c] == 'G' and grid[r+i][c] == 'G':
                        set_temp.add((r, c-i))
                        set_temp.add((r, c+i))
                        set_temp.add((r-i, c))
                        set_temp.add((r+i, c))
                        i += 1
                        list_temp.append(set_temp.copy())
                    else:
                        i = -1
    if not list_temp:
        return 1
    res = []
    for i in range(len(list_temp)):
        for j in range(i+1, len(list_temp)):
            if len(list_temp[i]&list_temp[j]) == 0:
                res.append(len(list_temp[i])*len(list_temp[j]))
    
    if not res:
        return len(max(list_temp, key = lambda i: len(i)))
    else:
        return max(res)  
      
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    print(str(result) + '\n')
