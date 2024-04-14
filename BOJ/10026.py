import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
n = int(input())

zido = [list(input().strip()) for _ in range(n)]
visited = [ [False] * n for _ in range(n)]
blind = [ [False] * n for _ in range(n)]
def print_zido(zido):
    for item in zido:
        print(*item)

def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True
    dnx,dny =[0,0,1,-1],[1,-1,0,0]
    color = zido[x][y]
    while queue:
        x,y = queue.popleft()
        for dx,dy in zip(dnx,dny):
            nx,ny = x +dx, y + dy
            if nx >=0 and nx <n  and ny >=0 and ny <n and not visited[nx][ny]:
                if zido[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    return None
def blind_bfs(x,y):
    queue = deque([(x,y)])
    blind[x][y] = True
    dnx,dny =[0,0,1,-1],[1,-1,0,0]
    color = zido[x][y]
    while queue:
        x,y = queue.popleft()
        for dx,dy in zip(dnx,dny):
            nx,ny = x +dx, y + dy
            if nx >=0 and nx <n  and ny >=0 and ny <n and not blind[nx][ny]:
                if color in ["R",'G'] and zido[nx][ny] in ["R", "G"]:
                    blind[nx][ny] = True
                    queue.append((nx,ny))
                elif color == zido[nx][ny]: # B의 경우
                    blind[nx][ny] = True
                    queue.append((nx,ny))
    return None
res = 0
blind_res = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            res += 1
            bfs(i,j)
        if not blind[i][j]:
            blind_res += 1
            blind_bfs(i,j)

print(res,blind_res)