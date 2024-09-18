import sys
from collections import deque
input = sys.stdin.readline
N,M,K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

recent_dict = {}
for i in range(N):
    for j in range(M):
        recent_dict[str(i)+ ','+ str(j)] = 0

def get_live_space():
    result = []
    for i in range(N):
        for j in range(M):
            if graph[i][j]== 0:
                continue
            result.append((i,j))
    result.sort(key = lambda x : (graph[x[0]][x[1]], -recent_dict[f'{x[0]},{x[1]}'], -(x[0] + x[1]), -x[1]))
    return result

def bfs():
    st_x, st_y = live_space[0]
    ed_x, ed_y = live_space[-1]
    queue = deque()
    queue.append((st_x,st_y))
    is_success = False
    while queue:
        x,y = queue.popleft()
        # exit conditions

        if x == ed_x and y == ed_y:
            is_success = True
            break
            # lazer공격 ㄱㄱ

        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]: # 우하좌상
            nx,ny = (x + dx) % N , (y + dy)% M
            if graph[nx][ny] == 0: continue

            if len(visited[nx][ny]) == 0: # 방문하지 않았다면
                queue.append((nx,ny))
                visited[nx][ny] = (x,y)

    if is_success:
        # lazer 때리면 됨.
        f_set.add((st_x, st_y))
        f_set.add((ed_x, ed_y))
        x, y= ed_x , ed_y
        demage = graph[st_x][st_y]
        graph[x][y] = max(0,graph[x][y] - demage)
        while True:
            x,y = visited[x][y]
            if x == st_x and y == st_y:
                break
            graph[x][y] = max(0,graph[x][y] - demage//2)
            f_set.add((x,y))
        return True
    return False
def bomb():
    # 그냥 target지점 기준 8개만 진행하면 됨.
    # 공격자는 피해 안받음.
    st_x, st_y = live_space[0]
    ed_x, ed_y = live_space[-1]
    demage = graph[st_x][st_y]
    f_set.add((st_x, st_y))
    f_set.add((ed_x, ed_y))
    graph[ed_x][ed_y] = max(0,graph[ed_x][ed_y] - demage)
    for dx, dy in [(-1,-1),(-1,0),(-1,1),  (0,-1),(0,1),  (1,-1), (1,0), (1,1)]:
        nx,ny = (ed_x + dx) % N , (ed_y + dy)% M
        if nx == st_x and ny == st_y: continue
        if graph[nx][ny] == 0: continue
        graph[nx][ny] = max(0,graph[nx][ny] - demage//2) 
        f_set.add((nx,ny))
def print_graph(arr = None):
    if arr is None:
        for item in graph:
            print(*item)
    else:
        for item in arr:
            print(*item)

for T in range(1,K + 1):
    visited = [[[] for _ in range(M)] for _ in range(N) ] # visited 초기화
    f_set = set()
    # attacker and target select
    print('turn', T)
    live_space = get_live_space()
    if len(live_space) == 1:
        break
    print('live_space', live_space)
    print('recent_dict', recent_dict)
    st_x,st_y = live_space[0]
    
    graph[st_x][st_y] += (N + M)
    recent_dict[f'{st_x},{st_y}'] = T
    print('after_atack')
    print_graph()

    
    # attack
    is_success = bfs()
    if not is_success:
        bomb()
    print('after_atack')
    print_graph()
    
    for i in range(N):
        for j in range(M):
            if (i,j) in f_set: continue
            if graph[i][j] == 0: continue
            graph[i][j] += 1
    print('after_atack')
    print_graph()
    print('*'*100)
print(max(map(max, graph)))


