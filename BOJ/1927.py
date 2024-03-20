import sys
class Heap:
    def __init__(self) -> None:
        self.arr = [0]
    def insert(self,num):
        # upheap
        self.arr.append(num)
        idx = len(self.arr)-1
        while idx >1 and self.arr[idx] < self.arr[idx//2]: # parent 보다 자식이 더 크다면
            self.arr[idx], self.arr[idx//2] = self.arr[idx//2], self.arr[idx]
            idx //=2
    
    def delete(self):
        if len(self.arr) == 1: return 0
        # root 랑 바꿔 주고
        self.arr[-1], self.arr[1] = self.arr[1], self.arr[-1]
        root = self.arr.pop() # root 를 가져온다.
        # 처음 부터 Down heap을 진행
        idx = 1
        size = len(self.arr)
        while True:
            if idx *2 < size and idx *2 +1 < size: # Left, right 모두 비교 가능하다면
                if self.arr[idx*2] <= self.arr[idx*2 + 1]: # 우선 순위가 L인 경우
                    target = idx*2
                else:
                    target = idx*2 + 1
            elif idx * 2 < size: # idx*2까지만 비교할 수 있다면
                target = idx*2
            else: # out of idx
                break
            if target != idx:
                if self.arr[idx] > self.arr[target]: # 즉 부모가  자식 보다 더 크다면
                    self.arr[idx], self.arr[target] = self.arr[target], self.arr[idx]
                    idx = target
                else:
                    break
            else:
                break
        return root
input = sys.stdin.readline
heap = Heap()

n = int(input())
result = []
for _ in range(n):
    cmd = int(input())
    if cmd == 0:
        res = heap.delete()
        result.append(res)
    else:
        heap.insert(cmd)
    
print('\n'.join(map(str,result)))
