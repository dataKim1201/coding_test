import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

def solution(cmds):
    min_x,max_x,min_y,max_y = 0,0,0,0
    direction = {
        -3: (1,0),
        -2: (0,-1),
        -1: (-1,0),
        0:  (0,1),
        1: (1,0),
        2: (0,-1),
        3: (-1,0)
    }
    x,y = 0,0
    L,R = 0,0
    for cmd in cmds:
        if cmd == 'F':
            dx,dy = direction[(R-L)%4]
            x += dx
            y += dy
            min_x,min_y,max_x,max_y = min(min_x,x), min(min_y,y), max(max_x,x), max(max_y,y)
        elif cmd == 'B':
            dx,dy = direction[(R-L)%4]
            x -= dx
            y -= dy
            min_x,min_y,max_x,max_y = min(min_x,x), min(min_y,y), max(max_x,x), max(max_y,y)
        elif cmd == 'L':
            L += 1
        elif cmd == 'R':
            R += 1
    return (max_x-min_x) * (max_y - min_y)

for _ in range(T):
    cmds = input().strip()
    print(solution(cmds))