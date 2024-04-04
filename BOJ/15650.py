import sys
from itertools import combinations
input = sys.stdin.readline
n,m = map(int,input().split())
for item in combinations(list(range(1,n+1)),m):
    print(*item)