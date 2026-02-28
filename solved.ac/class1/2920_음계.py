"""
https://www.acmicpc.net/problem/2920
제목: 음계
번호: 2920
"""

import sys

l = list(map(int, sys.stdin.readline().split()))

ascending = True
descending = True

for i in range(0, 8):
    if l[i] != i+1:
        ascending = False
        break

for j in range(0, 8):
    if l[j] != 8-j:
        descending = False
        break

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")