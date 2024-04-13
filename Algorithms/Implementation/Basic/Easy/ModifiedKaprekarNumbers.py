"""
kaprekarNumbers
ex. 5: 5^2 = 25 ==> 2+5 = 7 ==> 5!=7 No kaprekarNumbers
ex. 9: 9^2 = 81 ==> 8+1 = 9 ==> 9==9 kaprekarNumbers
ex. 45: 45^2 = 2025 ==> 20+25 = 45 ==> 45==45 kaprekarNumbers

If no modified Kaprekar numbers exist in the given range, 
print INVALID RANGE.

input
1
100

STDIN   Function
-----   --------
1       p = 1
100     q = 100

>>> 1 < n < 100
output
1 9 45 55 99
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#
def kaprekarNumbers(p, q):
    # Write your code here
    result = []
    for num in range(p, q+1):
        d = len(str(num))
        square = str(num*num)
        r = square[-d:]
        l = '0' if len(square) == d else square[:-d]
        if int(l) + int(r) == num:
            result.append(num)
    if result:
        print(*result)
    else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
