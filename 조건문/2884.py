time = input()
time = time.split(" ")

h = int(time[0])
m = int(time[1])

m -= 45

if m < 0:
    m += 60
    h -= 1

if h < 0:
    h = 23
print(h, m)
