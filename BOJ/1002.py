import sys
import math

input = sys.stdin.readline

T = int(input())
def L2_dist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1 -y2)**2)
for _ in range(T):
    x1,y1,r1,x2,y2,r2  = map(int,input().split())
    point_dist = L2_dist(x1,y1,x2,y2)
    if point_dist == 0 and r1 == r2:
        print(-1)
        continue
    elif point_dist == 0 and r1 != r2:
        print(0)
    elif r1 < r2 and point_dist < r2:
        if r2 == r1 + point_dist:
            print(1)
        elif r2 > r1 + point_dist:
            print(0)
        else:
            print(2)
    elif r1 > r2 and point_dist < r1:
        if r1 == r2 + point_dist:
            print(1)
        elif r1 > r2 + point_dist:
            print(0)
        else:
            print(2)
    elif point_dist == r1 + r2:
        print(1)
    elif point_dist < r1 + r2:
        print(2)
    elif point_dist > r1 + r2:
        print(0)
