import sys
input = sys.stdin.readline

M,N,K = map(int,input().split())
square_idx = [list(map(int,input().split())) for _ in range(K)]

graph = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]

from collections import deque
dx,dy = [0,0,1,-1], [1,-1,0,0]
def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    cnt = 1
    while queue:
        cx,cy = queue.popleft()
        
        for d_x,d_y in zip(dx,dy):
            nx,ny = cx + d_x, cy + d_y
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 0:
                cnt += 1
                visited[nx][ny] = True
                queue.append([nx,ny])
    return cnt


for indices in square_idx:
    y1,x1,y2,x2 = indices
    for x in range(x1,x2):
        for y in range(y1,y2):
            # 중복 우려
            graph[x][y] += 1
            visited[x][y] = True
answer = 0
ans_ls = []
for i in range(M):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 0:
            visited[i][j] = True
            res = bfs(i,j) # Number of square
            answer += 1
            ans_ls.append(res)
# print_graph()

print(answer)
print(*sorted(ans_ls))