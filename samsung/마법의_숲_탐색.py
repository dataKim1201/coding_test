import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
class Monster:
    def __init__(self,c,d) -> None:
        self.enterance = d
        self.init_map = [(-1,c),(-2,c-1),(-2,c),(-2,c+1), (-3,c)]
monster_list = []
for _ in range(K):
    c,d = map(int,input().split())
    monster_list.append(Monster(c-1,d))

result = 0
graph = [[0] * M for _ in range(N)]
# r 에  + 1 항상 해줘야 함.
def exit_latitude(d, center):
    x,y = center
    cx,cy = {0 : (-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}[d]
    return x + cx, y + cy

def monster_move(monster,idx = 2):
    global graph
    init_map = monster.init_map
    enterance = monster.enterance
    flag = True
    while flag:
        # print('init_map', init_map, 'flag' ,flag)
        # forward
        if all([ (i + 1 < N and 0 <= j < M) for i,j in init_map]) and all([graph[i+1][j] <= 0  for i,j in init_map if 0 <= i <N and 0 <=j < M ]):
            init_map = [(i+1, j) for i,j in init_map]
        # left 
        elif all([ (i + 1 < N and 0 <= j-1 < M) and (graph[i][j-1] <= 0)  for i,j in init_map]) and all([graph[i+1][j-1] <= 0  if i >= 0 else True for i,j in init_map ]):
            # init
            init_map = [(i+1, j-1) for i,j in init_map]
            enterance = (enterance - 1) % 4
        # right
        elif all([ (i + 1 < N and 0 <= j+1 < M) and (graph[i][j+1] <= 0)  for i,j in init_map]) and all([graph[i+1][j+1] <= 0  if i >= 0 else True for i,j in init_map]): # 서쪽 하늘
            init_map = [(i+1, j+1) for i,j in init_map]
            enterance = (enterance + 1) % 4
        else:
            flag = False
    print('init_map result', *init_map, 'enterance', enterance)
    return init_map,enterance
    # return init_map[2]

from collections import deque
def bfs(item):
    ox,oy = item
    queue = deque([])
    queue.append((ox,oy,False))
    visited = [[False] * M for _ in range(N)]
    res = ox + 1
    visited[ox][oy] = True
    print('ox,oy',ox,oy)
    while queue:
        x,y,move = queue.popleft()
        print('x,y,res',x,y,res, 'ox,oy', ox,oy, queue)
        for dx,dy in [(1,0),(-1,0),(0,-1),(0,1)]:
            nx,ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] >= 1:
                visited[x][y] = True
                res = max(res,nx+1)
                # out of range check
                # 2상관 없이 탐색
                if graph[nx][ny] == 2 or move:
                    queue.append([nx,ny,True])
                # elif move:
                #     queue.append([nx,ny, False])
                # if move == 2: # 탈출구에서 온놈이라면
                #     queue.append([nx,ny,graph[nx][ny]])
        # 여기서 out of range가 되면 range변경해주기


    return res

def print_graph():
    for item in graph:
        print(*item)
for _ in range(K):
    print('monster number', _)
    monster = monster_list[_]
    # monster move
    init_map,enterance = monster_move(monster,_)
    if not all([(0 <= i < N and 0 <= j < M) for i,j in init_map]):
        graph = [[0] * M for _ in range(N)]
        # 계산하지 않고 이동
        continue

    # 할당 해주자.
    for i,j in init_map:
        graph[i][j] = 1
    ex,ey = exit_latitude(enterance, init_map[2])
    graph[ex][ey] += 1
    print_graph()
    # item movement
    res = bfs(init_map[2])
    print(f'number {_}s result: {res} and total {result + res}')
    print('*'*100)
    result += res

print(result)