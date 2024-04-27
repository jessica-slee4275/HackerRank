"""
Example
packets = [1, 2, 3, 4, 5]
channels = 2

At least one packet has to go through each of the 2 channels.
One maximal solution is to transfer packets {1, 2, 3, 4}
through channel 1 and packet {5} through channel 2

channel 1 = [1, 2, 3, 4]
channel 2 = [5]

The quality of transfer for channel 1 = (2+3)/2 = 2.5
The quality of transfer for channel 2 = 5
Sum = 2.5 + 5 = 7.5 -> rounds up to 8

input
5
2
2
1
5
3
2

output
7

>>>
packets[] size n = 5
packets = [2, 2, 1, 5, 3]
channels = 2

input
3
89
48
14
3

output 
151

intput
1
1
1

output
1
"""
def maximumQuality(packets, channels):
    packets = sorted(packets, reverse=True)
    res = []
    q = 0
    for _ in range(channels-1):
        res.append([packets[0]])
        packets.pop(0)
    res.append(packets)
    print(res)

    for r in res:
        if len(r) > 1:
            if len(r)%2 == 1:
                q += (r[len(r)//2])
            else:
                q += ((r[len(r)//2-1]+r[len(r)//2])/2)
        else:
            q += r[0]
    
    return q

if __name__ == '__main__':
    packets = []
    for _ in range(int(input())):
        packets.append(int(input()))
    print(maximumQuality(packets, int(input())))
