import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
true = list(map(int,input().split()))
if len(true) != 1:
    true = true[1:]
parties = [list(map(int,input().split()))[1:] for _ in range(M)]
# sorted_parties = sorted(parties,key=lambda x: len(set(x) &set(true)), reverse=True)
answer = 0

def bfs():
    visited = 0
    queue = deque(true)
    while queue:
        cur = queue.popleft()
        visited |= (1<<cur) # 넣어주고
        for item in parties:
            if cur in item: # 파티에 참석했다면?
                for pp in item:
                    if pp not in true and not visited & (1<<pp):
                        true.append(pp)
                        queue.append(pp)
bfs()
for item in parties:
    if all([pp not in true for pp in item]):
        answer += 1
print(answer)