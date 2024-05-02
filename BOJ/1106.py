import sys
input = sys.stdin.readline
# 첫째 줄에 C와 형택이가 홍보할 수 있는 도시의 개수 N이 주어진다.
C, N = map(int,input().split())
# 둘째 줄부터 N개의 줄에는 각 도시에서 홍보할 때 대는 
# 비용과 그 비용으로 얻을 수 있는 
# 고객의 수가 주어진다. 
graph = []
for _ in range(N):
    cost, custom = map(int,input().split())
    graph.append([cost, custom])
INF = 1e9
def dynamic(arr):
    DP = [INF] * (C + 100)
    DP[0] = 0
    for i in range(len(arr)):
        cost,custom = arr[i]
        for j in range(C + 100):
            # if j >= custom:
            DP[j] = min(DP[j], DP[j-custom] + cost)
    return min(DP[C:])
print(dynamic(graph))
