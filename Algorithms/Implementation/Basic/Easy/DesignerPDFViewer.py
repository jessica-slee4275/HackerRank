"""
The first line contains 26 space-separated integers 
describing the respective heights of each consecutive lowercase English letter, 
ascii[a-z].

The second line contains a single word 
consisting of lowercase English alphabetic letters.

input
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc

>>> a=1, b=3, c=1
tallest letter = b -> 3mm

3*1mm*3mm = 9mm^2

output
9

input
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
zaba

>>> tallest letter = z -> 7mm
4*1mm*7mm = 28mm^2

output
28

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#
import string 

def designerPdfViewer(h, word):
    # Write your code here
    dict_h = {list(string.ascii_lowercase)[i]: h[i] for i in range(len(h))}

    m = 0 
    for w in word:
        m = max(dict_h[w], m)

    return len(word)*m
if __name__ == '__main__':

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(str(result) + '\n')
