n = int(input())
# stacks = [int(input()) for _ in range(n,1,-1)]x

def solution(n):
    tmp = 1
    status = []
    result = []
    for i in range(n):
        target = int(input())
        while tmp <= target:
            status.append(tmp)
            result.append('+')
            tmp +=1
        if tmp == target:
            result.append('-')
            status.pop()
            continue
        if status[-1] == target:
            result.append('-')
            status.pop()
        else:
            return 'NO'
    return result

ans = solution(n)
if isinstance(ans,list):
    for item in ans:
        print(item)
else:
    print(ans)