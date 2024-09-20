import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
#  10 2147483640 12
A,B,C = map(int,input().split())
pattern = []
def make_pattern(A,B,C):
    if B == 1:
        return A % C
    
    tmp = make_pattern(A,B//2,C)
    return (tmp * tmp * (1 if B %2  ==0 else A)) %C

print(make_pattern(A,B,C))
