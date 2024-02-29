# 벌집 문제 
# 내가 존재하는 벌집 마다 이동할 수 있는 방향이 6개
import sys
input = sys.stdin.readline

N = int(input())
res,i,s = 1,1,1

while s < N:
    s += 6*i
    i += 1
    res += 1
print(res)
