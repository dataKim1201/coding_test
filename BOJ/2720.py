# 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)의 개수를 구하는 프로그램을 
# 거스름돈은 항상 $5.00 이하이고, 손님이 받는 동전의 개수를 최소로 하려고 한다.
import sys
input = sys.stdin.readline

def greedy(target):
    res = []
    arr = [25, 10,5,1]
    for item in arr:
        if target < item: 
            res.append(0)
            continue
        res.append(target//item)
        target = target % item
    return res
n = int(input())
result = []

for _ in range(n):
    target = int(input())
    res = greedy(target)
    result.append(res)

for item in result:
    print(*item)