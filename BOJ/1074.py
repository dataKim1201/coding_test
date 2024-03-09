import sys
input = sys.stdin.readline

n,r,c = map(int,input().split())

target = 0
while True:
    if n == 0:
        break 
    if 2**(n-1) > r: # row 이게 작고 
        if 2**(n-1) > c: # column 이게 작은데
            target += 2**(n-1)* 2**(n-1)*0
        else: # column은 큰거니까
            target += 2**(n-1)* 2**(n-1)*1
            c -= 2**(n-1)
    else:
        if 2**(n-1) > c: # column 이게 작은데
            target += 2**(n-1)* 2**(n-1)*2
            r -= 2**(n-1)
        else: # column은 큰거니까
            target += 2**(n-1)* 2**(n-1)*3
            r -= 2**(n-1)
            c -= 2**(n-1)
    
    n -= 1

print(target)



def calc(arr,n,r,c):
    if len(arr) == 4:
        return arr[r + 2*c]
    if len(arr)//2**(n+1) > r: # row 이게 작고 
        if len(arr)//2**n> c: # column 이게 작은데
            target = 0
        else: # column은 큰거니까
            target = 1
            c -= len(arr)//2**(n+1)
    else:
        if len(arr)//2**(n+1) > c: # column 이게 작은데
            target = 2
            r -= len(arr)//2**(n+1)
        else: # column은 큰거니까
            target = 3
            r -= len(arr)//2**(n+1)
            c -= len(arr)//2**(n+1)
    
    result =[]
    for i in range(0,len(arr),len(arr)//4):
        item = arr[i:i + len(arr)//4]
        result.append(item)

    return calc(result[target],n-1, r,c)