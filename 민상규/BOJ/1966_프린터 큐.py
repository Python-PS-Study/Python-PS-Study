from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))  # 큐에 저장한다
    cnt = 1
    while True:
        if queue[0] == max(queue):  # 1.현재 Queue의 가장 앞에 있는 문서의 중요도가 제일 높을 경우
            if m == 0:  # 출력 - 원하는 문서인 경우
                answer = cnt
                break
            else:  # 출력 - 원하는 문서가 아닌 경우
                queue.popleft()
                cnt += 1
                m -= 1
        else:  # 2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
            queue.append(queue.popleft())  # 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다
            if m == 0:  # 원하는 문서가 맨 뒤로 갈 경우 m을 재설정 해준다
                m = len(queue) - 1
            else:
                m -= 1
    print(cnt)
