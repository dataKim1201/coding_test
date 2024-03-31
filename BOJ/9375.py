# 해빈이는 패션에 매우 민감해서 한번 입었던 옷들의 조합을 절대 다시 입지 않는다. 
# 예를 들어 오늘 해빈이가 안경, 코트, 상의, 신발을 입었다면, 다음날은 바지를 추가로 입거나 안경대신 렌즈를 착용하거나 해야한다. 
# 해빈이가 가진 의상들이 주어졌을때 과연 해빈이는 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?
import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    case = int(input())
    case_dict = {}
    for _ in range(case):
        name, kind = input().split()
        if kind not in case_dict:
            case_dict[kind] = 1
        else:
            case_dict[kind] += 1
    ans = 1
    for v in case_dict.values():
        ans *= v + 1
    print(ans-1)
