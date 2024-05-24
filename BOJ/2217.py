# 로프에 개수 만큼 반복문을 도는데
# 로프를 정렬하고 
# 로프와 가용가능한 로프의 수를 출력하여 더하면 된다. 
# 만약 같은 로프의 중량이 있는 경우? 무시해도 성립이 된다.
# 10,10,10, 7 8 2
# 1-> answer ; 10
# 2 -> answer : 20
# 2 -> answer : 30
# 3 -> answer: 24
# 4 -> answer: 28
# 5 -> answer: 10 break!! 요런 느낌

import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
sorted_arr = sorted(arr,reverse=True)
answer = 0
for idx, item in enumerate(sorted_arr):
    if answer < item* (idx + 1):
        answer = item*(idx+ 1)
print(answer)

