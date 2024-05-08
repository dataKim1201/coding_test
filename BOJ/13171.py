import sys
input = sys.stdin.readline
mod = 1000000007
target, bb = map(int,input().split())
def divide_square(bias):
    if bias == 1:
        return target % mod
    x = divide_square(bias//2) # 100 -> 50 -> 25 -> 12 -> 6 -> 3 -> 1
    if bias% 2== 0:
        return (x * x) %mod
    else:
        return (x * x * target) % mod
print(divide_square(bb))

target = int(1e18)
bb = int(1e18)
print(divide_square(bb))

# C^n = C^(n//2)*C^(n//2) or C^(n//2)*C^(n//2) * C

# 2 10