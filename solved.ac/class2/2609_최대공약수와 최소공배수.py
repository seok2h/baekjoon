"""
https://www.acmicpc.net/problem/2609
제목: 최대공약수와 최소공배수
번호: 2609
"""

# Hard coding
import sys

# A, B = map(int, sys.stdin.readline().split())
# for i in range(1, A * B):
#     if i % A == 0 and i % b == 0:
#         print(i)
#         break

A, B = map(int, input().split())

def gcd(A, B):
    while B > 0:
        A, B = B, A % B
    return A

def lcm(A, B):
    return A * B // gcd(A, B)

print(gcd(A, B))
print(lcm(A, B))
