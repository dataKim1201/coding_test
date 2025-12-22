# 9 X 9
import sys
input = sys.stdin.readline
n = 9
max_ls = [0,0]
max_val = 0
arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] > max_val:
            max_val = arr[i][j]
            max_ls = [i + 1, j + 1]
print(max_val)
print( * max_ls)

# 108384	88