import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n-1)]
tree = []
result = {key: 0 for key in range(1,n + 1)}
# def get_parent(root):
#     global tree
for root in range(1,n + 1):
    # if root in tree:
    #     continue
    for item in arr:
        if root in item:
            idx = 1 if item.index(root) == 0 else 0
            tmp = item[idx]
            # if tmp in tree:
            #     continue
            if result[tmp] == 0:
                result[tmp] = root
            tree.append(root)
#             get_parent(tmp)
# get_parent(1)
print(tree)
for i in range(2,n + 1):
    print(result[i])