import sys
input = sys.stdin.readline
n = int(input())
def get_LCM(a,b):
    for i in range(max(a,b), a*b + 1):
        if i % a == 0 and i % b == 0:
            return i

for _ in range(n):
    N,M,x,y = map(int, input().split())
    flag = False
    if N <= M:
        step = N
        aug = x
    else:
        step = M
        aug =y
    x = x if x != N else 0
    y = y if y != M else 0
    print(step,x)
    for i in range(0,get_LCM(N,M) + 1, step):
        if (i + aug) % N == x and (i + aug) % M == y:
            print(i + aug)
            flag = True
            break
    if not flag:
        print(-1)
    