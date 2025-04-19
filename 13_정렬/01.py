N = int(input())
L = []

for _ in range(N):
    L.append(int(input()))

L.sort()
for x in L:
    print(x)