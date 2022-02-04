import sys

file_path = (
    r'test_input.txt'
)
sys.stdin = open(file_path, 'r')

n = int(input())
answer = 0
for i in range(1, n + 1):
    num = i + sum(list(map(int, str(i))))
    if num == n:
        answer = i
        break
print(answer)
