import sys
from collections import deque
input = sys.stdin.readline

def check(x,y,visited=[]):
    if x == y and len(visited) > 0:
        return 1
    queue = deque([x])
    while queue:
        x = queue.popleft()
        for item in G[x]:
            if item not in visited:
                visited.append(item)
                queue.append(item)
    return 0

if __name__ == '__main__':
    N = int(input())
    zido = [list(map(int,input().split())) for _ in range(N)]
    G = {}
    for i in range(N):
        G[i] = []
        for j in range(N):
            if zido[i][j] == 1:
                G[i].append(j)
    # print("result", check(0,2))
    for i in range(N):
        for j in range(N):
            print(check(i,j),end=' ')
        print()