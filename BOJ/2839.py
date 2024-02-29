# 설탕 배달
import sys
input = sys.stdin.readline
N = int(input())
def solution(N):
    if N ==4:
        return -1
    elif N == 3:
        return 1
    target = N % 5
    if target == 2:
        if target % 3 == 0:
            return target // 3
        elif target % 8 == 0:
            return (target // 8) *2
        return -1
    else:
        if target == 0:
            return N//5
        elif target in [1,3]:
            return N//5 + 1 
        elif target == 4:
            return N//5 + 2
# print(solution(N))


# 어차피 공부니까 DP로 풀어보자
# 19 // 3 6 + 1 = 7
# 10 + 9  2+3 = 5
def solution2(N):
    if N == 4 : return -1
    if N in [3,5] : return 1
    for i in range(1,N//3 + 1):
        for k in range(i):
            if 3*k + 5*(i-k) == N:
                return i
            elif 3*(i-k) + 5*(k) == N:
                return i
    return -1
print(solution2(N))