import sys
from collections import deque
input = sys.stdin.readline

def change(case,cmd):
    if cmd == 'D': return case * 2 % 10000
    elif cmd == 'S': return case -1 % 10000
    elif cmd == 'L': return case*10 % 1000 + case // 1000
    elif cmd == "D": return case % 10 * 1000 + case//10
def bfs(case, target):
    queue = deque([(case, "")])
    command = ["D", "S", "L", "R"]
    visited = [False]*10000
    visited[case] = True
    while queue:
        tmp, cmd = queue.popleft()
        if tmp == target:
            return cmd
        for i in command:
            new_tmp = change(tmp,i)
            if not visited[new_tmp]:
                queue.append([new_tmp,cmd + i])
                visited[new_tmp] = True

T = int(input().strip())
res = []
for _ in range(T):
    case, target = map(int,input().split())
    res.append(bfs(case,target))
print('\n'.join(res))