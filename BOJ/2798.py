from itertools import combinations
n,m = map(int,input().split())
arr = list(map(int,input().split()))
candidates = [sum(item) for item in combinations(arr,3) if sum(item) <= m]
res = sorted(candidates,reverse=True)[0]
print(res)
