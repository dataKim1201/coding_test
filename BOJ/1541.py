import sys
from itertools import combinations
input = sys.stdin.readline
formula = input()
def solution(formula):
    # -가 무조건 하나는 존재한다는 뜻
    if '-' not in formula: return eval(formula)
    operations = formula.count('+') + formula.count('-')
    cand = list(range(operations))
    

# step이 n이면 나올 수 있는 결과도 n-1아님?
# 1 : 1
# 2 : 2
# 3 : 3


