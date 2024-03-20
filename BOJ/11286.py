import sys
input = sys.stdin.readline

class AbsHeap():
    def __init__(self) -> None:
        self.arr = [0]
    
    def insert(self,num):
        self.arr.append(num)
        idx = len(self.arr) -1 
        while idx > 1: # 절대값이 작다면 
            if abs(self.arr[idx]) == abs(self.arr[idx//2]) and self.arr[idx] < self.arr[idx//2]:
                self.arr[idx], self.arr[idx//2] = self.arr[idx//2] , self.arr[idx]
                idx //= 2
            elif abs(self.arr[idx]) < abs(self.arr[idx//2]):
                self.arr[idx], self.arr[idx//2] = self.arr[idx//2] , self.arr[idx]
                idx //= 2
            else: break
    def delete(self):
        if len(self.arr) == 1: return 0
        idx = 1
        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        root = self.arr.pop()
        size= len(self.arr)
        while idx < size:
            if 2*idx < size and 2*idx + 1 < size:
                if abs(self.arr[2*idx]) < abs(self.arr[2*idx +1]): # 음수 상관없이 작은게 우선 순위가 높음
                    target = 2*idx
                elif abs(self.arr[2*idx]) == abs(self.arr[2*idx +1]) and self.arr[2*idx] < self.arr[2*idx +1]: # 음수 상관없이 작은게 우선 순위가 높음
                    target = 2*idx
                else : 
                    target = 2*idx +1
            elif 2*idx < size:
                target = 2*idx
            else: break

            if target != idx :
                if abs(self.arr[idx]) >  abs(self.arr[target]):
                    self.arr[idx], self.arr[target] = self.arr[target], self.arr[idx]
                    idx = target
                elif abs(self.arr[idx]) ==  abs(self.arr[target]) and self.arr[idx] > self.arr[target]: # 부모가 더 크다면 바꿔야지
                    self.arr[idx], self.arr[target] = self.arr[target], self.arr[idx]
                    idx = target
                else: break
            else: break
        return root


n = int(input())
arr = AbsHeap()
result = []
for _ in range(n):
    cmd = int(input())
    if cmd == 0:
        res = arr.delete()
        result.append(res)
    else:
        arr.insert(cmd)

print('\n'.join(map(str,result)))