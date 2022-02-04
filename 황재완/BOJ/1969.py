# I/O template
import sys

file_path = (
        r'C:/Users/user/PycharmProjects/PS/' +
        r'input.txt'
)
sys.stdin = open(file_path, 'r')

# Solve here
# def DFS(L):
#     if L == M:
#         global min_dna, min_hd
#         tmp_dna = "".join(res)
#         hd = 0
#         for i in range(M):
#             for dna in dnas:
#                 if dna[i] != tmp_dna[i]: hd += 1
#         if hd < min_hd:
#             min_hd = hd
#             min_dna = tmp_dna
#
#     else:
#         for nucleotide in "ACGT":
#             res.append(nucleotide)
#             DFS(L + 1)
#             res.pop()
# N, M = map(int, input().split())
# dnas = [input() for _ in range(N)]
# res = []
# min_dna = ""
# min_hd = float('inf')
#
# DFS(0)
# print(min_dna)
# print(min_hd)
from collections import defaultdict
N, M = map(int, input().split())
dnas = [input() for _ in range(N)]
target_dna = ""
hd = 0
cnt = []
for i in range(M):
    temp_dict = defaultdict(int)
    for dna in dnas:
        temp_dict[dna[i]] += 1
    cnt.append(temp_dict)
for i in range(M):
    nucleotide, _ = min(list(cnt[i].items()), key=lambda x: (-x[1], x[0]))
    target_dna += nucleotide
    hd += N - cnt[i][nucleotide]
print(target_dna)
print(hd)
