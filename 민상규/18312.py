import sys

file_path = (
    r'test_input.txt'
)
sys.stdin = open(file_path, 'r')

n, k = input().split()
count = 0
for h in range(int(n) + 1):
    if h < 10:  # 1시 -> 01시
        h = ['0', str(h)]
    else:
        h = list(str(h))
    if k in h:
        count += 3600
    else:
        if int(k) < 6:
            count += 1575
        else:
            count += 684
print(count)
