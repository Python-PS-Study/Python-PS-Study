# import sys


def DFS(L, status, tot):
    global max_work
    if status > M:
        return
    if L == 24:
        max_work = max(max_work, tot)
    else:
        if (24 - L) * B + tot < max_work:
            return
        DFS(L + 1, status + A, tot + B)
        if status - C > 0:
            DFS(L + 1, status - C, tot + 0)  # 쉴때
        else:
            DFS(L + 1, 0, tot + 0)


# sys.stdin = open('input.txt', 'rt')
A, B, C, M = map(int, input().split())
max_work = 0
DFS(0, 0, 0)
print(max_work)
