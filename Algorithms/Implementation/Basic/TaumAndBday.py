"""

int b: the number of black gifts
int w: the number of white gifts
int bc: the cost of a black gift
int wc: the cost of a white gift
int z: the cost to convert one color gift to the other color

b*bc + w*wc

ex. 
b=3
w=5
bc=3
wc=4
z=1

b*bc+w*wc = 3*3+5*4 = 29
b*bc+w*z+w*bc = 3*3+5*1+5*3 = 29
b*z+b*wc+w*wc = 3*1+3*4+5*4 = 35

input
5       
10 10   
1 1 1   
5 9     
2 3 4   
3 6     
9 1 1   
7 7     
4 2 1   
3 3     
1 9 2   

STDIN   Function
-----   --------
5       t = 5
10 10   b = 10, w = 10
1 1 1   bc = 1, wc = 1, z = 1
5 9     b = 5, w = 5
2 3 4   bc = 2, wc = 3, z = 4
3 6     b = 3, w = 6
9 1 1   bc = 9, wc = 1, z = 1 if bc > wc+z, 9*1+3*1
7 7     b = 7, w = 7
4 2 1   bc = 4, wc = 2, z = 1 if bc > wc+z, (wc+z=3) 7*3+7*2
3 3     b = 3, w = 3
1 9 2   bc = 1, wc = 9, z = 2

output
20
37
12
35
12
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z
#

def taumBday(b, w, bc, wc, z):
    # Write your code here
    res = b*bc+w*wc
    res = min(b*bc+w*z+w*bc, res) 
    res = min(b*z+b*wc+w*wc, res) 

    return res
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        print(str(result) + '\n')
