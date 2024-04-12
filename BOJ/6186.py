import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
zido = [input() for _ in range(n)]

visited = [[False] * m  for _ in range(n)]
dx,dy = [1,-1,0,0], [0,0,1,-1]
def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx,ny= x + dx[k], y + dy[k]
            if 0<= nx < n and 0<=ny < m and not visited[nx][ny] and zido[nx][ny] == '#':
                visited[nx][ny] = True
                queue.append((nx,ny))

def dfs(x,y):
    if x < 0 or x >=n or y <0 or y >=m:
        return 
    if not visited[x][y] and zido[x][y] == '#':
        visited[x][y] = True
        for k in range(4):
            dfs(x + dx[k], y + dy[k])
cnt = 0
for i in range(n):
    for j in range(m):
        if zido[i][j] == '#' and not visited[i][j]:
            dfs(i,j)
            cnt += 1
print(cnt)
