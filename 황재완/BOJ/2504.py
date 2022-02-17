# I/O template
import sys

file_path = r'input.txt'
sys.stdin = open(file_path, 'r')
# input = sys.stdin.readline # 대량의 라인 단위 입력이 필요할 때 사용 input().rstrip()과 함께 쓴다.

# Solve here
def is_valid(PS):
    stack = []
    for parenthesis in PS:
        if parenthesis == '(' or parenthesis == '[':
            stack.append(parenthesis)
        elif parenthesis == ')':
            if not stack or stack[-1] != '(':
                return False
            else: stack.pop()
        elif parenthesis == ']':
            if not stack or stack[-1] != '[':
                return False
            else: stack.pop()
    return True if not stack else False

def evaluate_PS(PS):
    if not is_valid(PS):
        return 0
    stack = []
    for parenthesis in PS:
        if parenthesis == '(' or parenthesis == '[':
            stack.append(parenthesis)
        elif parenthesis == ')':
            if stack[-1] == '(':
                stack.pop()
                stack.append(2)
            else:
                value = 0
                while stack[-1] != '(':
                    value += stack.pop()
                stack.pop()
                value *= 2
                stack.append(value)
        elif parenthesis == ']':
            if stack[-1] == '[':
                stack.pop()
                stack.append(3)
            else:
                value = 0
                while stack[-1] != '[':
                    value += stack.pop()
                stack.pop()
                value *= 3
                stack.append(value)
    return sum(stack)
PS = list(input())

# 올바르지 않은 괄호열: 스택에 남아 있거나 짝이 스택에 없을 경우이다.
print(evaluate_PS(PS))