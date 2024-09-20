from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
visited = [[False] * m for _ in range(n)]
def bfs():
    queue = deque([[0,0,0]])
    directions = [(1,2),(1,-2),(2,1),(2,-1),(-1,-2),(-1,2),(-2,-1),(-2,1)]
    while queue:
        x,y,cnt = queue.popleft()
        visited[x][y] = True
        for dx,dy in directions:
            nx,ny = x + dx, y + dy
            if 0<=nx<n and 0<=ny < m and not visited[nx][ny]:
                queue.append([nx,ny,cnt + 1])
    if all([all(item) for item in visited]):
        return 'T'+ str(cnt)
    else:
        return 'F' + str(cnt)
print(bfs())