from collections import deque
import sys
input = sys.stdin.readline
class Deque:
    def __init__(self):
        self.dequeue = deque()
    def PUSH(self,x):
        self.dequeue.append(x)
    def push_front(self,x):
        self.dequeue.appendleft(x)
    def POP(self):
        if len(self.dequeue) == 0:
            return -1
        res = self.dequeue.popleft()
        return res
    def pop_back(self):
        if len(self.dequeue) == 0:
            return -1
        res = self.dequeue.pop()
        return res
    def is_empty(self):
        if len(self.dequeue) == 0:
            return 1
        return 0
    def front(self):
        if len(self.dequeue) == 0:
            return -1
        return self.dequeue[0]
    def back(self):
        if len(self.dequeue) == 0:
            return -1
        return self.dequeue[-1]
    def size(self):
        return len(self.dequeue)
    

if __name__ == '__main__':
    dequeue = Deque()
    T = int(input())
    for _ in range(T):
        res = input().split()
        if len(res) == 2:
            if res[0] == 'push_back':
                dequeue.PUSH(res[1])
            else:
                dequeue.push_front(res[1])
        elif res[0] == 'front':
            print(dequeue.front())
        elif res[0] == 'back':
            print(dequeue.back())
        elif res[0] == 'empty':
            print(dequeue.is_empty())
        elif res[0] == 'pop_front':
            print(dequeue.POP())
        elif res[0] == 'pop_back':
            print(dequeue.pop_back())
        elif res[0] == 'size':
            print(dequeue.size())