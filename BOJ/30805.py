# 사전 순 최대 부분 수열
# 두 배열이 주어지면  -> 수열의 부분 수열 집합을 구하고
# 사전 순 최대 부분 수열을 구해라.
import sys
from copy import deepcopy
input = sys.stdin.readline
N = int(input())
a_set = list(map(int,input().split()))
M = int(input())
b_set = list(map(int,input().split()))

common_set = set(a_set) & set(b_set)

if not common_set:
    print(0)
    exit()

result = []
while common_set:
    max_val = max(common_set)
    result.append(max_val)
    a_idx = a_set.index(max_val)
    b_idx = b_set.index(max_val)

    a_set = a_set[a_idx + 1 : ]
    b_set = b_set[b_idx + 1 : ]
    common_set = set(a_set) & set(b_set)


print(len(result))
print(*result)

# 9
# 5 4 3 1 5 3 7 5 5
# 8
# 5 7 2 1 3 5 4 3