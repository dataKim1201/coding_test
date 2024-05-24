# 500, 100, 50, 10, 5엔, 1엔
import sys
input = sys.stdin.readline
arr = [500, 100, 50, 10, 5, 1]
target = 1000 - int(input())
answer = 0
for item in arr:
    tmp = target//item
    answer += tmp
    target = target - tmp * item
    if target <= 0:
        break
print(answer)