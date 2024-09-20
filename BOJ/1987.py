import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
zido  = [input().strip() for _ in range(N)]
visited = [False for _ in range(ord('A'), ord('Z') + 1)]
dx, dy = [1,-1,0,0], [0,0,1,-1]

max_cnt = 1
visited[ord(zido[0][0]) - 65] = True
def find(x,y,cnt = 1):
    global max_cnt
    if cnt > max_cnt:
        max_cnt = cnt
    for i in range(4):
        nx, ny = dx[i] + x,dy[i] + y
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[ord(zido[nx][ny]) - 65]:
                visited[ord(zido[nx][ny]) - 65] = True
                find(nx,ny,cnt + 1)
                visited[ord(zido[nx][ny]) - 65] = False
find(0,0)
print(max_cnt)