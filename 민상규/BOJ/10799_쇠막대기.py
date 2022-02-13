import sys

file_path = (
    r'test_input.txt'
)
sys.stdin = open(file_path, 'r')

s = input()
cnt = 0
answer = 0
for i in s:
    if i == '(':
        cnt += 1
    else:
        cnt -= 1
        answer += cnt

print(answer)
