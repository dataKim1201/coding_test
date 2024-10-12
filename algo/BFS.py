# 탐색 조건, 방문 단위ㅌ, 취할 행동
# import sys
# input =sys.stdin.readline
# # BOJ 2468: 안전 영역

# # min max 잡고 크기가 몇개 생기는 지 최대 개수를 계산하라고 함.
# from collections import deque
# N = int(input())
# graph = [list(map(int,input().split())) for _ in range(N)]
# st,ed = min(sum(graph,[])), max(sum(graph,[]))

# def bfs(rain):
#     current = [ [i- rain for i in item ] for item in graph]
#     visited =[[False] * N for _ in range(N)]
#     cnt  = 0
#     for i in range(N):
#         for j in range(N):
#             if current[i][j] >= 1 and not visited[i][j]:
#                 cnt += 1
#                 queue = deque()
#                 queue.append([i,j])
#                 visited[i][j] = True
#                 while queue:
#                     x,y = queue.popleft()
#                     for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
#                         nx,ny = x + dx, y + dy
#                         if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and current[nx][ny] >= 1:
#                             queue.append([nx,ny])
#                             visited[nx][ny] = True
#     return cnt

# res = 1
# for rain in range(st,ed):
#     # ed 일때는 어차피 0임
#     res = max(res, bfs(rain))
# print(res)


# BOJ 14502: 연구소
# 0은 빈 칸, 1은 벽, 2는 바이러스
# 바이러스: 2보다 크거나 같고, 10보다 작거나 같은 자연수
# 바이러스는 한번에 쫙 퍼진다.
# 빈 칸의 개수는 3개 이상이다.
# 완탐 해야되나.
# from collections import deque
# import glob
# import sys
# input = sys.stdin.readline

# N,M = map(int,input().split())
# graph = [list(map(int,input().split())) for _ in range(N)]

# def bfs(block_ls,virus_ls):
#     current = [item[:] for item in graph]
#     for i,j in block_ls:
#         current[i][j] = 1
#     visited = [[False]*M for _ in range(N)]
#     queue = deque()
#     # print('*'*100)
#     # for item in current:
#     #     print(*item)

#     for i,j in virus_ls:
#         queue.append((i,j))
#         visited[i][j] = True
#     while queue:
#         x,y = queue.popleft()
#         for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
#             nx,ny = x + dx, y  + dy
#             if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and current[nx][ny] == 0:
#                 current[nx][ny] = 2
#                 visited[nx][ny] = True
#                 queue.append((nx,ny))
#     # print('*'*100)
#     # for item in current:
#     #     print(*item)
#     return sum([item.count(0) for item in current])
# block_ls_all = []
# virus_ls = []

# for i in range(len(graph)):
#     for j in range(len(graph[0])):
#         if graph[i][j] == 0:
#             block_ls_all.append((i,j))
#         elif graph[i][j] == 2:
#             virus_ls.append((i,j))
# result = 0
# def bt(virus_ls,v = [False] * len(block_ls_all)):
#     global result
#     if sum(v) == 3:
#         block_ls =[]
#         for idx, i in enumerate(v):
#             if i:
#                 block_ls.append(block_ls_all[idx])
#         result = max(bfs(block_ls,virus_ls),result)
#         return 
#     for i in range(len(block_ls_all)):
#         if not v[i]:
#             v[i] = True
#             bt(virus_ls,v)
#             v[i] = False
#     return 
#     # for i in range(len(block_ls_all)):
#     #     for j in range(i + 1, len(block_ls_all)):
#     #         for k in range(j + 1, len(block_ls_all)):
#     #             block_ls = [block_ls_all[i], block_ls_all[j], block_ls_all[k]]
#     #             result = max(bfs(block_ls, virus_ls), result)
# bt(virus_ls)
# print(result)

# BOJ 4963
# import sys
# from collections import deque
# input = sys.stdin.readline
# def bfs(i,j):
#     queue = deque()
#     queue.append((i,j))
#     v[i][j] = True
#     while queue:
#         x,y = queue.popleft()
#         for dx,dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
#             nx,ny = x + dx, y + dy
#             if 0 <= nx < N and 0 <= ny < M and not v[nx][ny] and graph[nx][ny] == 1:
#                 v[nx][ny] = True
#                 queue.append((nx,ny))

# while True:
#     M,N = map(int,input().split())
#     if N == 0 or M == 0:
#         break
#     if N == 1 and M == 1:
#         n =int(input())
#         print(n)
#         continue
#     graph = [list(map(int,input().split())) for _ in range(N)]
#     v = [[False]*M for _ in range(N)]
#     result = 0
#     for i in range(N):
#         for j in range(M):
#             if not v[i][j] and graph[i][j] == 1:
#                 result += 1
#                 bfs(i,j)
#     print(result)


# 연구소 v3
# 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.
# 이때는 탐색하던 숫자를 할당하면 됨!
from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

def bfs(virus_ls):
    current = [item[:] for item in graph]
    queue = deque()
    for i,j in virus_ls:
        queue.append((i,j))
        current[i][j] = 0
    print('*'*100)
    for item in current:
        print(*item)
    while queue:
        x,y = queue.popleft()
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x + dx, y  + dy
            if 0 <= nx < N and 0 <= ny < N and current[nx][ny] > 0 and current[x][y]+ 1 < current[nx][ny]:
                if current[nx][ny] == N*N: # 비활성화 바이러스
                    current[nx][ny] = current[x][y]
                    queue.appendleft((nx,ny))
                else:
                    current[nx][ny] = current[x][y] + 1 
                    queue.append((nx,ny))
    print('*'*100)
    for item in current:
        print(*item)
    return max(sum(current,[]))
virus_ls = []
inf = N*N + 2
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 2:
            virus_ls.append((i,j))
            graph[i][j] = N*N # 마지막에 1빼라
        elif graph[i][j] == 1:
            graph[i][j] = -1
        elif graph[i][j] == 0:
            graph[i][j] = inf
result = inf

K = len(virus_ls)
# def bt(virus_ls,v = [False] * K ):
#     global result
#     if sum(v) == M: # 얘네로 탈출 ㄱㄱ
#         cand_ls =[]
#         for idx, i in enumerate(v):
#             if i:
#                 cand_ls.append(virus_ls[idx])
#         result = min(bfs(cand_ls),result)
#         print(v,result)
#         return 
#     for i in range(len(virus_ls)):
#         if not v[i]:
#             v[i] = True
#             bt(virus_ls,v)
#             v[i] = False
#     return 

# bt(virus_ls)
from itertools import combinations
result = inf
for cand_ls in combinations(virus_ls,M):
    tmp = bfs(cand_ls)
    print(cand_ls, tmp)
    result = min(tmp, result)
print(result)
result = 0 if result == N*N else result
result = -1 if result == inf else result
print(result)