import sys
from bisect import bisect_left
input = sys.stdin.readline

def is_sub(arr):
    dist = [0 for _ in range(len(arr))]
    lst = [arr[0]]
    for i in range(len(arr)):
        if lst[-1] < arr[i]:
            lst.append(arr[i])
            dist[i] = len(lst) - 1
        else:
            idx = bisect_left(lst,arr[i]) # 어디에 넣을지
            lst[idx] = arr[i]
            dist[i] = i
    # 출력하기
    final_cnt = len(lst)
    print(final_cnt)
    res = []
    for i in range(len(dist) -1, -1, -1):
        if dist[i] == final_cnt:
            res.append(arr[i])
            final_cnt -= 1
    print(*res[::-1])
            
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    is_sub(arr)
    