# I/O template
import sys

file_path = r'input.txt'
sys.stdin = open(file_path, 'r')
# input = sys.stdin.readline # 대량의 라인 단위 입력이 필요할 때 사용 input().rstrip()과 함께 쓴다.

from itertools import compress

def make_subsets(L):  # 부분 집합
    if L == len(brackets):
        res.append(''.join(compress(exp, is_selected)))
        return
    is_selected[brackets[L][0]] = True
    is_selected[brackets[L][1]] = True
    make_subsets(L + 1)
    is_selected[brackets[L][0]] = False
    is_selected[brackets[L][1]] = False
    make_subsets(L + 1)


exp = input()
is_selected = [True] * len(exp)
stack = []
brackets = []
res = []
for i in list(range(len(exp))):
    if exp[i] == '(':
        stack.append(i)
    elif exp[i] == ')':
        brackets.append((stack.pop(), i))  # ('('인덱스, ')'인덱스)
make_subsets(0)
res.remove(exp)  # 원집합과 동일한 부분집합 제외
print(*sorted(set(res)), sep='\n')  # 사전순 출력
