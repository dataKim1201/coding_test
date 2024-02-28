from collections import deque
import sys
input = sys.stdin.readline
class Stack:
    def __init__(self):
        self.stack = deque([])
    def PUSH(self,x):
        self.stack.append(x)
    def POP(self):
        if len(self.stack) == 0:
            return -1
        res = self.stack.pop(-1)
        return res
    def is_empty(self):
        if len(self.stack) == 0:
            return 1
        return 0
    def TOP(self):
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    

if __name__ == '__main__':
    stack = Stack()
    T = int(input())
    for _ in range(T):
        res = input().split()
        if len(res) == 2:
            stack.PUSH(int(res[1]))
        elif res[0] == 'top':
            print(stack.TOP())
        elif res[0] == 'empty':
            print(stack.is_empty())
        elif res[0] == 'pop':
            print(stack.POP())
        elif res[0] == 'size':
            print(stack.size())