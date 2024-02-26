import sys
input = sys.stdin.readline
n,step = map(int,input().split())
arr = list(range(1,n+1))
res = []
step = step -1
idx = step
while arr:
    idx = idx %len(arr)
    res.append(arr[idx])
    arr.pop(idx)
    idx += step
result = '<'
result += ', '.join(list(map(str,res)))
result += '>'
print(result)
