import sys
input = sys.stdin.readline
for idx in range(3):
    item = input().strip()
    try:
        int(item)
        target = int(item) + (3-idx)
        break
    except:
        continue
result = ''
if target % 3 == 0 or target % 5== 0:
    if target % 3 == 0:
        result = 'Fizz'
    if target % 5 == 0:
        result += 'Buzz'
else:
    result = target
print(result)
    
