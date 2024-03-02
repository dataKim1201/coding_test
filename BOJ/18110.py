import sys
input = sys.stdin.readline
n = int(input())
def round(a,b = 0):
    if a - int(a) >= 0.5:
        return int(a) + 1
    return int(a)
def solution(n):
    if n == 0: return 0
    if n <= 3: return int(round(sum([int(input()) for _ in range(n)])/n))
    ex_num = int(round(n *0.15,0))
    arr = [int(input()) for _ in range(n)]
    return int(round(sum(sorted(arr)[ex_num:-ex_num]) /(n-2*ex_num),0))

print(solution(n))


# print(sorted(arr))
#     print(sorted(arr)[ex_num:-ex_num])
#     print(ex_num)
#     print(n-2*ex_num)
#     print(round(5/2,0))