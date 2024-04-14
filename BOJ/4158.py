import sys
input = sys.stdin.readline

while True:
    N,M = map(int,input().split())
    if N == 0 and M == 0: break
    n_arr= [int(input()) for _ in range(N)]
    m_arr = [int(input()) for _ in range(M)]
    i,j,ans = 0,0,0
    while i <N and j <M:
        if n_arr[i] == m_arr[j]:
            i += 1
            j += 1
            ans += 1
        elif n_arr[i] > m_arr[j]:
            j += 1
        elif n_arr[i] < m_arr[j]:
            i += 1
    print(ans)
