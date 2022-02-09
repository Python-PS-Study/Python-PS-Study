# 백준

## 3주차

### [1935 후위표기식2](https://github.com/wansang93/Algorithm/blob/master/BAEKJOON/problems/.md)

### [10799 쇠막대기](https://github.com/wansang93/Algorithm/blob/master/BAEKJOON/problems/10799.md)

### [1966 프린터 큐](https://github.com/wansang93/Algorithm/blob/master/BAEKJOON/problems/1966.md)

### [2346 풍선 터뜨리기](https://github.com/wansang93/Algorithm/blob/master/BAEKJOON/problems/2346.md)

### [2504 괄호의 값](https://github.com/wansang93/Algorithm/blob/master/BAEKJOON/problems/2504.md)

### [2800 괄호 제거](https://github.com/wansang93/Algorithm/blob/master/BAEKJOON/problems/2800.md)

## 2주차

### [15654 N과 M (5)](https://github.com/wansang93/Algorithm/blob/master/BAEKJOON/problems/15654.md)

```python
N, M = map(int, input().split())
answer = []
lst = sorted(list(map(int ,input().split())))
is_visited = [False] * N

def permutation(cnt):
    if cnt == M:
        print(*answer)
        return

    for i in range(N):
        if is_visited[i]:
            continue
        answer.append(lst[i])
        is_visited[i] = True
        permutation(cnt+1)
        answer.pop()
        is_visited[i] = False

permutation(0)

```

### [15652 N과 M (4)](https://github.com/wansang93/Algorithm/blob/master/BAEKJOON/problems/15652.md)

```python
N, M = map(int, input().split())
answer = []

def combinatino_repitition(cnt, start):
    if cnt == M:
        print(*answer)
        return

    for i in range(start, N+1):
        answer.append(i)
        combinatino_repitition(cnt+1, i)
        answer.pop()

combinatino_repitition(0, 1)

```

### [15651 N과 M (3)](https://github.com/wansang93/Algorithm/blob/master/BAEKJOON/problems/15651.md)

```python
N, M = map(int, input().split())
answer = []

def permutation_repitition(cnt):
    if cnt == M:
        print(*answer)
        return

    for i in range(1, N+1):
        answer.append(i)
        permutation_repitition(cnt+1)
        answer.pop()

permutation_repitition(0)

```

### [15650 N과 M (2)](https://github.com/wansang93/Algorithm/blob/master/BAEKJOON/problems/15650.md)

```python
N, M = map(int, input().split())
answer = []

def combination(cnt, start):
    if cnt == M:
        print(*answer)
        return
    
    for i in range(start, N+1):
        answer.append(i)
        combination(cnt+1, i+1)
        answer.pop()

combination(0, 1)

```

### [15649 N과 M (1)](https://github.com/wansang93/Algorithm/blob/master/BAEKJOON/problems/15649.md)

```python
N, M = map(int, input().split())
answer = []
is_visited = [False] * N

def permutation(cnt):
    if cnt == M:
        print(*answer)
        return
    
    for i in range(1, N+1):
        if is_visited[i-1]:
            continue
        answer.append(i)
        is_visited[i-1] = True
        permutation(cnt+1)
        answer.pop()
        is_visited[i-1] = False

permutation(0)

```

## 1주차

### [1969 DNA](https://github.com/wansang93/Algorithm/blob/master/BAEKJOON/problems/1969.md)

```python
# 내 풀이
N, M = map(int, input().split())
lst = [input() for _ in range(N)]
char_to_num = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
num_to_char = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
best_dna = ''
answer = 0

for i in range(M):
    cnt = [0, 0, 0, 0]  # A, C, G, T
    for j in range(N):
        idx = char_to_num[lst[j][i]]
        cnt[idx] += 1
    idx = cnt.index(max(cnt))
    best_dna += num_to_char[idx]
    answer += sum(cnt) - cnt[idx]

print(best_dna)
print(answer)

# 숏코딩(전치행렬 구한 뒤 하나씩 꺼내와서)
for line in dna:
    k = max('ACGT', key=lambda x: line.count(x))
    s += [k]
    c += len(i) - line.count(k)
```

### [15721 번대기](https://github.com/wansang93/Algorithm/blob/master/BAEKJOON/problems/15721.md)

```python
# 풀이 중 ㅜㅜ 개어렵...
```

### [18312 시각](https://github.com/wansang93/Algorithm/blob/master/BAEKJOON/problems/18312.md)

```python
N, K = input().split()
cnt = 0
for h in range(int(N)+1):
    for m in range(60):
        for s in range(60):
            if K in f"{h:02}{m:02}{s:02}":
                cnt += 1
print(cnt)
```

### [19532 수학은 비대면강의입니다](https://github.com/wansang93/Algorithm/blob/master/BAEKJOON/problems/19532.md)

```python
# 역행렬 구해서 해 구하기
a, b, c, d, e, f = map(int, input().split())
g = a*e-d*b
print((e*c-b*f)//g, (a*f-d*c)//g)

# 문제 의도
a, b, c, d, e, f = map(int, input().split())
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
```

### [2231 분해합](https://github.com/wansang93/Algorithm/blob/master/BAEKJOON/problems/2231.md)

```python
N = int(input())
# 시작 값을 1부터가 아닌 자릿수대로 계산해서 시작
start_num = max(0, N - 9*len(str(N)))

for i in range(start_num, N):
    if i + sum(map(int, str(i))) == N:
        print(i)
        break
else:
    print(0)
```

### [2798 블랙잭](https://github.com/wansang93/Algorithm/blob/master/BAEKJOON/problems/2798.md)

```python
# 내 풀이
N, M = map(int, input().split())
lst = list(map(int, input().split()))

max_value = 0
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            s = lst[i]+lst[j]+lst[k]
            if s <= M:
                max_value = max(max_value, s)
print(max_value)

# 조합 라이브러리 풀이
from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))
max_num = 0

for card in combinations(cards, 3):
    s = sum(card)
    if s <= M:
        max_num = max(max_num, s)
print(max_num)
```

### [22864 피로도](https://github.com/wansang93/Algorithm/blob/master/BAEKJOON/problems/22864.md)

```python
# 내 풀이
A, B, C, M = map(int, input().split())
fatigue = 0
hour = 0
work = 0

while hour < 24:
    if fatigue + A <= M:
        fatigue += A
        work += B
    else:
        fatigue -= C
        if fatigue < 0:
            fatigue = 0
    hour += 1

print(work)
```

숏코딩에서 배운거

```python
# 방법1. 음수면 0으로 하기
if fatigue < 0:
    fatigue = 0
# 방법2. 숏코딩
fatigue = max(fatigue, 0)
```
