# I/O template
import sys

file_path = r'input.txt'
sys.stdin = open(file_path, 'r')
# input = sys.stdin.readline # 대량의 라인 단위 입력이 필요할 때 사용 input().rstrip()과 함께 쓴다.

# Solve here
PS = input()
stack = []
is_last_right = False  # 전 괄호가 오른쪽 괄호인지 확인하는 플래그
total_cnt = 0
for parenthesis in PS:
    if parenthesis == '(':
        stack.append(parenthesis)
        is_last_right = False
    elif parenthesis == ')':
        stack.pop()
        if is_last_right:
            total_cnt += 1
        else:
            total_cnt += len(stack)
        is_last_right = True
print(total_cnt)
