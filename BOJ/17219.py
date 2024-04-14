import sys
input = sys.stdin.readline

n,m = map(int,input().split())

PW_DICT = {}
for _ in range(n):
    AD,PW = input().split()
    if AD not in PW_DICT:
        PW_DICT[AD] = PW
    
res = []
for _ in range(m):
    case = input().strip()
    res.append(PW_DICT[case])

print('\n'.join(res))