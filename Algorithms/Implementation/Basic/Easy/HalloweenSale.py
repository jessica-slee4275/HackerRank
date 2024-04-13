"""
int p: price of the first game
int d: discount from the previous game price
int m: minimum cost of a game
int s: starting budget

ex.
20 3 6 70
20, 17, 14, 11, 8, 6, 6, 6, 6, 6, 6
20 + 17 + 14 + 11 + 8 = 70
returns 5

input
20 3 6 80

output
6
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    res = 0
    game_prices = [p]
    price = p-d

    if p>s : return 0

    while price >= m:
        game_prices.append(price)
        price -= d
    
    while s > 0 and len(game_prices)>=1:
        res += 1
        s -= game_prices[0]
        game_prices = game_prices[1:]
        print(s, game_prices)
    res += s//m

    return res
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    print(str(answer) + '\n')
