import sys
input = sys.stdin.readline
# 퇴사하는 날짜가 입력으로 주어지고
# 퇴사하기 전 부터 근무 일수와 그 수당이 주어짐
# 남은 기간동안 이를 최대화 할 수 있는 과정과 그 결과를 구함.
D = int(input())

# 0은 근무일 수 1은 그 때의 보상
work_price = [list(map(int,input().split())) for _ in range(D)]
max_result = 0
def dfs(now,price):
    global max_result
    if now >= D:
        max_result = max(max_result, price)
        return
    if now + work_price[now][0] <=  D:
        dfs(now + work_price[now][0], price + work_price[now][1])
    dfs(now + 1, price)
dfs(0,0)
print(max_result)
#  	    1일	2일	3일	4일	5일	6일	7일
# Ti	3	5	1	1	2	4	2
# Pi	10	20	10	20	15	40	200
#  	    1일	2일	3일	4일	5일	6일	7일
# Ti	3	5	1	1	2	4	2
# Pi	10	20	10	20	15	40	200
# DP    10  20  20  30  45  45  45

# DP[1일] = max(DP[1일])