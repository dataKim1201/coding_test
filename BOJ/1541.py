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

# 2-3+4-5+4+6
# 0009+00090-2