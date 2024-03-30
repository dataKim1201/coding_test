

import sys
from itertools import combinations
from collections import Counter
input = sys.stdin.readline
n = int(input())
arr = [input().strip() for _ in range(n)]
k = int(input())
result =0

def change_jinbub_to_36(digit):
    result =''
    while digit:
        num = str(digit % 36) if digit % 36  <= 9 else chr(digit % 36 +55)
        result = num + result
        digit //= 36
    return result if result else '0'

# 원래 값을 구하고
for target in arr:
    result += int(target,36)


# 철자별 변화량을 계산한다.
candle = ''.join(arr)
candidates = [i for i in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' if i in candle]
diff = []

for letter in candidates:
    tmp_arr = '_'.join(arr)
    tmp_arr = tmp_arr.replace(letter,'Z')
    tmp_arr = tmp_arr.split('_')
    tmp_diff = 0
    for target in tmp_arr:
        tmp_diff += int(target,36)
    if tmp_diff-result> 0:
        diff.append(tmp_diff-result)

result = result + sum(sorted(diff,reverse=True)[:min(len(candle),k)])
print(change_jinbub_to_36(result))


# candidates = set(''.join(arr).replace('Z',''))
# for case in combinations(candidates,min(k,len(candidates))):
#     tmp_arr = '_'.join(arr)
#     for change_num in case:
#         tmp_arr = tmp_arr.replace(change_num,'Z')
#     tmp_arr = tmp_arr.split('_')
#     tmp = 0
#     if tmp_arr != arr:
#         for item in tmp_arr:
#             tmp += change_jinbub_to_10(item)
#         result = max(result,tmp)
# print(change_jinbub_to_36(result))
# 0001 -> 1
# 0011 -> 1 + 2*1
# 0111 -> 1 + 2*1 + 2*2
# 1111 -> 1 + 2**1 + 2**2 + 2**3

# GOOD -> D + O*36**1

# 3*36**4+1*36**3+34*36**2+30*36**1+11*36**0