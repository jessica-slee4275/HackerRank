"""
Find all the cavities on the map 
and replace their depths with the uppercase character X.

input
4
1112 
1912
1892
1234

STDIN   Function
-----   --------
4       grid[] size n = 4
1112    grid = ['1112', '1912', '1892', '1234']
1912
1892
1234

>>> 2 cells with the depth of 9 are not on the border 
and are surrounded on all sides by shallower cells.

output
1112
1X12
18X2
1234
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    max_num = 0
    res = []
    res.append(grid[0])
    
    for g in range(1, len(grid)-1):
        for c in grid[g]:
            max_num = max(max_num, int(c))

    for g in range(1, len(grid)-1):
        res.append(grid[g].replace(str(max_num), 'X'))
    if len(grid) > 1:
        res.append(grid[len(grid)-1])
    return res

if __name__ == '__main__':

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    print('\n'.join(result))
