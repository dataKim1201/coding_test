import sys
from collections import deque, defaultdict
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)
graph = defaultdict(list)

for _ in range(m):
    start, end, weight = map(int,input().split())
    graph[start].append([end,weight])

def dijkstra(s):
    dist = [INF] * (n + 1)
    queue = deque([s])
    dist[s] = 0
    while queue:
        x = queue.popleft()
        for n_node,weight in graph[x]:
            if dist[n_node] > dist[x] + weight:
                dist[n_node] = dist[x] + weight
                queue.append(n_node)
    return dist


for i in range(1,n + 1):
    res = dijkstra(i)
    for j in res[1:]:
        if j == INF:
            print(0,end = ' ')
        else:
            print(j,end=' ')
    print()