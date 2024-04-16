import sys
input = sys.stdin.readline

n = int(input())
arr = [float(input()) for _ in range(n)]
p_prod = []
for i in range(1,n):
    arr[i] = max(arr[i], arr[i]* arr[i-1])
    
print('%0.3f'% max(arr))