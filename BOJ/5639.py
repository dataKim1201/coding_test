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
pre_tree = []
while True:
    cmd = input()
    if not cmd:
        break
    pre_tree.append(int(cmd))

parrent = []
for idx, item in enumerate(pre_tree):
    if idx == 0:
        parrent.append(item)
    elif idx % 2 == 0:
        # 부모노드를 꺼내서
        # 그냥 
        

def change_search(tree):
    result = ''
    print(result)
    return None

a= [50, 
        30, 
            24, 
                5, 28, 
            45, 
        98, 
            52,
                60]