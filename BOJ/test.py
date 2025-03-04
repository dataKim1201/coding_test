# 2444: 별 찍기 - 7

# 입력: N
# 출력: 2N - 1

import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, 2*n):
    if i < n:
        print(' '*(n-i -1 ), '*'*(2*i - 1))
    elif i == n:
        print( '*'*(2*i -1))
    else:
        print(' '*(i-n), '*'*(2*(2*n - i) - 1))

for i in range(1, 2*n):
    if i < n:
        print((n-i), (2*i - 1))
    elif i == n:
        print(2*i -1)
    else:
        print((i-n), (2*(2*n - i) - 1))

'''
1 ; 4, 1
2 : 3, 3
3 : 2, 5
4 : 1, 7
5 : 0, 9
6 : 1, 7
7 : 2, 5
8 : 3, 3
9 ; 4, 1
     *
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''