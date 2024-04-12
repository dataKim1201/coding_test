import sys
from collections import deque
input = sys.stdin.readline
case = {
    'uno': [[(0,0),(0,1),(1,0),(1,1)]],
    'duo': [[(0,0),(1,0),(1,1),(2,1)], [(0,1),(0,2),(1,0),(1,1)], [(0,0),(0,1),(1,1),(1,2)], [(0,1),(1,0),(1,1),(2,0)]],
    'tuo': [[(0,0),(1,0),(2,0),(2,1)],[(0,1),(1,1),(2,0),(2,1)],[(0,0),(1,0),(1,1),(1,2)],[(0,2),(1,0),(1,1),(1,2)],[(0,0),(0,1),(1,0),(2,0)],[(0,0),(0,1),(1,1),(2,1)],[(0,0),(1,0),(0,1),(0,2)],[(0,0),(0,1),(0,2),(1,2)]],
    'quo': [[(0,0),(0,1),(0,2),(0,3)],[(0,0),(1,0),(2,0),(3,0)]],
    'ooo': [[(0,0),(0,1),(0,2),(1,1)],[(0,1),(1,0),(1,1),(1,2)],[(0,0),(1,0),(1,1),(2,0)],[(0,1),(1,0),(1,1),(2,1)]]
}

n,m = map(int,input().split())
zido = [list(map(int,input().split())) for _ in range(n)]
res = 0
dx,dy = [0,0,1,-1],[1,-1,0,0]
def calc_max(case):
    visited= [[False] * m  for _ in range(n)]
    x,y= 0,0
    visited[x][y] = True
    queue = deque([(x,y)])
    ans = 0
    while queue:
        x,y = queue.popleft()
        tmp = calc_tmp(x,y,case)
        if tmp:
            ans = max(ans,tmp)
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <=nx < n and 0<= ny <m and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True
    return ans

def calc_tmp(x,y,case):
    tmp = 0 
    for item in case:
        fx,fy = x + item[0], y + item[1]
        if 0 <=fx < n and 0<=fy <m:
            tmp += zido[fx][fy]
        else:
            return False
    return tmp

for key,vals in case.items():
    for val in vals: # 대해서 19개 밖에 안됨.
        tmp = calc_max(val)
        res = max(tmp,res)
print(res)