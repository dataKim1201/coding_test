# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
import sys 
input = sys.stdin.readline
answer = [1,1,2,2,2,8]
arr = list(map(int,input().split()))

print([a-b for a,b in zip(answer,arr)])