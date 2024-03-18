import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().strip().split())
zido = [list(map(int,input().strip().split())) for _ in range(n)]
dist = [ [-1] * m  for _ in range(n)]

def bfs(x,y):
    visited = [ [False] *m for _ in range(n)]
    visited[x][y] = True
    dist[x][y] = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    queue = deque([(x,y)])
    while queue:
        cx,cy = queue.popleft()
        for i,j in zip(dx,dy):
            nx,ny = cx + i, cy + j
            if any([nx < 0 , nx >= n , ny < 0 , ny >= m]):
                continue
            if zido[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx,ny))
                dist[nx][ny] = dist[cx][cy] + 1
                visited[nx][ny] = True
    return 

for ak in range(n):
    for aj in range(m):
        if zido[ak][aj] == 2:
            bfs(ak,aj)
        elif zido[ak][aj] == 0:
            dist[ak][aj] = 0 
for item in dist:
    print(*item)


# 15 15
# 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
# 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
    


