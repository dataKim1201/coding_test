import sys
input = sys.stdin.readline
def is_prime(target):
    if target <2: return True
    for i in range(2,int(pow(target,0.5))+1):
        if target % i == 0:
            return False
    return True
start, end = map(int,input().split())
res = []
for item in range(start, end+1):
    if item == 1:
        continue
    if is_prime(item):
        res.append(item)
for ss in res:
    print(ss)