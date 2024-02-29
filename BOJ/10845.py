from collections import deque
import sys
input = sys.stdin.readline
class Queue:
    def __init__(self):
        self.queue = deque()
    def PUSH(self,x):
        self.queue.append(x)
    def POP(self):
        if len(self.queue) == 0:
            return -1
        res = self.queue.popleft()
        return res
    def is_empty(self):
        if len(self.queue) == 0:
            return 1
        return 0
    def front(self):
        if len(self.queue) == 0:
            return -1
        return self.queue[0]
    def back(self):
        if len(self.queue) == 0:
            return -1
        return self.queue[-1]
    def size(self):
        return len(self.queue)
    

if __name__ == '__main__':
    queue = Queue()
    T = int(input())
    for _ in range(T):
        res = input().split()
        if len(res) == 2:
            queue.PUSH(res[1])
        elif res[0] == 'front':
            print(queue.front())
        elif res[0] == 'back':
            print(queue.back())
        elif res[0] == 'empty':
            print(queue.is_empty())
        elif res[0] == 'pop':
            print(queue.POP())
        elif res[0] == 'size':
            print(queue.size())