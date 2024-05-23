import sys
from collections import deque
input= sys.stdin.readline
INF = int(1e9)
n = int(input())
arr = [INF]  + list(map(int,input().split()))
a,b = map(int,input().split())
def bfs(start,end):
    queue = deque([[start,1]])
    visited = 0
    dist = [INF] * (n + 1)
    dist[start] = 0
    while queue:
        cur,cnt = queue.popleft()
        visited  |= (1 << cur)
        if cur == end:
            return dist[end]
        for i in range(cur, n + 1,arr[cur]):
            if not visited & (1 << i) and cnt < dist[i]:
                queue.append([i,cnt + 1])
                dist[i] = cnt
                # print('cur,i',cur,i)
                # print('dist[i]',dist[i])
        for i in range(cur,0,-arr[cur]):
            if not visited & (1 << i) and cnt < dist[i]:
                queue.append([i,cnt + 1])
                dist[i] = cnt
    if dist[end] == INF:
        return -1
    return dist[end]

print(bfs(a,b))



