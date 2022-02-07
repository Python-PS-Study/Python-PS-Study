import sys

file_path = (
    r'test_input.txt'
)
sys.stdin = open(file_path, 'r')

n, m = map(int, input().split())
s = []


def nm(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, n + 1):
        s.append(i)
        nm(i)
        s.pop()


nm(1)
