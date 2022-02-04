import sys
from itertools import combinations

file_path = (
    r'test_input.txt'
)
sys.stdin = open(file_path, 'r')

n, m = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0

for com in combinations(cards, 3):
    s = sum(com)
    if s <= m:
        answer = max(answer, s)

print(answer)
