'''
url: https://www.acmicpc.net/problem/1085
제목: 직사각형에서 탈출
번호: 1085

문제
한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 x, y, w, h가 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다.
'''

x, y, w, h = map(int, input().split())

minimum = 1000000

if w - x < minimum:
    minimum = w - x
    
if x < minimum:
    minimum = x
    
if h - y < minimum:
    minimum = h - y
    
if y < minimum:
    minimum = y
    
print(minimum)



