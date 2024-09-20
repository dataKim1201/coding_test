import sys
from collections import deque,defaultdict
input = sys.stdin.readline
INF = int(1e9)
def dijkstra(start,end):
    queue = deque([start])
    dist =[INF] * (n + 1)
    dist[start] = 0
    while queue:
        x= queue.popleft()
        for n_node,cost in graph[x]:
            if dist[n_node] > dist[x] + cost:
                dist[n_node] = dist[x] + cost
                queue.append(n_node)
    return dist[end]

if __name__ =='__main__':
    n,e = map(int,input().split())
    graph = defaultdict(list)
    for _ in range(e):
        start,end,cost = map(int,input().split())
        graph[start].append([end,cost])
        graph[end].append([start,cost])
    must_have = list(map(int,input().split()))
    answer = INF
    for mid,_ in enumerate(must_have):
        o_mid = 1 if mid == 0 else 0
        res = dijkstra(1,must_have[mid])+ dijkstra(must_have[mid],must_have[o_mid]) + dijkstra(must_have[o_mid],n)
        if answer > res:
            answer = res
    if answer >= INF:
        print(-1)
    else:
        print(answer)
    # last = dijkstra(must_have[mid],n)
    # print(middle + m_val+ last)
    # print(middle , m_val , last)
    

