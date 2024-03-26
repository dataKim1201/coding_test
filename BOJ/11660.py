import sys
input = sys.stdin.readline

n,q = map(int,input().split())
arr = [0]
for _ in range(n):
    arr.append([0] + list(map(int,input().strip().split())))
queries = [list(map(int,input().split())) for _ in range(q)]
# queries.append([1,2,3,3])
p_arr = [ [0] * (n + 1) for _ in range(n + 1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        p_arr[i][j] = arr[i][j] + p_arr[i-1][j] + p_arr[i][j-1] - p_arr[i-1][j-1]


for query in queries:
    x1, y1, x2, y2 = query
    print(p_arr[x2][y2] - p_arr[x2][y1-1] - p_arr[x1-1][y2] + p_arr[x1-1][y1-1])

# (3,3)부터 (4,4)까지의 2차원 구간합 = sums[4][4] - sums[4][3-1] - sums[3-1][4] + sum[3-1][3-1] 