L = []
for _ in range(5):
    L.append(int(input()))
L.sort()
print(int(sum(L)/len(L)))
print(L[2])