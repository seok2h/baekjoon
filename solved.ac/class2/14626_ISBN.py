"""
https://www.acmicpc.net/problem/14626
제목: ISBN
번호: 14626
"""

import sys

isbn = sys.stdin.readline().strip()
total = 0

for i, char in enumerate(isbn):
    if char == '*':
        position = i
        continue

    if i % 2 == 0:
        total += int(char)
    else:
        total += int(char) * 3 

if position % 2 == 0:
    if total % 10 == 0:
        print(0)
    else:
        print(10 - (total % 10))

else:
    for i in range(10):
        if (total + 3 * i) % 10 == 0:
            print(i)
            break
