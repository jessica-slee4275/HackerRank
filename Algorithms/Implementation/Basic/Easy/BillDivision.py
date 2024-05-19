"""
Anna and Brian split bill at a dinner

input
4 1
3 10 2 9
12

>> anna eat except bill[1]=10, 
total 3+2+9 = 14
each payment 14/2 = 7
charged 12
change 12 - 7 = 5

output
5

input
4 1
3 10 2 9
7

>> anna eat except bill[1]=10, 
total 3+2+9 = 14
each payment 14/2 = 7
charged 7
no change -> return 'Bon Appetit'

output
Bon Appetit
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    change = b-(sum(bill)-bill[k])/2
    if change == 0: print('Bon Appetit')
    else: print(int(change))
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)