import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())

arr = [[] for _ in range(n)]
for i in range(m):
    r,c = map(int,input().split())
    arr[r-1].append(c-1)
    arr[c-1].append(r-1)

# 현재 갈 수 있는 노드
# 갔을 때 다른 곳도 갈 수 있는 노드
# 현재 스텝에서 다른 곳을 방문 했을 때 그때의 방문 노드 
# 그 다음 스텝에서
def bfs(arr,start):
    queue = deque([arr[start]])
    visited = [False] * n
    num = [0] * n
    visited[start] = True
    i = 1
    while queue:
        item = queue.popleft()
        tmp = []
        for it in item:
            if not visited[it]:
                visited[it] = True
                num[it] += 1 *i
                tmp.extend(arr[it])
        res = [q for q in tmp if not visited[q]]
        if res:
            queue.append(res)
        i += 1
    return sum(num)

res = 9e99
result = 0
for i in range(n):
    tmp = bfs(arr,i)
    if res > tmp:
        result = i + 1
        res = tmp
print(result)
