'''
url: https://www.acmicpc.net/problem/11653
제목: 소인수분해
번호: 11653

문제
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

출력
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.
'''

# 실패한 알고리즘 : 시간초과
# n = int(input())
# pf_list = []
# i = 2

# while i != n:
#     if n % i == 0:
#         pf_list.append(i)
#         n /= i

#     else: # n % i != 0
#         i += 1
        
# pf_list.append(int(n))

# for x in pf_list:
#     print(x)

n = int(input())

if n == 1:
    print('')
    
for i in range(2, n + 1):
    if n % i == 0:
        while n % i == 0:
            print(i)
            n = n / i
