import sys
from itertools import combinations
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())
# back tracking
# 주어진 경우의 수에서
# 가능한 솔루션 3가지를 골라서 진행할 필요가 있음

# backtracking은 가능한 경우의 수에서 
# 모든 경우의수의 조함을 세는 방법
# def calc_distance(arr):

def calc_dist(candidates):
    dist = 0
    for i in range(2):
        item = candidates[i]
        for j in range(i + 1,3):
            item2 = candidates[j]
            for k in range(4):
                if item[k] != item2[k]:
                    dist += 1
    return dist
def backtracking(row,visited):
    global answer
    for i in range(n):
        for j in range(i + 1,n):
            for k in range(j + 1,n):
                answer = min(answer, calc_dist([mbti[i],mbti[j],mbti[k]]))
    # if row == 3:
    #     candidates = [mbti[idx] for idx, item in enumerate(visited) if item == True]
    #     answer = min(answer,calc_dist(candidates))
    # for i in range(n):
    #     if not visited[i]:
    #         visited[i] = True
    #         backtracking(row + 1, visited)
    #         visited[i] = False
    return None
    
res = []
for _ in range(T):
    answer = 999
    n = int(input())
    mbti = input().split()
    if n > 32:
        res.append(0)
    else:
        visited = [False] * n
        # mbti = ['ENTJ','INTP', 'ESFJ']
        # print(calc_dist([0,1,2]))
        backtracking(0,visited)
        res.append(answer)
    
for item in res:
    print(item)
