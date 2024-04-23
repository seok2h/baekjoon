"""
https://www.acmicpc.net/problem/10869
제목 : 사칙연산
번호 : 10869

문제
두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.

입력
두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

출력
첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
"""

string = input()

var = string.split(" ")
p1 = int(var[0])
p2 = int(var[1])

print(p1 + p2)
print(p1 - p2)
print(p1 * p2)
print(int(p1 / p2))
print(p1 % p2)