import sys
input = sys.stdin.readline
# arr = input().strip()
arr = 'c' * 500000
arr += 'a'* 500001

# bomb = input().strip()
bomb = 'ca'
# if len(set(arr) - set(bomb)) == 0:
#     print('FRULA')
# else:
while bomb in arr:
    arr = arr.replace(bomb,'')
if arr:
    print(arr)
