import sys
from copy import deepcopy
from itertools import combinations
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

def gcd(a,b):
    while b:
        a, b = b, a % b # 유클리드 알고리즘을 이용한 최대공약수 구하기
    return a

def knapsack(arr):
    INF = max(arr) + 1
    DP = [0] * INF
    for i in range(len(arr)):
        for j in range(1,INF):
            if DP[j]: # 0이 아니라면
                DP[gcd(j,arr[i])] += DP[j]
        DP[arr[i]] += 1
    return DP[1]
mod = 10000003
print(knapsack(arr)% mod)

# arr = [2,3,4]
# def check_prime(arr):
#     if len(arr)> 2:
#         return check_prime([check_prime(arr[:-1]),arr[-1]])
#     elif len(arr) == 2:
#         return gcd(arr[0],arr[1])


# def comb(arr):
#     if len(arr) == 1 and arr[0] == 1: return 1
#     result =0
#     DP= {}
#     for i in range(2,len(arr) + 1):
#         for item in combinations(arr,i):
#             if str(item) not in DP:
#                 print(list(item),check_prime(list(item)))
#                 if check_prime(list(item)) == 1:
#                     result += 1
#                 DP[str(item)] = check_prime(list(item))
#             else:
#                 if DP[str(item)] == 1:
#                     result += 1
#     return result
# cnt = 0
# visited = [False] * n
# prime = []
# no_prime = []
# def backtracking(cur):
#     global cnt
#     if cur == n:
#         return 
#     visited[cur] = True
#     if sum(visited) > 1:
#         # print()
#         tmp = [item for idx, item in enumerate(arr) if visited[idx]]
#         # print(cur,tmp,check_prime(tmp))
#         if tmp not in prime and tmp not in no_prime:
#             if check_prime(tmp) == 1:
#                 cnt += 1
#                 prime.append(tmp)
#             else:
#                 no_prime.append(tmp)
#         elif tmp in prime:
#             cnt += 1

#     backtracking(cur+1)
#     visited[cur] = False
#     backtracking(cur+1)

# if len(arr) == 1 and arr[0]==1:
#     print(1)
# else:
#     backtracking(0)
#     print(cnt)
