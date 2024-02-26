import sys
input = sys.stdin.readline
def combination(basis, k):
    # 5,2
    # 5, 4
    # 2,1
    # 20 / 2 = 10
    upper = 1
    lower = 1
    for i in range(basis,basis-k,-1):
        upper *= i
    for j in range(1,k+1):
        lower *= j
    return upper//lower

basis, k= map(int,input().split())
print(combination(basis,k))