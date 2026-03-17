"""
https://www.acmicpc.net/problem/1676
제목: 팩토리얼 0의 개수
번호: 1676
"""

import sys

N = int(sys.stdin.readline())
factorial = 1
zeros = 0

for i in range(1, N+1):
    factorial *= i

string_fact = str(factorial)

if string_fact[-1] == '0':
    for i in range(len(string_fact)-1, -1, -1):
        if string_fact[i] == '0':
            zeros += 1
        else:
            break

print(zeros)
