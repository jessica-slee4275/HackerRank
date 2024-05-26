"""
input
4 0
4 4

>>>
Function Description

Complete the queensAttack function in the editor below.

queensAttack has the following parameters:
- int n: the number of rows and columns in the board
- int k: the number of obstacles on the board
- int r_q: the row number of the queen's position
- int c_q: the column number of the queen's position
- int obstacles[k][2]: each element is an array of 2 integers, the row and column of an obstacle

Returns
- int: the number of squares the queen can attack

4 [o][o][o][Q]
3 [ ][ ][o][o]
2 [ ][o][ ][o]
1 [o][ ][ ][o]
   1  2  3  4

output
9

input
5 3
4 3
5 5
4 2
2 3

>>>
5 [ ][o][o][o][x]
4 [ ][x][Q][o][o]
3 [ ][o][o][o][ ]
2 [o][ ][x][ ][o]
1 [ ][ ][ ][ ][ ]
   1  2  3  4  5

output
10
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
    obstacle_set = {(r, c) for r, c in obstacles}

    count = 0
    for dr, dc in directions:
        r, c = r_q+dr, c_q+dc
        while 1<=r<=n and 1<=c<=n and (r,c) not in obstacle_set:
            count += 1
            print('move', r, c)
            r += dr
            c += dc
    return count

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(str(result) + '\n')
