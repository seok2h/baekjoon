
'''
url: https://www.acmicpc.net/problem/11050
제목: 이항 계수 1
번호: 11050

문제
자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 \(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 \(N\)과 \(K\)가 주어진다. (1 ≤ \(N\) ≤ 10, 0 ≤ \(K\) ≤ \(N\))

출력
\(\binom{N}{K}\)를 출력한다.
'''

import sys

N, K = map(int, sys.stdin.readline().split())
result = 1
for i in range(K):
    result *= N
    N -= 1

divisor = 1
for i in range(2, K+1):
    divisor *= i

print(result // divisor)
