import sys
n = int(sys.stdin.readline())
stars = [ [' '] * 2*n for _ in range(n)]

def gen_star(st,ed,size):
    if size == 3:
        # Do printing
        stars[st][ed] = '*'
        stars[st + 1][ed-1],stars[st + 1][ed + 1] = '*','*'
        for idx in range(-2,3):
            stars[st + 2][ed - idx] = '*'
    else:
        newSize= size//2
        gen_star(st, ed, newSize)
        gen_star(st + newSize, ed - newSize, newSize)
        gen_star(st + newSize, ed + newSize, newSize)

gen_star(0,n-1,n)
for star in stars:
    print(''.join(star))