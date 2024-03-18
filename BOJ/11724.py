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

def bfs(graph, start):
    visited= [start]
    queue = deque(graph[start])
    while queue:
        var = queue.popleft()
        if var not in visited:
            visited.append(var)
            for item in graph[var]:
                if item not in visited:
                    queue.extend(graph[item])
                    visited.append(item)
    return visited
i = 1
left = list(range(1,n+1))
cnt = 0
while left:
    res = bfs(graph,i)
    left = list(set(left) - set(res))
    cnt += 1
    if left:
        i = left[0]
    else:
        break
print(cnt)
# cnt = 0
# visited = []
# for i in range(1,n+1):
#     if i not in visited:
        
#         visited.extend(tmp)
#         cnt += 1 
# print(cnt)
            
