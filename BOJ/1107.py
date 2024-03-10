import sys
input = sys.stdin.readline
target = int(input())
missing = int(input())
def solution(target,missing):
    if missing:
        missing_btn = input().split()
        i = 1
        j = -1
    else:
        return min(abs(target-100),len(str(target)))
    
    # current loc
    candidates = abs(target-100)
    # ascending
    while i <= abs(target-100):
        if all([item not in missing_btn for item in str(target + i)]):
            print(str(target+i))
            candidates = min(candidates,len(str(target+i)) + i)
            break
        i +=1

    # descending
    while target + j >= 0: # 눌러야 하는 버튼 수 
        if all([item not in missing_btn for item in str(target + j)]):
            print(target+j)
            candidates = min(candidates,len(str(target+j)) - j)
            break
        j -=1

    return candidates
print(solution(target,missing))


    # for item in range(1000000):
    #     flag = all([i not in missing_btn for i in str(item)])
    #     if flag: # 아무것도 없다면
    #         candidates = min(candidates,abs(target-item) + len(str(item)))
    