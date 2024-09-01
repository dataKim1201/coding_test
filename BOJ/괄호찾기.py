'''
접근 방법: 최적해가 없나?
- 최솟값이다 보니 항상 만족하는 최적해가 있을 것이다.

- 즉, -가 등장한 경우는 우항을 항상 크게 만들면 된다.
- 다른 -를 만나면 그걸 종료하면됨


알고리즘 설명
1. -기준으로 split해서 -끼리 엮이는걸 제외하자.
2. item단위로 나머지 항끼리 더해서 return 하면 끝

-> 에러 사항 -> 0값 때문에 연산이 안됨
-> 0을 찾고 버리는 메타. (메타까지 몇메타)
'''
import sys
input = sys.stdin.readline
formula = input().strip()
def solution(formula):
    if '-' not in formula:
        return eval(formula)
    arr = formula.split('-')
    res = []
    for item in arr:
        tmp = 0
        for it in item.split('+'):
            if it.replace('0',''): # None이 아니라면
                tmp += int(it)
        res.append(str(tmp))
    return eval('-'.join(res))
print(solution(formula))


# 2+
# -3+4 
# -5+4+6
# 0009+00090-2