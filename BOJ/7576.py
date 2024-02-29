# 3차원 그래프 탐색
import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())


def bfs(queue,visited,zido):
    dms = [0,0,-1,1,0,0]
    dns = [1,-1,0,0,0,0]
    cnt = 0
    while queue:
        sss = queue.popleft()
        m,n,cnt = sss
        visited[m][n] = True
        for dm,dn in zip(dms,dns):
            nm,nn = m + dm, n + dn
            if nm >= 0 and nm <M and nn >= 0 and nn <N:
                if not visited[nm][nn]:
                    if zido[nm][nn] == 0:
                        zido[nm][nn] = 1
                        queue.append((nm,nn,cnt+1))
    if 0 in sum(zido,[]):
        return -1
    return cnt

def solution(M,N):
    zido = []
    for _ in range(M):
        zido.append(list(map(int,input().split())))
    visited = [[False] *N for _ in range(M)]
    res = 0
    queue =deque()
    for m in range(M):
        for n in range(N):
            if zido[m][n] == 1:
                queue.append((m,n,0))
    return bfs(queue,visited,zido)

print(solution(M,N))
