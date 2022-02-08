# I/O template
import sys

file_path = r'input.txt'
sys.stdin = open(file_path, 'r')


# input = sys.stdin.readline  # 대량의 라인 단위 입력이 필요할 때 사용

# Solve here
def DFS(L):
    if L == m:
        print(*res)
        return
    for i in range(1, n + 1):  # 중복 순열
        res[L] = i
        DFS(L + 1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    res = [0] * m
    DFS(0)
