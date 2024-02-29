import sys 
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n,m = map(int,input().split())
    wheight = list(map(int,input().split()))
    queue = deque([(idx,whght) for idx, whght in enumerate(wheight)])
    res = 0
    while queue:
        idx, item = queue.popleft()
        if all([item >= tt[1] for tt in queue]):
            res += 1
            if idx == m:
                break
        else:
            queue.append((idx,item))
        
    print(res)