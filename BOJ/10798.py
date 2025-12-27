# # 가로 읽기를 세로로 읽기
# import sys
# input = sys.stdin.readline
# arr = [input().strip() for _ in range(5)]
# max_length = max([len(item) for item in arr])

# output =''
# for i in range(max_length):
#     for j in range(5):
#         if len(arr[j])-1  >= i:
#             output += arr[j][i]

# print(output)

def custom_zip(*iterables, fillvalue=''):
    if not iterables:
        return

    max_length = max(len(it) for it in iterables)

    for i in range(max_length):
        yield list(
            it[i] if i < len(it) else fillvalue
            for it in iterables
        )

import sys
input = sys.stdin.readline
arr = [input().strip() for _ in range(5)]
print(''.join([ ''.join(item) for item in custom_zip(*arr)]))


