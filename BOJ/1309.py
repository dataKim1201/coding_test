import sys
n = int(input())

DP = [1,1,1]
for i in range(n-1):
    tmp2 = DP[0] + DP[2]
    tmp3 = DP[1] + DP[2]
    tmp1 = sum(DP)
    DP = [tmp2,tmp3,tmp1]

print(sum(DP)%9901)