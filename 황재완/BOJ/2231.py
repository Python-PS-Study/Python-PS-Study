# I/O template
import sys

file_path = (
        r'C:/Users/user/PycharmProjects/PS/' +
        r'input.txt'
)
sys.stdin = open(file_path, 'r')

# Solve here
n = int(input())
for i in range(1, n + 1):
    if i + sum(map(int, str(i))) == n:
        print(i)
        break
else:
    print(0)

