import sys
from collections import deque
# 접근법
'''
비상구: -11
사람: -11 < < 0
1. 동시에 이동한다 -> 복사 또는 0으로 새로운 arr을 만든다. -> 무조건
    다만 동시 이동이기 떄문에 
    new_arr[i][j] -= arr[i][j]로 업데이트는 한번에 해주어야 한다.
2. 이동의 우선순위는 상하/좌우 이다.

3. 회전할 사각형을 구하는 방법은
-> min([max(abs(person.x - dist.x), abs(person.y - dist.y)) for person in person_list])
이게 한변의 길이가 되어서 완전 탐색을 ㄱㄱ -> 출구랑 사람이 포함되어 있느냐 이런 느낌으로 다가

4. 회전 국룰은 좌표를 기준으로 작성해 보는 것

# 시계 방향
(0,0) (0,1) (0,2)      (2,0) (1,0) (0,0)
(1,0) (1,1) (1,2)  ->  (2,1) (1,1) (0,1)
(2,0) (2,1) (2,2)      (2,2) (1,2) (0,2)

(0,0) -> (0,2) -> j , N-i
(0,1) -> (1,2) -> j , N-i
(0,2) -> (2,2) -> j , N-i
(1,0) -> (0,1) -> j, N-i
(1,1) -> 
(1,2) -> (2,1) -> j, N-i

(2,0) -> (0,0) -> j, N-i
(2,2) -> (2,0) -> j, N-i

다만 부분회전인 경우 시작점 si, sj를 꼭 더해서 줘야 한다.
즉 그 결과 new_arr[si + i][sj + j] = arr[si + N -1-j][sj  + i]

# 반 시계 방향
(0,0) (0,1) (0,2)      (0,2) (1,2) (2,2)
(1,0) (1,1) (1,2)  ->  (0,1) (1,1) (2,1)
(2,0) (2,1) (2,2)      (0,0) (1,0) (2,0)

new_arr[i][j] = arr[j][N-i]

'''

input = sys.stdin.readline
class Runner:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        self.is_success = False
        self.move = 0
        self.check = False

def get_dist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)
def bfs():
    ex,ey = destination[0],destination[1]
    for runner in runner_list:
        if runner.is_success:
            continue
        x,y = runner.x, runner.y
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > 0:
                    continue # 벽 처리 했는딩
                if get_dist(nx,ny,ex,ey) < get_dist(runner.x,runner.y,ex,ey):
                    if nx == ex and ny == ey:
                        runner.is_success = True
                    # 이동 가능 하다면
                    runner.move += 1
                    runner.x = nx
                    runner.y = ny
                    break

def get_square():
    print('get square')
    length = 1e9
    for runner in runner_list:
        if runner.is_success: continue
        if length > max(abs(runner.x- destination[0]),abs(runner.y- destination[1])):
            length = max(abs(runner.x- destination[0]),abs(runner.y- destination[1]))
    print('length',length)
    print('destination',destination)
    r1,r2,c1,c2 = N,N,N,N
    for i in range(N):
        for j in range(N):
            if i + length >= N or j + length >= N:
                continue
            r1,r2,c1,c2 = i,i + length, j,j + length
            if r1 <= destination[0] <= r2 and \
                c1 <= destination[1] <= c2:
                for runner in runner_list:
                    if runner.is_success: continue
                    if r1 <= runner.x <= r2 and \
                        c1 <= runner.y <= c2:
                        return r1,r2,c1,c2
    return r1,r2,c1,c2

# def rotation(r1,r2,c1,c2):
#     length = r2-r1
#     change_list = []
#     for i in range(length):
#         for j in range(length):
#             change_list.append(graph[r1 + N -j -1][c1 + i])
#             if destination[0] == i and destination[1] == j:
#                 destination = [r1 + N -j , c1 + i ]
#             for runner in runner_list:
#                 if runner.is_success: continue
#                 if runner.x == i and runner.y == j:
#                     runner.x = r1 + N -j
#                     runner.y = c1 + i
#     for i in range(length):
#         for j in range(length):
#             graph[r1 + i][c1 + j] = change_list.pop(0)

def print_graph():
    for item in graph:
        print(*item)
def print_runner():
    for idx, runner in enumerate(runner_list):
        print(f'runner id {idx}',"runner.x,runner.y",runner.x,runner.y,'runner.move', runner.move,"runner.is_success", runner.is_success,"runner.check", runner.check)

N,M,K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
runner_list = []
for _ in range(M):
    x,y = map(int,input().split())
    runner_list.append(Runner(x-1,y-1))

destination = list(map(int,input().split()))
destination = [item -1 for item in destination]
for _ in range(K):

    print('*'*100)
    print(f'stage {_+ 1} destination {destination}')
    print('runner info')
    print_runner()
    # 선 이동
    bfs()
    print('after move runner info')
    if all([runner.is_success for runner in runner_list]): break
    print_runner()

    # 로테이션
    print('before rotation')
    print_graph()
    r1,r2,c1,c2 = get_square()
    print('rotation info', r1,r2,c1,c2)
    length = r2-r1 # 2
    change_list = []
    dest_change = False
    for runner in runner_list:
        runner.check = False
    for i in range(length +1):
        for j in range(length + 1):
            # x : 0 + 2  = 2
            # y : 0 + 2 - 0 
            change_list.append(graph[r1 + length -j ][c1 + i])
            if destination[0] == r1 + i and destination[1] == c1 + j and not dest_change:
                print('destination',destination)
                print('r1,j,c1,length,i', r1,j,c1,length,i)
                destination = [r1 + j ,c1 + length - i ]
                dest_change = True
                print('destination',destination)
            for runner in runner_list:
                if runner.is_success: continue
                
                if runner.x == r1 + i and runner.y == c1 + j:
                    if runner.check: 
                        print('check flag runner.x,runner.y', runner.x,runner.y)
                        continue
                    runner.check = True
                    print(runner.x,runner.y)
                    runner.x = r1 + j 
                    runner.y = c1 + length - i
                    print('r1 + j ', r1 + j )
                    print('c1 + length - i', c1 + length - i)
                    print(runner.x,runner.y)
    print('flag r1,c1, i,j', r1,c1, i,j)
    for i in range(length  + 1):
        for j in range(length + 1):
            graph[r1 + i][c1 + j] = change_list.pop(0)
    print('after rotation')
    print_graph()
    # destination change
    # rotation 한 스퀘어는 1씩 차감
    for i in range(r1,r2 + 1):
        for j in range(c1,c2 + 1):
            if graph[i][j] >= 1:
                graph[i][j] -= 1
    print('after deletion')
    print_graph()
    print('*'*100)
move_result = 0
for runner in runner_list:
    move_result += runner.move

print(move_result)
print(*list(map(lambda x: x + 1, destination)))