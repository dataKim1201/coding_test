import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int,input().split())
zido = [list(map(int,input().split())) for _ in range(n)]



def get_cur_dying(cheese_inds):
    output = []
    for cheese in cheese_inds:
        x,y = cheese
        tmp = 0
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < n  and 0 <= ny < m and zido[nx][ny] == -1:
                tmp += 1
        if tmp >= 2:
            output.append(cheese)
    return output

def get_out_air(x,y):
    visited = [[False] * m for _ in range(n)]
    queue = deque([[x,y]])
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0<= nx < n and 0<= ny < m and zido[nx][ny] == 0 and not visited[nx][ny]:
                # 바깥 공기만 모아 세우기
                queue.append([nx,ny])
    return visited

def solution():
    # get_out_air(0,0)
    cnt = 0
    flag = True
    while flag:
        out_air = get_out_air(0,0)
        dying = []
        flag = False
        for x in range(n):
            for y in range(m):
                if zido[x][y] == 1:
                    tmp = 0
                    for i in range(4):
                        nx,ny = x + dx[i], y + dy[i]
                        if out_air[nx][ny] and zido[nx][ny] == 0:
                            tmp += 1
                    if tmp >= 2:
                        dying.append([x,y])
                        flag = True
        for x,y in dying:
            zido[x][y] = 0
        cnt += 1
    return cnt

dx,dy = [1,-1,0,0],[0,0,1,-1]
print(solution())



# import sys
# from collections import deque

# input = sys.stdin.readline
# n,m = map(int,input().split())
# zido = [list(map(int,input().split())) for _ in range(n)]

# cheese_inds = []
# for i in range(len(zido)):
#     for j in range(len(zido[i])):
#         if zido[i][j] == 1:
#             cheese_inds.append([i,j])


# def get_cur_dying(cheese_inds):
#     output = []
#     for cheese in cheese_inds:
#         x,y = cheese
#         tmp = 0
#         for i in range(4):
#             nx,ny = x + dx[i], y + dy[i]
#             if 0 <= nx < n  and 0 <= ny < m and zido[nx][ny] == -1:
#                 tmp += 1
#         if tmp >= 2:
#             output.append(cheese)
#     return output

# def get_out_air(x,y):
#     global zido
#     visited = [ [False] * m for _ in range(n)]
#     queue = deque([[x,y]])
#     visited[x][y] =  True
#     while queue:
#         x,y = queue.popleft()
#         # zido[x][y] = -1
#         for i in range(4):
#             nx,ny = x + dx[i], y + dy[i]
#             if 0<= nx < n and 0<= ny < m and not visited[nx][ny]:
#                 if zido[nx][ny] >=1:
#                     # 바깥 공기만 모아 세우기
#                     zido[nx][ny] += 1
#                 else:
#                     queue.append([nx,ny])
#                     visited[nx][ny] = True
                

# def print_zido(zido):
#     print('*'*100)
#     for item in zido:
#         print(*list(map(int,item)))
#     print('*'*100)

# def solution(cheese_inds):
#     global zido 
#     cnt = 0
#     while True:
#         get_out_air(0,0)
#         for i in range(n):
#             for j in range(m):
#                 if zido[i][j] >=3: 
#                     zido[i][j] = 0
#                     flag = False
#                 elif zido[i][j] == 2:
#                     zido[i][j] = 1
#                     flag = False
#         if flag: break
#         cnt += 1

#     return cnt
#     #     cur_dying = get_cur_dying(cheese_inds)
#     #     for cheese in cur_dying:
#     #         x,y = cheese
#     #         get_out_air(x,y)
#     #     cheese_inds =  [item for item in cheese_inds if item not in cur_dying]
#     #     cnt += 1
#     # return cnt

# dx,dy = [1,-1,0,0],[0,0,1,-1]
# # print_zido(zido)
# # get_out_air(0,0)
# # print_zido(zido)
# print(solution(cheese_inds))
    
            




# # output = get_out_air(0,0,visited)
# visited = [[False] * m for _ in range(n)]
# is_out_air = get_out_air(0,0,visited)
# print('out air int 1')
# print_zido(is_out_air)


# cnt = 0
# while cheese_inds:
#     print('total cheese', cheese_inds)
#     print('get_cur_dying',get_cur_dying(cheese_inds,is_out_air))
#     for cheese in get_cur_dying(cheese_inds,is_out_air):
#         x,y = cheese
#         cheese_inds.remove(cheese)
#         zido[x][y] = 0
#         is_out_air = get_out_air(x,y,is_out_air)
#     print('out air int 1')
#     print_zido(is_out_air)
#     cnt += 1
# print(cnt)
