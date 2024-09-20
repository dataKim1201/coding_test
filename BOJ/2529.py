import sys
from copy import deepcopy
input = sys.stdin.readline
k = int(input())
A = list(input().split())
max_res, min_res = 0,1e10
res_max, res_min = '','-'
def check(arg1,op,arg2):
    if op == '>':
        return int(arg1) > int(arg2)
    return int(arg1) < int(arg2)
def find(cnt = ''):
    global max_res, min_res,res_max, res_min
    if len(cnt) >= 2:
        for i in range(len(cnt)-1):
            flag = True
            if not check(cnt[i], A[i], cnt[i + 1]):
                return False
        if flag and len(cnt) == len(A) + 1:
            if max_res < int(cnt):
                max_res = int(cnt)
                res_max = cnt
            if min_res > int(cnt):
                min_res = int(cnt)
                res_min = cnt
    for i in range(10):
        if str(i) not in cnt and len(cnt) < len(A) + 1:
            find(cnt + str(i))
    return
find()
print(res_max)
print(res_min)