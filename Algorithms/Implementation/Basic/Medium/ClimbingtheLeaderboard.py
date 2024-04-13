"""
An arcade game player wants to climb to the top of the leaderboard and track their ranking. 
The game uses Dense Ranking, so its leaderboard works like this:

- The player with the highest score is ranked number  on the leaderboard.
- Players who have equal scores receive the same ranking number, 
and the next player(s) receive the immediately following ranking number.

ranked = [100, 90, 90, 80] --> 1, 2, 2, 3
player = [70, 80, 105] --> print 4, 3, 1


input
7
100 100 50 40 40 20 10
4
5 25 50 120

output
6
4
2
1
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
from bisect import bisect_right
def climbingLeaderboard(ranked, player):
    # Write your code here
    """
    # bisect_right
    data = [1, 3, 5, 7, 9]
    position = bisect_right(data, 6) # 3
    
    """
    # print(sorted(set(ranked)))
    res = []
    scores = sorted(set(ranked))
    for p in player:
        res.append(len(scores)-bisect_right(scores, p)+1)
    return res
if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print('\n'.join(map(str, result)))
