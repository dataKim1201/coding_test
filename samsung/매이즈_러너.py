import sys
input = sys.stdin.readline
class Runner:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        self.move = 0
        self.is_success = False
        self.changed = False
def l1_dist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)
def get_minimum_square(x1,y1,x2,y2):
    if x1 == x2:
        print('here')
        print('x1,x2,y1,y2', x1,x2,y1,y2)
        if x1 - abs(y1-y2) >= 0:
            return x1 - abs(y1-y2), x1,min(y1,y2), max(y1,y2)
        else:
            return x1, x1 + abs(y1-y2),min(y1,y2), max(y1,y2)
    if y1 == y2:
        print('here2')
        print('x1,x2,y1,y2', x1,x2,y1,y2)
        if y1 -abs(x1-x2) >= 0:
            return min(x1,x2), max(x1,x2), y1 -abs(x1-x2), y1 
        else:
            return min(x1,x2), max(x1,x2), y1, y1 + abs(x1-x2)
    # 모두 다르다면?
    if abs(x1-x2) > abs(y1-y2):
        # x1기준으로 square
        return min(x1,x2), max(x1,x2), min(y1,y2), min(y1,y2) + abs(min(y1,y2) - abs(x1-x2))
    else:
        # y1 기준으로 square
        return min(x1,x2), min(x1,x2) + abs(min(x1,x2) - abs(y1-y2)),min(y1,y2), max(y1,y2)
    
def get_square():
    r1,r2,c1,c2 = N,N,N,N
    min_distant = N
    ex,ey = destination[0], destination[1]
    # dist가 제일 작은 runner를 찾고
    # destination과 runner를 이으는 최소각 정사각형을 만들어라.
    for runner in runner_list:
        if runner.is_success: continue
        x,y = runner.x, runner.y
        if (l1_dist(x,y,ex,ey) < min_distant) or \
            (l1_dist(x,y,ex,ey) == min_distant and  min(x,ex) < r1) or \
            (l1_dist(x,y,ex,ey) == min_distant and  min(y,ey) < c1):
            # 지금 조건에 부합한다면?
            # r1,r2,c1,c2를 저장.
            min_distant = l1_dist(x,y,ex,ey)
            r1,r2,c1,c2 = min(x,ex), max(x,ex), min(y,ey),max(y,ey)
    r1,r2,c1,c2 = get_minimum_square(r1,c1,r2,c2)           
    return r1,r2,c1,c2

N,M,K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
runner_list = []
for _ in range(M):
    x,y = map(int,input().split())
    runner_list.append(Runner(x-1,y-1))
destination = list(map(int,input().split()))
destination = [item - 1 for item in destination]

def move():
    ex,ey = destination[0], destination[1]
    for runner in runner_list:
        if runner.is_success:
            continue
        x,y = runner.x, runner.y
        for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
            nx,ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > 0: continue
                if l1_dist(nx,ny,ex,ey) < l1_dist(x,y,ex,ey):
                    if nx == ex and ny == ey:
                        runner.is_success = True
                    runner.move += 1
                    runner.x = nx
                    runner.y = ny
                    break

def print_graph():
    for item in graph:
        print(*item)

def print_runner():
    for runner in runner_list:
        print(f'coordinate: {runner.x}, {runner.y} move: {runner.move}, is_success: {runner.is_success}')

for T in range(K):
    print('*'*100)
    print(f'{T} stage go!!')
    # move first
    for runner in runner_list:
        runner.changed = False
    print('before run')
    print_runner()
    move()
    print('after_run')
    print_runner()
    # get square
    r1,r2,c1,c2 = get_square()
    print('r1,r2,c1,c2', r1,r2,c1,c2)
    # rotation
    tmp_list = []
    for j in range(c1, c2 + 1):
        for i in range(r2,r1 - 1, -1):
            tmp_list.append(int(graph[i][j]))
    for i in range(r1,r2 + 1):
        for j in range(c1,c2 + 1):
            graph[i][j] = tmp_list.pop(0)
    print('after rotation')
    print_graph()
    # deletion
    for i in range(r1,r2 + 1):
        for j in range(c1,c2 + 1):
            if graph[i][j] > 0:
                graph[i][j] -= 1
            for idx,  runner in enumerate(runner_list):
                if runner.is_success or runner.changed : continue
                if i == runner.x and j == runner.y:
                    print(f'chage runner info idx : {idx}')
                    print('i,j, -> changed', i,j, '->', j, c2 -i)
                    runner_list[idx].x = j
                    runner_list[idx].y = c2 - i
                    runner_list[idx].changed = True
            if i == destination[0] and j == destination[1]:
                destination = [j, c2 - i]
    print('after deletion')
    print_graph()
    print_runner()
    print('destination', *destination)
    print('*'*100)

move_result = 0
for runner in runner_list:
    move_result += runner.move
print(move_result)
print(*[item +1 for item in destination])