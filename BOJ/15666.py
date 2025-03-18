import sys
input = sys.stdin.readline

N,M = map(int,input().split())
candidates = sorted(list(set(map(int,input().split()))))
def is_ascending(arr):
    return not any([arr[i] > arr[i + 1] for i in range(len(arr)-1) ])

def backtracking(arr):
    if len(arr) == M:
        if is_ascending(arr):
            print(*arr)
        return
    
    for num in candidates:
        arr.append(num)
        backtracking(arr)
        arr.pop()

backtracking([])