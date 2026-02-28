"""
https://www.acmicpc.net/problem/10250
제목: ACM 호텔
번호: 10250
"""

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    
    if N % H == 0:
        y = H
        x = N // H
    else:
        y = N % H
        x = N // H + 1
    if x < 10:
        result = str(y) + "0" + str(x)
    else:
        result = str(y) + str(x)

    print(result)