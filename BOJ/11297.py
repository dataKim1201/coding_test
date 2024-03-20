import sys
input = sys.stdin.readline

class MaxHeap():
    def __init__(self) -> None:
        self.arr = [0]
    def insert(self,num):
        # UPHeap을 진행
        self.arr.append(num)
        idx = len(self.arr)-1
        while idx >1 and self.arr[idx] > self.arr[idx//2]: # 부모가 항상 커야 함
            self.arr[idx] , self.arr[idx//2] = self.arr[idx//2] , self.arr[idx]
            idx //= 2
    def delete(self):
        if len(self.arr) == 1: return 0
        idx = 1
        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        root = self.arr.pop()
        size= len(self.arr)
        while idx < size:
            if 2* idx < size and 2*idx + 1 < size:
                if self.arr[2*idx] >= self.arr[2*idx + 1]: # 우선 순위가 왼쪽이 더 높다면
                    target = 2*idx
                else:
                    target = 2*idx + 1
            elif 2*idx < size: #right는 볼 수 없다면
                target = 2*idx
            else: break
            if idx != target and self.arr[idx] < self.arr[target]: # 부모가 자식보다 작다면 바꿔야지
                self.arr[idx] , self.arr[target] = self.arr[target] , self.arr[idx]
                idx = target
            else: break
        return root
heap = MaxHeap()

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
