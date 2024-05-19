"""
The first line of input contains t, the number of test cases.

Each test case consists of two lines.

The first line has two space-separated integers, n and k, 
the number of students (size of a) and the cancellation threshold.
The second line contains  space-separated integers (a[1], a[2], ..., a[n]) 
that describe the arrival times for each student.

input
2
4 3
-1 -3 4 2
4 2
0 -1 2 1

>>> first test case k = 3, professor wants at least 3 students in attendance, 
but only 2 have arrived on time (-3, -1) -> class cancelled
first test case k = 2, professor wants at least 2 students in attendance, 
but only 2 have arrived on time (0, -1) -> class is not cancelled

output
YES
NO
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
    # Write your code here
    on_time = 0
    for student in a:
        if student <= 0:
            on_time += 1
    if on_time < k: return "YES"
    else: return "NO"

if __name__ == '__main__':

    t = int(input().strip())
    result = []
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result.append(angryProfessor(k, a))

    print(result)
