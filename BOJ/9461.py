# 1, 2, 3, 4,     5, 6,   7,  8,  9,  10,     11, 12
# 1, 1, 1, 2,     2, 3,   4,  5,  7,  9,      12, 17
# 0, 0, 0, 2,3    4, 3,4  2,6 3,7 4,8 9,5     6,10
import sys
input = sys.stdin.readline 
pando_arr = [0,1,1,1,2,2,3]
n = int(input())
for _ in range(n):
    case = int(input())
    if case > len(pando_arr)-1:
        for i in range(len(pando_arr),case+ 1):
            pando_arr.append(pando_arr[-1] + pando_arr[-5])
    print(pando_arr[case])
