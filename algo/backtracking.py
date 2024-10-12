# 17136
import sys

input = sys.stdin.readline
graph = [list(map(int, input().split())) for _ in range(10)]
paper = [0, 5, 5, 5, 5, 5]
answer = 30
# 현 좌표에서 사용할 수 있는 색종이가 무엇인지 판별
def check(x, y):
    number = []
    # 1~ 5까지 검사하는데
    # 원하는 것은 1, 2,3,4... 어디까지 할당할 수 있냐임.
    # 근데 5부터 돌면 왜 안되냐고?
    # 포함되는 것들 append할건데 i,j를 다 돌면서 가능한지를 check 하는 것이기 때문
    # 다 돌아야 하니까 -> all이면 True (가능함), 아니면 (불가능함)을 반환해야 하는 taks
    # 진행은 되는데 -> 1,2,3 에서 가는 거랑 5,4,3 에서 가는 거랑 비교하면 결국 return을 바로 못함.
    # 종료를 못한다고 보면 됨.
    # 그래서 flag를 줘야지
    for n in range(6, 1):
        for i in range(x, x + n):
            for j in range(y, y + n):
                # 0이 발견되면 그 뒤에 색종이도 못쓴다.
                if i < 0 or i >= 10 or j < 0 or j >= 10 or graph[i][j] == 0:
                    return number
        number.append(n)
    return number


# 그래프 색칠하기.
# 좌표, 윈도우 크기, 어떤 값으로 색칠할지
def colored(x, y, n, value):
    for i in range(x, x + n):
        for j in range(y, y + n):
            graph[i][j] = value


# 백트래킹 탐색
def dfs(blank):
    global answer
    # 빈공간이 없으면
    if blank == 0:
        answer = min(answer, 25 - sum(paper[1:]))
        return
    for i in range(10):
        for j in range(10):
            if graph[i][j] == 1:
                # 붙일 수 있는 모든 색종이의 크기
                number = check(i, j)
                for num in number[::-1]:
                    # 색종이가 있으면 붙이고 재귀
                    if paper[num] > 0:
                        paper[num] -= 1
                        colored(i, j, num, 0)
                        dfs(blank - (num ** 2))
                        paper[num] += 1
                        colored(i, j, num, 1)
                return # 그냥 시간복잡도 차이일듯한데
def dfs(blank):
    global answer
    if blank == 0:
        answer = min(answer, 25 - sum(paper[1:]))
        return 
    for i in range(10):
        for j in range(10):
            if graph[i][j] == 1:
                number = check(i,j) # i,j에서 가능한 block을 최대 크기 순서로 반환함.add()
                for num in number:
                    if paper[ ]

temp = 0  # 공간 세기
for i in range(10):
    for j in range(10):
        if graph[i][j] == 1:
            temp += 1
dfs(temp)
print(answer) if answer != 30 else print(-1)
            

current = [0,5,5,5,5,5]

def check(x,y):
    numbers = []
    for n in range(5,0,-1): # 최대 5번
        for i in range(x, x + n):
            for j in range(y,y + n):
                if i <0 or i >= 10 or j<0 or j>= 10 or graph[i][j] == 0:
                    return numbers
        numbers.append(n)

def assign(i,j,num,val):
    for x in range(i,i + num):
        for y in range(j,j + num):
            graph[x][y] = val

def dfs(blank):
    global answer
    if blank == 0 :
        answer = min(answer, 25- sum(paper[1:]))
        return 
    
    for i in range(10):
        for j in range(10):
            if graph[i][j] == 1:
                # 탐색 시작
                numbers = check(i,j)
                for num in numbers[::-1]:
                    # assgin
                    colored(i,j,num,0)
                    paper[num] -=1
                    dfs(blank - num**2)
                    # revoke
                    paper[num] +=1
                    colored(i,j,num,1)
                return 
