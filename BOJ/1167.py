import sys
from collections import defaultdict,deque
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N = int(input().strip())
graph = defaultdict(list)
for _ in range(N):
    cmd = list(map(int,input().split()))
    for i in range(1, len(cmd) -2, 2):
        graph[cmd[0]].append((cmd[i],cmd[i + 1]))
               
answer = 0

def bfs(x):
    global answer
    queue = deque([x])
    visited = [-1] * (N + 1)
    visited[x] = 0
    dist = [0,0]
    while queue:
        now = queue.popleft()
        for (node, weight) in graph[now]:
            if visited[node] == -1:
                visited[node] = visited[now] + weight
                queue.append(node)
                if visited[node] > dist[1]:
                    dist = [node, visited[node]]
    return dist
node = bfs(1)[0]
print(bfs(node)[1])

