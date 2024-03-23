import sys
input = sys.stdin.readline
n = int(input())

zido = [list(map(int,input().split())) for _ in range(n)]



def dfs(zido,n,black=0, white=0):
    if sum(sum(zido,[])) == 0:
        return  black + 1, white
    if  sum(sum(zido,[])) == n*n:
        return  black, white + 1
    
    candidates = []
    for items in [zido[:n//2], zido[n//2:]]:
        tmpL, tmpR = [],[]
        for item in items:
            tmpL.append(item[:n//2])
            tmpR.append(item[n//2:])
        candidates.append(tmpL)
        candidates.append(tmpR)
    # for idx, cand in enumerate(candidates):
    #     print(f'idx : {idx + 1}')
    #     for can in cand:
    #         print(*can)
    B,W = 0,0
    for cand in candidates:
        b,w = dfs(cand,n//2)
        B += b
        W += w
    return B,W

B,W = dfs(zido, n)
print('\n'.join(map(str,[B,W])))