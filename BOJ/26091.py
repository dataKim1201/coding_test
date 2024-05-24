import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
def solution(arr):
    if len(arr) == 1:
        return 0
    L,R = 0,len(arr)-1
    sorted_arr = sorted(arr)
    cnt = 0

    while L < R:
        if sorted_arr[L] + sorted_arr[R] >= m:
            cnt += 1
            L += 1
            R -= 1
        elif sorted_arr[L] + sorted_arr[R] < m:
            # L 을 해야할 지
            # R 을 해야할 지 ?
            L += 1
    return cnt
print(solution(arr))