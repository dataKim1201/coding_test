import sys
input = sys.stdin.readline
V,E  = map(int, input().split())


# 노드를 어떻게 정의해야하나 -> node
node_map = {i + 1 : {} for i in range(V)}

inf = float('inf')
graph = [[inf for _ in range(V)] for _ in range(V)]
for _ in range(E):
    st,ed, edge = map(int,input().split())
    graph[st][ed] = edge
    graph[ed][st] = edge
visited = [[False] * V for _ in range(V)]
answer = 0
visit_node = set()

while sum(visited, []) == V -1:
    min_edge = min(sum(graph,[]))
    for i in range(V):
        for j in range(V):
            if graph[i][j] == min_edge and not visited[i][j]:
                visited[i][j] = True
                answer += min_edge
                visit_node.add(i)
                visit_node.add(j)
print(answer)
# 최소 간선을 찾는다.
# 해당 간선을 방문처리하고 다음 간선을 찾는다.
# V-1이 될때 까지 찾는다.