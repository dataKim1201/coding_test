import sys
input = sys.stdin.readline
n = int(input())
arr = [300,60,10]
ans = []
for item in arr:
    if n >= item:
        ans.append(n//item)
        n = n%item
    else:
        ans.append(0)
if n != 0:
    print(-1)
else:
    print(*ans)
