import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    res = 0
    k, m, n = map(int,input().split())
    # if k < m:
    xx = (n-1) //k + 1 # 몫에 1을 더한값
    xx = str(xx) if len(str(xx)) == 2 else '0' + str(xx)
    yy = str(n % k if n %k != 0 else k)
    print(yy + xx)
    # else: # m이 더 큰 경우
    #     xx = n //m + 1 # 몫에 1을 더한값
    #     xx = str(xx) if len(str(xx)) == 2 else '0' + str(xx)
    #     yy = str(n % m if n % m != 0 else m)
    #     print(yy + xx)