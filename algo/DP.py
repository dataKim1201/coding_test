#### BOJ 1504 ####
# 특이한 최단 경로
# import sys
# input = sys.stdin.readline
# N,M = map(int,input().split())
# inf = 1e9
# DP = [[inf] * N for _ in range(N)]
# for _ in range(M):
#     s,e,c = map(int,input().split())
#     DP[s-1][e-1] = c
# v1,v2 = [item-1 for item in map(int,input().split())]

# def dijkstra(start,end):
#     queue = []
#     dist = [inf] * (N)
#     dist[start] = 0
#     queue.append(start)
#     while queue:
#         x = queue.pop(0)
#         for i in range(N):
#             if i != x and dist[i] > dist[x] + DP[x][i]:
#                 dist[i] = dist[x] + DP[x][i]
#                 queue.append(i)
#     return dist[end]
# # min(DP[0][v1] + DP[v1][v2] +DP[v2][N-1], DP[0][v2] + DP[v2][v1] +DP[v1][N-1])
# ans = min(dijkstra(0,v1) + dijkstra(v1,v2) + dijkstra(v2,N-1), dijkstra(0,v2) + dijkstra(v2,v1) + dijkstra(v1,N-1))
# if ans >= inf:
#     print(-1)
# else:
#     print(ans)


### FIBO EXP ###
# # 최적 부분 구조 & 중복 되는 부분 문제
# DP = [0] * 100
# def fibo(n):
#     if n <0: return False
#     if n <3: return 1
#     # n = n-1 + n-2일때
#     # 메모리 버켓은 2개만 필요하고
#     # n-1,n-2가 중복되고 있음을 알 수 있음.
#     DP = [1,1]
#     res = 0
#     for _ in range(3,n):
#         # N번 까지 진행
#         res = sum(DP)
#         # 이런 식으로 업데이트를 하자.
#         DP = [DP[-1],res]
#     return sum(DP)
# for i in range(3,100):
#     print(i,':',fibo(i))


# 개미 전사
# 조건이 arr 돌면서 얻을 수 있는 이득의 최대를 반환
from typing import List

# def ant_solder(arr:List):
#     DP = [0] * (len(arr)+ 2)
#     # 1 D arr
#     DP[0] = arr[0]
#     DP[1] = arr[1]
#     for i in range(2,len(arr)):
#         print(DP,i)
#         DP[i] = max(DP[i-1], DP[i - 2]+ arr[i]) # 어디로 갈래?
#     return DP[len(arr)-1]
# arr = [1,1,1,1,1, 1000,1]
# print(ant_solder(arr))
inf = 1e9
def make_one(numbers):
    if numbers <= 3:
        return 1
    if numbers % 2 == 0 and numbers >= 4:
        return min(make_one(numbers-1) + 1, make_one(numbers//4) + 1, make_one(numbers//2) + 1)
    elif numbers % 3 == 0:
        return min(make_one(numbers-1) + 1, make_one(numbers//3) + 1)
    else:
        return make_one(numbers-1) + 1


    # for k in range(1,5):
    #     DP[k] = 1
    # for i in range(5,numbers + 1):
    #     if i % 2 == 0:
    #         DP[i] = min(DP[i-1], DP[i//4], DP[i//2] ) + 1
    #     elif i % 3 == 0:
    #         DP[i] = min(DP[i-1], DP[i//3] ) + 1
    #     print(DP,i)
    # return DP[numbers]
numbers = 18
DP = [inf] * (numbers+1)
print(make_one(20))

