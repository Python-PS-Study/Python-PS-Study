# SSAFY 7th 9반 Python 만세

코테는 역시 파이썬이지!~

- [김완상 / wansang93](./김완상/README.md)
- [민상규 / monterey12](https://github.com/monterey12)
- [염규현 / gh-develop](https://github.com/gh-develop)
- [황재완 / JaewanHwang](https://github.com/JaewanHwang)

## Python Tip

우리끼리 코드리뷰하면서 좋았던 코드 남기기

### DeepCopy 쉽게 하기

```python
# 1차원 배열 deepcopy
deep_1st_lst = lst[:]

# 2차원 배열 deepcopy
deep_2ed_lst = [x[:] for x in lst]
```

### 카드셔플 홀수일 때 값처리

```python
# 홀수는 N//2+1 하고 짝수는 N//2로 한번에 하는 법
# 상규 방법
num = N // 2 + N % 2

# 완상 방법
num = (N-1) // 2 + 1

# 기존 방법
num = N // 2
if N % 2 == 1:
    num += 1
```

### 전치행렬

```python
# 열탐색 할 때 좋음
lst = [list(x) for x in zip(*lst)]
```
