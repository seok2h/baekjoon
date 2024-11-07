'''
url: https://www.acmicpc.net/problem/4134
제목: 다음 소수
번호: 4134

문제
정수 n(0 ≤ n ≤ 4*109)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.

출력
각각의 테스트 케이스에 대해서 n보다 크거나 같은 소수 중 가장 작은 소수를 한 줄에 하나씩 출력한다.
'''

import sys

n = int(sys.stdin.readline())

def check(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

for i in range(n):
    m = int(sys.stdin.readline())
    while True:
        if m==0 or m==1:
            print(2)
            break
        if check(m):
            print(m)
            break
        else:
            m += 1
