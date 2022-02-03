import sys
sys.stdin = open("bj2798_in.txt")

'''
블랙잭 게임
주어진 3장의 카드를 골라 제시된 숫자와 가장 가까운 합을 만들어 카드이 합을 정답으로 출력
'''


def find_sum(cards, answer):

        for i in range(N):      # 첫번째 카드 고정
            for j in range(i+1, N):  # 두번째 카드 고정
                for k in range(j+1, N):      # 세번째 카드 고정
                    # print(cards[i], cards[j], cards[k])

                    if cards[i]+cards[j]+cards[k] == M:
                        answer = cards[i] + cards[j] + cards[k] #M과 동일하면 리턴
                        return answer
                    elif answer < cards[i]+cards[j]+cards[k] < M:       #기존의 answer보다 크면서 M보다 작으면 answer업데이트
                        answer = cards[i] + cards[j] + cards[k]
                    elif cards[i]*3 >= M:       #반복문 탈출 조건: 제일 앞에 더하는 숫자*3이 M보다 크면 함수 리턴
                        return answer
        return answer   #모든 반복문이 끝난 후 리턴

N, M = map(int, input().split())    # N: 카드의 갯수 M: M에 최대한 가까운 카드 3장의 합
_cards = list(map(int, input().split()))        # 카드 저장
_cards.sort()   # 카드 오름차순으로 정렬

_answer = 0
# print(_cards)

print(find_sum(_cards, _answer))
