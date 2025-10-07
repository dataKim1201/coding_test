import sys
input = sys.stdin.readline

def dfs(current, visited):
    # 모든 도시를 방문한 경우
    if visited == (1 << n) - 1:
        return graph[current][0] if graph[current][0] != 0 else INF

    if dp[current][visited] != -1:
        return dp[current][visited]

    min_cost = INF
    for next_city in range(n):
        if visited & (1 << next_city) or graph[current][next_city] == 0:
            continue
        cost = dfs(next_city, visited | (1 << next_city)) + graph[current][next_city]
        min_cost = min(min_cost, cost)
        dp[current][visited] = min_cost

    
    return min_cost

if __name__ == '__main__':
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    # visited 상태를 비트마스크로 표현
    # dp[현재도시][방문상태] = 최소비용
    dp = [[-1] * (1 << n) for _ in range(n)]
    INF = float('inf')

    # 시작 도시는 0번부터
    print(dfs(0, 1 << 0))
