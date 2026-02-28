"""
https://www.acmicpc.net/problem/2577
제목: 숫자의 개수
번호: 2577
"""

import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

result = str(A * B * C)

print(result.count('0'))
print(result.count('1'))
print(result.count('2'))
print(result.count('3'))
print(result.count('4'))
print(result.count('5'))
print(result.count('6'))
print(result.count('7'))
print(result.count('8'))
print(result.count('9'))