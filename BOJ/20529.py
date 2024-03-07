import sys
from itertools import combinations
input = sys.stdin.readline

T = int(input())

def calc_distance(arr):
    res = 999
    idxs =[[0,1],[1,2],[2,0]]
    print(arr)
    for item in arr:
        for idx_1,idx_2 in idxs:
            A,B = item[idx_1],item[idx_2]
            tmp = 0
            for i in range(4):
                if A[i] != B[i]:
                    tmp += 1
        res = min(res,tmp)
    return res

for _ in range(T):
    n = int(input())
    mbti = input().split()
    res = combinations(mbti,3)
    print(calc_distance(list(res)))

