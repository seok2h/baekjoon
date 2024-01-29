string = input()
s = string.upper()
d = {}

for x in s:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

a = list(d.items())
count = 0

for x in a:
    if count < int(x[1]):
        char = x[0]
        count = x[1]

count2 = 0

for x in a:
    if count == int(x[1]):
        count2 += 1

if count2 > 1:
    print("?")
else:
    print(char)


