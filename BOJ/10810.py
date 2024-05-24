import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [0] * (n + 1)
for _ in range(m):
    st,end,val = map(int,input().split())
    for i in range(st,end + 1):
        arr[i] = val
print(*arr[1:])