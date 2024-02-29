'''
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.
'''
import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
c = Counter(arr)

target = c.most_common(1)[0][1]

ttr = [(val,cnt) for val, cnt in c.items() if cnt == target]

if len(ttr) <= 1:
    answer3 = ttr[0][0]
else:
    # print(sorted(ttr,key = lambda x: x[0],reverse=False))
    answer3 = sorted(ttr,key = lambda x: x[0],reverse=False)[1][0]


print(int(round(sum(arr)/N,0)))
print(sum(arr)//N)
print(sorted(arr,reverse=False)[N//2])
print(answer3)
print(max(arr)-min(arr))

# 5
