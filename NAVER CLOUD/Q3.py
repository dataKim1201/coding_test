'''
A= [12,3,4,5,1,2,1,4]
A[1: -1] + 10
A= [12,13,14,15,11,12,11,14]
A[4: -1] + 5
A= [12,13,14,15,16,17,16,19]
A[-2] + 2
A= [12,13,14,15,16,17,18,19]
k = 3

- 배열 A가 주어지고 부분 배열을 선택하여 원하는 만큼의 배열의 크기를 증가 시킬 수 있음.
- 부분 배열을 증가를 k번 하여 계속 증가하는 배열을 만들어야 함.
- 이때 k의 최솟값을 반환.
- 이때 엄격하게 증가하는 배열을 위해 i, i+1은 무조건 1이상의 차이가 있어야함.(같으면 안됨)
'''


def solution(A):
    if len(A) == 1: return 0
    cnt = 0
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            cnt += 1
    return cnt


'''
⚠️ 문제 있음

지금 구현은 그냥 “몇 번 감소하는지” 세는 거 → 실제 답과 다름.

예제 A=[12,3,4,5,1,2,1,4] → 기대 답 3인데, 이 코드는 3 반환 → 우연히 맞음. 다른 케이스에서 깨짐.

실제로는 LIS 구해서 len(A) - LIS 길이 해야 맞음.
'''

import bisect

def TOBE(A):
    lis = []
    for x in A:
        pos = bisect.bisect_left(A,x)
        if pos  == len(lis):
            lis.append(x)
        else:
            lis[pos] = x
    return len(A) - len(lis)

'''
A=[12,3,4,5,1,2,1,4]

x = 12
pos = 0
len(lis) = 0
->> lis = [12]

x = 3
pos = 1
len(lis) = 1
->> lis = [12,3]

x = 4
pos = 2
len(lis) = 2
->> lis = [12,3,4]

x = 5
pos = 3
len(lis) = 3
->> lis = [12,3,4,5]

x = 1
pos = 4
len(lis) = 4
->> lis = [12,3,4,5,1]

x = 2
pos = 5
len(lis) = 5
->> lis = [12,3,4,5,1,2]

x = 1
pos = 4
len(lis) = 6
->> lis = [12,3,4,5,1,2]

x = 4
pos = 2
len(lis) = 6
->> lis = [12,3,4,5,1,2]

'''
