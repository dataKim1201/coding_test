import sys
input = sys.stdin.readline
C,N = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

def dynamic(arr):
    DP = [0] * (C + 1)
    for i in range(len(arr)):
        for j in range(C, 0,-1):
            if j >= arr[i][1]:
                DP[j] = max(DP[j], DP[j-arr[i][1]] + arr[i][0])
    # print(*DP)
    return DP[C]

print(dynamic(arr))