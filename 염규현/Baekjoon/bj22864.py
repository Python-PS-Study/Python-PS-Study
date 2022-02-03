import sys
sys.stdin = open("bj22864_in.txt")

A, B, C, M = map(int, input().split())

'''
A: 피로도 증가
B: 처리량
C: 피로도 감소
M: 최대 피로도 
'''

hour = 0  # 시간
answer = 0  # 최대 처리량
stamina = 0  # 현재 피로도

while hour < 24:
    hour += 1
    if stamina+A <= M:  # 최대 피로도보다 피로도 증가한 값이 같거나 작으면
        answer += B  # 처리량 증가
        stamina += A  # 피로도 증가
    else:   # 휴식
        if stamina-C >= 0:
            stamina -= C  # 피로도 감소
        else:
            stamina = 0

print(answer)
