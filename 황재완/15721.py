# I/O template
import sys

file_path = (
        r'C:/Users/user/PycharmProjects/PS/' +
        r'input.txt'
)
sys.stdin = open(file_path, 'r')

# Solve here

# from collections import deque
#
# A = int(input())
# T = int(input())
# target = int(input())
# table = deque([i for i in range(A)])
# target_cnt = 0
# round_cnt = 1
# not_found = True
# while not_found:
#     this_round = [0, 1, 0, 1] + [0 for _ in range(round_cnt + 1)] + [1 for _ in range(round_cnt + 1)]
#     for now in this_round:
#         now_player = table.popleft()
#         if now == target:
#             target_cnt += 1
#             if target_cnt == T:
#                 print(now_player)
#                 not_found = False
#                 break
#         table.append(now_player)
#     round_cnt += 1

A = int(input())
T = int(input())
target = int(input())
tot_cnt = 0
bbun_degi_cnt = [0, 0]
turn_cnt = 1
while True:
    for bbun_degi in [0, 1, 0, 1] + [0] * (turn_cnt + 1) + [1] * (turn_cnt + 1):
        bbun_degi_cnt[bbun_degi] += 1
        if bbun_degi_cnt[target] == T:
            print(tot_cnt % A)
            break
        tot_cnt += 1
    else:
        turn_cnt += 1
        continue
    break

