import sys
from collections import deque
import heapq
input = sys.stdin.readline

V,E = map(int,input().split())
start = int(input())
zido = {i: [] for i in range(1,V + 1)}
for _ in range(E):
    u,v,w = map(int,input().split())
    zido[u].append([v,w])

def bfs(start):
    queue = []
    heapq.heappush(queue,(0,start))
    result = [1e9] * (V + 1)
    result[start] = 0
    while queue:
        cnt, x = heapq.heappop(queue)
        if result[x] < cnt:
            continue
        for nx, w in zido[x]:
            if  cnt + w < result[nx]:
                result[nx] = cnt + w
                heapq.heappush(queue,(cnt +w, nx))
                # queue.append((cnt + w,nx))

    result = ['INF' if result[i] == 1e9 else result[i] for i in range(1,len(result))]
    return result

ans = bfs(start)
for i in ans:
    print(i)