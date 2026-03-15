import sys
input = sys.stdin.readline

MOD = 1000000000
N = int(input())

prev = [[0] * 1024 for _ in range(10)]

for i in range(1, 10):
    prev[i][1 << i] = 1

for _ in range(1, N):
    curr = [[0] * 1024 for _ in range(10)]

    for last in range(10):
        for mask in range(1024):
            cur = prev[last][mask]
            if cur == 0:
                continue

            if last > 0:
                nxt = last - 1
                new_mask = mask | (1 << nxt)
                curr[nxt][new_mask] = (curr[nxt][new_mask] + cur) % MOD

            if last < 9:
                nxt = last + 1
                new_mask = mask | (1 << nxt)
                curr[nxt][new_mask] = (curr[nxt][new_mask] + cur) % MOD

    prev = curr

answer = sum(prev[last][1023] for last in range(10)) % MOD
print(answer)