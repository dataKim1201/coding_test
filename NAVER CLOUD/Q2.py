'''
A = [0,1,3,4,1,-1]
B = [0,2,2,5,-1,0]

이때 k는 3일때만 fair 하게 정의 됨. 따라서 fair point는 1개 답은 1을 반환 해야함.

**문제 범위**
A,B의 문자열은 0개 부터 ~개, (최대가 기억이 안남 대충 O(nlogn)까지 가능했던 것으로 대략 기억)
'''

def solution(A,B):
    presumA = [0]
    presumB = [0]
    for idx in range(1,len(A)):
        presumA.append(presumA[idx -1 ] + A[idx])
        presumB.append(presumB[idx -1 ] + B[idx])
    
    cnt = 0
    # 누적합 구하고 계산하는 로직 필요
    for k in range(len(A)-1):
        if presumA[-1] - presumA[k] == presumA[k] == presumB[-1] - presumB[k] == presumB[k]:
            cnt += 1    
    return cnt


'''
👍 좋은 점

prefix sum 접근은 올바른 방향.

⚠️ 개선

prefix sum 초기화 부분은 복잡 → itertools.accumulate 쓰면 깔끔.

조건식에 psumA[k] == psumB[k]까지 요구했는데, 문제 정의에 꼭 필요했는지는 확인 필요. (혹시 조건을 오해했을 가능성)

시간복잡도 O(N) 맞음 → 성능 OK.
'''

from itertools import accumulate
def TOBE(A,B):
    psumA = list(accumulate(A))
    psumB = list(accumulate(B))
    cnt = 0
    for i in range(len(A)):
        if psumA[i] == psumA[-1] - psumA[i] == psumB[i] == psumB[-1] - psumB[i]:
            cnt += 1
    return cnt