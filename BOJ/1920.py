import sys
input = sys.stdin.readline
n = int(input())
n_arr = list(map(int,input().split()))
m = int(input())
m_arr = list(map(int,input().split()))

result = []

for m_item in m_arr:
    if m_item in n_arr:
        result.append(1)
    else:
        result.append(0)
for item in result:
    print(item)
