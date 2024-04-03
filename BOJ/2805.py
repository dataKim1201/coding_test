import sys
input = sys.stdin.readline
n, target = map(int,input().split())
arr = list(map(int,input().split()))
start, end = 0, max(arr)
while start <= end:
    mid = (start + end)//2
    tmp = 0
    for tree in arr:
        if mid < tree:
            tmp += tree - mid
    if tmp >= target:
        start = mid + 1

    else:
        end = mid - 1
print(end)