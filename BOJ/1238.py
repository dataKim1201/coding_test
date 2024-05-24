from collections import defaultdict,deque
import sys
input = sys.stdin.readline
N,M,X = map(int,input().split())
graph =defaultdict(list)
for _ in range(M):
    start, end, weight = map(int,input().split())
    graph[start].append([end,weight])

def dijkstra(start):
    global X
    queue = deque([[start,0]])
    visited = 0
    INF = int(1e9)
    dist = [INF] * (N+1)
    while queue:
        x,res = queue.popleft()
        if dist[x] < res:
            continue
        for n_node,w in graph[x]:
            if dist[n_node] > res + w :
                dist[n_node] = res + w
                queue.append([n_node,res + w])
    if start != X:
        return dist[X]
    return dist
start_to_end = [0] * (N + 1) 
for i in range(1,N+1):
    if i != X:
        start_to_end[i] = dijkstra(i)
end_to_start = dijkstra(X)

print(max([start_to_end[i] + end_to_start[i] for i in range(1,N+1)]))