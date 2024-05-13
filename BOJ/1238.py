# import sys
# from collections import defaultdict, deque
# input = sys.stdin.readline

# N,M,X = map(int,input().split())
# INF = int(1e9)
# graph = defaultdict(list)
# for _ in range(M):
#     start,end,weight = map(int,input().split())
#     graph[start].append([end,weight])

# def dijkstra(start,end):
#     visited = 0
#     queue = deque([[start,0]])
#     result = INF
#     all_visited = eval('0b' + ''.join(['1' for _ in range(N)]))
#     while queue:
#         x,cnt = queue.popleft()
#         visited |= (1<<x)
#         if x == end:
#             result = min(result,cnt)
#             continue
#         if visited == all_visited:
#             break
#         for n_node, weight in graph[x]:
#             if not visited&(1<<n_node) and result > cnt + weight:
#                 queue.append([n_node,cnt + weight])
#     return result
# answer = 0
# for i in range(1,N + 1):
#     if i == X:
#         continue
#     tmp = dijkstra(i,X) + dijkstra(X,i)
#     answer = max(answer,tmp)
# print(answer)

# # for item in DP:
# #     for i in item:
# #         if i == INF:
# #             print(0,end = ' ')
# #         else:
# #             print(i,end=' ')
# #     print()


import sys
import heapq
INF = 1e10
def input(): return sys.stdin.readline().rstrip()

def dijkstra(s):
    global x
    dist = [INF] * (n+1)
    q = []
    heapq.heappush(q,(s,0))
    while q:
        w,d = heapq.heappop(q)
        if dist[w] < d:
            continue
        for nxt,c in graph[w]:
            if dist[nxt] > d + c:
                dist[nxt] = d+c
                heapq.heappush(q,(nxt,d+c))
    if s != x:
        return dist[x]
    return dist

n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
node2x = [0] * (n+1)
for i in range(1,n+1):
    if i != x:
        node2x[i] = dijkstra(i)
x2node = dijkstra(x)

print(max([x2node[i] + node2x[i] for i in range(1,n+1) if i != x]))