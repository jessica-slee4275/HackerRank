"""
Given an array of strings of digits, try to find the occurrence of a given pattern of digits. 
In the grid and pattern arrays, each string represents a row in the grid. 
For example, consider the following grid:

1234567890  
0987654321  
1111111111  
1111111111  
2222222222  

The pattern array is:
876543  
111111  
111111

input
2
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530
15 15
400453592126560
114213133098692
474386082879648
522356951189169
887109450487496
252802633388782
502771484966748
075975207693780
511799789562806
404007454272504
549043809916080
962410809534811
445893523733475
768705303214174
650629270887160
2 2
99
99

>>> 
first 
'
9505
3845
3530
' 
in 
'
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
'

output
YES
NO

second
'
99
99
'
in
'
400453592126560
114213133098692
474386082879648
522356951189169
887109450487496
252802633388782
502771484966748
075975207693780
511799789562806
404007454272504
549043809916080
962410809534811
445893523733475
768705303214174
650629270887160
'

input
1
2 6
999999
121211
2 2
99
11

output
YES
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

# timeout
# def gridSearch(G, P):
#     # Write your code here
#     res = False
#     for r in range(len(G)-len(P)+1):
#         temp = []
#         for i in range(len(P)):
#             temp.append([index for index in range(len(G[r+i])) if G[r+i].startswith(P[i], index)])
#         if len(temp) == len(P):
#             compare = set(temp[0])
#             for t_i in range(1, len(temp)):
#                 compare = compare.intersection(set(temp[t_i]))
#             if len(compare) == 1:
#                 res = True
#     return 'YES' if res else 'NO'


def gridSearch(G, P):
    res = False
    for r in range(len(G) - len(P) + 1):  
        for c in range(len(G[r]) - len(P[0]) + 1):  
            if G[r][c:c+len(P[0])] == P[0]: 
                found = True
                for i in range(1, len(P)):  
                    if G[r+i][c:c+len(P[0])] != P[i]:
                        found = False
                        break
                if found:  
                    res = True
                    break
        if res:
            break
            
    return 'YES' if res else 'NO'

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        print(result + '\n')
