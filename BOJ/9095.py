import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    case = int(input())
    dp = [0,1,2,4]
    for i in range(4,case + 1):
        dp.append(dp[i-3] + dp[i-2] + dp[i-1])
    print(dp[case])