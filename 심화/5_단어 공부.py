"""
https://www.acmicpc.net/problem/1157
제목 : 단어 공부
번호 : 1157

문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
"""

string = input()
s = string.upper()
d = {}

for x in s:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

a = list(d.items())
count = 0

for x in a:
    if count < int(x[1]):
        char = x[0]
        count = x[1]

count2 = 0

for x in a:
    if count == int(x[1]):
        count2 += 1

if count2 > 1:
    print("?")
else:
    print(char)


