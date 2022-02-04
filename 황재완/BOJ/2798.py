
# I/O template
import sys
file_path = (
    r'C:/Users/user/PycharmProjects/PS/' +
    r'input.txt'
)
sys.stdin = open(file_path, 'r')

# Solve here
from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
max_tot = 0

max_tot = max(filter(lambda x: x <= m, map(sum, combinations(cards, r=3))))


# for i in range(n - 2):
#     for j in range(i + 1, n - 1):
#         for k in range(j + 1, n):
#             if max_tot < cards[i] + cards[j] + cards[k] <= m:
#                 max_tot = cards[i] + cards[j] + cards[k]

print(max_tot)
