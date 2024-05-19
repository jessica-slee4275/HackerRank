"""

input
2
1 2 3
1 3 2

>>>
catA catB mouseC

[0    1    2    3     4]
[   catA catB mouseC   ]

catB catch mouseC -> print catB

[0    1    2     3     4]
[   catA mouseC catB    ]

catA and catB reach mouseC same time. mouseC escape -> print mouseC

output
Cat B
Mouse C
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if abs(x-z)<abs(y-z): return 'Cat A'
    if abs(x-z)>abs(y-z): return 'Cat B'
    return 'Mouse C'

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result + '\n')
