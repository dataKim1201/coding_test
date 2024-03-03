N = int(input()) #전체 사람 수
people = [] #사람 정보를 받을 list

for _ in range(N): #입력한 순서대로 정보를 입력받는다.
    x, y = map(int, input().split())
    people.append((x,y))

for i in people:
    rank = 1 #초기값은 전부 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]: #조건
            rank+=1 #조건 만족 시 count up
    print(rank, end = " ") #바로 출력
# import sys
# input = sys.stdin.readline
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
# s_arr = sorted(arr, key = lambda x : (x[0],x[1]),reverse = True)

# cnt = 1
# res = [1]
# # print(s_arr)
# for i in range(1,len(arr)):
#     if s_arr[i-1][0] > s_arr[i][0] and s_arr[i-1][1] > s_arr[i][1]:
#         cnt = res.count(cnt) +cnt
#         res.append(cnt)
#     else:
#         res.append(cnt)
# final = []
# for item in arr:
#     final.append(res[s_arr.index(item)])
# print(' '.join(map(str,final)))

# # 정렬하고 
# # 순서대로 번호를 부여하는데 
# # 해당 순서랑 겹치면 같은 번호 
