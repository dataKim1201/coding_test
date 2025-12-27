import sys
input = sys.stdin.readline

# 진짜 무식하게

zido = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    for i in range(x,x + 10):
        for j in range(y, y + 10):
            zido[i][j] = 1
print(sum(sum(zido, [])))