import sys
from collections import deque,defaultdict
input = sys.stdin.readline
INF = int(1e9)
n = 500
graph = [[0] * (n + 1) for _ in range(n + 1)]
dx,dy = [1,-1,0,0], [0,0,1,-1]
visited = [[False] * (n + 1) for _ in range(n + 1)]
def dijkstra():
    queue = deque([[0,0,0]])
    while queue:
        x,y,cnt= queue.popleft()
        visited[x][y] = True
        if x == n-1 and y == n-1:
            return cnt
        for i in range(4):
            nx,ny =  x + dx[i], y + dy[i]
            if 0<= nx < n and 0<= ny < n and not visited[nx][ny]:
                if graph[nx][ny] ==1: # 죽음의 길이 아니라면
                    queue.append([nx,ny,cnt + 1])
                elif graph[nx][ny] == 0:
                    queue.appendleft([nx,ny,cnt])
    return -1


danger = int(input())
danger_ls = [list(map(int,input().split())) for _ in range(danger)]
for d_item in danger_ls:
    x1,y1,x2,y2 = d_item
    for i in range(min(x1,x2), max(x1,x2) + 1):
        for j in range(min(y1,y2), max(y1,y2) + 1):
            graph[i][j] = 1

death = int(input())
death_ls = [list(map(int,input().split())) for _ in range(death)]
for d_item in death_ls:
    x1,y1,x2,y2 = d_item
    for i in range(min(x1,x2), max(x1,x2) + 1):
        for j in range(min(y1,y2), max(y1,y2) + 1):
            visited[i][j] = True

print(dijkstra())