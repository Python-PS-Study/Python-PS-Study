import sys

file_path = (
    r'test_input.txt'
)
sys.stdin = open(file_path, 'r')

# 뻔 = 0 / 데기 = 1
bdg = [0, 1, 0, 1]
arr = []
for n in range(2, 139):
    arr += bdg + [0] * n + [1] * n
    # if len(arr) >= 20000:
    #     print(n)
    #     break
    # T <=10000
    # if arr >= 20000
    # -> n = 129
a = int(input())
t = int(input())
target = int(input())
# i = -1
# for n in arr:
#     i += 1
#     if i == a:
#         i = 0
#     if n == target:
#         t -= 1
#     if t == 0:
#         print(i)
#         break

for i, n in enumerate(arr):
    if n == target:
        t -= 1
    if t == 0:
        print(i % a)
        break
