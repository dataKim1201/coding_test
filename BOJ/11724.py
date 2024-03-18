import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = {k:[] for k in range(1,n +1)}
# graph = [[] for k in range(n +1)]
for _ in range(m):
    a,b =map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

visited = [False] * (n+1)
def dfs(x):
    visited[x] = True
    for item in graph[x]:
        if not visited[item]:
            dfs(item)
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
        
print(cnt)
