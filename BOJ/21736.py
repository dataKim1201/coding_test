import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
zido = [list(input().strip()) for _ in range(n)]
dx,dy = [1,-1,0,0], [0,0,-1,1]
def bfs(x,y):
    queue = deque([(x,y)])
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    ans = 0
    while queue:
        x,y = queue.popleft()
        for way in range(4):
            nx,ny = x + dx[way], y + dy[way]
            if 0<= nx < n and 0<=ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if zido[nx][ny] == 'O':
                    queue.append((nx,ny))
                
                elif zido[nx][ny] == 'P':
                    queue.append((nx,ny))
                    ans += 1
    if ans == 0:
        return 'TT'
    return ans

for i in range(n):
    for j in range(m):
        if zido[i][j] == 'I':
            print(bfs(i,j))
            break

