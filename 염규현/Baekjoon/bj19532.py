import sys
sys.stdin = open("bj19532_in.txt")

# '''
# 수학은 비대면 강의입니다
#
# 문자가 2개인 연립방정식 해결
# ax+by=c
# dx+ey=f
#
# 정수 a, b, c, d, e, f가 공백으로 구분되어 차례대로 주어진다.(-999~999)
# 문제에서 언급한 방정식을 만족하는 (x,y)가 유일하게 존재. 이때 x와 y가 각각 -999이상 999이하의 정수인 경우만 입력으로 주어짐이 보장
# x,y를 공백으로 구분해 출력
# '''
#
#
# def find_equation(eq1, eq2):
#     answer = None
#     x, y = 0, 0
#
#     if eq1[0] == 0:
#         y = eq1[2]/eq1[1]
#         x = eq2[2]/eq2[0]
#         return int(x), int(y)
#     elif eq1[1] == 0:
#         x = eq1[2]/eq1[0]
#         y = eq2[2]/eq2[1]
#         return int(x), int(y)
#     else:
#         equation1 = [eq2[0]*num for num in eq1]
#         equation2 = [eq1[0]*num for num in eq2]
#
#         answer = [m - n for m, n in zip(equation1, equation2)]
#         # print(answer)
#         if answer[2] == 0:
#             y = 0
#             x = (equation2[2] - equation2[1] * y) / equation2[0]
#         elif answer[0] == 0:
#             y = answer[2] / answer[1]
#             x = (equation2[2] - equation2[1] * y) / equation2[0]
#         elif answer[1] == 0:
#             x = answer[2] / answer[0]
#             y = (equation2[2] - equation2[0] * x) / equation2[1]
#
#         return int(x), int(y)
#
#
# a, b, c, d, e, f = map(int, input().split())
#
# _equation1 = [a, b, c]
# _equation2 = [d, e, f]
# _answer = None
#
# # print(_equation1)
# # print(_equation2)
# ans_x, ans_y = find_equation(_equation1, _equation2)
# print(ans_x, ans_y)

a, b, c, d, e, f = map(int, input().split())


for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            break
