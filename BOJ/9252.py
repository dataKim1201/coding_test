import sys
read = sys.stdin.readline

word1, word2 = read().strip(), read().strip()
l1, l2 = len(word1) + 1, len(word2) + 1
# cache = [[0] * l2 for _ in range(l1)]
cache = [[''] * l2 for _ in range(l1)]

for i in range(1,l1):
    for j in range(1, l2):
        if word1[i-1] == word2[j-1]:
            cache[i][j] = cache[i-1][j-1] + word1[i-1]
        else:
            # cache[i][j] = max(cache[i][j-1], cache[i-1][j])
            if len(cache[i][j-1]) <= len(cache[i-1][j]):
                cache[i][j] = cache[i-1][j]
            else:
                cache[i][j] = cache[i][j-1]

print(len(cache[-1][-1]))
print(cache[-1][-1])

# 2개의 배열을 반복하면서
# 그 위치에 단어가 같은 경우
    # 겹치는 수를 증가한다. 
    # 겹칠때 -> 증가하는 수는 무엇이 될까?
    # 겹치는 수가 등장하기 바로 이전!! -> i-1, j-1 이 떄의 결과값에 1을 더 해야함!!
# 위치에 단어가 다른 경우 
    # 두배열의 이전 값을 비교하면서 겹치는 것이 있는지 검사한다. 

# 2개의 배열을 반복하면서
# 중복되는 정답
    # 현위치를 기준으로 만들 수 있는 부분 수열 중 정답이 되는 부분 수열의 단어 수 = 이전 배열까지 많들 수 있는 배열에서 겹치는 단어의 수
# 그 위

# ACAYKP
# CAPCAK

#      A C A Y K P
#    0 0 0 0 0 0 0
#  C 0 0 1 1 1 1 1
#  A 0 1 1 2 2 2 2
#  P 0 1 1 2 2 2 3
#  C 0 1 2 2 2 2 3
#  A 0 1 2 3 3 3 3
#  K 0 1 2 3 3 4 4

# 2,1 -> 'C'
# 1,1 -> 'A'
# 2,2 -> 'CA'
# 3,6 -> 'CAP'
# 4,2 -> 'CA'
# 5,1 -> 'A'
# 5,3 -> 'ACA'
# 6,5 -> 'ACAK'