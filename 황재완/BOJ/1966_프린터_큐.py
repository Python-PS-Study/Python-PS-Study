# I/O template
import sys

file_path = r'input.txt'
sys.stdin = open(file_path, 'r')
# input = sys.stdin.readline # 대량의 라인 단위 입력이 필요할 때 사용 input().rstrip()과 함께 쓴다.

# Solve here
from collections import deque

T = int(input())
for _ in range(T):
    cnt = 0
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    Q = deque(range(N))
    while True:
        if priority[Q[0]] >= max(map(lambda x: priority[x], Q)):
            cnt += 1
            cur = Q.popleft()
            if cur == M: break
        else:
            cur = Q.popleft()
            Q.append(cur)
    print(cnt)
