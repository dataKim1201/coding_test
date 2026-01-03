import sys
from collections import deque
input = sys.stdin.readline

def bfs(n,k):
    queue = deque()
    queue.append(n)
    count = [-1] * 100001
    dist = [-1] * 100001
    dist[n] = 0
    count[n] = 1
    while queue:
        crnt = queue.popleft()
        for nx in [crnt + 1, crnt -1, crnt *2]:
            if nx < 0 or nx > 100000: continue
            if dist[nx] == -1:
                dist[nx] = dist[crnt] + 1
                count[nx] = count[crnt]
                queue.append(nx)
            else: # 방문한 적이 있는 경우라면 -> count min처리
                if dist[nx] == dist[crnt] + 1:
                    count[nx] += count[crnt]
                # crnt 가 더 크면?
                # if dist[nx] < dist[crnt] + 1: continue
                # if dist[nx] > dist[crnt] + 1:
                #     count[nx] = 1
                #     dist[nx] = dist[crnt] + 1
    return dist[k], count[k]
n,k = map(int,input().split())
dist, cnt = bfs(n,k)
print(dist)
print(cnt)