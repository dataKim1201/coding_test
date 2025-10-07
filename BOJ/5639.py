'''
이진 검색 트리는 다음과 같은 세 가지 조건을 만족하는 이진 트리이다.

노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
왼쪽, 오른쪽 서브트리도 이진 검색 트리이다.

전위 순회 (루트-왼쪽-오른쪽)은 루트를 방문하고, 
왼쪽 서브트리, 
오른쪽 서브 트리를 순서대로 방문하면서 노드의 키를 출력한다. 

후위 순회 (왼쪽-오른쪽-루트)는 왼쪽 서브트리, 오른쪽 서브트리, 루트 노드 순서대로 키를 출력한다. 

예를 들어, 
위의 이진 검색 트리의 
전위 순회 결과는 50 30 24 5 28 45 98 52 60 이고, 

후위 순회 결과는 5 28 24 45 30 60 52 98 50 이다.

이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

# 전위 탐색 로직
    # 루트
    # 좌노드
    # 우노드
class Node:
    def __init__(self,x, left = None,right= None):
        self.root = x
        self.left = left
        self.right = right

def pre_traveler(node):
    print(node.root)
    if node.left is not None:
        pre_traveler(node.left)
    if node.right is not None:
        pre_traveler(node.right)

def post_traveler(node,cnt=0):
    if node.left is not None:
        post_traveler(node.left, cnt +1)
    if node.right is not None:
        post_traveler(node.right,cnt +1)
    print(node.root)

def get_tree(arr,res = []):
    for node in arr:
        res.append(node)
    return None

if __name__ == "__main__":
    Tree = Node(
        50,
        Node(
            30,
            Node(
                24,
                Node(5),
                Node(28)
            ),
            Node(45)
        ),
        Node(
            98,
            Node(
                52,
                None,
                Node(60)
            ),
        )
    )
    post_traveler(Tree)
# 후위 탐색 로직