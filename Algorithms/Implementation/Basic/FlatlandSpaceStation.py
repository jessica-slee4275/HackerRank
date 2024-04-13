"""
It is not a circular route, so the first city doesn't connect with the last city. 
Determine the maximum distance from any city to its nearest space station.

input
5 2
0 4

STDIN   Function
-----   --------
5 2     n = 5, c[] size m = 2
0 4     c = [0, 4]

>>>
c[0] has distance 0km, as it contains a space station.
c[1] has distance 1km to the space station in c[0].
c[2] has distance 2km to the space stations in c[0] and c[4].
c[3] has distance 1km to the space station in c[4].
c[4] has distance 0km, as it contains a space station.
max(0, 1, 2, 1, 0) = 2

output
2

input
6 6
0 1 2 4 3 5

output
0
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    maxd = max(c[0], n-c[-1]-1)
    for i in range(len(c)-1):
        maxd = max((c[i+1]-c[i])//2, maxd)
    return maxd
if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    print(str(result) + '\n')

