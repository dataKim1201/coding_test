import sys
input = sys.stdin.readline
while True:
    arr= list(map(int,input().split()))
    if not all(arr):
        break
    arr = [item**2 for item in arr]
    if max(arr) == sum(arr) - max(arr):
        print('right')
    else:
        print('wrong')