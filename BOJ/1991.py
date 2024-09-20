# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
import sys
input = sys.stdin.readline
n = int(input())
node = {}
for _ in range(n):
    root, left, right = input().split()
    node[root] = [left,right]

prime = ''
def prime_search(tree,root):
    global prime
    if root != '.':
        prime += root
    if tree[root][0] != '.': # left
        prime_search(tree,tree[root][0])
    if tree[root][1] != '.':
        prime_search(tree,tree[root][1])
    return
middle = ''
def middle_search(tree,root):
    global middle
    if tree[root][0] != '.': # left
        middle_search(tree,tree[root][0])
    if root != '.':
        print(root)
        middle += root
    if tree[root][1] != '.':
        middle_search(tree,tree[root][1])
    return

post = ''
def post_search(tree,root):
    global post
    if tree[root][0] != '.': # left
        post_search(tree,tree[root][0])
    if tree[root][1] != '.':
        post_search(tree,tree[root][1])
    if root != '.':
        post += root
    return

prime_search(node, 'A')
middle_search(node, 'A')
post_search(node, 'A')
print(prime)
print(middle)
print(post)