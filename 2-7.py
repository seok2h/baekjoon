
dice = input().split(" ")
a = int(dice[0])
b = int(dice[1])
c = int(dice[2])

if a == b == c:
    print(10000 + a * 1000)
elif a != b and b != c and a != c:
    print(max(a, b, c) * 100)
else:
    if a == b:
        print(1000 + a * 100)
    elif b == c:
        print(1000 + b * 100)
    else:
        print(1000 + a * 100)
