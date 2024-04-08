import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

zido = [list(map(int,input().split())) for _ in range(n)]

def bfs(x,y):
    queue = deque([(x,y,0,0,2)]) # cnt, 먹은 개수
    # visited 할필요 없음
    # zido 어떻게 반영할지? -> 
    dnx = [-1,1,0,0]
    dny = [0,0,1,-1]
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    while queue:
        x,y,cnt,e_cnt,size = queue.popleft()
        # 종료조건 -> 더 이상 먹을 수 있는 물고기가 없다면?
        if sum(visited,[]) == len(visited) * len(visited[0]):
            break
        for i,j in zip(dnx,dny):
            nx = x + i
            ny = y + j
            if nx >=0 and nx <n and ny >=0 and ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                else:
                    continue
                if zido[nx][ny] == 0: # 그냥 이동 0이니까
                    queue.append([nx,ny,cnt + 1,e_cnt,size])
                elif size < zido[nx][ny]: # 못먹는 감 -> 이동도 불가
                    continue
                elif size > zido[nx][ny]: # 먹어야지
                    zido[nx][ny] = 0
                    if size == e_cnt + 1:
                        queue.append([nx,ny,cnt + 1,e_cnt+1,size + 1])
                    else: # 사이즈는 안커짐
                        queue.append([nx,ny,cnt + 1,e_cnt+1,size])
                elif size == zido[nx][ny]:
                    zido[nx][ny] = 0
                    queue.append([nx,ny,cnt + 1,e_cnt,size])
    if e_cnt == 0:
        return 0
    return cnt
                    



for i in range(n):
    for j in range(n):
        if zido[i][j]== 9:
            res =bfs(i,j)
            break
print(res)
    
        