import sys
input = sys.stdin.readline
n = int(input())
res = [0]
for _ in range(n):
    tmp = int(input())
    if tmp:
        res.append(tmp)
    else:
        res.pop()

print(sum(res))