"""
3 5
member 1: 10101
member 2: 11110
member 3: 00010

3 5
10101
11110
00010

Members Subjects
(1,2)   [1,2,3,4,5]
(1,3)   [1,3,4,5]
(2,3)   [1,2,3,4]

return [5, 1] 5subjects & 1team

input
4 5
10101
11100
11010
00101

>>> '1' means the subject is known while '0' means it is not
The first is the maximum number of topics known, 
and the second is the number of teams that know that number of topics

output
5
2
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    # res = [0,0]
    # for i in range(len(topic)-1):
    #     for j in range(i+1, len(topic)):
    #         index = 0
    #         sub = 0 
    #         while index < len(topic[0]):
    #             if int(topic[i][index])+int(topic[j][index]) >= 1:
    #                 sub +=1
    #             index += 1
    #         if res[0] < sub:
    #             res[0] = sub
    #             res[1] = 1
    #         elif res[0] == sub:
    #             res[1] += 1
    # return res
    max_sub = 0
    max_teams = 0

    for i in range(len(topic)-1):
        for j in range(i+1, len(topic)):
            sub = bin(int(topic[i], 2) | int(topic[j], 2)).count('1')
            if sub > max_sub:
                max_sub = sub
                max_teams = 1
            elif max_sub == sub:
                max_teams += 1
                
    return [max_sub, max_teams]

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    print('\n'.join(map(str, result)))
