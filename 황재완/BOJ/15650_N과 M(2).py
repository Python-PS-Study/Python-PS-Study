# I/O template
import sys

file_path = r'input.txt'
sys.stdin = open(file_path, 'r')


# input = sys.stdin.readline  # 대량의 라인 단위 입력이 필요할 때 사용

# Solve here
def DFS(L, num):
    if L == m:
        print(*res)
        return
    for i in range(num + 1, n + 1):
        if ch[i] == 0:
            res[L] = i
            ch[i] = 1
            DFS(L + 1, i)
            ch[i] = 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    ch = [0] * (n + 1)
    res = [0] * m
    DFS(0, 0)
