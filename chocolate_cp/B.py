import sys
sys.set_int_max_str_digits(10000) 
input = sys.stdin.readline
T = int(input())

def get_result(n):
    if n==1: return 0
    if n %2 == 0:
        zero_num = n-2
        res = '1' + '0'* zero_num+ '1' if zero_num >=1 else '11'
    else:
        t = (n-3)//2 + 1
        tt = 2
        if t % 2 == 0:
            tt = 9
        zero_num = n -3
        res = '1' + '0'* (zero_num//2) + str(tt) + '0'* (zero_num//2) + '1' if zero_num >=1 else f'1{tt}1'
    return res

def check_pal(item):
    while len(item) > 1:
        if item[0] == item[-1]:
            item = item[1:-1]
        else:
            return False
    return True

print(get_result(5))
exit()
for n in range(T):
    # n = int(input())
    # target = get_result(n)
    # if int(target) % 11 == 0:
    #     continue
    # print(n)

    if n % 2==1:
        n = n-1
        flag = True
    zero_num = n-2
    res = '1' + '0'* zero_num+ '1' if zero_num >=1 else '11'
    
    end = ''.join(['9' for _ in range(n)])
    if flag:
        start = str(start) + '0'
        end = str(end) + '0'
    for item in range(int(start), int(end)+ 11, 11):
        if check_pal(str(item)):
            print(item)
            res = True
            break
    if not res:
        print(-1)



