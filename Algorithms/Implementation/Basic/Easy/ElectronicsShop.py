"""
input
10 2 3
3 1
5 2 8

>>> 
budget, the number of keyboard models, the number of usb drives
keyboard models []
drive drive []

output
9

2nd keyboard + 3rd usb drive = 8 + 1 = 9

input
5 1 1
4
5

>>> 
cannot buy in budget, returns -1

output
-1
"""


#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
import numpy
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    if min(keyboards)+min(drives) > b : return -1
    res = []
    for k in keyboards:
        for d in drives:
            if k+d <= b: res.append(k+d)
    # difference_arr = numpy.absolute(numpy.array(res)- b)
    # index = difference_arr.argmin()
    # return res[index]
    
    return sorted(res)[-1]

if __name__ == '__main__':

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(str(moneySpent) + '\n')