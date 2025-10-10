'''
3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100
'''

import sys

input = sys.stdin.readline
N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
B = [list(map(int,input().split())) for _ in range(N)]
C = [[i + j for i, j in zip(A[k],B[k])] for k in range(N)]
for item in C:
    print(*item)