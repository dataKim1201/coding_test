import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def dijkstra(s,end):
    dist = [INF] * (n + 1)
    queue = deque([[s,0]])
    dist[s] = 0
    minimum = INF
    while queue:
        x,ct = queue.popleft()
        if (dist[x] < ct):
            continue
        for n_node, cost in graph[x]:# ,key = lambda x : x[1]):
            if dist[n_node]  > dist[x] + cost:
                dist[n_node] = dist[x] + cost
                queue.append([n_node,dist[x] + cost])
    return dist[end]

INF = int(1e9)
n = int(input())
m = int(input())
if __name__ == '__main__':
    graph = defaultdict(list)
    for _ in range(m):
        start,end,cost = map(int,input().split())
        graph[start].append([end,cost])

    start, end = map(int,input().split())
    print(dijkstra(start,end))


# 5
# 8
# 1 2 2
# 1 3 1
# 1 4 2
# 1 5 10
# 2 4 6
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5