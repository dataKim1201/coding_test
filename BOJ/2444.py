import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, 2*n):
    if i < n:
        print(' '*(n-i -1 ), '*'*(2*i - 1))
    elif i == n:
        print('*'*(2*i -1))
    else:
        print(' '*(i-n- 1), '*'*(2*(2*n - i) - 1))