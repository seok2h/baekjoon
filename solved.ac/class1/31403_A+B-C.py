"""
https://www.acmicpc.net/problem/31403
제목: A + B - C
번호: 31403
"""

import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
C = sys.stdin.readline().strip()

print(int(A) + int(B) - int(C))
print(int((A+B)) - int(C))