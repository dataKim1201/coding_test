# psum

import sys
input = sys.stdin.readline
n,m  = map(int,input().split())
arr = list(map(int,input().split()))
psum = [0]
for i in range(n):
    psum.append(psum[i] + arr[i])
result = []
for _ in range(m):
    a,b = map(int,input().split())
    if a==b:
        result.append(arr[a-1])
        continue
    if a != 1:
        result.append(psum[b]- psum[a-1])
    else: # 1이면
        result.append(psum[b])

print('\n'.join(map(str,result)))