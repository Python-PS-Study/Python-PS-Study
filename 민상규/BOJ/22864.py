a, b, c, m = map(int, input().split())
p = 0
result = 0

for i in range(24):
    if p + a <= m:
        p += a
        result += b
    else:
        p -= c
        if p < 0:
            p = 0

print(result)
