import sys
input = sys.stdin.readline
n,target = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
cnt = 0
for i in range(len(arr)-1, -1,-1):
    if target == 0:
        break
    cnt = cnt + target//arr[i]
    target %= arr[i]
print(cnt)
