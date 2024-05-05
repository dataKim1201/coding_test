import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
N = int(input().strip())
graph = {}
for _ in range(N):
    cmd = list(map(int,input().split()))
    if cmd[0] not in graph:
        graph[cmd[0]] = []
    start = cmd[0]
    cmd = cmd[1:]
    for idx in range(len(cmd)):
        if cmd[idx] == -1:
            break
        if idx % 2== 0:
            end = cmd[idx]
        else:
            weight = cmd[idx]
            graph[start].append([end,weight])
            del end, weight

# print(graph)
answer = 0
final_end = 0
def dfs(start,visited = 0,cnt = 0): #, string = ''):
    global answer, final_end
    if not (visited & (1<< start)):
        visited |= (1<<start)
        for node in graph[start]:
            end,weight = node
            if not (visited & (1<< end)):
                result,_ = dfs(end,visited,cnt + weight)
                if result > answer:
                    answer = result
                    final_end = end
    return cnt, final_end
_,ed  = dfs(1,0,0)
dfs(ed,0,0)
print(answer)

