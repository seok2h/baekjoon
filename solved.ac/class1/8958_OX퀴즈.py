"""
https://www.acmicpc.net/problem/8958
제목: OX퀴즈
번호: 8958
"""

import sys

N = int(sys.stdin.readline())

for _ in range(N):
    string = sys.stdin.readline().strip()
    
    result = 0
    O = 1

    for s in string:
        if s == "O":
            result += O
            O += 1
        elif s == "X":
            O = 1
    
    print(result)
