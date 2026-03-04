"""
https://www.acmicpc.net/problem/1259
제목: 팰린드롬수
번호: 1259
"""

import sys

while True:
    isPalindrom = True
    string = sys.stdin.readline().strip()
    
    if string == '0':
        break
    
    for i in range(int(len(string) / 2)):
        if string[i] != string[-1 - i]:
            isPalindrom = False
            break

    if isPalindrom:
        print('yes')
    else:
        print('no')

