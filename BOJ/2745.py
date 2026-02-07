'''
BOJ.2745의 Docstring
B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.

10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

입력
첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)

B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.

출력
첫째 줄에 B진법 수 N을 10진법으로 출력한다.

1. A,Z의 진법 숫자를 구한다. 
2. 숫자에 매핑된 숫자를 부여한다. A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
3진법 예시
122
3 ** 0 + 2 = 2
3 ** 1 * 2 = 6
3 ** 2 * 1 = 9 ==> 17
2진법 예시
110
2 ** 0  + 0 = 0
2 ** 1 * 1 = 2
2 ** 2  * 1 = 4  --- 6
'''
import sys
input = sys.stdin.readline
N, B = input().split()
B = int(B)
answer = 0
alpha_map = {chr(item) : item-55 for item in range(65,91)}
for idx, i in enumerate(list(str(N))[::-1]):
    digit = alpha_map[i] if i in alpha_map else int(i)
    answer += (B ** idx) * digit
print(answer)

