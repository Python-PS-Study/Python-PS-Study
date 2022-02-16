import sys

file_path = (
    r'test_input.txt'
)
sys.stdin = open(file_path, 'r')

input()
arr = map(int, input().split())
arr = list(enumerate(arr, 1))  # 인덱스를 함께 저장한다 [(1, 3), (2, 2), (3, 1), (4, -3), (5, -1)]

idx = 0
answer = []
while arr:
    idx %= len(arr)
    number, move = arr.pop(idx)
    answer.append(number)
    idx += move - 1 if move > 0 else move  # 풍선이 터지면서 생기는 빈 공간을 양수의 경우에만 -1로 체크해준다

print(*answer)
