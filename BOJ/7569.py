# 3차원 그래프 탐색
import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline
N,M,H = map(int,input().split())


def bfs(queue,visited,zido):
    dhs = [0,0,0,0,-1,1]
    dms = [0,0,-1,1,0,0]
    dns = [1,-1,0,0,0,0]
    cnt = 0
    while queue:
        sss = queue.popleft()
        h,m,n,cnt = sss
        visited[h][m][n] = True
        for dh,dm,dn in zip(dhs,dms,dns):
            nh,nm,nn = h + dh, m + dm, n + dn
            if nh >=0 and nh <H and nm >= 0 and nm <M and nn >= 0 and nn <N:
                if not visited[nh][nm][nn]:
                    if zido[nh][nm][nn] == 0:
                        zido[nh][nm][nn] = 1
                        queue.append((nh,nm,nn,cnt+1))
    if 0 in sum(sum(zido,[]),[]):
        return -1
    return cnt

def solution(H,M,N):
    zido = []
    for _ in range(H):
        tmp = []
        for _ in range(M):
            tmp.append(list(map(int,input().split())))
        zido.append(deepcopy(tmp))
    visited = [[[False] *N for _ in range(M)] for _ in range(H)]
    res = 0
    queue =deque()
    for h in range(H):
        for m in range(M):
            for n in range(N):
                if zido[h][m][n] == 1:
                    queue.append((h,m,n,0))
                    # if tmp == -1:
                    #     return -1
                    # res = max(res,tmp)
    return bfs(queue,visited,zido)

print(solution(H,M,N))
