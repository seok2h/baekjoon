string = input()
var = string.split(" ")
A = int(var[0])
B = int(var[1])
C = int(var[2])

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)