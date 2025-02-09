# 숫자 1은 2초가 걸린다.
import sys
input = sys.stdin.readline
# UNUCIC는 868242와 같다.
digit = input().strip()
def converter(d):
    return ord(d) - 65
answer = 0
for d in digit:
    if converter(d) > 21:
        answer += 10
    elif converter(d) > 18:
        answer += 9
    elif converter(d) > 14:
        answer += 8
    elif converter(d) > 11:
        answer += 7
    elif converter(d) > 8:
        answer += 6
    elif converter(d) > 5:
        answer += 5
    elif converter(d) > 2:
        answer += 4
    else:
        answer += 3
print(answer)
# 2: ABC 012
# 3: DEF 345
# 4: GHI 678
# 5: JKL 9 10 11
# 6: MNO 12 13 14
# 7: PQRS 15 16 17 18
# 8: TUV 19 20 21
# 9: WXYZ 22 23 24 25
