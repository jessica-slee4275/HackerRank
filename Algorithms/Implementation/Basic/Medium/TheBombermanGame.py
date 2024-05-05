"""
Bomberman is immune to bombs, so he can move freely throughout the grid. 
Here's what he does:

1. Initially, Bomberman arbitrarily plants bombs in some of the cells, the initial state.
2. After one second, Bomberman does nothing.
3. After one more second, Bomberman plants bombs in all cells without bombs, thus filling the whole grid with bombs. No bombs detonate at this point.
4. After one more second, any bombs planted exactly three seconds ago will detonate. Here, Bomberman stands back and observes.
5. Bomberman then repeats steps 3 and 4 indefinitely.

input
6 7 3
.......
...O...
....O..
.......
OO.....
OO.....

>>>

r = rows
c = columns
n = n seconds
. empty
O bomb

STDIN           Function
-----           --------
6 7 3           r = 6, c = 7, n = 3
.......         grid =['.......', '...O...', '....O..',
...O...                '.......', 'OO.....', 'OO.....']
....O..
.......
OO.....
OO.....

bomb timer
  0s    ->   1s
0000000    0000000
0003000    0002000
0000300 -> 0000200
0000000    0000000
3300000    2200000
3300000    2200000

  2s    ->   3s
3333333    2220222
3331333    2200022
3333133 -> 2220002
3333333    0022022
1133333    0002222
1133333    0002222

output
OOO.OOO
OO...OO
OOO...O
..OO.OO
...OOOO
...OOOO

"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#
# def countUpdate(grid, sec):
#     for index in range(len(grid)):
#         grid[index] = grid[index].replace('2','1')
#         grid[index] = grid[index].replace('3','2')
#         if sec%2 == 0:
#             grid[index] = grid[index].replace('0','3')
#     return grid

# def bomberMan(n, grid):
#     # Write your code here
#     sec = 1
#     # 0 sec
#     for index in range(len(grid)):
#         grid[index] = grid[index].replace('O','3')
#         grid[index] = grid[index].replace('.','0')

#     while sec <= n:
#         if sec%3 == 0: 
#             # 3 sec
#             updated_list = [list(string) for string in grid]
#             for i in range(len(updated_list)):
#                 for j in range(len(updated_list[i])):
#                     if updated_list[i][j] == '1':
#                         if i>0 and updated_list[i-1][j] != '1': 
#                             updated_list[i-1][j] = '0' # up
#                             grid[i-1] = ''.join(updated_list[i-1])
#                         if i<len(updated_list)-1 and updated_list[i+1][j] != '1': 
#                             updated_list[i+1][j] = '0' # down
#                             grid[i+1] = ''.join(updated_list[i+1])
#                         if j>0 and updated_list[i][j-1] != '1': 
#                             updated_list[i][j-1] = '0' # left
#                         if j<len(updated_list[i])-1 and updated_list[i][j+1] != '1': 
#                             updated_list[i][j+1] = '0' # right
#                         updated_list[i][j] = '0'
                
#                 temp = ''.join(updated_list[i])
                
#                 grid[i] = temp.replace('3','2')
#                 print('i>>', grid[i])
#         else:    
#             grid = countUpdate(grid, sec)
#         print(sec, 's')
#         print('\n'.join(grid))
#         sec += 1
#     for index in range(len(grid)):
#         grid[index] = grid[index].replace('0','.')
#         grid[index] = grid[index].replace('3','O').replace('2','O').replace('1','O')    
#     return grid

def bomberMan(n, grid):
    # Write your code here
    def bom(idx):
        i, j = idx
        grid[i][j] = '.'
        if i > 0:
            grid[i-1][j] = '.'
        if i < len(grid) - 1:
            grid[i+1][j] = '.'
        if j > 0:
            grid[i][j-1] = '.'
        if j < len(grid[0]) - 1:
            grid[i][j+1] = '.'
    
    if n < 2:
        return grid
        
    grid = [list(row) for row in grid]
    
    while n >= 11:
        n -= 4
    
    bomlist = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                bomlist.append([i, j])
            else:
                grid[i][j] = 'O'
    print()
    print(bomlist)
    for g in grid:
        print(''.join(g))
        
    for x in range(3, n+1):
        if x % 2 != 0:
            for idx in bomlist:
                bom(idx)
            bomlist = []
            
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 'O':
                        bomlist.append([i, j])
            print(x, 'sec', bomlist)
            for g in grid:
                print(''.join(g))
        else:

            grid = [['O'] * len(row) for row in grid]
            print(x, 'sec')
            for g in grid:
                print(''.join(g))

    
    return [''.join(row) for row in grid]

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    for r in result:
        print(''.join(r))
