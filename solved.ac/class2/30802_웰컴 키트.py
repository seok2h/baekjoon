"""
https://www.acmicpc.net/problem/30802
제목: 웰컴 키트
번호: 30802
"""

import sys

N = int(sys.stdin.readline())
size_list = list(map(int, sys.stdin.readline().split()))
T, P = map(int, sys.stdin.readline().split())

Tbundle = 0

for num_size in size_list:
    if num_size % T == 0:
        Tbundle += num_size // T
    else:
        Tbundle += num_size // T + 1

print(Tbundle)
print(N // P, N % P)
