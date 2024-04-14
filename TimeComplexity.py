import time
def time_calc(func, args= None):
    start = time.time()
    func()
    end = time.time()
    return  f'{round(end - start,4)}, second'

def func():
    a = 1
    cmd = 90**7
    for _ in range(cmd):
        if a >0:
            a += 1
    return a

print(time_calc(func))