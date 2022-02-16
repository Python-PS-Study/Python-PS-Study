import sys

file_path = (
    r'test_input.txt'
)
sys.stdin = open(file_path, 'r')

arr = input()
stack = []
valid = True
for i in arr:  # 유효성 검사
    if i in ['(', '[']:
        stack.append(i)
    else:
        if not stack:
            valid = False
            break
        if i == ']':
            if stack.pop() != '[':
                valid = False
                break
        elif i == ')':
            if stack.pop() != '(':
                valid = False
                break
if not valid or stack:
    print(0)
else:
    for i in arr:
        answer = 0
        if i in ['(', '[']:
            stack.append(i)
        else:
            if i == ']':
                if stack[-1] == '[':
                    stack.pop()
                    stack.append(3)
                else:
                    while stack[-1] != '[':
                        answer += int(stack.pop())
                    stack.pop()
                    stack.append(answer * 3)
            elif i == ')':
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(2)
                else:
                    while stack[-1] != '(':
                        answer += int(stack.pop())
                    stack.pop()
                    stack.append(answer * 2)
    print(sum(stack))
