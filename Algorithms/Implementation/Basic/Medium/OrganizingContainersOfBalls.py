"""
David has several containers, each with a number of balls in it. 
He has just enough containers to sort each type of ball 
he has into its own container. 
David wants to sort the balls using his sort method.

David wants to perform some number of swap operations such that:

- Each container contains only balls of the same type.
- No two balls of the same type are located in different containers.
- Returns 'Possible' if all '0' in one container and all '1' in another container, 
if not 'Impossible'

Example containers = [[1, 4], [2, 3]]
Before swap
     Matrix M
             types
             0   1
containers 0 1   4
           1 2   3
container 0 [0, 1, 1, 1, 1] container 1 [1, 1, 1, 0, 0]

After swap
     Matrix M
             types
             0   1
containers 0 2   3
           1 1   4
container 0 [0, 1, 1, 1, 0] container 1 [1, 1, 1, 1, 0]
input
2
2
1 1
1 1
2
0 2
1 1

>>>
Before swap
     Matrix M
             types
             0   1
containers 0 1   1
           1 1   1

container 0 [0, 1] container 1 [1, 0]            
container0[1] -> container1[1]
container1[1] -> container0[1]

After swap
     Matrix M
             types
             0   1
containers 0 2   0
           1 0   2

container 0 [0, 0] container 1 [1, 1]                      
Possible
Impossible
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    n = len(container)
    container_capacity = [0]*n
    ball_counts = [0]*n

    for i in range(n):
        for j in range(n):
            container_capacity[i] += container[i][j]
            # the number of 'j' kind balls in 'i' container
            ball_counts[j] += container[i][j]
            # total number of 'j' kind balls
    container_capacity.sort()
    ball_counts.sort()

    if container_capacity == ball_counts:
        return "Possible"
    else:
        return "Impossible"
    
if __name__ == '__main__':

    q = int(input().strip())
    res = []
    
    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        res.append(result)

    print('\n'.join(res))
