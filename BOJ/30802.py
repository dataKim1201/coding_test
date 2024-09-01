import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
T, K = map(int,input().split())
res_t = 0
for item in arr:
    res_t += item//T
    if item % T:
        res_t += 1

print(res_t)
print(n//K, n%K)