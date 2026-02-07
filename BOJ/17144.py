import sys
from copy import deepcopy

input = sys.stdin.readline

def print_zido(zido):
    for item in zido:
        print(*item)

R,C,T = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(R)]

air_position = []
for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            air_position.append((i,j))


# T 시간 동안 작동이 이뤄짐
directions = [(1,0), (-1,0), (0,1), (0,-1)]

# 확산
def air_diffusion():
    global graph
    new_graph = [[ 0 for _ in range(C)] for _ in range(R)]

    def diff(x,y):
        org_val = graph[x][y]
        div_val =  org_val // 5
        for dx,dy in directions:
            nx,ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                new_graph[nx][ny] += div_val
                org_val -= div_val
        new_graph[x][y] += org_val

    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                diff(i,j)
            elif graph[i][j] == -1:
                new_graph[i][j] = -1
    graph = deepcopy(new_graph)

def air_operation(air_position):
    global graph
    new_graph = deepcopy(graph)
    up_idx, down_idx = air_position
    
    # up_operation
        # right : 공기 청정기 부터 그행 오른쪽 끝까지 
    x,y = up_idx
    new_graph[x][y] = -1
    new_graph[x][y + 1] = 0
    for i in range(y + 2, C):
        new_graph[x][i] = graph[x][i-1]
    left = deepcopy(graph[x][-1])
    
        # up
    new_graph[x -1][-1] = left
    for i in range(x -2, -1, -1):
        new_graph[i][-1] = graph[i+1][-1]
    left = deepcopy(graph[0][-1])
        # left
    new_graph[0][-2] = left
    for i in range(C-3, -1, -1):
        new_graph[0][i] = graph[0][i+1]
    left = deepcopy(graph[0][0])
        # down
    new_graph[1][0] = left
    for i in range(2, x):
        new_graph[i][0] = graph[i-1][0]

    # down_operation
    x,y = down_idx
    new_graph[x][y] = -1
    new_graph[x][y + 1] = 0
    # right : 공기 청정기 부터 그행 오른쪽 끝까지. 
    for i in range(y + 2, C):
        new_graph[x][i] = graph[x][i-1]
    left = deepcopy(graph[x][-1])
        # down
    new_graph[x+1][-1] = left
    
    for i in range(x +2 , R):
        new_graph[i][-1] = graph[i-1][-1]
    left = deepcopy(graph[-1][-1])

        # left
    new_graph[-1][-2] = left
    for i in range(C-3, -1, -1):
        new_graph[-1][i] = graph[-1][i+1]
    left = deepcopy(graph[-1][0])

        # up 
    new_graph[-2][0] = left
    for i in range(R-3, x, -1):
        new_graph[i][0] = graph[i+1][0]
    graph = deepcopy(new_graph)


for i in range(T):
    air_diffusion()
    air_operation(air_position)
print(sum(sum(graph,[])) + 2)
