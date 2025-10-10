import sys

def append(value, bst):
    if len(bst) == 0:
        bst.extend([value, [],[]])
        return 
    if value < bst[0]: # root node보다 크다면
        append(value, bst[1]) # 재귀적으로 다음 함수를 호출함
    if value > bst[0]: # 이게 더 크다면
        append(value, bst[2])

def print_post_order(bst):
    if len(bst) == 0:
        return 
    print_post_order(bst[1])
    print_post_order(bst[2])
    print(bst[0])

graph = []
sys.setrecursionlimit(20_000)
for num in sys.stdin:
    append(int(num), graph)
print_post_order(graph)