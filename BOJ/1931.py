import sys
input = sys.stdin.readline
def solution(n,arr):
    # 겹치는 것이랑
    # 제일 빨리 끝나는 것 위주로
    # print('sorted arr',arr)
    i= 0 
    cnt = 1
    last_time = arr[0][0] # 가장 늦게 끝나는 회의의 시작시긴
    for i in range(1,n):
        st_time = arr[i][1] # 다음 회의의 종료 시간
        if st_time < last_time: # 안 겹치면 : 다음 회의 종료시간이 이전 회의의 시작시간 보다 작아야 함.
            last_time = arr[i][0] # 이때 다음 스텝으로 주기 위해 last_time을 시작 시간으로 줌
            cnt += 1
    return cnt

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    print(solution(n,sorted(arr,key = lambda x : (x[1],x[0]), reverse=True)))
