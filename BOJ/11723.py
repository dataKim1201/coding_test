# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = set()
# for _ in range(n):
#     command = input().strip()
#     if command.startswith('add'):
#         arr.add(int(command.split(' ')[-1]))
#     elif command.startswith('remove'):
#         arr.remove(int(command.split(' ')[-1]))
#     elif command.startswith('check'):
#         if int(command.split(' ')[-1]) in arr:
#             print(1)
#         else:
#             print(0)
#     elif command.startswith('toggle'):
#         if int(command.split(' ')[-1]) in arr:
#             arr.remove(int(command.split(' ')[-1]))
#         else:
#             arr.add(int(command.split(' ')[-1]))
#     elif command == 'all':
#         arr = set([i for i in range(1,21)])
#     elif command == 'empty':
#         arr = set()


import sys
input = sys.stdin.readline
 

result = set()
for _ in range(int(input())):
    quest = input().strip().split()

    if len(quest) == 1:
        if quest[0] == 'empty':
            result = set()
        else:
            result = set(i for i in range(1, 21))
    else:
        que,val = quest
        val = int(val)
        if que == 'add':
            result.add(val)
        elif que == 'check':
            print(1 if int(quest[1]) in result else 0)
        elif que == 'remove':
            result.discard(val)
        else:
            if val in result:
                result.discard(val)
            else:
                result.add(val)
