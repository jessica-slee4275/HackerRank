"""
input
6 

output
     #
    ##
   ###
  ####
 #####
######
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here

    for _ in range(n):
        print(' '*(n-_-1)+'#'*(_+1))

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)