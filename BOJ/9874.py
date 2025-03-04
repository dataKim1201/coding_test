# 이 과제에서는 네 개의 정수 집합이 주어집니다. 
# 각 집합에서 정수를 하나씩 선택하여 그 합이 0이 되도록 하는 것이 과제입니다. 
# 이러한 선택이 정확히 하나만 존재한다고 가정할 수 있습니다.


# 입력
# 입력의 첫 번째 줄에는 공백 문자로 구분된 네 개의 숫자 a, b, c, d가 포함되며, 
# 네 집합 각각에 있는 요소의 수를 나타냅니다. 
# 이러한 각 숫자는 1 ≤ a, b, c, d ≤ 500인 양의 정수입니다. 
# 다음 a + b + c + d 줄에는 각각 -60000보다 작지 않고 60000보다 크지 않은 원소가 포함됩니다. 
# 첫 번째 집합의 요소가 먼저 나열되고 
# 두 번째 집합의 요소 등이 그 뒤에 나열됩니다.


# 출력은 공백 문자로 구분된 네 개의 정수로 구성됩니다. 
# 숫자는 입력 파일에 나열된 순서대로 표시되어야 합니다.

import sys
input = sys.stdin.readline

set_num = list(map(int,input().split()))

# 완탐으로 하면 좀 빡센데
# 4가지 경우의 수를 모두 곱해야 0이 되는 경우의 수가 있다는 거 아녀
# 백트래킹?
ans = [
    [ int(input()) for _ in range(t)] for t in set_num 
]
# print(ans)



# 매트릭스를 2개 만들어서 둘의 합을 한번 보자
aabb = sum([[a + b  for b in ans[1]] for a in ans[0]],[])
ccdd = sum([[c + d  for d in ans[3]] for c in ans[2]],[])


# print('aabb', aabb)
# print('ccdd', ccdd)
for i in range(len(aabb)):
    for j in range(len(ccdd)):
        if aabb[i] + ccdd[j] == 0:
            # print(i,j)
            # print((i+ 1)//set_num[1], (i + 1)  % set_num[1], (j + 1) // set_num[3], (j + 1) % set_num[3])
            print(ans[0][(i+ 1)//set_num[1]], ans[1][(i + 1) % set_num[0]], ans[2][(j + 1) // set_num[3]], ans[3][ (j + 1) % set_num[3]])
            break
            # set_num의 1원소의 개수를 i로 나눈 몫이 a의 index 
            # set_num의 1원소의 개수를 i로 나눈 나머지가 b의 index 
            # set_num의 3원소의 개수를 i로 나눈 몫이 c의 index 
            # set_num의 3원소의 개수를 i로 나눈 나머지가 d의 index



import sys
from collections import deque

input  = sys.stdin.readline

arr = list(map(int,input().split()))
visited = [False] * len(arr)

max_cnt = 0
min_cnt = int(1e9)

def find(cnt = ''):
    global max_cnt, min_cnt
    if cnt:
        if int(cnt) > max_cnt and all(visited):
            max_cnt = int(cnt) # 최대값 갱신
        if int(cnt) < min_cnt and all(visited):
            min_cnt = int(cnt)
    for idx, item in enumerate(arr):
        if not visited[idx]:
            visited[idx] = True
            find(cnt + str(item))
            visited[idx] = False
find()
print(max_cnt + min_cnt)