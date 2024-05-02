import sys
input = sys.stdin.readline 
formula = input().strip()

stack = []
output = ''

for i in formula:
    if i.isalpha():
        output += i
    elif i == '(':
        stack.append(i)
    elif i in '*/':
        while stack and stack[-1] in '*/':
            output += stack.pop()
        stack.append(i)
    elif i in '+-)':
        while stack and stack[-1] != '(':
            output += stack.pop()
        if i != ')':
            stack.append(i)
        else:
            stack.pop()
while stack:
    output += stack.pop()
print(output)
            
# ()를 만났으면 그안에서 해결이 되어야 한다.
# 사칙연산을 만나면 우선순위에 맞게 이를 반영해준다. 
# 피연산자도 사칙연산의 우선순위에 맞게 반영되어야 한다.

# text = input()
# answer = ''
# stack = [] # 연산자 관리용 
# for t in text :
#     print(stack, t)
#     print(answer)
#     if t.isalpha() :
#         answer += t    
#     else :        
#         if t == '(' :
#             stack.append(t)        
#         elif t == '*' or t == '/' :            
#             while stack and (stack[-1] == '*' or stack[-1] == '/') :                
#                 answer += stack.pop()            
#             stack.append(t)        
#         elif t == '+' or t == '-' :            
#             while stack and stack[-1] != '(' :                
#                 answer += stack.pop()            
#             stack.append(t)        
#         elif t == ')' :            
#             while stack and stack[-1] != '(' :               
#                 answer += stack.pop()            
#             stack.pop() # '('를 빼는 작업 
# while stack :    
#     answer += stack.pop() 
# print(answer)

