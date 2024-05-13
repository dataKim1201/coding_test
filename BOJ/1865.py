# 웜홀은 시간 반대로
# 도로는 시간 그대로 소요되는데
# 반복문 돌면서 시간이 
import sys
from collections import defaultdict,deque
input = sys.stdin.readline
TC = int(input())
INF = int(1e9)
def dijkstra(s):
    global doro,N
    queue = deque([s])
    dist = [INF] * (N + 1)
    # print(f'start: {s}')
    dist[s] = 0
    while queue:
        x = queue.popleft()
        if x == s and dist[x] != 0:
            return True
        print(x, doro[x])
        for n_node, weight in doro[x]:
            if dist[n_node] > dist[x] + weight:
                print(f'start:{x} => end:{n_node}, ({dist[n_node]} > {dist[x]} + {weight})')
                dist[n_node] = dist[x] + weight
                queue.append(n_node)
            # else:
                # print('wrong',end = ':')
                # print(f'start:{x} => end:{n_node}, ({dist[n_node]} < {dist[x]} + {weight})')
        print(queue,dist)
    return False


for _ in range(TC):
    N,M,W = map(int,input().split())
    doro = defaultdict(list)
    for _ in range(M):
        S,E,T = map(int,input().split())
        doro[S].append([E,T])
        doro[E].append([S,T])
    
    for _ in range(W):
        S,E,T = map(int,input().split())
        doro[S].append([E,-T])
    answer = ''
    for i in range(1,N+ 1):
        print(i)
        if dijkstra(i):
            answer = 'YES'
            break
    if answer != 'YES':
        print('NO')
    else:
        print(answer)