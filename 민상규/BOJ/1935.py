import sys

file_path = (
    r'test_input.txt'
)
sys.stdin = open(file_path, 'r')


def culc(oper, op1, op2):
    if oper == '*':
        return op1 * op2
    elif oper == '+':
        return op1 + op2
    elif oper == '/':
        return op1 / op2
    elif oper == '-':
        return op1 - op2


n = int(input())
s = input()  # 후위 표기식
stack = []  # 스택
operator = ('*', '+', '/', '-')  # 연산자 set
num = [int(input()) for _ in range(n)]  # [A,B,C,D...]
for x in s:  # 식 탐색
    if x in operator:
        op2 = stack.pop()
        op1 = stack.pop()
        stack.append(culc(x, op1, op2))  # 계산 결과 stack에 push
    else:
        stack.append(num[ord(x) - 65])  # ord('A') = 65

print("{:.2f}".format(stack[0]))
