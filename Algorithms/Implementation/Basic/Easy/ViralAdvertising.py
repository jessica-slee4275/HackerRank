"""
input
3

>>> 3 friends share
n <= 50
Day Shared Liked     Cumulative
1      5     2(5//2)   2
2      6     3(6//2)   5(2+3)     (5//2)*3=6
3      9     4(9//2)   9(5+4)     (6//2)*3=9
4     12     6(12//2)  15(9+6)    (9//2)*3=12
5     18     9(18//2)  24(15+9)   (18//2)*3=18

Returns
int: the cumulative likes at that day

output
9
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
"""
Day Shared   Liked     Cumulative
1      5     2(5//2)   2
2      6     3(6//2)   5(2+3)     (5//2)*3=6
3      9     4(9//2)   9(5+4)     (6//2)*3=9
4     12     6(12//2)  15(9+6)    (9//2)*3=12
5     18     9(18//2)  24(15+9)   (18//2)*3=18
"""
def viralAdvertising(n):
    # Write your code here
    shared = 5
    cumulative = 2
    # print(shared, shared//2, cumulative)
    for _ in range(1, n):
        shared = (shared//2)*3
        liked = shared//2
        cumulative += liked
        # print(shared, liked, cumulative)
        
    return cumulative
if __name__ == '__main__':

    n = int(input().strip())

    result = viralAdvertising(n)

    print(str(result) + '\n')
