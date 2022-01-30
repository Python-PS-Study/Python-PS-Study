import sys

file_path = (
    r'test_input.txt'
)
sys.stdin = open(file_path, 'r')

from collections import Counter

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
arr = [list(x) for x in zip(*arr)]

dna = ''
hd = 0

for i in arr:
    counter = Counter(i)
    counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    dna += counter[0][0]
    hd += counter[0][1]

print(dna)
print(n * m - hd)
