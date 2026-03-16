"""
https://www.acmicpc.net/problem/15829
제목: Hashing
번호: 15829
"""

import sys

n = int(sys.stdin.readline())
string = sys.stdin.readline().strip()
total = 0 

for i, c in enumerate(string):
    total += (ord(c) - ord('a') + 1) * (31 ** i)

print(total % 1234567891)