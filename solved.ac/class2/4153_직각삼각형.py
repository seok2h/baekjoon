"""
https://www.acmicpc.net/problem/4153
제목: 직각삼각형
번호: 4153
"""

import sys

while True:
    l = list(map(int, sys.stdin.readline().split()))
    l.sort()
    
    if l[0] == l[1] == l[2] == 0:
        break

    if (l[0] ** 2 + l[1] ** 2) == (l[2] ** 2):
        print('right')
    else:
        print('wrong')
