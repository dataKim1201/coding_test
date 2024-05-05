import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
N = int(input().strip())
graph = {i : [] for i in range(1,N+1)}
for _ in range(N-1):
    start,end,weight = map(int,input().split())
    graph[start].append([end,weight])
    graph[end].append([start,weight])



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