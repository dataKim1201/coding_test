from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
sangjun = Counter(list(map(int,input().split())))
m = int(input())
target = list(map(int,input().split()))
result = []

for item in target:
    if item not in sangjun:
        result.append(str(0))
    else:
        result.append(str(sangjun[item]))
res = ' '.join(result)
print(res)