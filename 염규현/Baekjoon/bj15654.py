import bisect


def permute_data(ans, data):
    if len(ans) == m:
        print(*ans)

    else:
        for i in data:
            tmp = ans[:]
            tmp.sort()
            index = bisect.bisect_left(tmp, i)
            if index < len(tmp) and tmp[index] == i:
                continue

            ans.append(i)
            permute_data(ans, data)
            ans.pop()


n, m = map(int, input().split())
_data = sorted(list(map(int, input().split())))
permute_data([], _data)
