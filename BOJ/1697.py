import sys

input = sys.stdin.readline
n,k =map(int,input().split())

dp = [999]*max(n+2,(k//n +1 )*n + 1)
dp[n] = 0
dp[n-1] = 1
dp[n+1] = 1
for idx, i in enumerate(range(n*2, (k//n +1 )*n +1,n)):
    # print('2L ',i)
    dp[i] = 1*(idx + 1)
for i in range(n,(k//n +1 )*n + 1,1 if n <k else -1):
    print(i)
    print(dp[i], dp[i//2]+1 ,dp[i-1]+1,dp[i+1]+1)
    if i %2==0:
        dp[i] = min(dp[i], dp[i//2]+1 ,dp[i-1]+1,dp[i+1]+1)
    elif i %2 != 0:
        dp[i] = min(dp[i],dp[i-1]+1,dp[i+1]+1)
print(dp[k])
