import sys
from collections import Counter
input = sys.stdin.readline
case = input().strip()
def make_palindrome(case):
    cnter = Counter(case)
    cnt = 0
    mid = None
    result = ''
    for key in cnter:
        if cnter[key] %2 == 1:
            cnt += 1
            mid = key
            cnter[key] -= 1
        if cnt > 1:
            return "I'm Sorry Hansoo"
    # 반개씩 만들면 되는 거자나
    for key in sorted(cnter):
        result += key*(cnter[key]//2)
    if mid:
        return result + mid + result[::-1]
    return result + result[::-1]

print(make_palindrome(case))