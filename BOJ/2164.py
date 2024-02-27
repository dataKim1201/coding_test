import sys
import math
input = sys.stdin.readline
n = int(input())
def card2(n):
    if n ==1 :
        return 1
    term = math.log(n,2)
    target = int(term) +1 if 2**int(term) != n else int(term)
    diff = 2**target - n
    return 2**target - 2 * diff

k = card2(n)
print(k)
