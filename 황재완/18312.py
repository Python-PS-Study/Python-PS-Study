# I/O template
import sys

file_path = (
        r'C:/Users/user/PycharmProjects/PS/' +
        r'input.txt'
)
sys.stdin = open(file_path, 'r')

# Solve here
n, k = map(int, input().split())
cnt = 0
for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if str(k) in list(f'{h:0>2}' + f'{m:0>2}' + f'{s:0>2}'):
                cnt += 1
print(cnt)
