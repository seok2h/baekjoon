import sys

T = int(sys.stdin.readline())
for i in range(T):
    n, m = map(int, sys.stdin.readline().split())
    m_factorial = 1
    n_factorial = 1
    msubn_factorial = 1

    for i in range(1, m+1):
        m_factorial *= i
    for j in range(1, n+1):
        n_factorial *= j
    for k in range(1, m-n+1):
        msubn_factorial *= k
    print(int(m_factorial / (msubn_factorial * n_factorial)))