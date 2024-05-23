import sys
input = sys.stdin.readline

string = input().strip()

bf = string[0]
one,zero =0,0
if bf == '1':
    one += 1
else:
    zero += 1
for i in string:
    if bf == '1' and i == '0':
        bf = '0'
        zero += 1
    elif bf == '0' and i == '1':
        bf = '1'
        one += 1
print(min(zero,one))
