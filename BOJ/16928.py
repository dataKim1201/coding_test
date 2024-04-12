import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
lift = {}
for _ in range(n):
    k,v = map(int,input().split())
    lift[k] = v
snake = {}
for _ in range(m):
    k,v = map(int,input().split())
    snake[k] = v
visited = [False] * 101
zido_cnt = [0] * 101
def bfs():
    queue = deque([1])
    while queue:
        now = queue.popleft()
        for i in range(1,7):
            next_m = now + i
            if next_m in snake:
                next_m = snake[next_m]
            elif next_m in lift:
                next_m = lift[next_m]
            if 1 <= next_m < 101 and not visited[next_m]:
                visited[next_m] = True
                zido_cnt[next_m] = zido_cnt[now] + 1
                queue.append(next_m)
    return zido_cnt[100]
print(bfs())
