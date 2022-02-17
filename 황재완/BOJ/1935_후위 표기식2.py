# I/O template
import sys

file_path = r'input.txt'
sys.stdin = open(file_path, 'r')
# input = sys.stdin.readline # 대량의 라인 단위 입력이 필요할 때 사용 input().rstrip()과 함께 쓴다.

# Solve here
N = int(input())
postfix = list(input())
operands = [input() for _ in range(N)]
stack = []
for char in postfix:
    if char.isalpha():
        stack.append(operands[ord(char) - 65])
    else:
        op2 = stack.pop()
        op1 = stack.pop()
        stack.append(str(eval(op1 + char + op2)))
res = float(stack.pop())
print(f'{res:0.2f}')
