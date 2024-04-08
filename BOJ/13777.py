import sys
input = sys.stdin.readline

def bin_search(case):
    result= []
    arr = [0 for _ in range(50)] # 50개 배열 선언
    arr[case-1] = 1
    i,j = 0,49
    while i <= j:
        mid = (i + j) //2 # 중앙선
        if mid < case-1: # case-1이 더 크다면?
            i = mid +1
        elif mid > case-1:
            j = mid -1
        elif mid == case-1: # 같다면?
            result.append(mid + 1)
            break
        result.append(mid + 1)
    return result




while True:
    case = int(input())
    if case == 0:
        break
    print(*bin_search(case))
