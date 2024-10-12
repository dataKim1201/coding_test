import sys
input = sys.stdin.readline
from collections import deque

class Monster:
    def __init__(self,c,d) -> None:
        self.init_map = self.initializing(c)
        self.enterance = d
    def initializing(self,c):
        return [(-1,c), (-2,c-1),(-2,c),(-2,c+1), (-3,c)] # 남, 서,본인, 동, 북
    def change_info(self,init_map,enterance):
        self.init_map = init_map
        self.enterance = enterance
    def is_inRange(self,x,y):
        return any([(x == i) and (y == j) for i,j in self.init_map])
    def get_enterance(self):
        return {0:self.init_map[4], 1:self.init_map[3], 2: self.init_map[0], 3: self.init_map[1] }[self.enterance] #0,1,2,3은 북, 동, 남, 서쪽

def movement(monster):
    init_map,enterance = monster.init_map, monster.enterance

    while all([(0 <= j < M) and (i < N-1) for i ,j in init_map]): # 
        print('init_map', init_map)
        if all([(graph[i+1][j] == 0) and (0<= j < M) and (i+1 < N) for i,j in init_map if 0<= i+1 < N ]): # graph가 범위안에 있고
            init_map = [ (i+ 1, j) for i,j in init_map]
        elif all([0 <= j-1 < M for i,j in init_map]) and all([(0<= j-1 < M) and (graph[i][j-1] == 0) for i,j in init_map if 0<= i < N]) and \
            all([(graph[i+1][j-1] == 0) and (i+1 < N) for i,j in init_map if 0<= i+1 < N]): # graph가 범위안에 있고

            init_map = [ (i+ 1, j-1) for i,j in init_map]
            enterance = (enterance - 1) %4
        elif all([0 <= j+1 < M for i,j in init_map]) and all([(0<= j+ 1 < M) and (graph[i][j+1] == 0) for i,j in init_map if 0<= i < N]) and \
            all([(graph[i+1][j+1] == 0) and (i+1 < N) for i,j in init_map if 0<= i+1 < N ]): # graph가 범위안에 있고
            init_map = [ (i+ 1, j+1) for i,j in init_map]
            enterance = (enterance + 1) %4
        else:
            print('here')
            break
    return init_map, enterance

def bfs(monster):
    x,y = monster.init_map[2] # 가장 자리
    queue = deque([])
    queue.append([x,y])
    visited = [[False] * M for _ in range(N)]
    res = x + 1
    new_monster = monster
    visited[x][y] = True
    while queue:
        print('queue',queue)
        x,y = queue.popleft()
        flag = False
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x + dx,y + dy
            if 0<=nx < N and 0<=ny <M and not visited[nx][ny] and graph[nx][ny] >=1:
                visited[nx][ny] = True
                res = max(res, nx + 1)
                if graph[nx][ny] == 2:
                    queue.append([nx,ny])
                if not monster.is_inRange(nx,ny): # out of range
                    print('nx,ny',nx,ny)
                    for new_monster in out_list: # 이전에만 존재하니께
                        if new_monster.is_inRange(nx,ny):
                            print('new_monster', new_monster.init_map)
                            flag = True
                            break
                
                    
        if flag:
            monster = new_monster
            print(monster.init_map)
            queue.append(monster.init_map[2]) # 1이어서 못갔었자나
    return res
def print_graph():
    for item in graph:
        print(*item)
N,M,K = map(int,input().split())
monster_list = []
for _ in range(K):
    c,d = map(int,input().split())
    monster_list.append(Monster(c-1,d))
out_list = []
graph = [[0]*M for _ in range(N)]
result = 0
for k in range(K):
    # monster는 업데이트 하지않음.
    new_graph = [item[:] for item in graph]
    monster = monster_list[k]
    # movement 진행
    init_map, enterance = movement(monster)
    # is success 확인
    print('k', k,'init_map', init_map)
    print('enterance', enterance)
    if any([(i < 0 ) or (j < 0) for i,j in init_map]):
        graph = [[0]* M for _ in range(N)]
        out_list = []
        continue
        # contin
    # assign
    monster.change_info(init_map,enterance)
    print('init_map',init_map)
    
    for i,j in init_map:
        graph[i][j] = 1
    ex,ey = monster.get_enterance()
    graph[ex][ey] += 1
    print_graph()
    # bfs
    res = bfs(monster)
    result += res
    print(f'{k} : res', res)
    out_list.append(monster)

print(result)
