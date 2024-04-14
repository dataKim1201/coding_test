import sys
input = sys.stdin.readline
n = int(input())
arr= list(map(int,input().split()))
B,C = map(int,input().split())
arr = [ i - B if B <= i else 0 for i in arr]
res = n
for item in arr:
    res += item//C if item % C == 0 else item//C + 1
print(res)