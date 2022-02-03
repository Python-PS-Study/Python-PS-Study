A = int(input())
T = int(input())
say = int(input())
bundegi = []
bun = degi = 1
turn = 0
while 1:
    prevbundegiNum = bun
    turn += 1
    # 번.데기.번.데기
    for _ in range(2):
        bundegi.append((bun, 0))
        bun += 1
        bundegi.append((degi, 1))
        degi += 1
    # 번 연속 turn+1번
    for _ in range(turn + 1):
        bundegi.append((bun, 0))
        bun += 1
    # 데기 연속 turn+1번
    for _ in range(turn + 1):
        bundegi.append((degi, 1))
        degi += 1
    # 이번 턴에 구하고자하는 구호가 있다면
    if prevbundegiNum < T <= bun:
        print(bundegi.index((T, say)) % A)
        break