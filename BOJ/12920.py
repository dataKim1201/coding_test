import sys
import math
input = sys.stdin.readline
n , k = map(int,input().split())
graph = []
for _ in range(n):
    m,v,c = map(int,input().split())
    # tmp = [[m,v,c]]
    i =1
    while c > 0:
        tmp = min(i,c)
        graph.append([m*tmp, v*tmp])
        i *=2
        c -= tmp

def dp(arr,k):
    dp = [0]*(k+1)
    for i in range(len(arr)):
        for j in range(k,0,-1):
            if j >=arr[i][0]: # 작다면
                dp[j] = max(dp[j],(dp[j-arr[i][0]] + arr[i][1]))
            else:
                break
    return dp[k]
# print(graph)
print(dp(graph, k))


# 2 10000
# 1 1 10000
# 5 100 100
# 9500 + 10000
# 100을 넘기는 문제가 있음.