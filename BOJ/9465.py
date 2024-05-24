import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    DP = [[0,0] for _ in range(n) ] # list of case : case1. a를 선택, case2. b를 선택  case3 모두 선택 안함.
    DP[0][0] = a[0]
    DP[0][1] = b[0]
    DP[1][0] = b[0] + a[1]
    DP[1][1] = a[0] + b[1]
    for i in range(2,n):
        DP[i][0] = max(DP[i-1][1], DP[i-2][0], DP[i-2][1]) + a[i] 
        DP[i][1] = max(DP[i-1][0], DP[i-2][0], DP[i-2][1]) + b[i] 
    print(max(DP[-1]))