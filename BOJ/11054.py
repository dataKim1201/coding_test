# bi-tonic
import sys
input = sys.stdin.readline

def is_bi_tonic(arr, k):
    cnt = 1
    # filtering
    # left, right 모두 k값보다 크거나 같으면 모두 삭제
    left_hand = [i for i in arr[:k] if i < arr[k]]
    right_hand = [i for i in arr[k+1:] if i < arr[k]]

    # is_increasing or downsizing
    left_cnt = is_sub(left_hand,asc = 1)
    right_cnt = is_sub(right_hand,asc = 0)
    cnt += left_cnt + right_cnt
    
    return cnt

def is_sub(arr,asc):
    if not arr:
        return 0
    dist = [0 for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and dist[i] < dist[j] and asc:
                dist[i] = dist[j]
            elif arr[i] < arr[j] and dist[i] < dist[j]  and not asc:
                dist[i] = dist[j]
        dist[i] += 1
    return max(dist)

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int,input().split()))
    
    answer = 0
    # k checking
    for k in range(len(arr)):
        tmp = is_bi_tonic(arr, k)
        answer = max(tmp, answer)
    
    print(answer)