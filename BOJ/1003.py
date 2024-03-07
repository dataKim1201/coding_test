import sys
input = sys.stdin.readline
T = int(input())
p_sum = [[1,0],[0,1]]
for _ in range(T):
    n = int(input())
    for i in range(2,max(len(p_sum),n)+1):
        if i >= len(p_sum):
            # append
            p_sum.append([p_sum[i-2][0] + p_sum[i-1][0],p_sum[i-2][1] + p_sum[i-1][1]])
    print(p_sum[n][0], p_sum[n][1])