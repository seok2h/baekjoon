a = input()
b = input()

sum = 0
i = 0
for x in b[::-1]:
    for y in a[::-1]:
        sum += int(x)*int(y)*(10**i)
        i+=1
    print(sum)
    i=0
    sum = 0
print(int(a) * int(b))