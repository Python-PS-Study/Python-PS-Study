
def repeat_permute(ans):
    # base case
    if len(ans) == m:
        print(*ans)

    else:
        for i in range(1, n+1):
            ans.append(i)
            repeat_permute(ans)
            ans.pop()


n, m = map(int, input().split())
repeat_permute([])
