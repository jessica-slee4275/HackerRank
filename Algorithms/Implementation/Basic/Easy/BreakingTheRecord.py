"""
>>> scores = [12, 24, 10, 24]
                                     Count
    Game  Score  Minimum  Maximum   Min Max
     0      12     12       12       0   0
     1      24     12       24       0   1
     2      10     10       24       1   1
     3      24     10       24       1   1

An array with the numbers of times she broke her records. 
Index 0 is for breaking most points records, 
and index 1 is for breaking least points records.

input
9
10 5 20 20 4 5 2 25 1

output
2 4

input
10
3 4 21 36 10 28 35 5 24 42

output
4 0
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min_score = scores[0]
    max_score = scores[0]
    min_cnt = 0
    max_cnt = 0
    for i in range(1, len(scores)):
        if min_score > scores[i]:
            min_cnt += 1
            min_score = min(min_score, scores[i])
        if max_score < scores[i]:
            max_cnt += 1
            max_score = max(max_score, scores[i])
    return  max_cnt, min_cnt

    # print('Game  Score  Minimum  Maximum   Min    Max')
    # min_score = 0
    # max_score = 0
    # print(0, '\t',  scores[0], '\t',scores[0], '\t',scores[0], '\t', min_score, '\t', max_score)
    # cnt = 1
    # lmin = []
    # lmax = []
    # lmin.append(scores[0])
    # lmax.append(scores[0])
    # res_min_score = 0
    # res_max_score = 0
    # while cnt < len(scores):
    #     # print(lmin[:cnt], scores[cnt])
    #     min_val = min(min(lmin[:cnt]), scores[cnt])
    #     lmin.append(min_val)
    #     max_val = max(max(lmax[:cnt]), scores[cnt])
    #     lmax.append(max_val)
    #     min_score = 0
    #     max_score = 0
    #     if min_val == scores[cnt] and min_val < min(scores[:cnt]): 
    #         min_score = 1
    #         res_min_score += 1
    #     if max_val == scores[cnt] and max_val > max(scores[:cnt]):
    #         max_score = 1
    #         res_max_score += 1

    #     print(cnt, '\t',  scores[cnt], '\t', min_val, '\t', max_val, '\t', min_score, '\t', max_score)
    #     cnt += 1
    # return res_max_score, res_min_score
if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))