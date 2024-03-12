import sys
input = sys.stdin.readline
n = int(input())
# n = int(10e6)
dp = [0] * (n+1)
for i in range(2, n+1): # 하면 n까지 탐색
    tmp = [dp[i-1] + 1] # 1을 빼서 하나 더 추가했을 때
    if i % 2 == 0:
        tmp.append(dp[i//2] + 1)
    if i % 3 == 0:
        tmp.append(dp[i//3] + 1)
    dp[i] = min(tmp)
print(dp[n])    