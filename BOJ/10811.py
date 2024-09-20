import sys
input = sys.stdin.readline

N,M = map(int,input().split()) # N: 바구니 개수, M: 바꿀 개수
arr = list(range(1,N + 1))
for _ in range(M):
    src,tgt = map(int,input().split())
    src -=1
    tgt -=1
    if src == 0:
        arr[src:tgt + 1] = arr[tgt:0:-1] + [arr[0]]
    else:
        arr[src:tgt + 1] =  arr[tgt:src-1:-1]
print(*arr)