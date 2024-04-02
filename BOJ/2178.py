# 1은 이동 가능하고
# 0은 이동 불가능 
# 최소 이동거리를 반환하여라

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
zido = [list(map(int,input().strip())) for _ in range(n)]
visited = [ [False]*m for _ in range(n)]

def bfs(zido, visited):
    queue = deque([[0,0,1]])
    visited[0][0] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while queue:
        x,y,cnt = queue.popleft()
        if x == n-1 and y == m-1:
            return cnt
        for dnx, dny in zip(dx,dy):
            nx = x + dnx
            ny = y + dny
            if nx >= 0 and nx < n and ny >=0 and ny <m:
                if not visited[nx][ny] and zido[nx][ny] == 1:
                   visited[nx][ny] = True
                   queue.append([nx,ny,cnt + 1])
print(bfs(zido,visited))