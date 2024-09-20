import sys
input = sys.stdin.readline
operation = '+-*/'
def gcd(res):
    bunja, bunmo = res
    while bunmo > 0:
        bunja, bunmo = bunmo, bunja % bunmo
    return bunja
def add(a,b):
    res = [a[1]*b[0] + a[0]*b[1],a[1]*b[1]]
    # 약분 처리
    gcd_num = gcd(res)
    # 정수 처리
    if res[1]//gcd_num == 1:
        return res[0]//gcd_num
    return [res[0]//gcd_num, res[1]//gcd_num]
def minus(a,b):
    res = [a[1]*b[0] - a[0]*b[1],a[1]*b[1]]
    # 약분 처리
    gcd_num = gcd(res)
    # 정수 처리
    if res[1]//gcd_num == 1:
        return res[0]//gcd_num
    return [res[0]//gcd_num, res[1]//gcd_num]
def multiply(a,b):
    res = [a[0] *b[0],a[1]*b[1]]
    # 약분 처리
    gcd_num = gcd(res)
    # 정수 처리
    if res[1]//gcd_num == 1:
        return res[0]//gcd_num
    return [res[0]//gcd_num, res[1]//gcd_num]
def divide(a,b):
    res = [a[0] *b[1],a[1]*b[0]]
    # 약분 처리
    gcd_num = gcd(res)
    # 정수 처리
    if res[1]//gcd_num == 1:
        return res[0]//gcd_num
    if res[1]//gcd_num == 0:
        return 'ERR'
    return [res[0]//gcd_num, res[1]//gcd_num]

def cleansing_args(args):
    result = []
    for arg in args:
        if isinstance(eval(arg), list):
            arg = eval(arg)
            if arg[1] < 0:
                result.append([-arg[0],-arg[1]])
            else:
                result.append(arg)
        else: # 정수로 표현 되었겠지
            arg = eval(arg)
            result.append([arg,1])
    return result

formula = input().strip()
op_list = []
args = []

for i in operation:
    i = i+ ' ' if i == '-' else i
    while i in formula:
        op_list.append(i) 
        args.append(formula.split(i)[0])
        formula = ' '.join(formula.split(i)[1:])
    # 하나는 끝났고 다음 반복문 돌때 
    # 남아 있는 op도 모두 없을 때만
args.append(formula.strip())

args = cleansing_args(args)

def get_solution(op,arg1,arg2):
    if op == '+':
        res = add(arg1,arg2)
    if op == '-':
        res = minus(arg1,arg2)
    if op == '*':
        res = multiply(arg1,arg2)
    if op == '/':
        res = divide(arg1,arg2)
    return res
get_solution(0,op_list[0])
from collections import deque
if '*' in op_list:
    while True:
        idx = op_list.index('*')
        op = op_list.pop(idx)
        arg1 = args.pop(idx)
        arg2 = args.pop(idx)
        res= get_solution(op,arg1,arg2)

while True:
    if '*' in op_list:
        idx = op_list.index('*')
    if '/' in op_list:
        idx2 = op_list.index('/')
