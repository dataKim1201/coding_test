import sys
from itertools import permutations
input = sys.stdin.readline
n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
result = set()
for item in permutations(arr,m):
    result.add(' '.join(map(str,item)))
for item in sorted(result):
    print(item)