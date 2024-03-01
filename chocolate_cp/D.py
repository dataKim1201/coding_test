import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = [input().strip() for _ in range(N)]
visited = [[False] * len(item) for item in arr]
queue = deque([0,0])
print(arr)
print(visited)
dx, dy = [0,1], [-1,1]
