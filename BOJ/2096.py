import sys
input = sys.stdin.readline

n = int(input())
arr = [[0,0,0]]
for _ in range(n):
    cmd = list(map(int,input().split()))
    arr.append(cmd)

DP = [0,0,0]
DP2 = [0,0,0]
for i in range(1,n + 1):
    tmp1= max(DP[0]+ arr[i][0], DP[1] + arr[i][0])
    tmp2= max(DP[0]+ arr[i][1], DP[1] + arr[i][1],DP[2] + arr[i][1])
    tmp3= max(DP[2]+  arr[i][2], DP[1] + arr[i][2])
    DP = [tmp1,tmp2,tmp3]
    tmp1= min(DP2[0]+ arr[i][0], DP2[1] + arr[i][0])
    tmp2= min(DP2[0]+ arr[i][1], DP2[1] + arr[i][1],DP2[2] + arr[i][1])
    tmp3= min(DP2[2]+  arr[i][2], DP2[1] + arr[i][2])
    DP2 = [tmp1,tmp2,tmp3]
    # print(i,*DP2,arr[i])
max_result = max(DP)
min_result = min(DP2)
# print('max_result')
# for item in DP:
#     tmp = [it[0] for it in item]
#     print(*tmp)


# print('min_result')
# for item in DP:
#     tmp = [it[1] for it in item]
#     print(*tmp)

print(max_result,min_result)