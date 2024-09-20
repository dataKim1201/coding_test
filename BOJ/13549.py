import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
visited = [-1] * 100001
queue = deque([n])
visited[n] =0
while queue:
    i = queue.popleft()
    if i == k:
        print(visited[i])
        break
    if 0 <= i - 1 <= 100000 and visited[i - 1] == -1:
        visited[i - 1] = visited[i] + 1
        queue.append(i - 1)
    if 0 <= i * 2 <= 100000 and visited[i * 2] == -1:
        visited[i * 2] = visited[i]
        queue.append(i * 2)
    if 0 <= i + 1 <= 100000 and visited[i + 1] == -1:
        visited[i + 1] = visited[i] + 1
        queue.append(i + 1)

import sys
from collections import deque

input = sys.stdin.readline

N, K = n,k
q = deque()
q.append(N)
visited = [-1 for _ in range(100001)]
visited[N]=0

while q:
    s=q.popleft()
    if s == K:
        print(visited[s])
        break
    if 0 <= s-1 < 100001 and visited[s-1]==-1:
        visited[s-1]=visited[s]+1
        q.append(s-1)
    if 0 <= s*2 < 100001 and visited[s*2]==-1:
        visited[s*2]=visited[s]
        q.appendleft(s*2)
    if 0 <= s+1 < 100001 and visited[s+1]==-1:
        visited[s+1]=visited[s]+1
        q.append(s+1)