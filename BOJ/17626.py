import sys
import math

input = sys.stdin.readline

target = int(input().strip())

cnt = 0

for _ in range(4): # 최대 4번
    if target == 0:
        break
    tmp = int(math.sqrt(target))
    target -= tmp**2
    print(target,tmp, tmp**2)
    cnt += 1
print(cnt)