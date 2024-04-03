import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
zido = [ list(map(int,input().strip())) for _ in range(n)]
visited = [ [False] * n for _ in range(n)]

def bfs(x,y,visited):
    cnt = 1
    dsx = [1,-1,0,0]
    dsy = [0,0,1,-1]
    visited[x][y] = True
    queue = deque([[x,y]])
    while queue:
        x,y = queue.popleft()
        for dx,dy in zip(dsx,dsy):
            nx = x + dx
            ny = y + dy
            if nx >=0 and nx < n and ny >= 0 and ny < n:
                if zido[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    cnt += 1
    return cnt, visited
result = []
for i in range(n):
    for j in range(n):
        if zido[i][j] == 1 and not visited[i][j]:
            res, visited = bfs(i,j,visited)
            result.append(res)

print(len(result))
print('\n'.join(map(str,sorted(result))))