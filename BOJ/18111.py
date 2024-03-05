import sys
from collections import Counter

input = sys.stdin.readline
def solution():
    n,m,b = map(int,input().split())
    arr = sum([list(map(int,input().split())) for _ in range(n)],[])
    counter = Counter(arr)
    # res = next(iter(counter.keys())
    # print(counter)
    if len(counter) == 1: return 0,arr[0]
    min_ar,max_ar = min(arr),max(arr)
    def calc_result(target,counter,B):
        needed_block = 0 
        res = 0
        for key,val in counter.items():
            if key > target:
                # 빼야지 빼는데 2초 걸림
                res += 2*val*(key-target)
                # 지갑은 두둑해지겠지
                needed_block += val*(key-target)
            elif key < target:
                # 넣어야 겠지 넣는데 1초 걸림
                res += (target - key)*val
                needed_block -= val *(target-key)
        if B + needed_block <0:
            return False
        return res
    answer = 9e99
    for target in range(max_ar,min_ar-1,-1):
        tmp =calc_result(target,counter,b)
        # print('res : ',target,tmp)
        if tmp and answer > tmp:
            answer = tmp
            best_floor= target

    return answer, best_floor

a,b= solution()
print(a,b)

