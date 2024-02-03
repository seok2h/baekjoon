"""
https://www.acmicpc.net/problem/2444
제목 : 별 찍기 - 7
번호 : 2444

문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
"""

N = int(input())
n, m = (N - 1), 1

for x in range(N):
    print((' ' * n) + ('*' * m))
    n = n - 1
    m = m + 2

n = 1
m -= 4

for x in range(N-1):
    print((' ' * n) + ('*' * m))
    n += 1
    m -= 2
