from collections import deque
from copy import deepcopy
f = open('input.txt','r')
cmd = deque([])
while True:
    line = f.readline()
    if not line: break
    cmd.append(line.strip())
dx,dy = [1,-1,0,0], [0,0,1,-1]


def dfs(x,y,dir,cnt=0):
    if x in [0,n-1] or y in [0,n-1]: # 도달 하면 
        if zido[x][y] == 0:
            return cnt
        else: return False
    nx,ny = x + dx[dir], y + dy[dir]
    if zido[nx][ny] == 0:
        return dfs(nx,ny,dir,cnt + 1)
    else: return False

def print_zido(zido):
    for item in zido:
        print(*item)

T = cmd.popleft()
for case in range(1,int(T) + 1):
    n = cmd.popleft(); n = int(n)
    zido = []
    for _ in range(n):
        cm = cmd.popleft()
        zido.append(list(map(int,cm.split())))

    # print_zido(zido)
    result = {}
    for i in range(n):
        for j in range(n):
            if i in [0,n-1] or j in [0,n-1]:
                continue
            if zido[i][j] == 1:
                tmp = []
                for k in range(4):
                    res = dfs(i,j,k)
                    if res:
                        tmp.append(res)
                    else:
                        tmp.append(0)
                result[f'{i}/{j}'] = deepcopy(tmp)
    ans = 0
    # for key,val in result.items():

    print(result)