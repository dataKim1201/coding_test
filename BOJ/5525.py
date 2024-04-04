import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
arr = input().strip()

cnt = 0
L,R = 0,0

while R < M:
    if arr[R:R + 3] == 'IOI':
        R  += 2
        if R - L == 2*N:
            cnt += 1
            L +=2
    else:
        R +=1
        L = R
print(cnt)