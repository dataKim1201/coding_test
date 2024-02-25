def merge_sort(arr,reverse=False):
    if len(arr) > 1:
        left_arr = merge_sort(arr[:len(arr)//2],reverse)
        right_arr = merge_sort(arr[len(arr)//2:],reverse)

        l= r= 0
        result = []
        while l < len(left_arr) and r <len(right_arr):
            rr = left_arr[l] >= right_arr[r] if reverse else left_arr[l] < right_arr[r]
            if rr:
                result.append(left_arr[l])
                l +=1
            else:
                result.append(right_arr[r])
                r += 1
        if reverse:
            if l < len(left_arr): result.extend(left_arr[l:])
            if r < len(right_arr): result.extend(right_arr[r:])
        else:
            if r < len(right_arr): result.extend(right_arr[r:])
            if l < len(left_arr): result.extend(left_arr[l:])
    else:
        return arr
    return result

def solution(n,arr):
    arr = merge_sort(arr)
    i =0
    result = 0
    while i < len(arr):
        result +=  (n - i) * arr[i]
        i += 1
    return result 

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(solution(n,arr))

