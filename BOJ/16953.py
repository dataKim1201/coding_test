import sys
from collections import deque
input =sys.stdin.readline

n,target = map(int,input().split())
def moving(curr, way):
    if way == 0: # 2를 곱해라
        return curr * 2
    elif way == 1:
        return int(str(curr) + '1')


def bfs(n,target):
    visited = []
    # for i in range(n): visited[i] = True
    # visited[n] = True
    queue = deque([(n,0)])
    while queue:
        x, cnt = queue.popleft()
        if x == target:
            return cnt 
        for i in range(2):
            nx = moving(x,i)
            if nx <= target and nx not in visited:
                visited.append(nx)
                queue.append((nx,cnt + 1))
    return -1

if __name__ == '__main__':
    ans = bfs(n,target)
    if ans != -1:
        print(ans + 1)
    else:
        print(ans)