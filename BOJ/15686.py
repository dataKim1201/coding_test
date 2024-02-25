from itertools import combinations
def L1_norm(x,y):
    return sum([abs(x[i]-y[i]) for i in range(len(x))])

def var_search(map):
    home_idx = []
    cousine_idx = []
    for i in range(N):
        for j in range(N):
            if map[i][j] == 0:
                continue
            elif map[i][j] == 1:
                home_idx.append([i,j])
            elif map[i][j] == 2:
                cousine_idx.append([i,j])
    return home_idx,cousine_idx

def calc_result(home_idx, cousine_idx,m):
    final = 999999
    candidates = combinations(cousine_idx,m)
    for candi in candidates:
        result = []
        for item in home_idx:
            tmp = 999
            for chin in candi:
                tmp = min(tmp,L1_norm(item,chin))
            result.append(tmp)
        final = min(final, sum(result))
    return final
if __name__ == '__main__':
    N,M = map(int, input().split())

    map = [list(map(int,input().split())) for _ in range(N)]
    home_idx, cousine_idx = var_search(map)
    result = calc_result(home_idx, cousine_idx,M)
    print(result)