# I/O template
import sys

file_path = r'input.txt'
sys.stdin = open(file_path, 'r')
# input = sys.stdin.readline # 대량의 라인 단위 입력이 필요할 때 사용 input().rstrip()과 함께 쓴다.

# Solve here
# 덱 이용한 구현
from collections import deque

N = int(input())
move = list(map(int, input().split()))
Q = deque(range(N))
res = [1]
cur = Q.popleft()
while Q:
    if move[cur] > 0:
        for _ in range(move[cur] - 1):
            Q.append(Q.popleft())
        cur = Q.popleft()
    elif move[cur] < 0:
        for _ in range(-move[cur] - 1):
            Q.appendleft(Q.pop())
        cur = Q.pop()
    res.append(cur + 1)
print(*res)
