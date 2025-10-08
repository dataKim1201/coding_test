# return is_grouped
import sys
input = sys.stdin.readline

def is_grouped(string):
    visited = ''
    for s in string:
        if s not in visited:
            visited += s
        elif visited[-1] != s: return 0
    return 1

N = int(input())
answer = sum([is_grouped(input()) for _ in range(N)])
print(answer)