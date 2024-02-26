import sys
from copy import deepcopy
input = sys.stdin.readline
n = int(input())
arr = []

for idx, _ in enumerate(range(n)):
    tmp = input().split()
    tmp  = [int(tmp[0]),tmp[1]]
    tmp.append(idx)
    arr.append(deepcopy(tmp))
arr = sorted(arr,key = lambda x : (x[0], x[2]))
for item in arr:
    print(item[0],item[1])
