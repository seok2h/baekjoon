"""
https://www.acmicpc.net/problem/2475
제목 : 검증수
번호 : 2475
"""

import sys

l = list(map(int, sys.stdin.readline().split()))
print(sum(list(map(lambda x: x**2, l))) % 10)
