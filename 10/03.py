'''
url: https://www.acmicpc.net/problem/3009
제목: 네 번째 점
번호: 3009

문제
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.
'''

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if x1 == x2:
    x = x3
elif x1 == x3:
    x = x2
else:
    x = x1

if y1 == y2:
    y = y3
elif y1 == y3:
    y = y2
else:
    y = y1
    
print(x, y)