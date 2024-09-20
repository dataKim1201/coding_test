
import sys
from collections import deque
input = sys.stdin.readline

arr = list(map(int,input().split()))
visited = [False] * len(arr)

max_cnt = 0
min_cnt = int(1e9)
def find(cnt = ''):
    global max_cnt,min_cnt
    if cnt:
        if int(cnt) > max_cnt and all(visited):
            max_cnt = int(cnt) # 최대값 갱신
        if int(cnt) < min_cnt and all(visited):
            min_cnt = int(cnt) # 최대값 갱신
    for idx, item  in enumerate(arr):
        if not visited[idx]:
            visited[idx] = True # 방문 처리 하고 보냄
            find(cnt + str(item))
            visited[idx] = False # 갔다 와서 방문 취소하고 다른 경우의 수를 보겠다 이거지 나머지 for loop 중에서 안가본데를 탐색 하겠지 그러면
find()
print(max_cnt + min_cnt)