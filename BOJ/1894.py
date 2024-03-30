import sys
input = sys.stdin.readline
def solution(arr):

    xy1 = [arr[0],arr[1]]
    xy2 = [arr[2],arr[3]]
    xy3 = [arr[6],arr[7]]
    print(xy1,xy2,xy3)
    ans = xy3
    def calc_diff(xy1,xy2):
        return xy1[0]-xy2[0], xy1[1] - xy2[1]
    diff_1 = calc_diff(xy3,xy2)
    diff_2 = calc_diff(xy1,xy2)
    # 그 2개의 차이로 가는데 만나는 것
    for i in range(2):
        if i % 2==0:
            cand1 = ans[0] + diff_1[0], ans[1] + diff_1[1]
        else: cand1 = ans[0] - diff_1[0], ans[1] - diff_1[1]
        for j in range(2):
            if i % 2==0:
                cand2 = ans[0] + diff_2[0], ans[1] + diff_2[1]
            else: cand2 = ans[0] - diff_2[0], ans[1] - diff_2[1]
            if cand1 == cand2:
                return cand1
    return -1
while True:
    cmd = input().split()
    if cmd =='\n':
        break
    arr = list(map(float,cmd))
    print(solution(arr))



