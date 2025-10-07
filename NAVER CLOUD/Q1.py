'''
문제 예시
Example test:   'acbcbba' -> 1
OK (b 문자만 3개로 홀수 개 존재 +10

Example test:   'axxaxa' -> 2
OK (a,x 모두 홀수 번 등장)

Example test:   'aaaa' -> 0
OK (홀수 번 등장하는 문자가 없음)

문제 범위
문자열 S는 0~500,000 (최대 범위는 정확히 기억이 안남)
'''

def solution(S):
    s_dict = {}
    cnt = 0
    for s in S:
        if s not in s_dict:
            s_dict[s] = 1
        else:
            s_dict[s] += 1
    for k,v in s_dict.items():
        if v % 2 != 0:
            cnt += 1
    return cnt

'''
👍 좋은 점

직접 dict로 counting 잘 구현하셨음.

⚠️ 개선

len(S)가 0,1,2일 때 따로 분기할 필요 없음 → 일반 로직으로 커버됨.

if i in s_dict.keys(): → if i in s_dict: (keys() 호출 불필요)

collections.Counter 쓰면 깔끔.

⏱ 복잡도: O(N) → 적합.
✅ 예외: S=""도 잘 동작.
'''

from collections import Counter
def TO_BE(S):
    return sum([v % 2 for v in Counter(S).values()])
