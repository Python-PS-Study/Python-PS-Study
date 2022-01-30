import sys

file_path = (
    r'test_input.txt'
)
sys.stdin = open(file_path, 'r')

a, b, c, d, e, f = map(int, input().split())

y = int((a * f - d * c) / (a * e - b * d))
x = int((f - e * y) / d)

print(x, y)
