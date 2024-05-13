import sys

def mat_mul(A, B):
    temp = [[0, 0] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += (A[i][k]*B[k][j])
            temp[i][j] %= 1000000
    return temp
def merge_divide(n):
    mat = [[1,1],[1,0]]
    if n == 1:
        return mat
    x = merge_divide(n//2)
    if n % 2== 0:
        return mat_mul(x,x)
    else:
        return mat_mul(mat_mul(x,x),mat)
n = int(sys.stdin.readline())
print(merge_divide(n)[0][1])