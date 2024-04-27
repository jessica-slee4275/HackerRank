"""
Example

row - User
col - book

110
110
001

M[i][j] if j was gifted a book by i
User 0 has gifted a book to user 1 and so they are connected [0][1], 
while person 2 has not received a book from anyone or gifted book to anyone.
M[i][j] = 1 if i == j 

input
4
1100
1110
0110
0001

>>> size of related[] n = 4
related = ['1100', '1110', '0110', '0001']
[0][1]
[1][0]
(related[0], related[1])
[1][2]
[2][1]
(related[1], related[2])

set{related[0], related[1], related[2]}
set{related[3]}

output
2

input
5
10000
01000
00100
00010
00001

>>>
set{related[0]}
set{related[1]}
set{related[2]}
set{related[3]}
set{related[4]}

output
5
"""
def countGroups(related):
    arr = [[int(e) for e in r] for r in related]
    
    direct_related = set()
    for i in range(len(related)):
        for j in range(len(related)):
            if i != j and arr[i][j] == 1 and arr[i][j] == arr[j][i]:
                direct_related.add(i)
                direct_related.add(j)
    
    return len(related)-len(direct_related)+1 if direct_related else len(related)-len(direct_related)
if __name__ == '__main__':
    related = []
    for _ in range(int(input())):
        related.append(input())
    print(countGroups(related))
