'''
url: https://www.acmicpc.net/problem/1193
제목: 분수찾기
번호: 1193

문제
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.



1/1
1/2
1/3
1/4
1/5
…


2/1
2/2
2/3
2/4
…
…


3/1
3/2
3/3
…
…
…


4/1
4/2
…
…
…
…


5/1
…
…
…
…
…


…
…
…
…
…
…



이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

출력
첫째 줄에 분수를 출력한다.
'''
import sys

fraction_position = int(sys.stdin.readline())
n = 1

def diffSP(n):
    return int((n + 1) * n / 2 - fraction_position)

while diffSP(n) < 0:
    n += 1

# x/y
if (n % 2 == 0):
    x, y = n - diffSP(n), 1 + diffSP(n) 
    
else:
    x, y = 1 + diffSP(n), n - diffSP(n)

print(f"{x}/{y}")

"""
더 단순화하는 방법 (출처: https://velog.io/@hwsa1004/%EB%B0%B1%EC%A4%80-1193%EB%B2%88-%EB%B6%84%EC%88%98%EC%B0%BE%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%92%80%EC%9D%B4)
import sys

num = int(sys.stdin.readline())
line = 1

while num > line:
    num -= line
    line += 1

if line % 2 == 0:
    a = num
    b = line - num + 1

elif line % 2 == 1:
    a = line - num + 1
    b = num

print(f"{a}/{b})
"""
