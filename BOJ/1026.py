import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(sum([i * j for i, j in zip(sorted(a,reverse=True),sorted(b))]))
# 그리디하게
# A는 제일 큰 수로 정렬
# B는 제일 작은 수로 정렬해서 곱하면 됨.