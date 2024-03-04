# r의 값은 26보다 큰 소수인 31로 하고 M의 값은 1234567891
import sys
input = sys.stdin.readline
n  = int(input())
tt = input()
res = sum([(ord(tt[i])-96) * (31**i) for i in range(n)]) % 1234567891
print(res)