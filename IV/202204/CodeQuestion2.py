"""
Example
4
2
3
2
1

power = [2, 3, 2, 1]

n = 4 servers
Power[0, 0] = min([2])*sum([2])                   = 2*2 = 4
Power[0, 1] = min([2, 3])*sum([2, 3])             = 2*5 = 10
Power[0, 2] = min([2, 3, 2])*sum([2, 3, 2])       = 2*7 = 14
Power[0, 3] = min([2, 3, 2, 1])*sum([2, 3, 2, 1]) = 1*8 = 8
Power[1, 1] = min([3])*sum([3])                   = 3*3 = 9
Power[1, 2] = min([3, 2])*sum([3, 2])             = 2*5 = 10
Power[1, 3] = min([3, 2, 1])*sum([3, 2, 1])       = 1*6 = 6
Power[2, 2] = min([2])*sum([2])                   = 2*2 = 4
Power[2, 3] = min([2, 1])*sum([2, 1])             = 1*3 = 3
Power[3, 3] = min([1])*sum([1])                   = 1*1 = 1

Overall sum : 69

input
3
2
1
3

>>> power [] size n = 3
power = [2, 1, 3]

output
27

input
2
2
4

output
32
"""
def findTotalPower(power):
    res = 0
    for i in range(len(power)):
        for j in range(i, len(power)):
            res += min(power[i:j+1])*sum(power[i:j+1])
            # print(i, j, min(power[i:j+1])*sum(power[i:j+1]))
    return res

if __name__ == '__main__':
    power = []
    for _ in range(int(input())):
        power.append(int(input()))
    print(findTotalPower(power))
