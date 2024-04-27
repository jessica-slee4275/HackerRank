"""
- Intersection of A and B is null
- Union A and B is equal to original array
- The number of elements in subset A is minimal
- The sum of A's weights is greater than the sum of B's weights.

Example

n = 5
arr = [3, 7, 5, 6, 2]

The 2 subsets in arr that satisfy the conditions for A are [5, 7] and [6, 7]:
- A is minimal size 2
- Sum(A) = (5+7)=12 > Sum(b) = (2+3+6)=11
- Sum(A) = (6+7)=13 > Sum(b) = (2+3+5)=10
- Intersection of A and B is null and their union is equal to arr
- The subset A where the sum of its weight is maximal is [6,7]

Complete the minimalHeaviestSetA function
minimalHeaviestSetA has the following parameter(s):
    int arr[]: an integer array of the weights of each item in the set
Returns:
    int[]: an integer array with the values of subset A

input
6
5
3
2
4
1
2

>>> arr[] size n = 6
arr[] = [5, 3, 2, 4, 1, 2]

output
4
5
"""
def minimalHeaviestSetA(l):
    l = sorted(l, reverse=True)
    i = 2
    while i < len(l):
        if sum(l[0:i]) > sum(l[i:]):
            return sorted(l[0:i])
        i += 1
    return None

if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        l.append(int(input()))
    print('\n'.join(map(str, minimalHeaviestSetA(l))))
