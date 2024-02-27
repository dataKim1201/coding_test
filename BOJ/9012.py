import sys
input = sys.stdin.readline

def bucket_checker(arr):
    bucket = []
    for idx, item in enumerate(arr):
        if item == '(':
            bucket.append(item)
        else: # ')'인 경우
            if len(bucket) >  0:
                bucket.pop()
            else:
                return 'NO'
    if bucket:
        return 'NO'
    return 'YES'

T = int(input())
for _ in range(T):
    arr = input()
    print(bucket_checker(arr.strip()))