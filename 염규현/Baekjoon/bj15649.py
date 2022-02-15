import bisect


def permute(ans):
    if len(ans) == m:
        print(*ans)

    else:
        for i in range(1, n+1):
            tmp = ans[:]
            tmp.sort()
            index = bisect.bisect_left(tmp, i)
            if index < len(tmp) and tmp[index] == i:
                continue

            ans.append(i)
            permute(ans)
            ans.pop()


n, m = map(int, input().split())
permute([])
