import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
rank = sorted(set(arr))
result = {rank[i]: i for i in range(len(rank))}

print(*map(lambda x : result[x],arr))