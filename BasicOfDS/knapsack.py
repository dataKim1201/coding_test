from collections import deque
'''
graph: list of (val, weight)
visited: used result
'''

def bfs(graph,limit):
    print(graph)
    visited = [False] * len(graph)
    queue = deque([(0,graph[0][0], graph[0][1]), (0, 0, 0)])
    visited[0] = True
    result = 0
    while queue:
        x, bag_weight,happiness = queue.popleft()
        if bag_weight >= limit:
            continue
        if result < happiness:
            result = happiness
            result_bag_weight = bag_weight
        # result = max(result, happiness)
        # for i in range(2):
        nx = x + 1
        if nx < len(graph) and not visited[nx]:
            visited[nx] = True
            queue.append((nx, bag_weight + graph[nx][0], happiness + graph[nx][1]))
            queue.append((nx, bag_weight, happiness))
    print('calories', result_bag_weight, 'happiness', result)
    return happiness

# def dfs(graph, limit):
#     if graph[0][0] < limit:
#         result = dfs(graph[1:],limit - graph[0][1])
#         result +=graph[0][1]
#     else: # 넘는다면?

def dynamic(graph, limit, DP = [[[0,0]]]):
    # print(graph)
    result = 0
    for i in range(len(graph)):
        tmp = []
        print(DP[-1])
        for bf_w, bf_h in DP[-1]:
            if bf_w + graph[i][0] <= limit:
                result = max(result, graph[i][1] + bf_h)
                tmp.append([graph[i][0] + bf_w, graph[i][1] + bf_h])
            if [bf_w,bf_h] not in tmp:
                tmp.append([bf_w,bf_h])
        DP.append(tmp)
    print(DP[-1])
    return result # sorted(DP[-1],key = lambda x : x[1], reverse=True)[0][1] # max([item[1] for item in DP[-1]])
# graph = [(123,89), (154,90), (258,30), (354, 50), (365,90), (150,79), (95,90), (195, 10)]
# print(bfs(sorted(graph,key = lambda x: -x[1]/x[0]), 750))
import sys
input = sys.stdin.readline
n = int(input())
graph1 = list(map(int,input().split()))
graph2 = list(map(int,input().split()))
graph = [ [w,h] for w,h in zip(graph1,graph2)]
def dp(arr,k):
    dp = [0]*(k+1)
    for i in range(n):
        for j in range(k,0,-arr[i][0]):
            if j >=arr[i][0]: # 작다면
                dp[j] = max(dp[j],(dp[j-arr[i][0]] + arr[i][1]))
    return dp[k]
print(dp(graph, 99))