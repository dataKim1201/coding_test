import sys
from collections import Counter
input = sys.stdin.readline

query = input().strip()
bomb = input().strip()
stack = []
for i in range(len(query)):
    stack.append(query[i])
    if stack[-1] == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        for j in range(len(bomb)):
            stack.pop()
if stack:
    print(stack)
else:
    print('FRULA')