import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
zido = [list(map(int,input().strip())) for _ in range(n)]


def bfs():
    x,y = 0,0
    cnt = 1
    visited = [[[0,0] for _ in range(m)] for _ in range(n)]
    visited[x][y][int(False)] = 1
    queue = deque([(x,y,False)])
    dx, dy= [1,-1,0,0], [0,0,1,-1]
    tt = 1
    while queue:
        x,y,used = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][int(used)]
        for way in range(4):
            nx, ny = x + dx[way], y + dy[way]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][int(used)] == 0: # and (visited[nx][ny] < 0 or visited[nx][ny] > visited[x][y] + 1)
                if zido[nx][ny] == 1 and not used:
                    visited[nx][ny][int(True)] = visited[x][y][int(used)] + 1
                    queue.append((nx,ny, True))

                elif zido[nx][ny] == 0: # 아직 방문하지 않았다면
                    visited[nx][ny][int(used)] = visited[x][y][int(used)] + 1
                    queue.append((nx,ny, used))    
    return -1


print(bfs())
# for item in visited:
#     print(*item)
# 6 5
# 00000
# 11110
# 00000
# 01111
# 01111
# 00010