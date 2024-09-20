#  \(M\)개의 자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 \(\binom{N}{K}\)를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline
INF = 4000000
DP = [[1] * INF for _ in range(INF//2)] # C는 최대 20000
T = int(input())
def binom(n,k):
    
    return None
for _ in range(T):
    n,k = map(int,input().split())
    print(binom(n,k))