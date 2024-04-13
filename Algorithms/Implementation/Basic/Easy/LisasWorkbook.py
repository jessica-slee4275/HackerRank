"""
input
5 3
4 2 6 1 10

STDIN       Function
-----       --------
5 3         n = 5, k = 3
4 2 6 1 10  arr = [4, 2, 6, 1, 10]

>>>
Lisa's workbook with n=5 chapters and a maximum of k=3 problems per page. 
Special problems are outlined in red, and page numbers are in yellow squares.

chapter1 = [p1, p2, p3, p4] -> 2 pages -> page1 [p1, p2, p3] page2 [p4] => page1 p1
chapter2 = [p1, p2] -> 1 page -> page3 [p1, p2]
chapter3 = [p1, p2, p3, p4, p5, p6] -> 2 pages -> page4 [p1, p2, p3] page5 [p4, p5, p6] => page5 p5 
chapter4 = [p1] -> 1 page -> page6 [p1]
chapter5 = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10] -> 4 pages -> page7 [p1, p2, p3] page8 [p4, p5, p6] page9 [p7, p8, p9] page10 [p10] => page9 p9, page10 p10

There are 4 special problems and thus we print the number 4 on a new line.

output
4
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    # Write your code here
    res = 0
    page = 1
    for i in arr:
        li = [ele for ele in range(1, i+1)]
        new_li = []
        si = 0
        ei = k
        set_range = len(li)//k if len(li)%k == 0 else len(li)//k +1
        for _ in range(set_range):
            if page in li[si:ei]:
                res += 1
            new_li.append(li[si:ei])
            si+=k
            ei+=k
            page+=1
    return res
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    print(str(result) + '\n')
