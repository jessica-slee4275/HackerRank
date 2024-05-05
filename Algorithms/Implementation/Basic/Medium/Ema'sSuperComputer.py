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

    # for i in range(len(grid)):
    #     grid[i] = list(grid[i])
    #     grid[i].append('o')
    #     grid[i].insert(0,'o')
    # grid.append(['o' for i in range(len(grid[0]))])
    # grid.insert(0,['o' for i in range(len(grid[0]))])
    # for g in grid:
    #     print(''.join(g))
    # res = []
    # for i in range(1,len(grid)-1):
    #     for j in range(1, len(grid[0])-1):
    #         if grid[i][j]=='G':
    #             currCord = []
    #             currCord.append((i,j))
    #             area = 1
    #             start = 1
    #             res.append([area,currCord.copy()])
    #             while ((grid[i-start][j]=='G') & (grid[i+start][j]=='G') & (grid[i][j-start]=='G') & (grid[i][j+start]=='G')):
    #                 currCord.append((i-start,j))
    #                 currCord.append((i+start,j))
    #                 currCord.append((i,j-start))
    #                 currCord.append((i,j+start))
    #                 area+=4
    #                 start+=1
    #                 res.append([area,currCord.copy()])
    # result = 0      
    # for i in range(len(res)-1):
    #     for j in range(i+1,len(res)):
    #         if (len(set(res[i][1]).intersection(set(res[j][1])))==0) & (res[i][0]*res[j][0]>result):
    #             result = res[i][0]*res[j][0]
    # return result

def twoPluses(grid):
    # Write your code here
    grid = [list(row) for row in grid]
    res = set()
    res_val = 0 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'G':
                valid = True
                num = 1
                while valid:
                    if i-num>=0 and j-num>=0 and i<len(grid)-num and j<len(grid[i])-num:
                        if grid[i-num][j] == 'G' and grid[i+num][j] == 'G' and grid[i][j-num] == 'G' and grid[i][j+num] == 'G':
                            grid[i-num][j] = 'B'
                            grid[i+num][j] = 'B' 
                            grid[i][j-num] = 'B' 
                            grid[i][j+num] = 'B'
                            print(num, i, j)
                            # print(4*num+1)
                            res.add((i,j))
                            valid = True
                            num += 1
                        else:
                            valid = False
                    else:
                        valid = False

    return 4*num+1    
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
