import sys
input = sys.stdin.readline
directions = [(0,1), (-1,0), (0,-1), (1,0)]

def solution():
    cnt = 0
    s_bodies = [(0,0)]
    cur_idx = (0,1)
    while True:
        # 이동 하기
        dx,dy = cur_idx
        x,y = s_bodies[0]
        nx,ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < N and (nx,ny) not in s_bodies:
            cnt += 1
            # 사과 먹기
            if zido[nx][ny] == 1:
                s_bodies = [(nx,ny)] + s_bodies
                zido[nx][ny] = 0
            else:
                s_bodies = [(nx,ny)] + s_bodies[:-1]
                
            # 회전하기
            if cnt in spin_dict:
                dirt = spin_dict[cnt]
                idx = directions.index((dx,dy))
                if dirt == 'L':
                    n_idx = (idx + 1) % 4
                if dirt == 'D':
                    n_idx = 3 if idx == 0 else idx - 1
                cur_idx = directions[n_idx]
        else:
            return  cnt + 1
        
if __name__ == '__main__':
    N = int(input())
    K = int(input())
    apples = [tuple((i-1 for i in map(int,input().split()))) for _ in range(K)]
    zido = [[0 for _ in range(N)] for _ in range(N)]

    for idx in apples:
        x,y = idx
        zido[x][y] = 1

    L = int(input())
    spin_dict = {}
    for _ in range(L):
        t,l = input().split()
        spin_dict[int(t)] = l

    print(solution())
