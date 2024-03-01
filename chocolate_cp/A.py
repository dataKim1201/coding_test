# 뒤에 오는 느낌표는 팩토리얼
# 앞에 오는 느낌표는 부정의 뜻
# 우선순위는 팩토리얼이 먼저

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    case = input()
    flag = False
    front = []
    back = []
    for i in case:
        if not flag and i == '!':
            front.append(i)
        elif i.isdigit():
            flag = True
            num = int(i)
        elif flag and i == '!':
            back.append(i)
    if len(back) >= 1:
        num = 1
    if len(front) % 2 == 1:
        num = 1 if num ==0 else 0
    print(num)

    # if '0' in case:
    #     num = 0
    #     front, back = case.split('0')
    #     if len(back) >= 1:
    #         num = 1
    #     if len(front) %2 == 1:
    #         num = 1 if num == 0 else 0
    # else:
    #     num = 1
    #     front, back = case.split('1')
    #     if len(back) >= 1:
    #         num = 1
    #     if len(front) %2 == 1:
    #         num = 1 if num == 0 else 0
    # print(num)