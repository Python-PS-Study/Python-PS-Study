import sys

file_path = (
    r'test_input.txt'
)
sys.stdin = open(file_path, 'r')

from itertools import combinations

s = input()
stack = []
pair = []
answer = set()
for idx, x in enumerate(s):  # 괄호의 인덱스를 쌍으로 저장
    if x == '(':
        stack.append(idx)
    if x == ')':
        pair.append([stack.pop(), idx])

for i in range(1, len(pair) + 1):  # 고르는 수 1 ~ len(pair) ->부분집합?
    for c in combinations(pair, i):
        result = list(s[:])
        for start, end in c:
            result[start] = ' '
            result[end] = ' '
        answer.add(''.join(result).replace(' ', ''))

for i in sorted(answer):
    print(i)
