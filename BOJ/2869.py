import sys 
input = sys.stdin.readline
a,b,v = map(int,input().split())

print((v-b-1) // (a-b) + 1)


# V 몫으로 계산을 해야한다.
# A 로 몫을 계산한 이후
# B로 떨어지는 걸 생각해야함.
# B가 A보다 큰 경우의 수는 제외
# 결국에는 올라갔다가 내려오는 걸 생각하는데 마지막에 나머지가 A로 올라갈 수만 있다면  + 1해서 마무리 하면 안됨?
# V의 나머지가 A보다 크지 않다면

# 5 1 6
# 2 -1*5 = -3

# 3 // 3+1