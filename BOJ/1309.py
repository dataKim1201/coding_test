import sys
input = sys.stdin.readline
n = int(input())

DP = [[1,1,1]] 
for i in range(2,n + 1):
    tmp1 = sum(DP[-1])
    tmp2 = DP[-1][0] + DP[-1][2]
    tmp3 = DP[-1][1] + DP[-1][0]
    DP.append([tmp1,tmp2,tmp3])
print(sum(DP[n]))