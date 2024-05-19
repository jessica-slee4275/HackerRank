"""
input
7 11 
5 15
3 2
-2 2 1
5 -6

s t
a b
m n
apples
oranges

contains 'm' space-separated integers denoting the respective distances 
that each apple falls from point 'a'
contains 'n' space-separated integers denoting the respective distances 
that each apple falls from point 'b'

s: integer, starting point of Sam's house location.
t: integer, ending location of Sam's house location.
a: integer, location of the Apple tree.
b: integer, location of the Orange tree.
apples: integer array, distances at which each apple falls from the tree.
oranges: integer array, distances at which each orange falls from the tree.


>>>
The red region denotes the house, where 's' is the start point, 
and t is the endpoint. The apple tree is to the left of the house, 
and the orange tree is to its right.

Assume the trees are located on a single point, 
where the apple tree is at point 'a', and the orange tree is at point 'b'.

When a fruit falls from its tree, it lands 'd' units of distance 
from its tree of origin along the x-axis. 
*A negative value of 'd' means the fruit fell 'd' units to the tree's left, 
and a positive value of 'd' means it falls 'd' units to the tree's right. *

output
1
1
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    res = [0, 0]
    for apple in apples:
        if a + apple >= s and a + apple <= t:
            res[0] += 1
    for orange in oranges:
        if b + orange >= s and b + orange <= t:
            res[1] += 1
    for r in res:
        print(r)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
