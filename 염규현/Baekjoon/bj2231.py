import sys
sys.stdin = open("bj2231_in.txt")

'''
분해합 문제
어떤 자연수 N이 있을 때 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합
EX) 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다.

자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구하시오

IDEA: XYZ-> 100X+1X+10Y+1Y+1Z+1Z ( X,Y,Z는 0~9사이 정수)
'''


def find_least_constructor():
    answers = list()

    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):

                            if (a*100001+b*10001+c*1001+d*101+e*11+f*2) == N:   # N과 같은 수가 있다면

                                answer = list()  # answer list를 만들어서 추가
                                answer.append(str(a))
                                answer.append(str(b))
                                answer.append(str(c))
                                answer.append(str(d))
                                answer.append(str(e))
                                answer.append(str(f))
                                answers.append(answer)  # answers에 answer를 추가

    ans = 1000000  # ans를 1000000으로 초기화 
    if len(answers) != 0:  # answers에 크기가 0이 아니라면
        for i in range(len(answers)):
            result = ""
            for j in range(6):
                result += answers[i][j]

            if ans > int(result.lstrip("0")):  # 문자열 앞에 0을 제거한 값이 ans보다 작다면
                ans = int(result.lstrip("0"))  # 문자열값을 정수로 바꾸고 ans를 업데이트
        return ans

    else:  # answers에 크기가 0이라면
        return 0


N = int(input())  # N: 자연수

print(find_least_constructor())
