import sys

def append(value, bst):
    if len(bst) == 0:
        bst.extend([value, [], []])
        return
    if value < bst[0]:
        append(value, bst[1])
    elif value > bst[0]:
        append(value, bst[2])

def print_post_order(bst):
    if len(bst) == 0:
        return
    print_post_order(bst[1])
    print_post_order(bst[2])
    print(bst[0])

sys.setrecursionlimit(20_000)
graph = []
for num in sys.stdin:
    append(int(num), graph)
print_post_order(graph)