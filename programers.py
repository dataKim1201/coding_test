from collections import deque
from copy import deepcopy
def available(target,arr):
    queue = deque([(arr, False)])
    while queue:
        ar,flag= queue.popleft()
        # print(queue)
        if target not in ar:
            continue
        if len(ar) == 1:
            break 

        for i in range(len(ar)-1):
            new_tmp = deepcopy(ar)
            # print(target,new_tmp,flag,i)
            if new_tmp[i] > new_tmp[i+ 1]: # i가 크다면 i를 삭제하는 행위
                tmp = new_tmp.pop(i)
                queue.append(deepcopy(new_tmp), flag)
                if not flag: # i + 1을 빼자
                    if i+ 1 < len(new_tmp): #가능하면
                        queue.append((deepcopy(new_tmp[:i] + [tmp] + new_tmp[i+1:]),not flag))
                    else: # i +2 == n-1이라는 뜻
                        queue.append((deepcopy(new_tmp[:i] + [tmp]),not flag))
            else:
                tmp = new_tmp.pop(i + 1)
                queue.append((deepcopy(new_tmp), flag))
                if not flag: # i를 뺴자
                    if i+ 2 < len(new_tmp): #가능하면
                        queue.append((deepcopy(new_tmp[:i] + [tmp] + new_tmp[i+2:]),not flag))
                    else: # i +2 == n-1이라는 뜻, 그러면 i
                        queue.append((deepcopy(new_tmp[:i] +[tmp]),not flag))
    if target in ar and len(ar) == 1:
        return True
    else: return False

def solution(a):
    answer = 0
    a = sorted(a)
    for target in a:
        if available(target,a):
            answer += 1
    return answer

if __name__ == '__main__':
    cases = [[9,-1,-5],	[-16,27,65,-2,58,-92,-71,-68,-61,-33]	]
    for case in cases:
        print(solution(case))