"""
https://www.acmicpc.net/problem/7568
제목: 덩치
번호: 7568
"""

import sys

n = int(sys.stdin.readline())

data = []

for _ in range(n):
    weight, height = map(int, sys.stdin.readline().split())
    data.append((weight, height))

for i in range(n):
    rank = 1
    for j in range(n):
        if data[j][0] > data[i][0] and data[j][1] > data[i][1]:
            rank += 1
    print(rank, end=" ")
