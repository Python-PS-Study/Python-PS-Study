import sys

file_path = (
    r'test_input.txt'
)
sys.stdin = open(file_path, 'r')

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []


def nm():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(n):
        if arr[i] in s: continue
        s.append(arr[i])
        nm()
        s.pop()


nm()
